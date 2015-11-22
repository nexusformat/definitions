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

import os.path
import sys
import re
import lxml.etree
import logging
import itertools

__contributors__ = ('Kurt McKee <contactme@kurtmckee.org>',
                    'Anthony Scopatz <ascopatz@enthought.com>',
                    'Pete Jemian <jemian@anl.gov>',
                   )
INDENT = ' '*4


def write_footnotes(footnotes):
    if len(footnotes) == 0:
        return None
    s = ".. rubric:: Footnote"
    if len(footnotes) > 1:
        s += "s"
    s += '\n\n'
    for note in footnotes:
        s += '.. [#] '
        if len(note.split('\n')) == 1:
            s += note + '\n'
        else:
            s += '\n'
            for line in note.split("\n"):
                s += INDENT + line + '\n'
    return s


class Db2Rst:
    ''' 
    handle conversion of DocBook source code files 
    into ReST: Restructured Text source code documents
    '''
    
    def __init__(self):
        self.remove_comments = False
        self.write_unused_labels = False
        self._linked_ids = set()        # which id/labels are really needed
        self.id_attrib = "id"           # can modify if namespace is present
        self.linkend = "linkend"        # can modify if namespace is present
        self.output_dir = None          # if converting a set of docbook files
        self.namespacePrefix = None     # as used in the DocBook file
        self.ns = ""
    
    def process(self, dbfile, converter=None):
        '''
        process one DocBook XML file
        
        :param str dbfile: name of DocBook source code file
        :param obj converter: optional subclass override of Convert
        :return: None or string buffer with converted ReST source
        '''
        logging.info('parsing %s with converter %s' % (dbfile, str(converter)))
        parser = lxml.etree.XMLParser(remove_comments=self.remove_comments)
        logging.info('created the parser')
        tree = lxml.etree.parse(dbfile, parser=parser)
        logging.info('parsed XML file')
        root = tree.getroot()
        if self.namespacePrefix in root.nsmap:
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
            if elem.tag in (self.ns + "xref", self.ns + "link"):
                for nskey, nsstr in elem.nsmap.items():
                    ns = "{%s}" % nsstr
                    for term in ('linkend', 'href'):
                        text = elem.get(ns + term)
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
            f = open(os.path.join(self.output_dir, fname + '.rst'), 'wb')
            f.write(obj.files[fname].encode('utf-8').strip())
            f.close()
        # write the index if it doesn't exist already
        if 'index' not in obj.files:
            f = open(os.path.join(self.output_dir, 'index.rst'), 'wb')
            f.write(output)
            f.write('\n\n.. toctree::\n   :maxdepth: 1\n\n')
            for fname in sorted(obj.files):
                f.write('   %s\n' % (fname,))
            f.close()
        # write a simple conf.py
        c = open(os.path.join(self.output_dir, 'conf.py'), 'wb')
        c.write("extensions = []\n")
        c.write("master_doc = 'index'\n")
        c.write("project = u'projname'\n")
        c.write("#copyright = u'2012, authname'\n")
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
    
    def __init__(self, el, parent=None, namespace=None):
        self.el = el
        self.files = {}
        if parent is None:
            parent = Db2Rst()       # looks inverted, provides basic constants
        if namespace is not None:
            parent.ns = "{%s}" % namespace
        self.parent = parent        # object that called the converter
        self._not_handled_tags = set()      # to avoid duplicate error reports
        self._substitutions = set()         # to avoid duplicate substitutions
        
        # _buffer is flushed after the end of paragraph
        # used for ReST substitutions
        self._buffer = ""
        self.footnotes = []

    def __str__(self):
        output = self._conv(self.el)
        
        notes = write_footnotes(self.footnotes)
        if notes is not None:
            output += '\n' + notes

        # remove trailing whitespace
        output = re.sub(r"[ \t]+\n", "\n", output)
        # leave only one blank line
        output = re.sub(r"\n{3,}", "\n\n", output)
        return output.encode('utf-8')

    def _conv(self, el, do_assert=True):
        '''
        Element to string conversion.
        Looks for a defined function e_tag() and calls it,
        where tag is the element name.
        The function e_tag() has one argument, 
        the DocBook element node to process.
        '''
        tag = str(el.tag)
        if tag == "<built-in function ProcessingInstruction>":
            logging.info("_conv(): line %d in %s" % (el.sourceline, 
                                                     str(el.base)))
            logging.info("ignoring ProcessingInstruction for now")
            return ""
        if tag == "<built-in function Comment>":
            #logging.info("_conv(): line %d in %s" % (el.sourceline, 
            #                                         str(el.base)))
            #logging.info("ignoring Comment for now")
            return self.Comment(el)
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
        #
        #if len(self.footnotes):
        #    print len(self.footnotes), self._what(el)
        #
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
            self._warn("skipping text of <%s>: %s" % (self._get_path(el), 
                                                      el.text))
        for i in el.getchildren():
            if i.tail is not None and not i.tail.isspace():
                self._warn("skipping tail of <%s>: %s" % (self._get_path(i), 
                                                          i.tail))
    
    def _no_special_markup(self, el):
        return self._concat(el)
    
    def _remove_indent_and_escape(self, s):
        """
        remove indentation from the string s
        escape some of the special chars
        """
        s = "\n".join(i.lstrip().replace("\\", "\\\\") for i in s.splitlines())
        # escape inline mark-up start-string characters (even if there is no
        # end-string, docutils show warning if the start-string is not escaped)
        # TODO: handle also Unicode: � � � � � � as preceding chars
        s = re.sub(r"([\s'\"([{</:-])" # start-string is preceded by one of these
                   r"([|*`[])" # the start-string
                   r"(\S)", # start-string is followed by non-whitespace
                   r"\1\\\2\3", # insert backslash
                   s)
        return s
    
    def _concat(self, el):
        """
        concatenate .text with children (self._conv'ed to text) and their tails
        """
        s = ""
        xml_id = el.get(self.parent.id_attrib)
        if xml_id is not None and (
                self.parent.write_unused_labels 
                or xml_id in self.parent._linked_ids):
            s += "\n\n.. _%s:\n\n" % xml_id
        if el.text is not None:
            s += self._remove_indent_and_escape(el.text)
        for i in el.getchildren():
            # FIXME: fails for an empty <entry> element in a <table>
            s += self._conv(i)
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
        return sum(1 for _ in el.iterancestors())
    
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
        return "\n\n" + t + "\n" + char[level - 2] * len(t)
    
    def _join_children(self, el, sep):
        self._has_no_text(el)
        return sep.join(self._conv(i) for i in el.getchildren())
    
    def _block_separated_with_blank_line(self, el):
        pi = [i for i in el.iterchildren() if isinstance(i, 
                                         lxml.etree._ProcessingInstruction)]
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
    
    ###################      DocBook elements    #####################
    
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
        s += INDENT + self._original_xml(el)
        s += "\n\n"
        return s
    
    def _include_source(self, el):
        s = "literalinclude:: %s\n"
        s += INDENT + ":language: %s\n"
        s += INDENT + ":linenos:\n"
        s += INDENT + ":tab-width: %s\n"
        s += "\n" + INDENT
        return self._directive(el, s)
    
    def _literal_source(self, el):
        #return "\n::\n" + self._indent(el, 4) + "\n"
        #s = "\n\n.. code-block:: guess"
        return self._directive(el, 'code-block: guess\n    :linenos:\n\n    ')
    
    def Comment(self, el):
        return self._indent(el, 4, "..  ")

    def ProcessingInstruction(self, el):
        # TODO: How/where to call this?
        return self._docbook_source(el, "ProcessingInstruction")
    
    def e_figure(self, el):
        return self._docbook_source(el, 'FIGURE')
    
    def e_example(self, el):
        return self._docbook_source(el, 'EXAMPLE')
    
    def e_informalexample(self, el):
        return self._docbook_source(el, 'INFORMALEXAMPLE')
    
    def e_calloutlist(self, el):
        return self._docbook_source(el, 'CALLOUTLIST')

    def e_include(self, el):
        '''
        process  "include" directives 
        as triggered by a statement such as this::
        
            <include href="preface.xml"/>
        
        This produces the ReST result::
        
            .. include:: preface.xml
        '''
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        href = el.get('href', None)
        if href is not None:
            return "\n\n.. include:: %s\n\n" % href
        return "\n\n.. UNHANDLED LINE %d in %s" % (el.sourceline, str(el.base))
    
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
        if el.attrib.get('condition'):
            return u":abbr:`%s (%s)`" % (el.text, el.attrib['condition'])
        else:
            return u":abbr:`%s`" % (el.text,)
    
    #def e_userinput(self, el):
    #    return u":kbd:`%s`" % (el.text,)

    def e_quote(self, el):
        q = " ".join(el.text.split("\n"))
        return u'"%s"' % (q,)
    
    # links
    
    def e_ulink(self, el):
        url = el.get("url")
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
        return ":ref:`%s`" % el.get("linkend")
    
    def e_link(self, el):
        # <link linkend="">some text</link>
        # <link xlink:href="#RegExpName"/>
        # <link xlink:href="#RegExpName">regular expression example</link>
        text = self._concat(el).strip().strip("`")
        # TODO: handle properly
        link = el.get(self.parent.linkend)
        if link is None:
            return ":ref:`%s`" % text
        else:
            if text is None or len(text) == 0 or text.strip("`") == link:
                return ":ref:`%s`" % link.lstrip('#')
            else:
                return ":ref:`%s <%s>`" % (text, link.lstrip('#'))
    
    
    # math and media
    # the DocBook syntax to embed equations is sick. 
    # Usually, (inline)equation is
    # a (inline)mediaobject, which is imageobject + textobject
    
    def e_inlineequation(self, el):
        self._supports_only(el, (self.parent.ns + "inlinemediaobject",))
        return self._concat(el).strip()
    
    def e_informalequation(self, el):
        self._supports_only(el, (self.parent.ns + "mediaobject",))
        return self._concat(el)
    
    def e_equation(self, el):
        self._supports_only(el, (self.parent.ns + "title", 
                                 self.parent.ns + "mediaobject"))
        title = el.find(self.parent.ns + "title")
        if title is not None:
            s = "\n\n**%s:**" % self._concat(title).strip()
        else:
            s = ""
        for mo in el.findall(self.parent.ns + "mediaobject"):
            s += "\n" + self._conv(mo)
        return s
    
    def e_mediaobject(self, el, substitute=False):
        self._supports_only(el, (self.parent.ns + "imageobject", 
                                 self.parent.ns + "textobject"))
        # assume the most common case is one imageobject and one (or none)
        alt = ""
        for txto in el.findall(self.parent.ns + "textobject"):
            self._supports_only(txto, (self.parent.ns + "phrase",))
            if alt:
                alt += "; "
            alt += self._normalize_whitespace(
                          self._concat(txto.find(self.parent.ns + "phrase")))
        symbols = []
        img = ""
        for imgo in el.findall(self.parent.ns + "imageobject"):
            self._supports_only(imgo, (self.parent.ns + "imagedata",))
            fileref = imgo.find(self.parent.ns + "imagedata").get("fileref")
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
        return "``%s``" % self._concat(el).strip()
    
    def e_constant(self, el):
        self._has_only_text(el)
        return "``%s``" % (
                           (el.text or '') + 
                           ''.join(map(self._conv, el.getchildren())))
    
    e_varname = e_constant
    
    # popular block elements
    
    def e_title(self, el):
        # Titles in some elements may be handled from the title's parent.
        t = self._concat(el).strip()
        level = self._get_level(el)
        #parent = el.getparent().tag
        ## title in elements other than the following will trigger assertion
        #? parent in ("book", "chapter", "section", "variablelist", "appendix")
        return self._make_title(t, level)
    e_screen = _literal_source
    e_literallayout = _literal_source
    e_programlisting = _include_source
    
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
        # This is not handled now and raises exception at runtime 
        # due to short list
        s = self._concat(el)
        if s is None:
            s = ""
        return s.strip()
    
    # lists
    
    def e_glosslist(self, el):
        self._supports_only(el, (self.parent.ns + "glossentry"))
        return self._concat(el)
    
    def e_glossentry(self, el):
        self._supports_only(el, (self.parent.ns + "glossterm",
                                 self.parent.ns + "glossdef"))
        s = "\n\n"
        t = self._concat(el.find(self.parent.ns + "glossterm")) + "\n" + " "*4
        s += self._indent(el.find(self.parent.ns + "glossdef"), 4, t)
        return s
    
    def e_glossterm(self, el):
        return self._concat(el)
    
    def e_glossdef(self, el):
        return self._join_children(el, ", ")
    
    def e_itemizedlist(self, el, bullet="-"):
        # ItemizedList ::= (ListItem+)
        s = ""
        for i in el.getchildren():
            s += self._indent(i, len(bullet) + 1, bullet + " ")
        return s + "\n\n"
    
    def e_orderedlist(self, el):
        # OrderedList ::= (ListItem+)
        return self.e_itemizedlist(el, bullet="#.")
    
    def e_simplelist(self, el):
        # SimpleList ::= (Member+)
        # The simplelist is the most complicated one. There are 3 kinds of 
        # SimpleList: Inline, Horiz and Vert.
        if el.get("type") == "inline":
            return self._join_children(el, ", ")
        else:
            # members should be rendered in tabular fashion, with number
            # of columns equal el[columns]
            # but we simply transform it to bullet list
            return self.e_itemizedlist(el, bullet="+")
    
    def e_variablelist(self, el):
        #VariableList ::= ((Title,TitleAbbrev?)?, VarListEntry+)
        #VarListEntry ::= (Term+,ListItem)
        self._supports_only(el, (self.parent.ns + "title", 
                                 self.parent.ns + "varlistentry"))
        s = ""
        title = el.find(self.parent.ns + "title")
        if title is not None:
            s += self._conv(title)
        for entry in el.findall(self.parent.ns + "varlistentry"):
            s += "\n\n"
            s += ", ".join(self._concat(i).strip() 
                           for i in entry.findall(self.parent.ns + "term"))
            s += self._indent(entry.find(self.parent.ns + "listitem"), 4)[1:]
        return s
    
    def e_qandaset(self, el):
        #self._supports_only(el, ("qandaentry", "question", "answer"))
        s = ""
        for entry in el.findall(self.parent.ns + "qandaentry"):
            q = " ".join(self.childNodeText(entry, "question").split("\n"))
            s += "\n\n#. %s" % q
            # TODO: check this!
            s += "\n\n%s" % self._indent(entry.find(self.parent.ns + "answer"), 4)
        return s
    #e_question = _no_special_markup
    #e_answer = _no_special_markup
    
    def childNodeText(self, el, tag):
        '''looks for a child XML node and returns its text, or None'''
        result = el.find(self.parent.ns + tag)
        if result is not None:
            result = self._concat(result).strip()
        return result

    def e_index(self, el):
        ''' <index/> directive automatically handled by sphinx '''
        return ''

    def e_indexterm(self, el):
        # http://www.docbook.org/tdg/en/html/indexterm.html
        '''
        The resulting .rst document will contain some entries such as::
        
            :index:`EDIT_ME <!NAPI>`
        
        Since the EDIT_ME text will appear in the final, formatted document, 
        it is necessary to replace EDIT_ME with appropriate text from the local context
        and weave this index entry into the local context.
        
        * Use the index role (requires sphinx v.1.1+) for all DocBook <indexterm> elements
        * use the (implied) single option as default
        * avoid the triple option, it looks bad due to the commas
        * options for 'see' (and 'seealso' treated synonymously) should be entered as additional index roles
        '''
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        preferred_significance = el.get("significance", "normal") == 'preferred'
        nodes = [el.find(self.parent.ns+t) for t in ('primary', 'secondary', 'tertiary')]
        s = ""
        if len([c for c in nodes if c is not None]) > 0:
            terms = [self._concat(node).strip() for node in nodes if node is not None]
            items = "; ".join(terms)
            if preferred_significance:
                items = "!" + items
            s += ":index:`EDIT_ME <%s>` " % items     # EDIT_ME will appear in the formatted text, fix it in the editor
        
        # are there any "see" or "seealso" elements?
        related_nodes =  [el.find(self.parent.ns+t) for t in ('see', 'seealso')]
        if len([c for c in related_nodes if c is not None]) > 0:
            seealso_terms = [self._concat(node).strip() for node in related_nodes if node is not None]
            items = "; ".join(list(itertools.chain(*[seealso_terms, [terms[0]]])))
            s += ":index:`EDIT_ME <see: %s>` " % items
        return s
    
    def e_footnote(self, el):
        '''
        Collect the content of footnotes in a queue.
        Return a generic reference ([#]_) for now.
        Write out the queue contents later.
        "Later" could be when the file is done processing, 
        before writing, or earlier.
        '''
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        s = self._concat(el).strip()
        self.footnotes.append(s)
        return ' [#]_'
    
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
        self._supports_only(el, (self.parent.ns + "personname",
                                 self.parent.ns + "address",
                                 self.parent.ns + "affiliation",
                                 self.parent.ns + "email",))
        s = "\n\n"
        s += self._conv(el.find(self.parent.ns + "personname")).strip()
        node = el.find(self.parent.ns + "email")
        if node is not None:
            s += " ``<%s>``" % self._conv(node).strip()
        node = el.find(self.parent.ns + "affiliation")
        if node is not None:
            s += ", " + self._conv(node).strip()
        node = el.find(self.parent.ns + "address")
        if node is not None:
            s += ", " + self._join_children(node, ", ").strip()
        return s
    
    def e_personname(self, el):
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
        self._supports_only(el, (self.parent.ns + "abbrev",
                                 self.parent.ns + "authorgroup",
                                 self.parent.ns + "author",
                                 self.parent.ns + "editor",
                                 self.parent.ns + "title",
                                 self.parent.ns + "publishername",
                                 self.parent.ns + "pubdate",
                                 self.parent.ns + "address"))
        s = "\n"
    
        abbrev = el.find(self.parent.ns + "abbrev")
        if abbrev is not None:
            self._has_only_text(abbrev)
            s += "[%s] " % abbrev.text
    
        auth = el.find(self.parent.ns + "authorgroup")
        if auth is None:
            auth = el.find(self.parent.ns + "author")
        if auth is not None:
            s += "%s. " % self._conv(auth)
    
        editor = el.find(self.parent.ns + "editor")
        if editor is not None:
            s += "%s. " % self._conv(editor)
    
        title = el.find(self.parent.ns + "title")
        if title is not None:
            self._has_only_text(title)
            s += "*%s*. " % title.text.strip()
    
        address = el.find(self.parent.ns + "address")
        if address is not None:
            self._supports_only(address, (self.parent.ns + "otheraddr",))
            s += "%s " % address.findtext(self.parent.ns + "otheraddr")
    
        publishername = el.find(self.parent.ns + "publishername")
        if publishername is not None:
            self._has_only_text(publishername)
            s += "%s. " % publishername.text
    
        pubdate = el.find(self.parent.ns + "pubdate")
        if pubdate is not None:
            self._has_only_text(pubdate)
            s += "%s. " % pubdate.text
        return s
    
    def e_bibliography(self, el):
        self._supports_only(el, (self.parent.ns + "biblioentry",))
        s = self._make_title("Bibliography", 2) + "\n"
        s += self._join_children(el, "\n")
        return s
    
    def e_revision(self, el):
        self._supports_only(el, (self.parent.ns + "date",
                                 self.parent.ns + "authorinitials",
                                 self.parent.ns + "revnumber",
                                 self.parent.ns + "revdescription",))
        t = []
        for k, v in {"date": "*%s*",
                     "revnumber": "**%s**",
                     "authorinitials": "*%s*"}.items():
            node = el.find(self.parent.ns + k)
            if node is not None:
                self._has_only_text(node)
                t.append(v % node.text)
        s = "\n\n"
        s += self._indent(el.find(self.parent.ns + "revdescription"), 
                          4, ", ".join(t) + "\n    ")
        return s

    def e_table(self, el):
        # Probably fails for these cases at least:
        #     * <entry /> (empty DocBook elements) 
        #     * <entry spanname="fullrow" ...
        t = Table()
        tgroup_node = el.find(self.parent.ns+'tgroup')
        thead = tgroup_node.find(self.parent.ns+'thead')
        if thead is not None:
            row = thead.find(self.parent.ns+'row')
            t.labels = self._get_entry_text_list( row )

        tbody = tgroup_node.find(self.parent.ns+'tbody')
        t.rows = map(self._get_entry_text_list, 
                     tbody.findall(self.parent.ns+'row'))

        s = t.reST(fmt='simple')
        return s
    
    def _get_entry_text_list(self, parent_node):
        '''
        Return a list with the text of the child "entry" nodes.
        The members of the list are strings with optional line breaks.
        This is useful in the analysis of tables.
        '''
        nodes = parent_node.findall(self.parent.ns+'entry')
        rowText = [self._conv(item).split("\n") for item in nodes]
        return map( "\n".join, rowText)


