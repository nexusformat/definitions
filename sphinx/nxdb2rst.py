#!/usr/bin/env python

########### SVN repository information ###################
# $Date: 2011-11-10 00:33:02 -0600 (Thu, 10 Nov 2011) $
# $Author: Pete Jemian $
# $Revision: 1009 $
# $URL: https://svn.nexusformat.org/definitions/trunk/sphinx/runner.py $
# $Id: runner.py 1009 2011-11-10 06:33:02Z Pete Jemian $
########### SVN repository information ###################

'''
Overrides certain handler routines for
translating DocBook elements into restructured 
text (reST) documents.
'''


import os
import db2rst
import lxml.etree
import logging
import argparse

NEXUS_DIR = "../docbook"
NEXUS_DIR = os.path.abspath(NEXUS_DIR)
INDENT = ' '*4
__description__ = "Translate NeXus Docbook source files into ReST source files"
__version__ = "$Id: runner.py 1009 2011-11-10 06:33:02Z Pete Jemian $"


class Convert(db2rst.Convert):
    '''
    NeXus overrides of the db2rst Convert class for these DocBook elements:
    + table
    + figure
    + informalexample
    + example
    + programlisting
    + programlistingco
    + subtitle
    + info
    + revdescription
    + legalnotice
    + revhistory
    + areaspec
    + calloutlist
    + callout
    + xi:include  where xmlns:xi="http://www.w3.org/2001/XInclude"
    '''

    def e_table(self, el):
        s = "\n\n"
        id = el.get(self.parent.id_attrib, "")
        if len(id) > 0:
            s += ".. _%s:\n\n" % id
        
        s += ".. rubric:: Table: "
        title = self.childNodeText(el, 'title')
        if title is not None:
            s += title
        s += "\n\n"
        
        t = db2rst.Table()
        tgroup_node = el.find(self.parent.ns+'tgroup')
        thead = tgroup_node.find(self.parent.ns+'thead')
        if thead is not None:
            row = thead.find(self.parent.ns+'row')
            t.labels = self.get_entry_text_list( row )

        tbody = tgroup_node.find(self.parent.ns+'tbody')
        rows = tbody.findall(self.parent.ns+'row')
        t.rows = map(self.get_entry_text_list, rows)

        s = t.reST(fmt='simple')
        return s
    
    def get_entry_text_list(self, parent_node):
        '''
        Return a list with the text of the child entry nodes.
        The members of the list are strings with optional line breaks.
        '''
        nodes = parent_node.findall(self.parent.ns+'entry')
        rowText = [self._conv(item).split("\n") for item in nodes]
        return map( "\n".join, rowText)
    
    def pick_line(self, text, lineNum):
        '''
        pick the specific line of text or supply an empty string
        '''
        if lineNum < len(text):
            s = text[lineNum]
        else:
            s = ""
        return s
    
    def e_figure(self, el):
        '''
        may contain a programlisting or a mediaobject
        
        .. figure:: nexuslogo.png
            :width: 200px
            :align: center
            :height: 100px
            :alt: alternate text
            :figclass: align-center
        '''
        id = el.get(self.parent.id_attrib, "")
        title = self.childNodeText(el, "title")
        
        content = self._concat(el).strip()
        
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        pl_node = el.find(self.parent.ns+"programlisting")
        if pl_node is not None:
            # contains a programlisting
            s = "\n\n.. compound::\n\n"
            s += INDENT + ".. rubric:: Figure: %s\n\n" % title
            for line in content.split('\n'):
                s += line + '\n'
            s += '\n' + INDENT
            return s

        mo_node = el.find(self.parent.ns+"mediaobject")
        if mo_node is None:
            return content + " --> e_figure"
        # contains a mediaobject
        
        io_node = mo_node.find(self.parent.ns+"imageobject")
        if io_node is None:
            return content + " --> e_figure"
        # contains an imageobject

        image_node = io_node.find(self.parent.ns+"imagedata")
        if image_node is None:
            return content + " --> e_figure"
        # contains imagedata
        
        #  <imagedata fileref="img/woni-schematic.png" width="240pt" scalefit="1"/>
        # .. figure:: picture.png
        #     :scale: 50 %
        #     :alt: map to buried treasure
        name = image_node.get('fileref')
        width = image_node.get('width', None)
        height = image_node.get('height', None)
        scalefit = image_node.get('scalefit', None)
        # TODO: Need to handle width
        # TODO: Need to handle scalefit
        # TODO: Is height used at all?  Might remove it.
        s = "\n\n.. compound::\n\n"
        s += INDENT + ".. _%s:\n\n" % id
        s += INDENT + ".. rubric:: Figure: %s\n\n" % title
        s += "\n\n" + ".. figure:: %s\n" % name
        s += INDENT + ":alt: %s\n" % id
        s += "\n"
        for line in str(title).split('\n'):
            s += INDENT + line + '\n'
        return s

    def e_informalexample(self, el):
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        return self._concat(el)

    def e_example(self, el):
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        id = el.get(self.parent.id_attrib, "")
        title = self.childNodeText(el, "title")
        pl_node = el.find(self.parent.ns+"programlisting")
        plco_node = el.find(self.parent.ns+"programlistingco")
        if (pl_node is not None) or (plco_node is not None):
            # contains a programlisting
            node = pl_node
            if node is None:
                node = plco_node
            s = "\n\n.. compound::\n\n"
            s += INDENT + ".. rubric:: Figure: %s\n\n" % title
            for line in self._concat(node).strip().split('\n'):
                s += line + '\n'
            s += '\n' + INDENT
            return s
        return self._concat(el).strip() + " --> e_example"

    def e_programlisting(self, el):
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        language = el.get("language", "guess")
        linenumbering = 'numbered' in el.get("linenumbering", '')
        s = self._concat(el).strip()
        lmatch = '.. include::'
        if s.startswith(lmatch):    # include a program
            s = "\n.. literalinclude:: %s\n" % s[len(lmatch):].strip()
            s += INDENT + ':tab-width: 4\n'
            if linenumbering:
                s += INDENT + ':linenos:\n'
            s += INDENT + ':language: %s\n' % language
            s += '\n' + INDENT
            return s
        
        # inline content
        t = '\n\n.. code-block:: %s\n' % language
        if linenumbering:
            t += INDENT + ':linenos:\n'
        t += '\n'
        for line in s.split('\n'):
            t += INDENT + line + '\n'
        return t

    def e_programlistingco(self, el):
        pl_node = el.find(self.parent.ns+"programlisting")
        if pl_node is not None:     # ignore the callout and just process the listing
            return self._concat(pl_node).strip()
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        return self._concat(el).strip() + " --> e_programlistingco"
    
    def e_subtitle(self, el):
        '''
        figure with a caption::
        
            .. _fig.data-pre-nexus:
            
            .. figure:: data-pre-nexus.jpg
                :width: 200 pt
                :alt: example NeXus data file hierarchy
            
                *N* separate file formats
        '''
        t = self._concat(el).strip()
        return "\n\n" + t + "\n" + "@" * len(t)
    
    def e_info(self, el):
        '''
        NeXus-style <info ... element
        '''
        s = self._make_title("Volume Information", 1)
        s += "\n\n.. rubric:: %s\n\n" % self.childNodeText(el, "title")
        s += ".. How to get the current subversion info here (from subtitle.xml or ...)?\n\n"
        s += "|today|\n\n"
        
        s += ".. author group could be shown here\n\n"

        pubdate = self.childNodeText(el, "pubdate")
        orgname = self.childNodeText(el.find(self.parent.ns+'org'), "orgname")
        uri = self.childNodeText(el.find(self.parent.ns+'org'), "uri")
        s += "Published %s by %s, %s\n\n" % (pubdate, orgname, uri)

        year = self.childNodeText(el.find(self.parent.ns+'copyright'), "year")
        holder = self.childNodeText(el.find(self.parent.ns+'copyright'), "holder")
        s += "Copyright (c) %s, %s\n\n" % (year, holder)

        s += self._make_title("Legal Notices", 2) + "\n\n"
        for notice in el.findall(self.parent.ns+'legalnotice'):
            s += self._conv(notice).strip() + "\n\n"

        s += ".. release information could be shown here\n\n"
        s += ".. revision history could be shown here\n\n"
        return s
    
    e_revdescription = db2rst.Convert._no_special_markup
    e_legalnotice = db2rst.Convert._no_special_markup

    def e_revhistory(self, el):
        '''
        Revision history of the NeXus manual
        '''
        t = db2rst.Table()
        t.labels = ('date', 'release', 'description', 'who?', )
        for revnode in el.findall(self.parent.ns+'revision'):
            node = revnode.find(self.parent.ns+'revnumber')
            if node is None:
                revnumber = ""
            else:
                revnumber = node.text
            date = self.childNodeText(revnode, "date")
            authorinitials = self.childNodeText(revnode, "authorinitials")
            revdescription = self.childNodeText(revnode, "revdescription")
            t.rows.append( [date, revnumber, revdescription, authorinitials, ] )
        
        s = self._make_title("Revision History", 1)
        s += "\n\n"
        s += t.reST(fmt='complex')
        return s

    def e_xi_include(self, el):
        '''
        process Xinclude "include" directives 
        as triggered by this attribute in the root element::
        
            xmlns:xi="http://www.w3.org/2001/XInclude"

        and a statement such as this::
        
            <xi:include href="preface.xml"/>
        
        This produces the ReST result::
        
            .. include:: preface.xml
        '''
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        href = el.get('href', None)
        if href is not None:
            return "\n\n.. include:: %s\n\n" % href
        return "\n\n.. UNHANDLED LINE %d in %s" % (el.sourceline, str(el.base))
    
    def e_areaspec(self, el):
        # related to e_calloutlist
        # idea: when the XML file is first open, 
        # parse all the \programlistingco\areaspec\\area elements
        # and build a dictionary with the coords v. xml:id
        # Then, use that dictionary when processing each callout element
        '''
                <programlistingco>
                    <areaspec>
                        <area xml:id="ex.write.open-co" linkends="ex.write.open" coords="6"/>
                        <area xml:id="ex.write.entry.group-co" linkends="ex.write.entry.group" coords="7"/>
                        <area xml:id="ex.write.data.group" coords="9"/>
                        <area xml:id="ex.write.tth.array" coords="12"/>
                        <area xml:id="ex.write.tth.array.write" coords="14"/>
                        <area xml:id="ex.write.tth.array.attr" coords="15"/>
                        <area xml:id="ex.write.tth.array.close" coords="16"/>
                        <area xml:id="ex.write.remainder" coords="17"/>
                        <area xml:id="ex.write.close" coords="20"/>
                    </areaspec>
                    <programlisting language="c" linenumbering="numbered"
                ><xi:include href="examples/ex-c-write.c" parse="text"
                /></programlisting>
                </programlistingco>
                
                <callout arearefs="ex.write.open-co" xml:id="ex.write.open">
                    <para>
                        [line 6]
                        Open the file <code>NXfile.nxs</code> with 
                        <emphasis>create</emphasis> 
                        access (implying write access).
                        NAPI<footnote><para><xref linkend="NAPI"/></para></footnote>
                        returns a file identifier of type <code>NXhandle</code>.
                    </para>
                </callout>
        '''
        return ""

    def e_calloutlist(self, el):
        # FIXME:
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        s = "\n\n.. compound::\n\n"
        s += INDENT + ".. _%s:\n\n" % id
        s += INDENT + ".. rubric:: Callout List\n\n"
        for node in el.findall(self.parent.ns+'callout'):
            t = self._concat(node).strip()
            s += INDENT + "#. callout item:\n"
            for line in t.split('\n'):
                s += INDENT + INDENT + line + '\n'
        return s

    def e_callout(self, el):
        # FIXME:
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        return self._concat(el).strip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('docbook_file', action='store', help="DocBook file name (input)")
    parser.add_argument('-v', '--version', action='version', version=__version__)
    args = parser.parse_args()
    dbfile = args.docbook_file.strip()
    if not os.path.exists(dbfile):
        print "%s does not exist" % dbfile
        exit(1)
    converter = db2rst.Db2Rst()
    result = converter.process( dbfile, Convert )
    if result is not None:
        print result

