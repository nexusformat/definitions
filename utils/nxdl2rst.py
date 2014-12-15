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
from collections import OrderedDict
import lxml.etree


def printf(str, *args):
    print(str % args, end='')

def fmtTyp( node ):
    typ = node.get('type', ':ref:`NX_CHAR <NX_CHAR>`') # per default
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    return typ

def fmtUnits( node ):
    units = node.get('units', '')
    if not units:
        return ''
    if units.startswith('NX_'):
        units = '\ :ref:`%s <%s>`' % (units, units)
    return ' {units=%s}' % units

def getDocBlocks( ns, node ):
    docnodes = node.xpath('nx:doc', namespaces=ns)
    if docnodes is None or len(docnodes)==0:
        return ''
    if len(docnodes) > 1:
        raise Exception( 'Too many doc elements: line %d, %s' % 
                         (node.sourceline, os.path.split(node.base)[1]) )
    docnode = docnodes[0]

    # be sure to grab _all_ content in the documentation
    # it might look like XML
    s = lxml.etree.tostring(docnode, pretty_print=True,
                            method='c14n', with_comments=False).decode('utf-8')
    m = re.search(r'^<doc[^>]*>\n?(.*)\n?</doc>$', s, re.DOTALL )
    if not m:
        raise Exception( 'unexepcted docstring [%s] ' % s )
    text = m.group(1)

    # Blocks are separated by whitelines
    blocks = re.split( '\n\s*\n', text )
    if len(blocks)==1 and len(blocks[0].splitlines())==1:
        return [ blocks[0].rstrip().lstrip() ]

    # Indentation must be given by first line
    m = re.match(r'(\s*)(\S+)', blocks[0])
    if not m:
        return [ '' ]
    indent = m.group(1)

    # Remove common indentation as determined from first line
    if indent=="":
        raise Exception( 'Missing initial indentation in <doc> of %s [%s]' %
                         ( node.get('name'), blocks[0] ) )

    out_blocks = []
    for block in blocks:
        lines = block.rstrip().splitlines()
        out_lines = []
        for line in lines:
            if line[:len(indent)]!=indent:
                raise Exception( 'Bad indentation in <doc> of %s [%s]: expected "%s" found "%s".' %
                                 ( node.get('name'), block,
                                   re.sub(r'\t',"\\\\t", indent ),
                                   re.sub(r'\t',"\\\\t", line ),
                            ) )
            out_lines.append( line[len(indent):] )
        out_blocks.append( "\n".join(out_lines) )
    return out_blocks

def getDocLine( ns, node ):
    blocks = getDocBlocks( ns, node )
    if len(blocks)==0:
        return ''
    if len(blocks)>1:
        raise Exception( 'Unexpected multi-paragraph doc [%s]' %
                         '|'.join(blocks) )
    return re.sub(r'\n', " ", blocks[0])

def analyzeDimensions( ns, parent ):
    node_list = parent.xpath('nx:dimensions', namespaces=ns)
    if len(node_list) != 1:
        return ''
    node = node_list[0]
    # rank = node.get('rank') # ignore this
    node_list = node.xpath('nx:dim', namespaces=ns)
    dims = []
    for subnode in node_list:
        value = subnode.get('value')
        if not value:
            value = 'ref(%s)' % subnode.get('ref')
        dims.append( value )
    return '[%s]' % ( ', '.join(dims) )

def printEnumeration( indent, ns, parent ):
    node_list = parent.xpath('nx:item', namespaces=ns)
    if len(node_list) == 0:
        return ''

    if len(node_list) == 1:
        printf( '%sObligatory value: ' % ( indent ) )
    else:
        printf( '%sAny of these values:' % ( indent ) )

    docs = OrderedDict()
    for item in node_list:
        name = item.get('value')
        docs[name] = getDocLine(ns, item)

    ENUMERATION_INLINE_LENGTH = 60
    def show_as_typed_text(msg):
        return '``%s``' % msg
    oneliner = ' | '.join( map(show_as_typed_text, docs.keys()) )
    if ( any( doc for doc in docs.values() ) or
         len( oneliner ) > ENUMERATION_INLINE_LENGTH ):
        # print one item per line
        print('\n')
        for name, doc in docs.items():
            printf( '%s  * %s' % ( indent, show_as_typed_text(name) ) )
            if doc:
                printf( ': %s' % ( doc ) )
            print('\n')
    else:
        # print all items in one line
        print(' %s' % ( oneliner ) )
    print('')

def printDoc( indent, ns, node, required=False):
    blocks = getDocBlocks(ns, node)
    if len(blocks)==0:
        if required:
            raise Exception( 'No documentation for: ' + node.get('name') )
        print('')
    else:
        for block in blocks:
            for line in block.splitlines():
                print( '%s%s' % ( indent, line ) )
            print()

