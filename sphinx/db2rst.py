#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    DocBook to ReST converter
    =========================
    This script may not work out of the box, but is easy to extend.
    If you extend it, please send me a patch: wojdyr at gmail. 

    Docbook has >400 elements, most of them are not supported (yet).
    ``pydoc db2rst`` shows the list of supported elements.

    In reST, inline markup can not be nested (major deficiency of reST).
    Since it is not clear what to do with, say,
    <subscript><emphasis>x</emphasis></subscript>
    the script outputs incorrect (nested) reST (:sub:`*x*`)
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
import lxml.etree as ET

__contributors__ = ('Kurt McKee <contactme@kurtmckee.org>',
                    'Anthony Scopatz <ascopatz@enthought.com>',
                   )

# If this option is True, XML comment are discarded. Otherwise, they are
# converted to ReST comments.
# Note that ReST doesn't support inline comments. XML comments
# are converted to ReST comment blocks, what may break paragraphs.
REMOVE_COMMENTS = False

# id attributes of DocBook elements are translated to ReST labels.
# If this option is False, only labels that are used in links are generated.
WRITE_UNUSED_LABELS = False

# to avoid duplicate error reports
_not_handled_tags = set()

# to remember which id/labels are really needed
_linked_ids = set()

# to avoid duplicate substitutions
_substitutions = set()

# buffer that is flushed after the end of paragraph,
# used for ReST substitutions
_buffer = ""

def _main():
    if len(sys.argv) < 2 or len(sys.argv) > 3 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        sys.stderr.write(__doc__)
        sys.exit()
    input_file = sys.argv[1]
    if len(sys.argv) == 3:
        output_dir = sys.argv[2]
    else:
        output_dir = None
    sys.stderr.write("Parsing XML file `%s'...\n" % input_file)
    parser = ET.XMLParser(remove_comments=REMOVE_COMMENTS)
    tree = ET.parse(input_file, parser=parser)
    for elem in tree.getiterator():
        if elem.tag in ("xref", "link"):
            _linked_ids.add(elem.get("linkend"))
    obj = Convert(tree.getroot())
    if output_dir is not None:
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
    else:
        print obj

