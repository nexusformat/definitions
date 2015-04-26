#!/usr/bin/env python

# Tested under both python2 and python3.

'''
Read the NeXus NXDL class specification and describe it.  
Write a restructured text (.rst) document for use in the NeXus manual in 
the NeXus NXDL Classes chapter.
'''

# testing:  see file dev_nxdl2rst.py

from __future__ import print_function
import os, sys, re

version = re.compile(r"^<\?xml version")
stylesheet = re.compile(r"^<\?xml-stylesheet")

with open(sys.argv[1],"r") as in_file:
    for line in in_file:

        if version.match(line) or stylesheet.match(line):
            continue

        print(line)

