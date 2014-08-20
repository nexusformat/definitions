#!/usr/bin/env python

'''
Read the the NeXus NXDL class specification and describe it.  
Write a restructured text (.rst) document for use in the NeXus manual in 
the NeXus NXDL Classes chapter.
'''

# testing:
# cd /tmp
# mkdir out
# /G/nx-def/utils/nxdl2rst.py /G/nx-def/applications/NXsas.nxdl.xml > nxsas.rst && sphinx-build . out
# then point browser to file:///tmp/out/nxsas.html

import os, sys, re
import lxml.etree
try:
    from pyRestTable import rest_table
except:
    import rst_table as rest_table 

# find the directory of this python file
BASEDIR = os.path.split(os.path.abspath(__file__))[0]
NEXT_TABLE_NUMBER = 1
SUBTABLES = []

def fmtTyp( node ):
    typ = node.get('type', 'untyped (:ref:`NX_CHAR <NX_CHAR>`)')
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    return typ

def fmtUnits( node ):
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ' :ref:`%s <%s>`' % (units, units)
    if units:
        return ( ' {units=%s}' % units )
    return ''

def getDocFromNode(ns, node, retval=None):
    docnodes = node.xpath('nx:doc', namespaces=ns)
    if docnodes is None or len(docnodes)==0:
        return retval
    if len(docnodes) > 1:
        things = (node.sourceline, os.path.split(node.base)[1])
        raise Exception, 'Too many doc elements: line %d, %s' % things
    
    # be sure to grab _all_ content in the documentation
    # it might look like XML
    s = lxml.etree.tostring(docnodes[0], pretty_print=True)
    p1 = s.find('>')+1
    p2 = s.rfind('</')
    text = s[p1:p2].lstrip('\n')    # cut off the enclosing tag
    
    lines = text.splitlines()
    if len(lines) > 1:
        indent0 = len(lines[0]) - len(lines[0].lstrip())
        indent1 = len(lines[1]) - len(lines[1].lstrip())
        if len(lines) > 2:
            indent2 = len(lines[2]) - len(lines[2].lstrip())
        else:
            indent2 = 0
        if indent0 == 0:
            indent = max(indent1, indent2)
            text = lines[0]
        else:
            indent = indent0
            text = lines[0][indent:]
        for line in lines[1:]:
            if not len(line[:indent].strip()) == 0:
                msg = 'Something wrong with indentation on this line:\n' + line
                raise Exception, msg
            text += '\n' + line[indent:]
    return text.lstrip()

def printAttribute( ns, node, indent ):
    doc = getDocFromNode(ns, node, retval='')
    doc = doc.strip()
    doc = re.sub( '\n', ' ', doc )
    print( '%s**%s**: %s%s' % (
        indent, '@'+node.get('name'), fmtTyp(node), fmtUnits(node) ) )
    print( '%s  %s\n' % ( indent, doc ) )

    

def printFullTree(ns, parent, name, indent):
    '''
    recursively print the full tree structure
    
    :param dict ns: dictionary of namespaces for use in XPath expressions
    :param lxml_element_node parent: parent node to be documented
    :param str name: name of elements, such as NXentry/NXuser
    :param indent: to keep track of indentation level
    '''

    for node in parent.xpath('nx:field', namespaces=ns):
        name = node.get('name')
        print( '%s**%s**: %s %s\n' % (
            indent, name, fmtTyp(node), fmtUnits(node) ) )

        doc = getDocFromNode(ns, node, retval='')
        node_list = node.xpath('nx:enumeration', namespaces=ns)
        if len(node_list) == 1:
            doc += ' -:- ' + getEnumerationDescription(ns, node_list[0])
        node_list = node.xpath('nx:dimensions', namespaces=ns)
        if len(node_list) == 1:
            doc += ' -:- ' + getDimensionsDescription(ns, node_list[0])
        doc = doc.strip()
        doc = re.sub( '\n', ' ', doc )
        print( '%s  %s\n' % ( indent, doc ) )

        # TODO: look for "deprecated" element, add to doc

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            printAttribute( ns, subnode, indent+'  ' )
    
    for node in parent.xpath('nx:group', namespaces=ns):
        name = node.get('name', '')
        typ = node.get('type', 'untyped (this is an error; please report)')
        if typ.startswith('NX'):
            if name is '':
                name = '(%s)' % typ.lstrip('NX')
            typ = ':ref:`%s`' % typ
        print( '%s**%s**: %s' % (indent, name, typ ) )

        doc = getDocFromNode(ns, node, retval='')
        doc = doc.strip()
        doc = re.sub( '\n', ' ', doc )
        print( '%s  %s\n' % ( indent, doc ) )

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            printAttribute( ns, subnode, indent+'  ' )

        nodename = '%s/%s' % (name, node.get('type'))
        printFullTree(ns, node, nodename, indent+'  ')

    for node in parent.xpath('nx:link', namespaces=ns):
        print( '%s**%s** --> %s\n' % (
            indent, node.get('name'), node.get('target') ) )
        doc = getDocFromNode(ns, node, retval='')
        doc = doc.strip()
        doc = re.sub( '\n', ' ', doc )
        print( '%s  %s\n' % ( indent, doc ) )

