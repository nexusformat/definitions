#!/usr/bin/env python
"""
   Insert the NXDL instance file into the Docbook XML file
   at the designated location 
   (matched by text ___COPY_NXDL_HERE___)
   and also the correct path for the URL
   (matched by text ___NXDL_INSTANCE_FILE_LOCATION___)
"""

########### SVN repository information ###################
# $Date: 2008$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################


import sys


def usage():
    """
       show how to use this program
    """
    print 'usage:  addnxdlcode.py  NXDLinstance.nxdl.xml docbookfile.xml'
    sys.exit(1)


def _main():
    """
       do the work
    """
    if len(sys.argv) != 3:
        usage()
    nxdlfile = sys.argv[1]
    docbookfile = sys.argv[2]
    # read the NXDL instance
    #fd = open(nxdlfile, 'r')
    #nxdl = fd.read()
    #fd.close()
    # read the docbook file
    fd = open(docbookfile, 'r')
    db = fd.read()
    fd.close()
    
    # find and replace text
    matchtext = '___COPY_NXDL_HERE___'
    cdata = '<xi:include'
    cdata += ' xmlns:xi="http://www.w3.org/2001/XInclude"'
    cdata += ' href="' + nxdlfile + '"'
    cdata += ' parse="text"/>'
    newdocbook = db.replace(matchtext, cdata)
    db = newdocbook
    
    # find and replace text
    matchtext = '___NXDL_INSTANCE_FILE_LOCATION___'
    newdocbook = db.replace(matchtext, nxdlfile.strip('../'))
    db = newdocbook

    # write the docbook file again
    fd = open(docbookfile, 'w')
    fd.write(db)
    fd.close()
    return


if __name__ == '__main__':
    _main()
