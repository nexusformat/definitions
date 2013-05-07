#!/usr/bin/env python

'''
Show the NeXus base class tree and hierarchy. 

originally:
traverse the NeXus XML Schema and NXDL files 
to build Python Objects from NeXus classes

.. note::  This is a tool for maintenance of the NXDL repository.
'''

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################


import os
import sys
import gnosis.xml.objectify
import glob


NeXusDir = os.path.join('..', )


def readXml(xmlFile):
    '''use gnosis to read an XML file and return an object to its contents'''
    if not os.path.exists(xmlFile):
        raise RuntimeError("Cannot find XML file: " + xmlFile)
    return gnosis.xml.objectify.XML_Objectify(xmlFile).make_instance()


class NXDL_schema(object):
    
    def __init__(self, schemaDir):
        if not os.path.exists(schemaDir):
            raise RuntimeError("Cannot find root directory: " + schemaDir)
        self.schemaDir = os.path.abspath(schemaDir)
        self.schemaFile = 'nxdl.xsd'
        self.nxdlTypesFile = 'nxdlTypes.xsd'
        pwd = os.getcwd()
        os.chdir(schemaDir)
        self.nxdl_schema = readXml(self.schemaFile)
        self.nxdlTypes_schema = readXml(self.nxdlTypesFile)
        self.parse_schema()
        os.chdir(pwd)
        
    def parse_schema(self):
        #for node in self.nxdl_schema.xs_element:
        #    print node.name
        pass
    
    def getSchemaDir(self):
        '''return the directory (absolute path) with the NeXus XML Schema for NXDL (nxdl.xsd)'''
        return self.schemaDir
    
    def getSchemaFile(self):
        '''return the absolute path of the NeXus XML Schema for NXDL (nxdl.xsd)'''
        return os.path.abspath(os.path.join(self.schemaDir, self.schemaFile))


class NXDL_class(object):
    
    def __init__(self, nxdlFile):
        if not os.path.exists(nxdlFile):
            raise RuntimeError("Cannot find NXDL file: " + nxdlFile)
        self.nxdlFile = nxdlFile
        self.nxdlDir = os.path.split(os.path.abspath(nxdlFile))[0]
        self.ancestors = {}
        self.parents = {}
        self.children = {}
        self.nxdl = readXml(nxdlFile)
        self.classname = self.nxdl.name
        self.parse_nxdl()
        
    def parse_nxdl(self,):
        pass
    
    def getNxdlDir(self):
        '''return the directory (absolute path) with the NeXus NXDL file'''
        return self.nxdlDir
    
    def getNxdlFile(self):
        '''return the absolute path of the NeXus NXDL file'''
        return os.path.abspath(os.path.join(self.nxdlDir, self.nxdlFile))


def read_definitions(dirName):
    NXDL_classes = {}
    for xmlFile in glob.glob(os.path.join(NeXusDir, dirName, '*.nxdl.xml', )):
        node = NXDL_class(xmlFile)
        NXDL_classes[node.nxdl.name] = node
        if 'extends' in node.nxdl.__dict__:
            # print node.getNxdlFile(), node.nxdl.extends
            if node.nxdl.extends not in ('NXobject'):
                node.parents[node.nxdl.extends] = None
        if 'group' in node.nxdl.__dict__:
            for grp in node.nxdl.group:
                node.children[grp.type] = None
    return NXDL_classes


def showTree(classname, tree, indent, branch_nodes):
    '''return a text list of the tree hierarchy starting from node classname'''
    spacer = ' '*2
    s = [spacer*indent + classname,]
    if classname in branch_nodes:    # prevent recursion
        if len(tree[classname].children) > 0:
            s[0] += '...'
    else:
        branch_nodes.append( classname )
        for node in sorted(tree[classname].children):
            s += showTree(node, tree, indent+1, branch_nodes)
    return s


def assign_relatives(tree):
    '''discover and assign any relatives of the tree nodes'''
    # child nodes
    for nodename, node in tree.items():
        for kid in node.children.keys():
            tree[kid].parents[nodename] = None

    # ancestor nodes
    for nodename, node in tree.items():
        examine = node.parents.keys()
        while len(examine) > 0:
            parent = examine.pop()
            if parent not in node.ancestors:
                if parent not in ( nodename ):
                    tree[nodename].ancestors[parent] = None
                    # need to add grandparents, ...
                    examine += tree[parent].parents.keys()


if __name__ == '__main__':
    schema = NXDL_schema(NeXusDir)

    base_classes = read_definitions('base_classes')
    applications = read_definitions('applications')
    contributed  = read_definitions('contributed_definitions')

    assign_relatives(base_classes)    # associate parent nodes with child nodes
    
    heads = []
    for nodename, node in base_classes.items():
        if len(node.parents) == 0:
            heads.append(nodename)

    for nodename in sorted(heads):
        # TODO: write output in XML (filename passed on command line)
        print '\n'.join(showTree(nodename, base_classes, 0, []))
