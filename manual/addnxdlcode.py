#!/usr/bin/env python
"""
   Insert the NXDL instance file into the Docbook XML file
   at the designated location (indicated by the text
   ___COPY_NXDL_HERE___)
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
    fd = open(nxdlfile, 'r')
    nxdl = fd.read()
    fd.close()
    # read the docbook file
    fd = open(docbookfile, 'r')
    db = fd.read()
    fd.close()
    # find and replace the text
    matchtext = '___COPY_NXDL_HERE___'
    newdocbook = db.replace(matchtext, nxdl)
    # write the docbook file again
    fd = open(docbookfile, 'w')
    fd.write(newdocbook)
    fd.close()
    return


if __name__ == '__main__':
    _main()
