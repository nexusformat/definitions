#!/usr/bin/env python

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

'''
Runs the ``db2rst`` program on a specific DocBook XML file.
This code was written to test the db2rst code as it is being 
extended to convert the NeXus documentation into sphinx:

    converter = Db2Rst()
    result = converter.process( input_file )
    if result is not None:
        return str(obj)

'''


import sys, os
import db2rst
import lxml.etree as ET
import logging

NEXUS_DIR = "../manual"
NEXUS_DIR = os.path.abspath(NEXUS_DIR)
DocBook_FILE_LIST = []


class NeXus_Convert(db2rst.Convert):
    '''
    NeXus overrides of the db2rst standard Convert class
    '''

    def e_table(self, el):
        # This still breaks for tables with embedded lists and other pathologies.
        s = "\n\n"
        id = el.get(self.parent.id_attrib, "")
        if len(id) > 0:
            s += ".. _%s:\n\n" % id
        
        s += ".. rubric:: Table: "
        title = self.childNodeText(el, 'title')
        if title is not None:
            s += title
        s += "\n\n"
        
        # get number of columns
        cols = int(el.find(self.parent.ns+'tgroup').attrib['cols'])
        
        # calculate the widths of all the columns
        row_nodes = ET.ETXPath( './/%srow' % self.parent.ns )(el)
        widths = [ 0  for _ in range(cols)]
        for r in row_nodes:
            i = 0
            for c in r.findall(self.parent.ns+'entry'):
                widths[i] = max( len( self._conv(c, do_assert = False) ), widths[i])
                i += 1
        fmt = ' '.join(['%%-%is' % (size,) for size in widths]) + '\n'
        divider = fmt % tuple(['=' * size for size in widths])
        
        s += divider   # top row of table

        tgroup = el.find(self.parent.ns+'tgroup')
        thead = tgroup.find(self.parent.ns+'thead')
        if thead is None:
            s += fmt % tuple(['..' for _ in range(cols)])
        else:
            nodes = thead.find(self.parent.ns+'row').findall(self.parent.ns+'entry')
            s += fmt % tuple(map(self._conv, nodes))

        s += divider   # label-end row of table

        tbody = tgroup.find(self.parent.ns+'tbody')
        rows = tbody.findall(self.parent.ns+'row')
        for row in rows:
            entries = row.findall(self.parent.ns+'entry')
            s += fmt % tuple(map(self._conv, entries))
        
        s += divider   # bottom row of table
        return s


def buildList(item):
    path = os.path.join(NEXUS_DIR, item)
    DocBook_FILE_LIST.append(path)


buildList("applying-nexus.xml")
buildList("authorgroup.xml")
buildList("ClassDefinitions.xml")  # problems with <entry /> in <table>
buildList("community.xml")
buildList("datarules.xml")
buildList("design.xml")
buildList("faq.xml")
buildList("fileformat.xml")
buildList("h5py-example.xml")
buildList("history.xml")
buildList("installation.xml")
buildList("introduction.xml")
buildList("issues.xml")
buildList("license.xml")
buildList("mailinglist.xml")
buildList("motivations.xml")  # some <primary> element is not getting handled here
buildList("napi-java.xml")    # ... or here ...
buildList("NIAC.xml")
buildList("NXDL.xml")
buildList("preface.xml")
buildList("revhistory.xml")
buildList("rules.xml")
buildList("subversion.xml")
buildList("utilities.xml")
buildList("validation.xml")
buildList("classes/NXentry.xml")
buildList("examples.xml")

converter = db2rst.Db2Rst()
converter.removeComments(False)
converter.writeUnusedLabels(True)
converter.id_attrib = "{http://www.w3.org/XML/1998/namespace}id"
converter.linkend = "{http://www.w3.org/1999/xlink}href"

for xml_file in DocBook_FILE_LIST:
    logging.basicConfig(filename='runner.log',level=logging.INFO)
    logging.info("Processing DocBook file `%s'...\n" % xml_file)
    result = converter.process( xml_file, NeXus_Convert )
    header = '.. $%s$\n\n' % 'Id'      # ID string updated by version control
    if result is not None:
        rst_file = os.path.splitext(os.path.basename(xml_file))[0] + '.rst'
        f = open(rst_file, 'w')
        f.write( header )
        f.write( result )
        f.close()
    logging.info("-"*60 + "\n")
