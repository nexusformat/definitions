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


from lxml import etree
import copy
import glob
import gnosis.xml.objectify
import os
import sys
import time

NeXusDir = os.path.join('..', )
XML_ROOT_TAG = 'NXDL_class_hierarchy'
spacer = ' '*2
newline_spacer = '\n' + spacer


def readXml(xmlFile):
    '''use gnosis to read an XML file and return an object to its contents'''
    if not os.path.exists(xmlFile):
        raise RuntimeError("Cannot find XML file: " + xmlFile)
    return gnosis.xml.objectify.XML_Objectify(xmlFile).make_instance()


def yyyymmdd_hhmmss(time_float = None):
    '''return an ISO8601 time string'''
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime( time_float ))


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


def build_hierarchy_dict(classname, tree, branch_nodes):
    '''return a dictionary of the tree hierarchy starting from node classname'''
    d = {classname: {}}
    if classname in branch_nodes:    # prevent recursion
        if len(tree[classname].children) > 0:
            d[classname] = {'...': {}}
    else:
        branch_nodes.append( classname )
        for node in sorted(tree[classname].children):
            t = build_hierarchy_dict(node, tree, branch_nodes)
            d[classname][node] = t[node]
    return d


def hierarchy_text_list(tree):
    '''return a text list rendition of the tree hierarchy in tree'''
    s = []   # use a list, it's more efficient
    for classname, classgroups in sorted(tree.items()):
        s += [ classname ]
        if len(classgroups) > 0:
            s += [ spacer + _ for _ in hierarchy_text_list(classgroups) ]
    return s


def _attach_xml_branch(parent, branch):
    '''add this branch to the parent XML document'''
    for classname, classgroups in sorted(branch.items()):
        node = etree.SubElement(parent, 'group')
        node.attrib['name'] = classname
        if len(classgroups) > 0:
            _attach_xml_branch(node, classgroups)


def hierarchy_xml_file(tree, xmlfile):
    '''write the tree hierarchy to an XML file'''
    root = etree.Element(XML_ROOT_TAG)
    root.attrib['date'] = yyyymmdd_hhmmss()
    _attach_xml_branch(root, tree)

    text = etree.tostring(root, pretty_print=True, encoding='utf-8')
    f = open(xmlfile, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    #f.write('<?xml-stylesheet type="text/xsl" href="%s"?>\n' % xslt)
    f.write( text )
    f.close()


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

    all_classes = copy.deepcopy(base_classes)
#     all_classes.update(applications)
#     all_classes.update(contributed)

    assign_relatives(all_classes)    # associate parent nodes with child nodes
    
    heads = []
    for nodename, node in all_classes.items():
        if len(node.parents) == 0:
            heads.append(nodename)

    for nodename in sorted(heads):
        d = build_hierarchy_dict(nodename, all_classes, [])

        htl = hierarchy_text_list(d)
        print '\n'.join(htl)
        
        xmlFile = 'hierarchy_' + nodename + '.xml'
        hierarchy_xml_file(d, xmlFile)
