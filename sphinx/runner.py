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

DocBook_FILE_LIST = []
DocBook_FILE_LIST.append( "../manual/applying-nexus.xml" )
DocBook_FILE_LIST.append( "../manual/authorgroup.xml" )
DocBook_FILE_LIST.append( "../manual/ClassDefinitions.xml" )  # problems with <entry /> in <table>
DocBook_FILE_LIST.append( "../manual/community.xml" )
DocBook_FILE_LIST.append( "../manual/datarules.xml" )
DocBook_FILE_LIST.append( "../manual/design.xml" )
DocBook_FILE_LIST.append( "../manual/faq.xml" )
DocBook_FILE_LIST.append( "../manual/fileformat.xml" )
DocBook_FILE_LIST.append( "../manual/h5py-example.xml" )
DocBook_FILE_LIST.append( "../manual/history.xml" )
DocBook_FILE_LIST.append( "../manual/installation.xml" )
DocBook_FILE_LIST.append( "../manual/introduction.xml" )
DocBook_FILE_LIST.append( "../manual/issues.xml" )
DocBook_FILE_LIST.append( "../manual/license.xml" )
DocBook_FILE_LIST.append( "../manual/mailinglist.xml" )
DocBook_FILE_LIST.append( "../manual/motivations.xml" )
DocBook_FILE_LIST.append( "../manual/napi-java.xml" )
DocBook_FILE_LIST.append( "../manual/NIAC.xml" )
DocBook_FILE_LIST.append( "../manual/NXDL.xml" )
DocBook_FILE_LIST.append( "../manual/preface.xml" )
DocBook_FILE_LIST.append( "../manual/revhistory.xml" )
DocBook_FILE_LIST.append( "../manual/rules.xml" )
DocBook_FILE_LIST.append( "../manual/subversion.xml" )
DocBook_FILE_LIST.append( "../manual/utilities.xml" )
DocBook_FILE_LIST.append( "../manual/validation.xml" )

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
