#!/usr/bin/env python

# Tested under both python2 and python3.

'''
Strip certain XML declarations from an XML file.

Read a NeXus NXDL class specification and write it to stdout,
stripping out these XML declarations:

* ``<?xml version``
* ``<?xml stylesheet``
'''

from __future__ import print_function
import os, sys, re

version = re.compile(r"^<\?xml version")
stylesheet = re.compile(r"^<\?xml-stylesheet")

with open(sys.argv[1],"r") as in_file:
    for line in in_file.read().splitlines():

        # Note:
        # This next test assumes that XML declarations are the only text 
        # on their respective lines in the .nxdl.xml file.
        # If the line also includes an opening of a new tag, this code 
        # will break that opening and the resulting .sch file will be invalid.
        #
        # wrong:
        #     <?xml-stylesheet type="text/xsl" href="nxdlformat.xsl" ?><!--
        #
        # correct:
        #     <?xml-stylesheet type="text/xsl" href="nxdlformat.xsl" ?>
        #     <!--
        
        if version.match(line) or stylesheet.match(line):
            continue

        print(line)

