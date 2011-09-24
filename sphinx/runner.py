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

XML_FILE = "../manual/faq.xml"
XML_FILE = "../manual/applying-nexus.xml"
args = []
args.append( sys.argv[0] )
args.append( XML_FILE )

def old():
    result = db2rst._main(args)
    if result is not None:
        rst_file = os.path.splitext(XML_FILE)[0] + '.rst'
        f = open(rst_file, 'w')
        f.write( result )
        f.close()

converter = db2rst.Db2Rst()
converter.removeComments(False)
converter.writeUnusedLabels(True)
converter.id_attrib = "{http://www.w3.org/XML/1998/namespace}id"
converter.linkend = "{http://www.w3.org/1999/xlink}href"
result = converter.process( XML_FILE )
header = '.. $%s$\n\n' % 'Id'      # ID string updated by version control
if result is not None:
    rst_file = os.path.splitext(os.path.basename(XML_FILE))[0] + '.rst'
    f = open(rst_file, 'w')
    f.write( header )
    f.write( result )
    f.close()