def getDimensionsDescription(ns, parent):
    desc = ''
    rank = parent.get('rank')
    node_list = parent.xpath('nx:dim', namespaces=ns)
    if len(node_list) > 0:
        desc += '\nDimensions:'
        if rank is not None:
            desc += ' (rank=%s)' % rank
        desc += '\n'*2
    for node in node_list:
        desc += '\n* %s: ``%s``' % (node.get('index'), node.get('value'))
    return desc


def getEnumerationDescription(ns, parent):
    desc = ''
    node_list = parent.xpath('nx:item', namespaces=ns)
    if len(node_list) > 0:
        if len(node_list) == 1:
            desc += '\nThis value: '
        else:
            desc += '\nAny of these value(s):\n\n'
        for item in node_list:
            name = item.get('value')
            doc = getDocFromNode(ns, item, retval=None)
            if doc is not None:
                if len(node_list) == 1:
                    row = '``%s``' % name
                else:
                    row = '* ``%s``:' % name
                for line in doc.splitlines():
                    row += '\n  ' + line
            else:
                if len(node_list) == 1:
                    row = '``%s``' % name
                else:
                    row = '* ``%s``:' % name
            desc += row + '\n'
    return desc

if __name__ == '__main__':

    # get NXDL_SCHEMA_FILE
    developermode = True
    developermode = False
    if developermode and len(sys.argv) != 2:
        # use default input file
        NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'applications', 'NXarchive.nxdl.xml')
        NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'applications', 'NXsas.nxdl.xml')
        #NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'base_classes', 'NXcrystal.nxdl.xml')
        #NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'base_classes', 'NXobject.nxdl.xml')
        #NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXarpes.nxdl.xml')
        #NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXmagnetic_kicker.nxdl.xml')
        
    else:
        # get input file from command line
        if len(sys.argv) != 2:
            print 'usage: %s someclass.nxdl.xml' % sys.argv[0]
            exit()
        NXDL_SCHEMA_FILE = sys.argv[1]

    # parse input file into tree
    if not os.path.exists(NXDL_SCHEMA_FILE):
        print 'Cannot find %s' % NXDL_SCHEMA_FILE
        exit()
    tree = lxml.etree.parse(NXDL_SCHEMA_FILE)

    # The following URL is outdated, but that doesn't matter;
    # it won't be accessed; it's just an arbitrary namespace name.
    # It only needs to match the xmlns attribute in the NXDL files.
    NAMESPACE = 'http://definition.nexusformat.org/nxdl/@NXDL_RELEASE@'
    ns = {'nx': NAMESPACE}
    
    root = tree.getroot()
    name = root.get('name')
    title = name

    subdir = os.path.split(os.path.split(tree.docinfo.URL)[0])[1]
    index_cat = {
                 'base_classes': 'Base Classes',
                 'applications': 'Application Definitions',
                 'contributed_definitions': 'Contributed Definitions',
                 }[subdir]

    # print ReST comments and section header
    print( '.. auto-generated by script %s from the NXDL source %s' %
           (sys.argv[0], sys.argv[1]) )
    print
    print '.. index:: ! class definition -- %s; %s' % (index_cat, name)
    print '.. index:: ! %s' % name
    print
    print '.. _%s:\n' % name
    print '='*len(title)
    print title
    print '='*len(title)

    # print category
    print
    print '**Category**:'
    print '  %s.' % ( root.get('category').strip() )

    # print official description of this class
    print
    print '**Description**:'
    doc = getDocFromNode(ns, root)
    if doc is None:
        raise Exception, 'No documentation for: ' + name
    doc = doc.strip()
    doc = re.sub( '\n', ' ', doc )
    print '  %s\n' % doc
    print

    # print category
    extends = root.get('extends')
    if extends is not None:
        extends = ':ref:`%s`' % extends
    else:
        extends = ''
    print
    print '**Extends**:'
    print '  %s.' % ( extends )

    # TODO: change instances of \t to proper indentation
    html_root = 'https://github.com/nexusformat/definitions/blob/master'
        
    # print experimental full tree
    print '**Structure**:\n'
    printFullTree(ns, root, name, '  ')

    # print symbol list
    node_list = root.xpath('nx:symbols', namespaces=ns)
    print '**Symbols**:\n'
    if len(node_list) == 0:
        print '  No symbol table.'
    elif len(node_list) > 1:
        print '  Invalid symbol table.'
    else:
        doc = getDocFromNode(ns, node_list[0])
        if doc is not None:
            for line in doc.splitlines():
                print '  %s' % line
            print
        for node in node_list[0].xpath('nx:symbol', namespaces=ns):
            doc = getDocFromNode(ns, node)
            print '  :%s:' % node.get('name')
            for line in doc.splitlines():
                print '    %s' % line
            print

    # print group references
    print '**Groups cited**:\n'
    node_list = root.xpath('//nx:group', namespaces=ns)
    groups = []
    for node in node_list:
        g = node.get('type')
        g_ref = ':ref:`%s`' % g
        if g.startswith('NX') and g_ref not in groups:
            groups.append(g_ref)
    txt = 'none'
    if len(groups) > 0:
        txt = ', '.join(sorted(groups))
    print '  %s.' % ( txt )

    # print history (currently, only a version number is available)
    print '**History**:\n'
    print '  Introduced in NeXus version %s.' % ( root.get('version').strip() )

    # print NXDL source location
    print '**Source**:\n'
    print '  Automatically generated from %s/%s/%s.nxdl.xml.' % (
        html_root, subdir, name)