class Table:
    '''
    Construct a table in reST (no row or column spans).
    Each cell may have multiple lines, separated by "\n"
    
    EXAMPLE
    
    These commands::
    
        t = Table()
        t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
        t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
        t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
        print t.reST(fmt='complex')

    build this table source code::
    
        +------------+-----------+--------+-------------------+
        + Name       + Type      + Units  + Description       +
        + and        +           +        + (and Occurrences) +
        + Attributes +           +        +                   +
        +============+===========+========+===================+
        + one,       + buckle my + shoe.  + ...               +
        + two        +           +        +                   +
        +            +           +        +                   +
        +            +           + three, +                   +
        +            +           + four   +                   +
        +------------+-----------+--------+-------------------+
        + class      + NX_FLOAT  + ..     + ..                +
        +------------+-----------+--------+-------------------+
    '''
    
    def __init__(self):
        self.rows = []
        self.labels = []
    
    def reST(self, indentation = '', fmt = 'simple'):
        '''render the table in reST format'''
        return {'simple': self.simple_table,
                'complex': self.complex_table,}[fmt](indentation)
    
    def simple_table(self, indentation = ''):
        '''render the table in simple rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = " ".join(['='*w for w in width]) + '\n'
        fmt = " ".join(["%%-%ds" % w for w in width]) + '\n'
        
        rest = '%s%s' % (indentation, separator)         # top line
        rest += self._row(self.labels, fmt, indentation) # labels
        rest += '%s%s' % (indentation, separator)        # end of the labels
        for row in self.rows:
            rest += self._row(row, fmt, indentation)     # each row
        rest += '%s%s' % (indentation, separator)        # end of table
        return rest
    
    def complex_table(self, indentation = ''):
        '''render the table in complex rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = '+' + "".join(['-'*(w+2) + '+' for w in width]) + '\n'
        label_sep = '+' + "".join(['='*(w+2) + '+' for w in width]) + '\n'
        fmt = '|' + "".join([" %%-%ds |" % w for w in width]) + '\n'
        
        rest = '%s%s' % (indentation, separator)         # top line
        rest += self._row(self.labels, fmt, indentation) # labels
        rest += '%s%s' % (indentation, label_sep)         # end of the labels
        for row in self.rows:
            rest += self._row(row, fmt, indentation)     # each row
            rest += '%s%s' % (indentation, separator)    # row separator
        return rest
    
    def _row(self, row, fmt, indentation = ''):
        '''
        Given a list of <entry nodes in this table <row, 
        build one line of the table with one text from each entry element.
        The lines are separated by line breaks.
        '''
        text = ""
        if len(row) > 0:
            for line_num in range( max(map(len, [_.split("\n") for _ in row])) ):
                item = [self._pick_line(r.split("\n"), line_num) for r in row]
                text += indentation + fmt % tuple(item)
        return text
    
    def find_widths(self):
        '''
    measure the maximum width of each column, 
    considering possible line breaks in each cell
    '''
        width = []
        if len(self.labels) > 0:
            width = [max(map(len, _.split("\n"))) for _ in self.labels]
        for row in self.rows:
            row_width = [max(map(len, _.split("\n"))) for _ in row]
            if len(width) == 0:
                width = row_width
            width = map( max, zip(width, row_width) )
        return width
    
    def _pick_line(self, text, lineNum):
        '''
        Pick the specific line of text or supply an empty string.
        Convenience routine when analyzing tables.
        '''
        if lineNum < len(text):
            s = text[lineNum]
        else:
            s = ""
        return s


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
    if output_dir is not None:
        converter.output_dir = output_dir
    result = converter.process(input_file)
    if result is not None:
        return str(result)


if __name__ == '__main__':
    #result = original_main(sys.argv)
    docbook_file = 'docbook.xml'
    if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        docbook_file = sys.argv[1]
    result = original_main([sys.argv[0], docbook_file])
    if result is not None:
        print result