class Convert(object):
    def __init__(self, el):
        self.el = el
        self.files = {}

    def __str__(self):
        output = self._conv(self.el)
        # remove trailing whitespace
        output = re.sub(r"[ \t]+\n", "\n", output)
        # leave only one blank line
        output = re.sub(r"\n{3,}", "\n\n", output)
        return output.encode('utf-8')

    def _conv(self, el):
        "element to string conversion; usually calls e_element_name() to do the job"
        if hasattr(self, 'e_' + str(el.tag)):
            s = getattr(self, 'e_' + str(el.tag))(el)
            assert s, "Error: %s -> None\n" % self._get_path(el)
            return s
        elif isinstance(el, ET._Comment):
            if el.text.strip():
                return self.Comment(el)
            else:
                return u''
        else:
            if el.tag not in _not_handled_tags:
                self._warn("Don't know how to handle <%s>" % el.tag)
                #self._warn(" ... from path: %s" % self._get_path(el))
                _not_handled_tags.add(el.tag)
            return self._concat(el)
    
    def _warn(self, s):
        sys.stderr.write("WARNING: %s\n" % s)
    
    def _supports_only(self, el, tags):
        "print warning if there are unexpected children"
        for i in el.getchildren():
            if i.tag not in tags:
                self._warn("%s/%s skipped." % (el.tag, i.tag))
    
    def _what(self, el):
        "returns string describing the element, such as <para> or Comment"
        if isinstance(el.tag, basestring):
            return "<%s>" % el.tag
        elif isinstance(el, ET._Comment):
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
        # TODO: handle also Unicode: ‘ “ ’ « ¡ ¿ as preceding chars
        s = re.sub(r"([\s'\"([{</:-])" # start-string is preceded by one of these
                   r"([|*`[])" # the start-string
                   r"(\S)",    # start-string is followed by non-whitespace
                   r"\1\\\2\3", # insert backslash
                   s)
        return s
    
    def _concat(self, el):
        "concatate .text with children (self._conv'ed to text) and their tails"
        s = ""
        id = el.get("id")
        if id is not None and (WRITE_UNUSED_LABELS or id in _linked_ids):
            s += "\n\n.. _%s:\n\n" % id
        if el.text is not None:
            s += self._remove_indent_and_escape(el.text)
        for i in el.getchildren():
            s += self._conv(i)
            if i.tail is not None:
                if len(s) > 0 and not s[-1].isspace() and i.tail[0] in " \t":
                    s += i.tail[0]
                s += self._remove_indent_and_escape(i.tail)
        return s
    
    def _original_xml(self, el):
        return ET.tostring(el, with_tail=False)
    
    def _no_markup(self, el):
        s = ET.tostring(el, with_tail=False)
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
        pi = [i for i in el.iterchildren() if isinstance(i, ET._ProcessingInstruction)]
        if pi and 'filename=' in pi[0].text:
            fname = pi[0].text.split('=')[1][1:-1].split('.')[0]
            #import pdb; pdb.set_trace()
            el.remove(pi[0])
            self.files[fname] = self._conv(el)
            return "\n"
        else:
            s = "\n\n" + self._concat(el)
            global _buffer
            if _buffer:
                s += "\n\n" + _buffer
                _buffer = ""
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
    
    def Comment(self, el):
        return self._indent(el, 12, ".. COMMENT: ")
    
    
    # general inline elements
    
    def e_emphasis(self, el):
        return "*%s*" % self._concat(el).strip()
    phrase = e_emphasis
    citetitle = e_emphasis
    replaceable = e_emphasis
    
    def e_firstterm(self, el):
        self._has_only_text(el)
        return ":dfn:`%s`" % el.text
    
    def e_acronym(self, el):
        if el.attrib.get('condition'):
            return u":abbr:`%s (%s)`" % (el.text, el.attrib['condition'])
        else:
            return u":abbr:`%s`" % (el.text, )
    
    def e_userinput(self, el):
        return u":kbd:`%s`" % (el.text, )

    def e_quote(self, el):
        return u'"%s"' % (el.text, )
    
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
    # (in DocBook was: the section called “Variables”)
    
    def e_xref(self, el):
        return ":ref:`%s`" % el.get("linkend")
    
    def e_link(self, el):
        return ":ref:`%s <%s>`" % (self._concat(el).strip(), el.get("linkend"))
    
    
    # math and media
    # the DocBook syntax to embed equations is sick. Usually, (inline)equation is
    # a (inline)mediaobject, which is imageobject + textobject
    
    def e_inlineequation(self, el):
        self._supports_only(el, ("inlinemediaobject",))
        return self._concat(el).strip()
    
    def e_informalequation(self, el):
        self._supports_only(el, ("mediaobject",))
        return self._concat(el)
    
    def e_equation(self, el):
        self._supports_only(el, ("title", "mediaobject"))
        title = el.find("title")
        if title is not None:
            s = "\n\n**%s:**" % self._concat(title).strip()
        else:
            s = ""
        for mo in el.findall("mediaobject"):
            s += "\n" + self._conv(mo)
        return s
    
    def e_mediaobject(self, el, substitute=False):
        global _substitutions
        self._supports_only(el, ("imageobject", "textobject"))
        # i guess the most common case is one imageobject and one (or none)
        alt = ""
        for txto in el.findall("textobject"):
            self._supports_only(txto, ("phrase",))
            if alt:
                alt += "; "
            alt += self._normalize_whitespace(self._concat(txto.find("phrase")))
        symbols = []
        img = ""
        for imgo in el.findall("imageobject"):
            self._supports_only(imgo, ("imagedata",))
            fileref = imgo.find("imagedata").get("fileref")
            s = "\n\n.. image:: %s" % fileref
            if (alt):
                s += "\n   :alt: %s" % alt
            if substitute:
                if fileref not in _substitutions:
                    img += s[:4] + " |%s|" % fileref + s[4:] # insert |symbol|
                    _substitutions.add(fileref)
                symbols.append(fileref)
            else:
                img += s
        img += "\n\n"
        if substitute:
            return img, symbols
        else:
            return img
    
    def e_inlinemediaobject(self, el):
        global _buffer
        subst, symbols = self.mediaobject(el, substitute=True)
        _buffer += subst
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
    
    def e_screen(self, el):
        return "\n::\n" + self._indent(el, 4) + "\n"
    e_literallayout = e_screen
    e_programlisting = e_screen
    
    def e_blockquote(self, el):
        return self._indent(el, 4)
    
    e_book = _no_special_markup
    e_article = _no_special_markup
    e_para = _block_separated_with_blank_line
    e_section = _block_separated_with_blank_line
    e_appendix = _block_separated_with_blank_line
    e_chapter = _block_separated_with_blank_line
    
    
    # lists
    
    def e_itemizedlist(self, el, bullet="-"):
        # ItemizedList ::= (ListItem+)
        s = ""
        for i in el.getchildren():
            s += self._indent(i, 2, bullet+" ")
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
        self._supports_only(el, ("title", "varlistentry"))
        s = ""
        title = el.find("title")
        if title is not None:
            s += self._conv(title)
        for entry in el.findall("varlistentry"):
            s += "\n\n"
            s += ", ".join(self._concat(i).strip() for i in entry.findall("term"))
            s += self._indent(entry.find("listitem"), 4)[1:]
        return s
    
    
    # admonition directives
    
    def e_note(self, el):
        return self._indent(el, 3, ".. note:: ")
    def e_caution(self, el):
        return self._indent(el, 3, ".. caution:: ")
    def e_important(self, el):
        return self._indent(el, 3, ".. important:: ")
    def e_tip(self, el):
        return self._indent(el, 3, ".. tip:: ")
    def e_warning(self, el):
        return self._indent(el, 3, ".. warning:: ")
    
    
    # bibliography
    
    def e_author(self, el):
        self._supports_only(el, ("firstname", "surname"))
        return el.findtext("firstname") + " " + el.findtext("surname")
    
    e_editor = e_author
    
    def e_authorgroup(self, el):
        return self._join_children(el, ", ")
    
    def e_biblioentry(self, el):
        self._supports_only(el, ("abbrev", "authorgroup", "author", "editor", "title",
                            "publishername", "pubdate", "address"))
        s = "\n"
    
        abbrev = el.find("abbrev")
        if abbrev is not None:
            self._has_only_text(abbrev)
            s += "[%s] " % abbrev.text
    
        auth = el.find("authorgroup")
        if auth is None:
            auth = el.find("author")
        if auth is not None:
            s += "%s. " % self._conv(auth)
    
        editor = el.find("editor")
        if editor is not None:
            s += "%s. " % self._conv(editor)
    
        title = el.find("title")
        if title is not None:
            self._has_only_text(title)
            s += "*%s*. " % title.text.strip()
    
        address = el.find("address")
        if address is not None:
            self._supports_only(address, ("otheraddr",))
            s += "%s " % address.findtext("otheraddr")
    
        publishername = el.find("publishername")
        if publishername is not None:
            self._has_only_text(publishername)
            s += "%s. " % publishername.text
    
        pubdate = el.find("pubdate")
        if pubdate is not None:
            self._has_only_text(pubdate)
            s += "%s. " % pubdate.text
        return s
    
    def e_bibliography(self, el):
        self._supports_only(el, ("biblioentry",))
        return self._make_title("Bibliography", 2) + "\n" + self._join_children(el, "\n")

    # table support

    def _calc_col_width(self, el):
        return len(self._conv(el).strip())

    def e_table(self, el):
        # get each column size
        text = (el.getchildren()[0].text or '') + (el.getchildren()[0].tail or '') + '\n\n'
        cols = int(el.find('tgroup').attrib['cols'])
        colsizes = map(max, zip(*[map(self._calc_col_width, r) for r in el.xpath('.//row')]))
        fmt = ' '.join(['%%-%is' % (size,) for size in colsizes]) + '\n'
        text += fmt % tuple(['=' * size for size in colsizes])
        text += fmt % tuple(map(self._conv, el.find('tgroup').find('thead').find('row').findall('entry')))
        text += fmt % tuple(['=' * size for size in colsizes])
        for row in el.find('tgroup').find('tbody').findall('row'):
            text += fmt % tuple(map(self._conv, row.findall('entry')))
        text += fmt % tuple(['=' * size for size in colsizes])
        return text
        

if __name__ == '__main__':
    _main()

