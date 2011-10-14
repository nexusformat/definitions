#!/usr/bin/env python

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

'''
Extracts documentation from NXDL files and builds the NeXus manual page.

For an example of what the DocBook page provides, see
http://download.nexusformat.org/doc/html/ClassDefinitions-Base.html#NXentry
'''


import sys, os
import lxml.etree


class Describe:
    
    def __init__(self):
        self.nxdlFile = None
        self.nxdlType = None
        self.nxdlName = None
        self.fileSuffix = '.rst'
    
    def parse(self, nxdlFile):
        self.nxdlFile = os.path.normpath( nxdlFile )
        
        ns = {'nx': 'http://definition.nexusformat.org/nxdl/3.1'}
        stem, self.nxdlName = os.path.split(nxdlFile[:nxdlFile.find('.nxdl.xml')])
        self.nxdlType = os.path.split(stem)[1]
        
        tree = lxml.etree.parse(nxdlFile)
        pass
    
    def report(self, outputDir = '.'):
        rstFile = os.path.join(outputDir, self.nxdlType , self.nxdlName+ self.fileSuffix)
        return rstFile


if __name__ == '__main__':
    NXDL_DIRS = ['../base_classes', '../applications', '../contributed_definitions', ]
    OUTPUT_DIR = '.'
    nxdl_file_list = []
    for dir in NXDL_DIRS:
        fulldir = os.path.abspath(dir)
        for _, dirs, files in os.walk(dir):
            if '.svn' in dirs:
                dirs.remove('.svn')
            for file in files:
                if file.endswith('.nxdl.xml'):
                    nxdlFile = os.path.join(fulldir, file)
                    nxdl_file_list.append(nxdlFile)
                    obj = Describe()
                    obj.parse(nxdlFile)
                    print obj.report(OUTPUT_DIR)
    print len(nxdl_file_list), ' NXDL files discovered'
