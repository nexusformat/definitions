#!/usr/bin/env python
from argparse import ArgumentError

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
        self.ns = {'nx': 'http://definition.nexusformat.org/nxdl/3.1'}
    
    def parse(self, nxdlFile):
        self.nxdlFile = os.path.normpath( nxdlFile )
        
        stem, self.nxdlName = os.path.split(nxdlFile[:nxdlFile.find('.nxdl.xml')])
        self.nxdlType = os.path.split(stem)[1]
        
        self.tree = lxml.etree.parse(nxdlFile)
        pass
    
    def report(self, outputDir = '.'):
        rstFile = os.path.join(outputDir, self.nxdlType , self.nxdlName+ self.fileSuffix)
        path, _ = os.path.split(self.nxdlFile)
        
        # make the XSLT transformation, see: http://lxml.de/xpathxslt.html#xslt
        self.xsltFile = "nxdlformat.xsl"                        # could learn from the XML file?
        xsltFile = os.path.join(path, self.xsltFile)
        xslt = lxml.etree.XSLT( lxml.etree.parse(xsltFile) )    # prepare the transform
        text = str( xslt( self.tree ) )                         # make the transform
        
        root = self.tree.getroot()
        
        rest = self.make_heading(self.nxdlName, 1, self.nxdlName, True)

        rest += ".. index::  ! classes - %s; %s\n\n" % (self.nxdlType, self.nxdlName)
        rest += self.make_definition('category', self.nxdlType)
        #N = ":index:`%s <single: ! %s; %s>`" % (self.nxdlName, self.nxdlType, self.nxdlName)
        URL = "http://svn.nexusformat.org/definitions/trunk/%s/%s.nxdl.xml" % (self.nxdlType, self.nxdlName)
        rest += self.make_definition('NXDL source:', "%s\n\n(%s)" % (self.nxdlName, URL) )
        rest += self.make_definition('version', root.get('version', 'unknown') )
        rest += self.make_definition('SVN Id', root.get('svnid', 'none') )
        extends = root.get('extends', 'none')
        if extends != "none":
            extends = ":ref:`%s`" % extends
        rest += self.make_definition('extends class:', extends )
        rest += self.make_definition('other classes included:', self.groups_list(root) )
        rest += self.make_definition('symbol list:', self.symbols_list(root) )
        rest += self.make_definition('documentation:', "? process with db2rst ?" )  # TODO: 

        rest += "\n"
        rest += self.make_heading("Basic Structure of " + self.nxdlName, 2)
        rest += "::\n\n" + self.indented_lines(4, text)
        
        '''
Table 3.3. NXaperture
Name and Attributes    Type    Units    Description (and Occurrences)
     NXgeometry          

location and shape of aperture
     NXgeometry          

location and shape of each blade
material     NX_CHAR         

Absorbing material of the aperture
description     NX_CHAR         

Description of aperture
     NXnote          

describe an additional information in a note*
        '''
        
        return rstFile, rest
    
    def make_heading(self, title, level, ref = None, upperBar = False):
        '''Return a formatted ReST heading
        
        :param str title: the text of the title
        :param int level: level number (1, 2, 3, 4, ...)
        :param str ref: (optional) text of the reference label
        :param bool upperBar: (optional) add an upper bar to the heading
        '''
        s = ""
        if ref is not None:
            s += "..  _%s:\n\n" % ref
        
        symbols = "# = - ~ ^ . * + _".split()
        if level < 1 or level > len(symbols):
            raise ArgumentError, "level must be between 1 and %d, received %d" % (len(symbols), level)
        
        bar = symbols[level-1]*len(title) + "\n"
        if upperBar:
            s += bar
        s += title + "\n" + bar + "\n"
        
        return s
    
    def make_definition(self, term, definition):
        '''Return a string-formatted ReST definition
        
        :param str term: the thing to be defined
        :param str definition: the words to describe the term
        '''
        s = term + "\n"
        s += self.indented_lines(4, definition)
        s += "\n"
        return s
    
    def indented_lines(self, numSpaces, lines):
        '''Return a string of indented lines from text with line breaks
        
        :param int numSpaces: number of spaces to indent
        :param str lines: text with embedded line breaks (assumes UNIX EOL - might be a problem)
        '''
        s = ""
        indent = " "*numSpaces
        for line in lines.split("\n"):
            s += "%s%s\n" % (indent, line)
        return s
    
    def groups_list(self, root):
        '''Return a string of ReST references to the groups used
        in this NXDL, sorted alphabetically
        
        :param root: root of XML tree
        '''
        groups = lxml.etree.ETXPath( './/{%s}group' % self.ns['nx'] )(root)
        if len(groups) > 0:
            L = []
            for G in groups:
                N = G.get('type')
                if N not in L:
                    L.append(":ref:`%s`" % N)
            groups = ", ".join(sorted(L))
        else:
            groups = "none"
        return groups
    
    def symbols_list(self, root):
        '''Return a string of ReST references to the symbols defined
        in this NXDL
        
        :param root: root of XML tree
        '''
        symbols = "none"
        node = root.find( '{%s}symbols' % self.ns['nx'] )
        if node is not None:
            symbols = ""
            DN = node.find( '{%s}doc' % self.ns['nx'] )  # TODO: doc needs db2rst
            if DN is not None:
                symbols += DN.text + "\n\n"
            for SN in lxml.etree.ETXPath( './/{%s}symbol' % self.ns['nx'] )(node):
                S = "``%s``" % SN.get('name')
                T = "%s" % SN.find( '{%s}doc' % self.ns['nx'] ).text  # TODO: doc needs db2rst
                symbols += self.make_definition(S, T )
        return symbols


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
                    rstFile, restText = obj.report(OUTPUT_DIR)
                    print rstFile
                    print restText
                    # FIXME: temporary only
                    _, n = os.path.split(rstFile)
                    f = open (n, 'w')
                    f.write(restText)
                    f.close()
    print len(nxdl_file_list), ' NXDL files discovered'
