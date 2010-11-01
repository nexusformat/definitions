#!/usr/bin/env python
"""
   Fix links in the DocBook source files for each. 
   NXDL class  The XSLT cannot determine the
   category for each included group.  We want to
   make a URL to the final HTML documentation
   for any included groups.
"""

########### SVN repository information ###################
# $Date: 2008$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################

import os
import sys
import re
import pprint

def findCategory(classname):
    dirs = ('applications',  'contributed_definitions', 'base_classes')
    pattern = "../%s/%s.nxdl.xml"
    for dir in dirs:
        testfile = pattern % (dir, classname)
        if os.path.exists(testfile):
            return dir
    return None

testFile = sys.argv[1]
#testFile = "C:\Users\Pete\Documents\eclipse\NeXus\definitions\trunk\manual\classes\NXcrystal"

findPattern = "\<link\>(NX[_\w]+)\</link\>"
replaceItem = "\1"
formatString = '<link xlink:href="%s" xmlns:xlink="http://www.w3.org/1999/xlink">%s</link>'
formatUrl = 'http://download.nexusformat.org/doc/html/ClassDefinitions-%s.html#%s'

map = {'base_classes' : 'Base', 'applications' : 'Application', 'contributed_definitions' : 'Contributed'}

rePattern = re.compile(findPattern)

if not os.path.exists(testFile): exit
f = open(testFile)
buf = f.read()
f.close()

m = rePattern.search(buf)
corrections = 0
while m != None:
    className = m.group(1)
    category = findCategory(className)
    #print className, category
    if category == None:
        pattern = "<link>%s</link>" % className
        nbuf = re.sub(pattern, className + " (not found)", buf)
        buf = nbuf
        corrections += 1
    else:
        url = formatUrl % (map[category], className)
        replaceString = formatString % (url, className)
        pattern = "<link>%s</link>" % className
        nbuf = re.sub(pattern, replaceString, buf)
        buf = nbuf
        corrections += 1
    m = rePattern.search(buf)
if corrections > 0:
    f = open(testFile, "w")
    f.write(buf)
    f.close()
