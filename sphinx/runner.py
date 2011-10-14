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
converted into a class that can be called simply:

    converter = Db2Rst()
    result = converter.process( input_file )
    if result is not None:
        return str(obj)

The plan is to add namespace consideration into ``db2rst``
to aid in converting the NeXus documentation from DocBook into ReSt.
Additional handlers will also need to be added for the tags used 
in the NeXus docs.
'''


import sys, os
import db2rst

NEXUS_DIR = "../manual"
#NEXUS_DIR = "../../NeXus/definitions/trunk/manual"
NEXUS_DIR = os.path.abspath(NEXUS_DIR)
DocBook_FILE_LIST = []


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
buildList("motivations.xml")
buildList("napi-java.xml")
buildList("NIAC.xml")
buildList("NXDL.xml")
buildList("preface.xml")
buildList("revhistory.xml")
buildList("rules.xml")
buildList("subversion.xml")
buildList("utilities.xml")
buildList("validation.xml")
buildList("classes/NXentry.xml")

converter = db2rst.Db2Rst()
converter.removeComments(False)
converter.writeUnusedLabels(True)
converter.id_attrib = "{http://www.w3.org/XML/1998/namespace}id"
converter.linkend = "{http://www.w3.org/1999/xlink}href"
converter.useStdTableHandler = False

for xml_file in DocBook_FILE_LIST:
    sys.stderr.write("Processing DocBook file `%s'...\n" % xml_file)
    result = converter.process( xml_file )
    header = '.. $%s$\n\n' % 'Id'      # ID string updated by version control
    if result is not None:
        rst_file = os.path.splitext(os.path.basename(xml_file))[0] + '.rst'
        f = open(rst_file, 'w')
        f.write( header )
        f.write( result )
        f.close()
    sys.stderr.write("-"*60 + "\n")
