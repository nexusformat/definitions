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
import rest_table

NEXUS_DIR = "../manual"
NEXUS_DIR = os.path.abspath(NEXUS_DIR)


class Convert(db2rst.Convert):
    '''
    NeXus overrides of the db2rst Convert class for these DocBook elements:
    + table
    + example
    + informalexample
    + figure
    + subtitle
    + info
    + revdescription
    + legalnotice
    + revhistory
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
        
        t = rest_table.Table()
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
    
    def e_example(self, el):
        '''
        Must parse an example specification such as::
        
            <example 
                    xmlns="http://docbook.org/ns/docbook" 
                    xmlns:xlink="http://www.w3.org/1999/xlink" 
                    xmlns:xi="http://www.w3.org/2001/XInclude" 
                    xml:id="native.hdf5.simple.write" 
                    xreflabel="Writing a simple NeXus file using native HDF5 commands">
                <title>Writing a simple NeXus file using native HDF5 commands</title>
                <programlisting linenumbering="numbered" language="c"
                    ><xi:include href="examples/nxh5write.c" parse="text"
                        /></programlisting>
            </example>

        into reST commands such as::
        
            .. code-block:: c        [ text | xml | python | c | ... ]
                :linenos: 
                
                [copy examples/napi-example.c file contents here]

        or::
        
            .. literalinclude:: napi-example.c  [ copy this file into same folder as .rst ]
                :linenos: 
                :tab-width: 4
        
        '''
        s = self.program_listing(el)
        # see ClassDefinitions.xml, line 143 for another representation
        if s is None:
            logging.info("line %d in %s" % (el.sourceline, str(el.base)))
            logging.info( "no <programlisting /> element" )
            s = self._docbook_source(el, 'EXAMPLE')  # unparsed representation
        return s
    
    def e_informalexample(self, el):
        s = self.program_listing(el)
        if s is None:
            logging.info("line %d in %s" % (el.sourceline, str(el.base)))
            logging.info( "no <programlisting /> element" )
            s = self._docbook_source(el, 'INFORMALEXAMPLE')  # unparsed representation
        return s
    
    def program_listing(self, el):
        '''
        could be in a figure or example
        '''
        child = self.parent.ns+"programlisting"
        pl_obj = el.find(child) 
        if pl_obj is None:
            grandchild = self.parent.ns+"programlistingco" + "/" + child
            pl_obj = el.find(grandchild)
            if pl_obj is None:
                return None
        logging.info("program_listing(): line %d in %s" % (el.sourceline, str(el.base)))
        #print el.sourceline, str(el.base)
        # read the XML
        id = el.get(self.parent.id_attrib, None)
        title_obj = el.find(self.parent.ns+"title")
        if title_obj is not None:
            title = self._concat( title_obj ).strip()
            # TODO Where is title used?
        xreflabel = el.get("xreflabel", None)
        language = pl_obj.get("language", "text")
        #
        # build the reST
        indent = " "*4
        s = ""
        if id:
            s += "\n.._%s:\n" % id
        s += "\n.. code-block:: %s\n" % language
        s += indent + ":linenos:\n\n" 
        xi = "{http://www.w3.org/2001/XInclude}"
        inc_obj = pl_obj.find(xi + "include")
        if inc_obj is not None:
            filename = inc_obj.get("href", None)
            full_filename = os.path.join( NEXUS_DIR, filename )
            if os.path.exists(full_filename):
                # copy the include file into the reST
                file = open(full_filename, 'r')
                for line in file:
                    s += indent + line.rstrip() + "\n"
        else:
            for line in pl_obj.text.split("\n"):
                s += indent + line.rstrip() + "\n"
        return s
    
    def e_figure(self, el):
        '''
        standard figure
        '''
        logging.info("line %d in %s" % (el.sourceline, str(el.base)))
        s = self.program_listing(el)
        if s is not None:
            return s
        s = self.mediaobject(el)
        if s is not None:
            return s
        s = self._docbook_source(el, 'FIGURE')  # unparsed representation
        return s
    
    def mediaobject(self, el):
        '''
        Docbook mediaobject (has a caption)::

            <figure 
                    xml:id="fig.example.NeXus.hierarchy" 
                    xreflabel="Example NeXus file hierarchy">
                <title>Example of a NeXus file</title>
                <mediaobject>
                    <imageobject>
                        <imagedata fileref="img/Hierarchy.png" width="300pt"
                            scalefit="1"/>
                    </imageobject>
                </mediaobject>
            </figure> 

        will be written as::
        
            .. _fig.example.NeXus.hierarchy:
            
            .. figure:: img/Hierarchy.png
                :width: 300 pt
                :alt: figure of Example NeXus file hierarchy
            
                Example of a NeXus file
        '''
        s = ""
        mo = el.find(self.parent.ns+"mediaobject")
        if mo is None:
            return None
        id = el.get(self.parent.id_attrib, None)
        title = self._concat( el.find(self.parent.ns+"title") ).strip()
        xreflabel = el.get("xreflabel", None)
        img_data_objs = lxml.etree.ETXPath( './/%simagedata' % self.parent.ns )(el)
        if len(img_data_objs) < 1:
            raise RuntimeWarning, "no <imagedata /> element found"
        if len(img_data_objs) > 1:
            raise RuntimeWarning, "multiple <imagedata /> elements found"
        s = ""
        obj = img_data_objs[0]
        file = obj.get("fileref", "")
        width = obj.get("width", None)
        indent = " "*4
        if id:
            s += "\n.._%s:\n\n" % id
        s += ".. figure:: %s\n" % file
        if width:
            s += indent + ":width: %s\n" % width
        if xreflabel:
            s += indent + ":alt: figure of %s\n" % xreflabel
        if title:
            s += "\n"*2 + indent + "%s\n" % title
        return s
    
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
        s += "\n\n.. rubric:: %s\n\n" % el.find(self.parent.ns+'title').text
        s += ".. How to get the current subversion info here (from subtitle.xml or ...)?\n\n"
        s += "|today|\n\n"
        
        s += ".. author group could be shown here\n\n"

        pubdate = el.find(self.parent.ns+'pubdate').text
        orgname = el.find(self.parent.ns+'org').find(self.parent.ns+'orgname').text
        uri = el.find(self.parent.ns+'org').find(self.parent.ns+'uri').text
        s += "Published %s by %s, %s\n\n" % (pubdate, orgname, uri)

        year = el.find(self.parent.ns+'copyright').find(self.parent.ns+'year').text
        holder = el.find(self.parent.ns+'copyright').find(self.parent.ns+'holder').text
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
        t = rest_table.Table()
        t.labels = ('date', 'release', 'description', 'who?', )
        for revnode in el.findall(self.parent.ns+'revision'):
            node = revnode.find(self.parent.ns+'revnumber')
            if node is None:
                revnumber = ""
            else:
                revnumber = node.text
            date = revnode.find(self.parent.ns+'date').text
            authorinitials = revnode.find(self.parent.ns+'authorinitials').text
            revdescription = self._conv(revnode.find(self.parent.ns+'revdescription')).strip()
            t.rows.append( [date, revnumber, revdescription, authorinitials, ] )
        
        s = self._make_title("Revision History", 1)
        s += "\n\n"
        s += t.reST(fmt='complex')
        return s
