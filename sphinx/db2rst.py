#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    DocBook to ReST converter
    =========================
    This script may not work out of the box, but is easy to extend.
    If you extend it, please send me a patch: wojdyr at gmail. 

    Docbook has >400 elements, most of them are not supported (yet).
    ``pydoc db2rst`` shows the list of supported elements.

    In ReST, inline markup can not be nested (major deficiency of ReST).
    Since it is not clear what to do with, say,
    <subscript><emphasis>x</emphasis></subscript>
    the script outputs incorrect (nested) ReST (:sub:`*x*`)
    and it is up to user to decide how to change it.

    Usage:
        db2rst.py file.xml > file.rst
        db2rst.py file.xml output_directory/

    :copyright: 2009 by Marcin Wojdyr.
    :license: BSD.
	:URL: https://raw.github.com/kurtmckee/db2rst/master/db2rst.py
"""

import os
import os.path
import sys
import re
import lxml.etree
import logging

__contributors__ = ('Kurt McKee <contactme@kurtmckee.org>',
                    'Anthony Scopatz <ascopatz@enthought.com>',
                    'Pete Jemian <jemian@anl.gov>',
                   )


class Db2Rst:
    ''' 
    handle conversion of DocBook source code files 
    into ReST: Restructured Text source code documents
    '''
    
    def __init__(self):
        self.namespaces = {}
        self.remove_comments = False
        self.write_unused_labels = False
        self._linked_ids = set()            # to remember which id/labels are really needed
        self.id_attrib = "id"               # can modify if namespace is present (a hack until namespaces are supported here)
        self.linkend = "linkend"            # can modify if namespace is present (a hack until namespaces are supported here)
        self.output_dir = None              # if converting a set of docbook files
        self.namespacePrefix = None         # as used in the DocBook file
        self.ns = ""
    
    def process(self, dbfile, converter  = None):
        '''
        process one DocBook XML file
        
        :param str dbfile: name of DocBook source code file
        :param obj converter: optional subclass of Convert to provide additional or override handlers
        :return: None or string buffer with converted ReST source
        '''
        logging.info('parsing %s with converter %s' % (dbfile, str(converter)))
        parser = lxml.etree.XMLParser(remove_comments=self.remove_comments)
        logging.info('created the parser')
        tree = lxml.etree.parse(dbfile, parser=parser)
        logging.info('parsed XML file')
        root = tree.getroot()
        self.ns = "{%s}" % root.nsmap[self.namespacePrefix]
        self._linked_ids = self._get_linked_ids(tree)
        if converter is None:
            obj = Convert(root, self)
        else:
            obj = converter(root, self)
        if self.output_dir:
            self.writeToDir(obj)
            return None
        else:
            return str(obj).strip() + "\n"
    
    def _get_linked_ids(self, tree):
        '''
        discover all the ids referenced in the file
        
        :param tree: name of DocBook source code file
        :type tree: lxml document tree
        :return [str]: list of strings containing all the ids
        '''
        ids = set()
        for elem in tree.getiterator():
            if elem.tag in (self.ns+"xref", self.ns+"link"):
                for nskey, nsstr in elem.nsmap.items():
                    ns = "{%s}" % nsstr
                    for term in ('linkend', 'href'):
                        text = elem.get(ns+term)
                        if text is not None:
                            ids.add(text.lstrip('#'))
        return ids

    def writeToDir(self, obj):
        '''
        Write the ReST files to the named directory.
        Generate an ``index.rst`` file as directed.
        
        :param obj: db2rst.Convert object
        '''
        if self.output_dir is None:
            return
            output = str(obj).strip()
        for fname in obj.files:
            f = open(os.path.join(output_dir, fname + '.rst'), 'wb')
            f.write(obj.files[fname].encode('utf-8').strip())
            f.close()
        # write the index if it doesn't exist already
        if 'index' not in obj.files:
            f = open(os.path.join(output_dir, 'index.rst'), 'wb')
            f.write(output)
            f.write('\n\n.. toctree::\n   :maxdepth: 1\n\n')
            for fname in sorted(obj.files):
                f.write('   %s\n' % (fname, ))
            f.close()
        # write a simple conf.py
        c = open(os.path.join(output_dir, 'conf.py'), 'wb')
        c.write("extensions = []\n")
        c.write("master_doc = 'index'\n")
        c.write("project = u'projname'\n")
        c.write("#copyright = u'2011, authname'\n")
        c.write("exclude_patterns = ['_build']\n")
        c.close()

    def removeComments(self, remove):
        '''
        Either remove comments from source stream (True)
        or convert them to ReST-format comments.
        
        :param bool remove: if True, XML comment will be discarded

        This DocBook (XML) comment::
        
           <!-- This is a comment
                with two lines. -->

        becomes this ReST code::
        
           .. COMMENT: This is a comment
                       with two lines.
        
        .. note:: Note that ReST doesn't support inline comments. XML comments
                  are converted to ReST comment blocks, which may break paragraphs.
        '''
        self.remove_comments = remove
    
    def writeUnusedLabels(self, write):
        '''
        Any ``id`` attributes of DocBook elements are translated to ReST labels.
        
        :param bool write: if False, only labels that are used in links are generated.
        '''
        self.write_unused_labels = write



class Convert(object):
    ''' converts DocBook tree into reST '''
    
    def __init__(self, el, parent = None, namespace = None):
        self.el = el
        self.files = {}
        if parent is None:
            parent = Db2Rst()       # looks inverted but provides basic constants
        if namespace is not None:
            parent.ns = "{%s}" % namespace
        self.parent = parent        # db2rst.Db2Rst object that called the converter
        self._not_handled_tags = set()      # to avoid duplicate error reports
        self._substitutions = set()         # to avoid duplicate substitutions
        self._buffer = ""                   # buffer that is flushed after the end of paragraph, used for ReST substitutions

    def __str__(self):
        output = self._conv(self.el)
        # remove trailing whitespace
        output = re.sub(r"[ \t]+\n", "\n", output)
        # leave only one blank line
        output = re.sub(r"\n{3,}", "\n\n", output)
        return output.encode('utf-8')

    def _conv(self, el, do_assert = True):
        '''
        Element to string conversion.
        Looks for a defined function e_tag() and calls it,
        where tag is the element name.
        The function e_tag() has one argument, 
        the DocBook element node to process.
        '''
        #logging.info("_conv(): line %d in %s" % (el.sourceline, str(el.base)))
        tag = str(el.tag)
        if tag == "<built-in function ProcessingInstruction>":
            logging.info("_conv(): line %d in %s" % (el.sourceline, str(el.base)))
            logging.info("ignoring ProcessingInstruction for now")
            return ""
        if tag == "<built-in function Comment>":
            logging.info("_conv(): line %d in %s" % (el.sourceline, str(el.base)))
            logging.info("ignoring Comment for now")
        if tag.find(self.parent.ns) == 0:
            # strip off the default namespace
            tag = tag[len(self.parent.ns):]
        if tag.startswith("{"):
            # identify other namespaces by prefix used in XML file
            ns, rawTag = tag[1:].split("}")
            if ns in el.nsmap.values():
                # find the namespace prefix, given its full value
                prefix = [k for k, v in el.nsmap.iteritems() if v == ns][0]
            if prefix is not None:
                tag = "_".join([prefix, rawTag])
        method_name = 'e_' + tag
        if hasattr(self, method_name):
            return getattr(self, method_name)(el)   # call the e_tag(el) method
        elif isinstance(el, lxml.etree._Comment):
            if el.text.strip():
                return self.Comment(el)
            else:
                return u''
        else:
            if el.tag not in self._not_handled_tags:
                logging.info("line %d in %s" % (el.sourceline, str(el.base)))
                self._warn("Don't know how to handle <%s>" % el.tag)
                self._not_handled_tags.add(el.tag)
            return self._concat(el)
    
    def _warn(self, s):
        logging.warning(s)
    
    def _supports_only(self, el, tags):
        "print warning if there are unexpected children"
        for i in el.getchildren():
            if i.tag not in tags:
                self._warn("%s/%s skipped." % (el.tag, i.tag))
    
    def _what(self, el):
        "returns string describing the element, such as <para> or Comment"
        if isinstance(el.tag, basestring):
            return "<%s>" % el.tag
        elif isinstance(el, lxml.etree._Comment):
            return "Comment"
        else:
            return str(el)
    
    def _has_only_text(self, el):
        "print warning if there are any children"
        if el.getchildren():
            self._warn("children of %s are skipped: %s" % (self._get_path(el),
                                  ", ".join(self._what(i) for i in el.getchildren())))
    
    def _has_no_text(self, el):
        "print warning if there is any non-blank text"
        if el.text is not None and not el.text.isspace():
            self._warn("skipping text of <%s>: %s" % (self._get_path(el), el.text))
        for i in el.getchildren():
            if i.tail is not None and not i.tail.isspace():
                self._warn("skipping tail of <%s>: %s" % (self._get_path(i), i.tail))
    
    def _no_special_markup(self, el):
        return self._concat(el)
    
    def _remove_indent_and_escape(self, s):
        "remove indentation from the string s, escape some of the special chars"
        s = "\n".join(i.lstrip().replace("\\", "\\\\") for i in s.splitlines())
        # escape inline mark-up start-string characters (even if there is no
        # end-string, docutils show warning if the start-string is not escaped)
        # TODO: handle also Unicode: � � � � � � as preceding chars
        s = re.sub(r"([\s'\"([{</:-])" # start-string is preceded by one of these
                   r"([|*`[])" # the start-string
                   r"(\S)",    # start-string is followed by non-whitespace
                   r"\1\\\2\3", # insert backslash
                   s)
        return s
    
    def _concat(self, el):
        "concatenate .text with children (self._conv'ed to text) and their tails"
        s = ""
        id = el.get(self.parent.id_attrib)
        if id is not None and (self.parent.write_unused_labels or id in self.parent._linked_ids):
            s += "\n\n.. _%s:\n\n" % id
        if el.text is not None:
            s += self._remove_indent_and_escape(el.text)
        for i in el.getchildren():
            s += self._conv(i)      # FIXME: fails for an empty <entry> element in a <table>
            if i.tail is not None:
                if len(s) > 0 and not s[-1].isspace() and i.tail[0] in " \t":
                    s += i.tail[0]
                s += self._remove_indent_and_escape(i.tail)
        return s
    
    def _original_xml(self, el):
        return lxml.etree.tostring(el, with_tail=False)
    
    def _no_markup(self, el):
        s = lxml.etree.tostring(el, with_tail=False)
        s = re.sub(r"<.+?>", " ", s) # remove tags
        s = re.sub(r"\s+", " ", s) # replace all blanks with single space
        return s
    
    def _get_level(self, el):
        "return number of ancestors"
        return sum(1 for i in el.iterancestors())
    
    def _get_path(self, el):
        t = [el] + list(el.iterancestors())
        return "/".join(str(i.tag) for i in reversed(t))
    
    def _make_title(self, t, level):
        '''
        :param str t: title
        :param int level: [1...] indicating priority of section level
        '''
        if level == 1:
            return "\n\n" + "=" * len(t) + "\n" + t + "\n" + "=" * len(t)
        char = ["#", "=", "-", "~", "^", ".", "*", "+", "_", ",", ":", "'", 
                "!", "?", '"', '$', '%', '&', ';', '(', ')', '/', '<', '>', 
                "@", "[", "]", "`", "{", "}", "|", "\\", ]
        return "\n\n" + t + "\n" + char[level-2] * len(t)
    
    def _join_children(self, el, sep):
        self._has_no_text(el)
        return sep.join(self._conv(i) for i in el.getchildren())
    
    def _block_separated_with_blank_line(self, el):
        pi = [i for i in el.iterchildren() if isinstance(i, lxml.etree._ProcessingInstruction)]
        if pi and 'filename=' in pi[0].text:
            fname = pi[0].text.split('=')[1][1:-1].split('.')[0]
            #import pdb; pdb.set_trace()
            el.remove(pi[0])
            self.files[fname] = self._conv(el)
            return "\n"
        else:
            s = "\n\n" + self._concat(el)
            if self._buffer:
                s += "\n\n" + self._buffer
                self._buffer = ""
            return s
    
    def _indent(self, el, indent, first_line=None):
        "returns indented block with exactly one blank line at the beginning"
        lines = [" "*indent + i for i in self._concat(el).splitlines()
                 if i and not i.isspace()]
        if first_line is not None:
            # replace indentation of the first line with prefix `first_line'
            lines[0] = first_line + lines[0][indent:]
        return "\n\n" + "\n".join(lines)
    
    def _normalize_whitespace(self, s):
        return " ".join(s.split())
    
    ###################           DocBook elements        #####################
    
    # special "elements"
    
    def _directive(self, el, name):
        '''
        Creates a reST directive::
        
          .. name: ``el.text`` provides the content.
                   Indentation is sized automatically like this.
        
        Some directives have two colons:
        
           .. note:: This is an advisory note.
        
        Some might only have one colon.  
        If you need two, supply it in the caller.
        
        :param XML_node el: node of the lxml document tree
        :param str name: text to be written after the two dots
        '''
        prefix = ".. %s: " % name
        indentation = len(prefix)
        return self._indent(el, indentation, prefix)
    
    def _docbook_source(self, el, name):
        s = "\n\n.. rubric:: %s\n\n::\n\n" % name
        s += " "*4 + self._original_xml( el )
        s += "\n\n"
        return s
    
    def _literal_source(self, el):
        return "\n::\n" + self._indent(el, 4) + "\n"
    
    def Comment(self, el):
        # _original_xml
        return self._directive(el, 'COMMENT')

    def ProcessingInstruction(self, el):
        # TODO: How/where to call this?
        return self._docbook_source(el, "ProcessingInstruction")
    
    def e_figure(self, el):
        return self._docbook_source(el, 'FIGURE')
    
    def e_example(self, el):
        return self._docbook_source(el, 'EXAMPLE')
        #s = "\n\n.. code-block:: guess"
        #return self._directive(el, 'code-block: guess\n    :linenos:\n    ')
    
    def e_informalexample(self, el):
        return self._docbook_source(el, 'INFORMALEXAMPLE')
    
    def e_calloutlist(self, el):
        return self._docbook_source(el, 'CALLOUTLIST')

    def e_xi_include(self, el):
        '''
        process Xinclude "include" directives 
        as triggered by this attribute in the root element::
        
            xmlns:xi="http://www.w3.org/2001/XInclude"

        and a statement such as this::
        
            <xi:include href="preface.xml"/>
        
        This _should_ result in a toctree entry but there may exist
        questions/problems related to file paths and subdirectories.
        For now, leave a big fat comment.
        Try to pull the referenced file from the href attribute.
        '''
        f = el.get("href", None)
        if f is None:
            s = self._docbook_source(el, "INCLUDE")
        else:
            s = "\n\n.. rubric:  INCLUDE %s\n\n" % f
        return s
    
    e_include = e_xi_include    # handle this the same way
    
    # general inline elements
    
    def e_emphasis(self, el):
        return "*%s*" % self._concat(el).strip()
    e_phrase = e_emphasis
    e_citetitle = e_emphasis
    e_replaceable = e_emphasis

    def e_literal(self, el):
        return "``%s``" % self._concat(el).strip()
    e_code = e_literal
    
    def e_firstterm(self, el):
        self._has_only_text(el)
        return ":dfn:`%s`" % el.text
    
    def e_acronym(self, el):
        if el.attrib.get('condition'):      # TODO: confirm if needs: self.parent.ns+
            return u":abbr:`%s (%s)`" % (el.text, el.attrib['condition'])
        else:
            return u":abbr:`%s`" % (el.text, )
    
    def e_userinput(self, el):
        return u":kbd:`%s`" % (el.text, )

    def e_quote(self, el):
        q = " ".join( el.text.split("\n") )
        return u'"%s"' % (q, )
    
    # links
    
    def e_ulink(self, el):
        url = el.get("url")      # TODO: confirm if needs: self.parent.ns+
        text = self._concat(el).strip()
        if text.startswith(".. image::"):
            return "%s\n   :target: %s\n\n" % (text, url)
        elif url == text:
            return text
        elif text.strip():
            return "`%s <%s>`_" % (text, url)
        else:
            return "`%s <%s>`_" % (url, url)
    
    # TODO:
    # put labels where referenced ids are 
    # e.g. <appendix id="license"> -> .. _license:\n<appendix>
    # if the label is not before title, we need to give explicit title:
    # :ref:`Link title <label-name>`
    # (in DocBook was: the section called �Variables�)
    
    def e_xref(self, el):
        return ":ref:`%s`" % el.get("linkend")      # TODO: confirm if needs: self.parent.ns+
    
    def e_link(self, el):
        # <link linkend="">some text</link>
        # <link xlink:href="#RegExpName"/>
        # <link xlink:href="#RegExpName">regular expression example</link>
        text = self._concat(el).strip().strip("`")
        # TODO: handle properly
        link = el.get( self.parent.linkend )      # TODO: confirm if needs: self.parent.ns+
        if link is None:
            return ":ref:`%s`" % text
        else:
            if text is None or len(text) == 0 or text.strip("`") == link:
                return ":ref:`%s`" % link.lstrip('#')
            else:
                return ":ref:`%s <%s>`" % (text, link.lstrip('#'))
    
    
    # math and media
    # the DocBook syntax to embed equations is sick. Usually, (inline)equation is
    # a (inline)mediaobject, which is imageobject + textobject
    
    def e_inlineequation(self, el):
        self._supports_only(el, (self.parent.ns+"inlinemediaobject",))
        return self._concat(el).strip()
    
    def e_informalequation(self, el):
        self._supports_only(el, (self.parent.ns+"mediaobject",))
        return self._concat(el)
    
    def e_equation(self, el):
        self._supports_only(el, (self.parent.ns+"title", self.parent.ns+"mediaobject"))
        title = el.find(self.parent.ns+"title")
        if title is not None:
            s = "\n\n**%s:**" % self._concat(title).strip()
        else:
            s = ""
        for mo in el.findall(self.parent.ns+"mediaobject"):
            s += "\n" + self._conv(mo)
        return s
    
    def e_mediaobject(self, el, substitute=False):
        self._supports_only(el, (self.parent.ns+"imageobject", self.parent.ns+"textobject"))
        # assume the most common case is one imageobject and one (or none)
        alt = ""
        for txto in el.findall(self.parent.ns+"textobject"):
            self._supports_only(txto, (self.parent.ns+"phrase",))
            if alt:
                alt += "; "
            alt += self._normalize_whitespace(self._concat(txto.find(self.parent.ns+"phrase")))
        symbols = []
        img = ""
        for imgo in el.findall(self.parent.ns+"imageobject"):
            self._supports_only(imgo, (self.parent.ns+"imagedata",))
            fileref = imgo.find(self.parent.ns+"imagedata").get("fileref")      # TODO: confirm if needs: self.parent.ns+
            s = "\n\n.. image:: %s" % fileref
            if (alt):
                s += "\n   :alt: %s" % alt
            if substitute:
                if fileref not in self._substitutions:
                    img += s[:4] + " |%s|" % fileref + s[4:] # insert |symbol|
                    self._substitutions.add(fileref)
                symbols.append(fileref)
            else:
                img += s
        img += "\n\n"
        if substitute:
            return img, symbols
        else:
            return img
    
    def e_inlinemediaobject(self, el):
        subst, symbols = self.mediaobject(el, substitute=True)
        self._buffer += subst
        return "".join("|%s|" % i for i in symbols)
    
    def e_subscript(self, el):
        return "\ :sub:`%s`" % self._concat(el).strip()
    
    def e_superscript(self, el):
        return "\ :sup:`%s`" % self._concat(el).strip()
    
    
    # GUI elements
    
    def e_menuchoice(self, el):
        if all(i.tag in ("guimenu", "guimenuitem") for i in el.getchildren()):
            self._has_no_text(el)
            return ":menuselection:`%s`" % \
                    " --> ".join(i.text for i in el.getchildren())
        else:
            return self._concat(el)
    
    def e_guilabel(self, el):
        self._has_only_text(el)
        return ":guilabel:`%s`" % el.text.strip()
    e_guiicon = e_guilabel
    e_guimenu = e_guilabel
    e_guimenuitem = e_guilabel
    e_mousebutton = _no_special_markup
    
    e_uri = _no_special_markup
    
    # system elements
    
    def e_keycap(self, el):
        self._has_only_text(el)
        return ":kbd:`%s`" % el.text
    
    def e_application(self, el):
        self._has_only_text(el)
        return ":program:`%s`" % el.text.strip()
    
    def e_userinput(self, el):
        return "``%s``" % self._concat(el).strip()
    
    e_systemitem = e_userinput
    e_prompt = e_userinput
    
    def e_filename(self, el):
        self._has_only_text(el)
        return ":file:`%s`" % el.text
    
    def e_command(self, el):
        return ":command:`%s`" % self._concat(el).strip()
    
    def e_parameter(self, el):
        if el.get("class"): # this hack is specific for fityk manual
            return ":option:`%s`" % self._concat(el).strip()
        return self.e_emphasis(el)
    
    def e_cmdsynopsis(self, el):
        # just remove all markup and remember to change it manually later
        return "\n\nCMDSYN: %s\n" % self._no_markup(el)
    
    # programming elements
    
    def e_function(self, el):
        #self._has_only_text(el)
        #return ":func:`%s`" % self._concat(el)
        return "``%s``" % self._concat(el).strip()
    
    def e_constant(self, el):
        self._has_only_text(el)
        #return ":constant:`%s`" % el.text
        return "``%s``" % ((el.text or '') + ''.join(map(self._conv, el.getchildren())))
    
    e_varname = e_constant
    
    # popular block elements
    
    def e_title(self, el):
        # Titles in some elements may be handled from the title's parent.
        t = self._concat(el).strip()
        level = self._get_level(el)
        parent = el.getparent().tag
        ## title in elements other than the following will trigger assertion
        #if parent in ("book", "chapter", "section", "variablelist", "appendix"):
        return self._make_title(t, level)
    e_screen = _literal_source
    e_literallayout = _literal_source
    e_programlisting = _literal_source
    
    def e_blockquote(self, el):
        return self._indent(el, 4)
    
    e_set = _no_special_markup
    e_volume = _no_special_markup
    e_book = _no_special_markup
    e_article = _no_special_markup
    e_para = _block_separated_with_blank_line
    e_section = _block_separated_with_blank_line
    e_appendix = _block_separated_with_blank_line
    e_chapter = _block_separated_with_blank_line
    e_preface = _block_separated_with_blank_line
    e_simplesect = _block_separated_with_blank_line
    e_revhistory = _block_separated_with_blank_line
    e_info = _block_separated_with_blank_line
    
    def e_revhistory(self, el):
        # TODO: only make a title here if no title has been defined
        s = self._make_title("Revision History", 1)
        s += self._block_separated_with_blank_line(el)
        return s
    
    def e_entry(self, el):
        # TODO: FIXME: <entry spanname="fullrow" ...  
        # This is not handled now and raises exception at runtime due to short list
        s = self._concat(el)
        if s is None:
            s = ""
        return s.strip()
    
    # lists
    
    def e_glosslist(self, el):
        self._supports_only(el, (self.parent.ns+"glossentry"))
        return self._concat(el)
    
    def e_glossentry(self, el):
        self._supports_only(el, (self.parent.ns+"glossterm", 
                                 self.parent.ns+"glossdef"))
        s = "\n\n"
        t = self._concat( el.find(self.parent.ns+"glossterm") ) + "\n" + " "*4
        s += self._indent(el.find(self.parent.ns+"glossdef"), 4, t)
        return s
    
    def e_glossterm(self, el):
        return self._concat(el)
    
    def e_glossdef(self, el):
        return self._join_children(el, ", ")
    
    def e_itemizedlist(self, el, bullet="-"):
        # ItemizedList ::= (ListItem+)
        s = ""
        for i in el.getchildren():
            s += self._indent(i, len(bullet)+1, bullet+" ")
        return s + "\n\n"
    
    def e_orderedlist(self, el):
        # OrderedList ::= (ListItem+)
        return self.e_itemizedlist(el, bullet="#.")
    
    def e_simplelist(self, el):
        # SimpleList ::= (Member+)
        # The simplelist is the most complicated one. There are 3 kinds of 
        # SimpleList: Inline, Horiz and Vert.
        if el.get("type") == "inline":      # TODO: confirm if needs: self.parent.ns+
            return self._join_children(el, ", ")
        else:
            # members should be rendered in tabular fashion, with number
            # of columns equal el[columns]
            # but we simply transform it to bullet list
            return self.e_itemizedlist(el, bullet="+")
    
    def e_variablelist(self, el):
        #VariableList ::= ((Title,TitleAbbrev?)?, VarListEntry+)
        #VarListEntry ::= (Term+,ListItem)
        self._supports_only(el, (self.parent.ns+"title", self.parent.ns+"varlistentry"))
        s = ""
        title = el.find(self.parent.ns+"title")
        if title is not None:
            s += self._conv(title)
        for entry in el.findall(self.parent.ns+"varlistentry"):
            s += "\n\n"
            s += ", ".join(self._concat(i).strip() for i in entry.findall(self.parent.ns+"term"))
            s += self._indent(entry.find(self.parent.ns+"listitem"), 4)[1:]
        return s
    
    def e_qandaset(self, el):
        #self._supports_only(el, ("qandaentry", "question", "answer"))
        s = ""
        for entry in el.findall(self.parent.ns+"qandaentry"):
            q = " ".join(self.childNodeText(entry, "question").split("\n"))
            s += "\n\n#. %s" % q
            # TODO: check this!
            s += "\n\n%s" % self._indent( entry.find(self.parent.ns+"answer"), 4)
        return s
    #e_question = _no_special_markup
    #e_answer = _no_special_markup
    
    def childNodeText(self, el, tag):
        '''looks for a child XML node and returns its text, or None'''
        result = el.find(self.parent.ns+tag)
        if result is not None:
            result = self._concat(result).strip()
        return result

    def e_index(self, el):
        ''' <index/> directive automatically handled by sphinx '''
        return ''

    def e_indexterm(self, el):
        ''' 
        In sphinx v1.1, an index role was added.
        Now assume all <indexentry> elements are to be :index:`tag`.
        (http://sphinx.pocoo.org/markup/misc.html#role-index)
        
        This DocBook code::

            <indexterm>
                <primary>NeXus International Advisory Committee</primary>
                <see>NIAC</see>
            </indexterm>
            <indexterm significance="preferred"><primary>units</primary></indexterm>
        
        should generate this ReST code::
        
            :index:`see: NeXus International Advisory Committee; NIAC `
            :index:`! units`
        '''
        if len(el.findall(self.parent.ns+"primary")) == 0:
            raise RuntimeError, "indexterm has no primary element"
        self._supports_only(el, (self.parent.ns + 'primary',
                                 self.parent.ns + 'secondary',
                                 self.parent.ns + 'tertiary',
                                 self.parent.ns + 'see',
                                 self.parent.ns + 'seealso',))
        # TODO need routines for primary, secondary, tertiary
        pri = self.childNodeText(el, "primary").strip("`")
        s = ""
        for term in ('see', 'seealso', ):
            text = self.childNodeText(el, term)
            if text is not None:
                if len(s) > 0:
                    s += " "
                s += ":index:`INDEX_POINT <%s: %s; %s>`" % (term, pri, text)
        if len(s) == 0:
            if el.attrib.get('significance', "").lower() == "preferred":
                s += "! "
            s += pri
            sec = self.childNodeText(el, "secondary")
            if sec is not None:
                s += "; " + sec.strip("`")
            # ReST and Sphinx do not provide for tertiary index specifications.
            # Do the best we can here.
            ter = self.childNodeText(el, "tertiary")
            if ter is not None:
                s += " - " + ter.strip("`")
            # still need to edit the ReST to replace INDEX_POINT with short printable text.
	    s = ":index:`INDEX_POINT <single: %s>`" % s
        return s
    e_primary = _no_special_markup
    e_secondary = _no_special_markup
    e_tertiary = _no_special_markup
    
    def e_footnote(self, el):
        self._supports_only(el, (self.parent.ns+"para",))
        s = "{FOOTNOTE: %s}" % self._conv(el.find(self.parent.ns+"para")).strip()
        return s
    
    # admonition directives
    
    def e_note(self, el):
        return self._directive(el, 'note:')
    def e_caution(self, el):
        return self._directive(el, 'caution:')
    def e_important(self, el):
        return self._directive(el, 'important:')
    def e_tip(self, el):
        return self._directive(el, 'tip:')
    def e_warning(self, el):
        return self._directive(el, 'warning:')
    
    # bibliography
    
    def e_author(self, el):
        # <author> could be in <biblioentry> or <authorgroup>.  
        # Hope these conditionals help it apply to both.
        self._supports_only(el, (self.parent.ns+"personname", 
                                 self.parent.ns+"address", 
                                 self.parent.ns+"affiliation", 
                                 self.parent.ns+"email",))
        s = "\n\n"
        s += self._conv(el.find(self.parent.ns+"personname")).strip()
        node = el.find(self.parent.ns+"email")
        if node is not None:
            s += " ``<%s>``" % self._conv(node).strip()
        node = el.find(self.parent.ns+"affiliation")
        if node is not None:
            s += ", " + self._conv(node).strip()
        node = el.find(self.parent.ns+"address")
        if node is not None:
            s += ", " + self._join_children(node, ", ").strip()
        return s
    
    def e_personname(self, el):
        #self._supports_only(el, (self.parent.ns+"firstname", self.parent.ns+"surname"))
        #return el.findtext(self.parent.ns+"firstname") + " " + el.findtext(self.parent.ns+"surname")
        return self._join_children(el, " ").strip()
    
    e_editor = e_author
    e_firstname = _no_special_markup        # _has_only_text
    e_surname = _no_special_markup
    e_othername = _no_special_markup
    e_affiliation = _no_special_markup
    e_orgname = _no_special_markup
    e_city = _no_special_markup
    e_state = _no_special_markup
    e_country = _no_special_markup

    def e_email(self, el):
        self._has_only_text(el)
        return self._concat(el).strip()
    
    def e_authorgroup(self, el):
        # TODO: only make a title here if no title has been defined
	s = self._make_title("Authorgroup", 1)
	s += self._join_children(el, ", ")
        return s

    def e_biblioentry(self, el):
        self._supports_only(el, (self.parent.ns+"abbrev", 
                                 self.parent.ns+"authorgroup", 
                                 self.parent.ns+"author", 
                                 self.parent.ns+"editor", 
                                 self.parent.ns+"title",
                                 self.parent.ns+"publishername", 
                                 self.parent.ns+"pubdate", 
                                 self.parent.ns+"address"))
        s = "\n"
    
        abbrev = el.find(self.parent.ns+"abbrev")
        if abbrev is not None:
            self._has_only_text(abbrev)
            s += "[%s] " % abbrev.text
    
        auth = el.find(self.parent.ns+"authorgroup")
        if auth is None:
            auth = el.find(self.parent.ns+"author")
        if auth is not None:
            s += "%s. " % self._conv(auth)
    
        editor = el.find(self.parent.ns+"editor")
        if editor is not None:
            s += "%s. " % self._conv(editor)
    
        title = el.find(self.parent.ns+"title")
        if title is not None:
            self._has_only_text(title)
            s += "*%s*. " % title.text.strip()
    
        address = el.find(self.parent.ns+"address")
        if address is not None:
            self._supports_only(address, (self.parent.ns+"otheraddr",))
            s += "%s " % address.findtext(self.parent.ns+"otheraddr")
    
        publishername = el.find(self.parent.ns+"publishername")
        if publishername is not None:
            self._has_only_text(publishername)
            s += "%s. " % publishername.text
    
        pubdate = el.find(self.parent.ns+"pubdate")
        if pubdate is not None:
            self._has_only_text(pubdate)
            s += "%s. " % pubdate.text
        return s
    
    def e_bibliography(self, el):
        self._supports_only(el, (self.parent.ns+"biblioentry",))
        return self._make_title("Bibliography", 2) + "\n" + self._join_children(el, "\n")
    
    def e_revision(self, el):
        self._supports_only(el, (self.parent.ns+"date",
                                 self.parent.ns+"authorinitials",
                                 self.parent.ns+"revnumber",
                                 self.parent.ns+"revdescription",))
        t = []
        for k, v in {"date": "*%s*", 
                     "revnumber": "**%s**", 
                     "authorinitials": "*%s*"}.items():
            node = el.find(self.parent.ns+k)
            if node is not None:
                self._has_only_text(node)
                t.append( v % node.text )
        s = "\n\n"
        s += self._indent(el.find(self.parent.ns+"revdescription"), 4, ", ".join(t) + "\n    ")
        return s

    #  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
    #  + + + + + + + + + + + + table support + + + + + + + + + + + +
    #  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

    def _calc_col_width(self, el):
        return len(self._conv(el).strip())

    def e_table(self, el):
        # consider refactoring this code!  
        # It fails now at the zip() due to
        #     empty <entry /> DocBook elements 
        #     or <entry spanname="fullrow" ...
        # get each column size
        text = (el.getchildren()[0].text or '') + (el.getchildren()[0].tail or '') + '\n\n'
        cols = int(el.find(self.parent.ns+'tgroup').attrib['cols'])
        colsizes = self._column_widths(el)
        fmt = ' '.join(['%%-%is' % (size,) for size in colsizes]) + '\n'
        divider = fmt % tuple(['=' * size for size in colsizes])
        text += divider
        node = el.find(self.parent.ns+'tgroup').find(self.parent.ns+'thead')
        if node is not None:
            text += fmt % tuple(map(self._conv, node.find(self.parent.ns+'row').findall(self.parent.ns+'entry')))
        text += divider
        for row in el.find(self.parent.ns+'tgroup').find(self.parent.ns+'tbody').findall(self.parent.ns+'row'):
            text += fmt % tuple(map(self._conv, row.findall(self.parent.ns+'entry')))
        text += divider
        return text
    
    def _column_widths(self, el):
        ''' returns a list with the maximum width of each column '''
        # FIXME: This fails on empty <entry /> DocBook elements at the zip().
        # TODO: make this code more obvious and easier to maintain
        return map(max, zip(*[map(self._calc_col_width, r) for r in lxml.etree.ETXPath( './/%srow' % self.parent.ns )(el)]))


def original_main(args):
    if len(args) < 2 or len(args) > 3 or args[1] == '-h' or args[1] == '--help':
        sys.stderr.write(__doc__)
        sys.exit()
    input_file = args[1]
    if len(args) == 3:
        output_dir = args[2]
    else:
        output_dir = None
    sys.stderr.write("Parsing XML file `%s'...\n" % input_file)

    converter = Db2Rst()
    result = converter.process( input_file )
    if result is not None:
        return str(result)


if __name__ == '__main__':
    result = original_main(sys.argv)
    if result is not None:
        print result