def printAttribute( ns, kind, node, indent ):
    name = node.get('name')
    index_name = re.sub( r'_', ' ', name )
    print( '%s.. index:: %s (%s attribute)\n' %
           ( indent, index_name, kind ) )
    print( '%s**@%s**: %s%s\n' % (
        indent, name, fmtTyp(node), fmtUnits(node) ) )
    printDoc(indent+'  ', ns, node)
    node_list = node.xpath('nx:enumeration', namespaces=ns)
    if len(node_list) == 1:
        printEnumeration( indent+'  ', ns, node_list[0] )


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
        index_name = re.sub( r'_', ' ', name )
        dims = analyzeDimensions(ns, node)
        print( '%s.. index:: %s (field)\n' %
               ( indent, index_name ) )
        print( '%s**%s%s**: %s%s\n' % (
            indent, name, dims, fmtTyp(node), fmtUnits(node) ) )

        printDoc(indent+'  ', ns, node)

        node_list = node.xpath('nx:enumeration', namespaces=ns)
        if len(node_list) == 1:
            printEnumeration( indent+'  ', ns, node_list[0] )

        # TODO: look for "deprecated" element, add to doc

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            printAttribute( ns, 'field', subnode, indent+'  ' )
    
    for node in parent.xpath('nx:group', namespaces=ns):
        name = node.get('name', '')
        typ = node.get('type', 'untyped (this is an error; please report)')
        if typ.startswith('NX'):
            if name is '':
                name = '(%s)' % typ.lstrip('NX')
            typ = ':ref:`%s`' % typ
        print( '%s**%s**: %s\n' % (indent, name, typ ) )

        printDoc(indent+'  ', ns, node)

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            printAttribute( ns, 'group', subnode, indent+'  ' )

        nodename = '%s/%s' % (name, node.get('type'))
        printFullTree(ns, node, nodename, indent+'  ')

    for node in parent.xpath('nx:link', namespaces=ns):
        print( '%s**%s** --> %s\n' % (
            indent, node.get('name'), node.get('target') ) )
        printDoc(indent+'  ', ns, node)


def main():
    '''
    standard command-line processing
    '''
    if len(sys.argv) != 2:
        print( 'usage: %s someclass.nxdl.xml' % sys.argv[0] )
        exit()
    nxdl_file = sys.argv[1]

    # parse input file into tree
    if not os.path.exists(nxdl_file):
        print( 'Cannot find %s' % nxdl_file )
        exit()
    tree = lxml.etree.parse(nxdl_file)

    # The following URL is outdated, but that doesn't matter;
    # it won't be accessed; it's just an arbitrary namespace name.
    # It only needs to match the xmlns attribute in the NXDL files.
    NAMESPACE = 'http://definition.nexusformat.org/nxdl/@NXDL_RELEASE@'
    ns = {'nx': NAMESPACE}
    
    root = tree.getroot()
    name = root.get('name')
    title = name
    if len(name)<2 or name[0:2]!='NX':
        raise Exception( 'Unexpected class name "%s"; does not start with NX' %
                         ( name ) )
    lexical_name = name[2:] # without padding 'NX', for indexing
    lexical_name = re.sub( r'_', ' ', lexical_name )
    
    # retrieve category from directory
    subdir = os.path.split(os.path.split(tree.docinfo.URL)[0])[1]
    # TODO: check for consistency with root.get('category')
    category_for_listing = {
                 'base_classes': 'base class',
                 'applications': 'application definition',
                 'contributed_definitions': 'contributed definition',
                 }[subdir]

    # print ReST comments and section header
    print( '.. auto-generated by script %s from the NXDL source %s' %
           (sys.argv[0], sys.argv[1]) )
    print('')
    print( '.. index::' )
    print( '    ! %s (%s)' % (name,category_for_listing) )
    print( '    ! %s (%s)' % (lexical_name,category_for_listing) )
    print( '    see: %s (%s); %s' %
           (lexical_name,category_for_listing, name) )
    print('')
    print( '.. _%s:\n' % name )
    print( '='*len(title) )
    print( title )
    print( '='*len(title) )

    # print category, version, parent class
    extends = root.get('extends')
    if extends is None:
        extends = 'none'
    else:
        extends = ':ref:`%s`' % extends

    print('')
    print( '**Status**:\n' )
    print( '  %s, extends %s, version %s' %
           ( category_for_listing.strip(),
             extends,
             root.get('version').strip() ) )

    # print official description of this class
    print('')
    print( '**Description**:\n' )
    printDoc('  ', ns, root, required=True)


    # print symbol list
    node_list = root.xpath('nx:symbols', namespaces=ns)
    print( '**Symbols**:\n' )
    if len(node_list) == 0:
        print( '  No symbol table\n' )
    elif len(node_list) > 1:
        raise Exception( 'Invalid symbol table in ' % root.get('name') )
    else:
        printDoc( '  ', ns, node_list[0] )
        for node in node_list[0].xpath('nx:symbol', namespaces=ns):
            doc = getDocLine(ns, node)
            printf( '  **%s**' % node.get('name') )
            if doc:
                printf( ': %s' % doc )
            print('\n')

    # print group references
    print( '**Groups cited**:' )
    node_list = root.xpath('//nx:group', namespaces=ns)
    groups = []
    for node in node_list:
        g = node.get('type')
        if g.startswith('NX') and g not in groups:
            groups.append(g)
    if len(groups) == 0:
        print( '  none\n' )
    else:
        out = [ (':ref:`%s`' % g) for g in groups ]
        txt = ', '.join(sorted(out))
        print( '  %s\n' % ( txt ) )
        out = [ ('%s (base class); used in %s' % (g, category_for_listing)) for g in groups ]
        txt = ', '.join(out)
        print( '.. index:: %s\n' % ( txt ) )


    # TODO: change instances of \t to proper indentation
    html_root = 'https://github.com/nexusformat/definitions/blob/master'
        
    # print full tree
    print( '**Structure**:\n' )
    for subnode in root.xpath('nx:attribute', namespaces=ns):
        printAttribute( ns, 'file', subnode, '  ' )
    printFullTree(ns, root, name, '  ')

    # print NXDL source location
    print( '**Source**:' )
    print( '  Automatically generated from %s/%s/%s.nxdl.xml' % (
        html_root, subdir, name) )


if __name__ == '__main__':
    main()
