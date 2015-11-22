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
import nxdb2rst, db2rst
import logging

NEXUS_DIR = "../docbook"
NEXUS_DIR = os.path.abspath(NEXUS_DIR)

DocBook_FILE_LIST = []


def buildList(item):
    path = os.path.join(NEXUS_DIR, item)
    if os.path.exists(path):
        DocBook_FILE_LIST.append(path)


buildList("applying-nexus.xml")
buildList("authorgroup.xml")
buildList("ClassDefinitions.xml")  # problems with <entry /> in <table>
buildList("community.xml")
buildList("datarules.xml")
buildList("design.xml")
buildList("examples.xml")
buildList("ex_code_napi.xml")
buildList("ex_code_native.xml")
buildList("faq.xml")
buildList("fileformat.xml")
buildList("h5py-example.xml")
#buildList("hierarchy.xml")    # not used in the manual now
buildList("history.xml")
#buildList("impatient.xml")    # not used in the manual now
buildList("installation.xml")
buildList("introduction.xml")
buildList("issues.xml")
buildList("license.xml")
buildList("mailinglist.xml")
buildList("motivations.xml")
buildList("napi-java.xml")
#buildList("NAPI.xml")        # !!! problem here !!!  <entry spanname="fullrow" ...
buildList("NeXusManual.xml")
buildList("NIAC.xml")
buildList("nxdl_desc.xml")
buildList("NXDL.xml")
buildList("preface.xml")
#buildList("releaseinfo.xml")  # can we get this another way?  use |today|
buildList("revhistory.xml")
buildList("Roadmap.xml")
buildList("rules.xml")
buildList("strategies.xml")
buildList("subversion.xml")
buildList("Summary.xml")
buildList("types.xml")
buildList("units.xml")
buildList("utilities.xml")
buildList("v1frontinfo.xml")
buildList("v2frontinfo.xml")
buildList("validation.xml")
buildList("volume1.xml")
buildList("volume2.xml")
buildList("writer_1_3.xml")
buildList("writer_2_1.xml")  # does not strip DocBook namespace from elements!


converter = db2rst.Db2Rst()
converter.namespacePrefix = None
converter.removeComments(False)
converter.writeUnusedLabels(True)
converter.id_attrib = "{http://www.w3.org/XML/1998/namespace}id"
converter.linkend = "{http://www.w3.org/1999/xlink}href"

logging.basicConfig(filename='runner.log',level=logging.INFO)
for xml_file in DocBook_FILE_LIST:
    logging.info("Processing DocBook file `%s'..." % xml_file)
    result = converter.process( xml_file, nxdb2rst.Convert )
    header = '.. $%s$\n\n' % 'Id'      # ID string updated by version control
    if result is not None:
        rst_file = os.path.splitext(os.path.basename(xml_file))[0] + '.rst'
        f = open(rst_file, 'w')
        f.write( header )
        f.write( result )
        f.close()
    logging.info("-"*60)


# TODO: need to deal with these
NEEDS_HANDLING = '''
include these files by name (with source code formatting)
.. rubric:  INCLUDE examples/h5py/writer_2_1.py
.. rubric:  INCLUDE examples/h5py/writer_2_1_h5dump.txt

These things go into a table of contents
.. rubric:  INCLUDE NAPI.xml
.. rubric:  INCLUDE NXDL.xml

authorgroup is unformatted, improve it programmatically?
'''
