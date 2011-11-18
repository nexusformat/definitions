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
import db2rst
import nxdb2rst
from argparse import ArgumentError


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
    
    def report(self, outputDir = '.'):
        rstFile = os.path.join(outputDir, self.nxdlType , self.nxdlName+ self.fileSuffix)
        path, _ = os.path.split(self.nxdlFile)
        
        root = self.tree.getroot()
        
        rest = self.make_heading(self.nxdlName, 1, self.nxdlName, True)

        rest += ".. index::  ! . NXDL %s; %s\n\n" % (self.nxdlType, self.nxdlName)
        
        URL = "http://svn.nexusformat.org/definitions/trunk/%s/%s.nxdl.xml" % (self.nxdlType, self.nxdlName)
        extends = root.get('extends', 'none')
        if extends != "none":
            extends = ":ref:`%s`" % extends

        rest += self.get_doc(root, "No documentation provided.") + "\n\n"
        
        t = db2rst.Table()
        t.labels = ('item', 'Description', )
        t.rows.append( ['category', self.nxdlType, ] )
        t.rows.append( ['NXDL class', "*%s*" % self.nxdlName, ] )
        t.rows.append( ['URL', "%s" % URL, ] )
        t.rows.append( ['version', root.get('version', 'unknown'), ] )
        t.rows.append( ['SVN Id', "`" + root.get('svnid', 'none') + "`", ] )
        t.rows.append( ['extends class', extends, ] )
        t.rows.append( ['included classes', self.groups_list(root), ] )
        rest += t.reST(fmt='simple')
        
        rest += "\n"
        rest += ".. rubric:: Basic Structure of **%s**\n\n" % self.nxdlName
        # make the XSLT transformation, see: http://lxml.de/xpathxslt.html#xslt
        self.xsltFile = "nxdlformat.xsl"                        # could learn from the XML file?
        xsltFile = os.path.join(path, self.xsltFile)
        xslt = lxml.etree.XSLT( lxml.etree.parse(xsltFile) )    # prepare the transform
        text = ":linenos:\n\n"
        text += str( xslt( self.tree ) )                         # make the transform
        rest += ".. code-block:: text\n" + self.indented_lines(4, text)
        
        rest += self.symbols_table(root) + "\n\n"
        
        rest += self.top_attributes_table(root) + "\n\n"
        
        t = db2rst.Table()
        t.labels = ('Name and Attributes', 
                    'Type', 
                    'Units', 
                    'Description (and Occurrences)', )
        for node in root.findall('*'):
            try:
                tag = node.tag.split('}')[-1]
            except:
                continue
            if tag in ('group', 'field'):
                name = node.get('name', {'group': '', 'field': 'unknown'}[tag])
                type = node.get('type', {'group': 'unknown', 'field': 'NX_CHAR'}[tag])
                units = ''
                description = ''
                t.rows.append( [name, type, units, description, ] )
        
        rest += "\n.. rubric:: Comprehensive Structure of **%s**\n\n" % self.nxdlName
        rest += t.reST()
        
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
        '''Return a string of reST references to the groups used
        in this NXDL, sorted alphabetically
        
        :param root: root of XML tree
        '''
        groups = lxml.etree.ETXPath( './/{%s}group' % self.ns['nx'] )(root)
        if len(groups) > 0:
            L = []
            for G in groups:
                N = ":ref:`%s`" % G.get('type')
                if N not in L:
                    L.append( N )
            groups = ",\n".join(sorted( L ))
        else:
            groups = "none"
        return groups
    
    def symbols_table(self, root):
        '''Return a table of ReST references to the symbols defined in this NXDL
        
        :param root: root of XML tree
        '''
        rest = "\n.. rubric:: Symbols used in definition of **%s**\n\n" % self.nxdlName
        symbols = "none"
        node = root.find( '{%s}symbols' % self.ns['nx'] )
        if node is None:
            rest += 'No symbols are defined in this NXDL file\n'
        else:
            table = db2rst.Table()
            table.labels = ('Symbol', 'Description', )
            title = self.get_doc(node, None)
            if title is not None:
                rest += title + "\n"
            for SN in lxml.etree.ETXPath( './/{%s}symbol' % self.ns['nx'] )(node):
                symbol = "``%s``" % SN.get('name')
                desc = "%s" % self.get_doc(SN).strip('\n')
                table.rows.append( [symbol, desc] )
            rest += table.reST()
        return rest

    def get_doc(self, node, undefined = ""):
        DN = node.find( '{%s}doc' % self.ns['nx'] )
        if DN is None:
            doc = undefined
        else:
            # TODO: this could be much, much better
            ns = self.ns['nx']
            obj = Convert(DN, namespace=ns)
            doc = str(obj).strip() + "\n"
            #doc = DN.text
        return doc
    
    def top_attributes_table(self, root):
        '''Return a table of ReST references to the attributes defined
        in the root element of this NXDL
        
        :param root: root of XML tree
        '''
        rest = ""
        nodelist = root.findall( '{%s}attribute' % self.ns['nx'] )
        if len(nodelist) > 0:
            fmt = "\n.. rubric:: Attributes of ``definition`` element in **%s**\n\n"
            rest = fmt % self.nxdlName
            table = db2rst.Table()
            table.labels = ('Attributes', 'Type', 'Units', 'Description (and Occurrences) ', )
            for node in nodelist:
                name = '@' + node.get('name')
                type = node.get('type', 'NX_CHAR')
                # FIXME: this has not been finished
                units = node.get('type', '..')
                # start db2rst parsing from this node
                # put result into description
                description = '..'
                table.rows.append( [name, type, units, description] )
            rest += table.reST()
        return rest


class Convert(nxdb2rst.Convert):
    '''
    Treat our NXDL doc element like a DocBook para element
    '''
    e_doc = db2rst.Convert.e_para


if __name__ == '__main__':
    NXDL_DIRS = ['../base_classes', 
                 '../applications', 
                 '../contributed_definitions', ]
    OUTPUT_DIR = os.path.join(*list('./source/volume2/NXDL'.split('/')))
    nxdl_file_list = []
    for dir in NXDL_DIRS:
        fulldir = os.path.abspath(dir)
        for _, dirs, files in os.walk(dir):
            if '.svn' in dirs:
                dirs.remove('.svn')
            for file in sorted(files):
                if file.endswith('.nxdl.xml'):
                    nxdlFile = os.path.join(fulldir, file)
                    nxdl_file_list.append(nxdlFile)
                    obj = Describe()
                    obj.parse(nxdlFile)
                    rstFile, restText = obj.report(OUTPUT_DIR)
                    print rstFile
                    print restText
                    f = open (rstFile, 'w')
                    f.write(restText + "\n")
                    f.close()
    print len(nxdl_file_list), ' NXDL files discovered'
