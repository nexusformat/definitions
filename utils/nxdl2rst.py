#!/usr/bin/env python

'''
Read the NeXus NXDL class specification and describe it.
Write a restructured text (.rst) document for use in the NeXus manual in
the NeXus NXDL Classes chapter.
'''

# testing:  see file dev_nxdl2rst.py

from collections import OrderedDict
from html import parser as HTMLParser
import lxml.etree
import os
import pyRestTable
import re
import sys
from local_utilities import printf, replicate


INDENTATION_UNIT = '  '
listing_category = None
anchor_list = []  # list of all hypertext anchors


def addAnchor(anchor):
    """Add a hypertext anchor to the list."""
    anchor_list.append(anchor)


def printAnchorList():
    """Print the list of hypertext anchors."""

    def sorter(key):
        return key.lower()

    if len(anchor_list) > 0:
        print("")
        print("Hypertext Anchors")
        print("-----------------\n")
        print(
            "Table of hypertext anchors for all groups, fields,\n"
            "attributes, and links defined in this class.\n\n"
        )
        table = pyRestTable.Table()
        table.addLabel("documentation (reST source) anchor")
        table.addLabel("web page (HTML) anchor")
        for ref in sorted(anchor_list, key=sorter):
            # fmt: off
            anchor = (
                ref
                .lower()
                .lstrip("/")
                .replace("_", "-")
                .replace("@", "-")
                .replace("/", "-")
            )
            table.addRow(
                (
                    ":ref:`%s <%s>`" % (ref, ref),
                    ":ref:`#%s <%s>`" % (anchor, ref),
                )
            )
            # fmt: on
        print(table)


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
        raise Exception( 'unexpected docstring [%s] ' % s )
    text = m.group(1)

    # substitute HTML entities in markup: "<" for "&lt;"
    # thanks: http://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
    htmlparser = HTMLParser.HTMLParser()
    try:		# see #661
        import html
        text = html.unescape(text)
    except (ImportError, AttributeError):
        text = htmlparser.unescape(text)

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


def get_minOccurs(node, use_application_defaults):
    '''
    get the value for the ``minOccurs`` attribute

    :param obj node: instance of lxml.etree._Element
    :param bool use_application_defaults: use special case value
    :returns str: value of the attribute (or its default)
    '''
    # TODO: can we improve on the default by exmaining nxdl.xsd?
    minOccurs_default = {True: '1', False: '0'}[use_application_defaults]
    minOccurs = node.get('minOccurs', minOccurs_default)
    return minOccurs


def get_required_or_optional_text(node, use_application_defaults):
    '''
    make clear if a reported item is required or optional

    :param obj node: instance of lxml.etree._Element
    :param bool use_application_defaults: use special case value
    :returns: formatted text
    '''
    tag = node.tag.split('}')[-1]
    nm = node.get('name')
    if tag in ('field', 'group'):
        optional_default = not use_application_defaults
        optional = node.get('optional', optional_default) in (True, 'true', '1', 1)
        recommended = node.get('recommended', None) in (True, 'true', '1', 1)
        minOccurs = get_minOccurs(node, use_application_defaults)
        if minOccurs in ('0', 0) or optional:
            optional_text = '(optional) '
        elif recommended:
            optional_text = '(recommended) '
        elif minOccurs in ('1', 1):
            optional_text = '(required) '
        else:
            # this is unexpected and remarkable
            # TODO: add a remark to the log
            optional_text = '(``minOccurs=%s``) ' % str(minOccurs)
    elif tag in ('attribute',):
        optional_default = not use_application_defaults
        optional = node.get('optional', optional_default) in (True, 'true', '1', 1)
        recommended = node.get('recommended', None) in (True, 'true', '1', 1)
        optional_text = {True: '(optional) ', False: '(required) '}[optional]
        if recommended:
            optional_text = '(recommended) '
    else:
        optional_text = '(unknown tag: ' + str(tag) + ') '
    return optional_text


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


def hyperlinkTarget(parent_path, name, nxtype):
    """Return internal hyperlink target for HTML anchor."""
    if nxtype == "attribute":
        sep = "@"
    else:
        sep = "/"
    target = "%s%s%s-%s" % (
        parent_path, sep, name, nxtype
    )
    addAnchor(target)
    return ".. _%s:\n" % target


def printEnumeration( indent, ns, parent ):
    node_list = parent.xpath('nx:item', namespaces=ns)
    if len(node_list) == 0:
        return ''

    if len(node_list) == 1:
        printf('%sObligatory value:', indent)
    else:
        printf('%sAny of these values:', indent)

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
            printf('%s  * %s', indent, show_as_typed_text(name))
            if doc:
                printf(': %s', doc)
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


def printAttribute( ns, kind, node, optional, indent, parent_path ):
    name = node.get('name')
    index_name = name
    print("%s%s" % (indent, hyperlinkTarget(parent_path, name, 'attribute'))
    )
    print( '%s.. index:: %s (%s attribute)\n' %
           ( indent, index_name, kind ) )
    print( '%s**@%s**: %s%s%s\n' % (
        indent, name, optional, fmtTyp(node), fmtUnits(node) ) )
    printDoc(indent+INDENTATION_UNIT, ns, node)
    node_list = node.xpath('nx:enumeration', namespaces=ns)
    if len(node_list) == 1:
        printEnumeration( indent+INDENTATION_UNIT, ns, node_list[0] )


def printIfDeprecated( ns, node, indent ):
    deprecated = node.get('deprecated', None)
    if deprecated is not None:
        print( '\n%s.. index:: deprecated\n' % indent)
        fmt = '\n%s**DEPRECATED**: %s\n'
        print( fmt % (indent, deprecated ) )


def printFullTree(ns, parent, name, indent, parent_path):
    '''
    recursively print the full tree structure

    :param dict ns: dictionary of namespaces for use in XPath expressions
    :param lxml_element_node parent: parent node to be documented
    :param str name: name of elements, such as NXentry/NXuser
    :param indent: to keep track of indentation level
    :param parent_path: NX class path of parent nodes
    '''
    global listing_category

    use_application_defaults = listing_category in (
        'application definition',
        'contributed definition')

    for node in parent.xpath('nx:field', namespaces=ns):
        name = node.get('name')
        index_name = name
        dims = analyzeDimensions(ns, node)

        optional_text = get_required_or_optional_text(node, use_application_defaults)
        print("%s%s" % (indent, hyperlinkTarget(parent_path, name, 'field')))
        print( '%s.. index:: %s (field)\n' %
               ( indent, index_name ) )
        print(
            '%s**%s%s**: %s%s%s\n' % (
                indent, name, dims, optional_text, fmtTyp(node), fmtUnits(node)
                ))

        printIfDeprecated( ns, node, indent+INDENTATION_UNIT )
        printDoc(indent+INDENTATION_UNIT, ns, node)

        node_list = node.xpath('nx:enumeration', namespaces=ns)
        if len(node_list) == 1:
            printEnumeration( indent+INDENTATION_UNIT, ns, node_list[0] )

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            optional = get_required_or_optional_text(subnode, use_application_defaults)
            printAttribute( ns, 'field', subnode, optional, indent+INDENTATION_UNIT, parent_path+"/"+name )

    for node in parent.xpath('nx:group', namespaces=ns):
        name = node.get('name', '')
        typ = node.get('type', 'untyped (this is an error; please report)')

        optional_text = get_required_or_optional_text(node, use_application_defaults)
        if typ.startswith('NX'):
            if name == '':
                name = typ.lstrip('NX').upper()
            typ = ':ref:`%s`' % typ
        print("%s%s" % (indent, hyperlinkTarget(parent_path, name, 'group')))
        print( '%s**%s**: %s%s\n' % (indent, name, optional_text, typ ) )

        printIfDeprecated(ns, node, indent+INDENTATION_UNIT)
        printDoc(indent+INDENTATION_UNIT, ns, node)

        for subnode in node.xpath('nx:attribute', namespaces=ns):
            optional = get_required_or_optional_text(subnode, use_application_defaults)
            printAttribute( ns, 'group', subnode, optional, indent+INDENTATION_UNIT, parent_path+"/"+name )

        nodename = '%s/%s' % (name, node.get('type'))
        printFullTree(ns, node, nodename, indent+INDENTATION_UNIT, parent_path+"/"+name)

    for node in parent.xpath('nx:link', namespaces=ns):
        name = node.get('name')
        print("%s%s" % (indent, hyperlinkTarget(parent_path, name, 'link')))
        print( '%s**%s**: :ref:`link<Design-Links>` (suggested target: ``%s``)\n' % (
            indent, name, node.get('target') ) )
        printDoc(indent+INDENTATION_UNIT, ns, node)


def print_rst_from_nxdl(nxdl_file):
    '''
    print restructured text from the named .nxdl.xml file
    '''
    global listing_category
    # parse input file into tree
    tree = lxml.etree.parse(nxdl_file)

    # The following URL is outdated, but that doesn't matter;
    # it won't be accessed; it's just an arbitrary namespace name.
    # It only needs to match the xmlns attribute in the NXDL files.
    NAMESPACE = 'http://definition.nexusformat.org/nxdl/3.1'
    ns = {'nx': NAMESPACE}

    root = tree.getroot()
    name = root.get('name')
    title = name
    parent_path = "/"+name  # absolute path of parent nodes, no trailing /
    if len(name)<2 or name[0:2]!='NX':
        raise Exception( 'Unexpected class name "%s"; does not start with NX' %
                         ( name ) )
    lexical_name = name[2:] # without padding 'NX', for indexing

    # retrieve category from directory
    #subdir = os.path.split(os.path.split(tree.docinfo.URL)[0])[1]
    subdir = root.attrib["category"]
    # TODO: check for consistency with root.get('category')
    listing_category = {
                 'base': 'base class',
                 'application': 'application definition',
                 'contributed': 'contributed definition',
                 }[subdir]

    use_application_defaults = listing_category in (
        'application definition',
        'contributed definition')

    # print ReST comments and section header
    print( '.. auto-generated by script %s from the NXDL source %s' %
           (sys.argv[0], sys.argv[1]) )
    print('')
    print( '.. index::' )
    print( '    ! %s (%s)' % (name,listing_category) )
    print( '    ! %s (%s)' % (lexical_name,listing_category) )
    print( '    see: %s (%s); %s' %
           (lexical_name,listing_category, name) )
    print('')
    print( '.. _%s:\n' % name )
    print( '='*len(title) )
    print( title )
    print( '='*len(title) )

    # print category & parent class
    extends = root.get('extends')
    if extends is None:
        extends = 'none'
    else:
        extends = ':ref:`%s`' % extends

    print('')
    print( '**Status**:\n' )
    print( '  %s, extends %s' %
           ( listing_category.strip(),
             extends ) )

    printIfDeprecated(ns, root, '')

    # print official description of this class
    print('')
    print( '**Description**:\n' )
    printDoc(INDENTATION_UNIT, ns, root, required=True)


    # print symbol list
    node_list = root.xpath('nx:symbols', namespaces=ns)
    print( '**Symbols**:\n' )
    if len(node_list) == 0:
        print( '  No symbol table\n' )
    elif len(node_list) > 1:
        raise Exception( 'Invalid symbol table in ' % root.get('name') )
    else:
        printDoc( INDENTATION_UNIT, ns, node_list[0] )
        for node in node_list[0].xpath('nx:symbol', namespaces=ns):
            doc = getDocLine(ns, node)
            printf('  **%s**', node.get('name'))
            if doc:
                printf(': %s', doc)
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
        out = [ ('%s (base class); used in %s' % (g, listing_category)) for g in groups ]
        txt = ', '.join(out)
        print( '.. index:: %s\n' % ( txt ) )

    # TODO: change instances of \t to proper indentation
    html_root = 'https://github.com/nexusformat/definitions/blob/main'

    # print full tree
    print( '**Structure**:\n' )
    for subnode in root.xpath('nx:attribute', namespaces=ns):
        optional = get_required_or_optional_text(subnode, use_application_defaults)
        printAttribute( ns, 'file', subnode, optional, INDENTATION_UNIT, parent_path) # FIXME: +"/"+name )
    printFullTree(ns, root, name, INDENTATION_UNIT, parent_path)

    printAnchorList()

    # print NXDL source location
    subdir_map = {
                  'base': 'base_classes',
                  'application': 'applications',
                  'contributed': 'contributed_definitions',
                  }
    print("")
    print( '**NXDL Source**:' )
    print( '  %s/%s/%s.nxdl.xml' % (
        html_root, subdir_map[subdir], name) )


def main():
    '''
    standard command-line processing
    '''
    import argparse
    parser = argparse.ArgumentParser(description='test nxdl2rst code')
    parser.add_argument('nxdl_file', help='name of NXDL file')
    results = parser.parse_args()
    nxdl_file = results.nxdl_file

    if not os.path.exists(nxdl_file):
        print( 'Cannot find %s' % nxdl_file )
        exit()

    print_rst_from_nxdl(nxdl_file)

    # if the NXDL has a subdirectory,
    # copy that subdirectory (quietly) to the pwd, such as:
    #  contributed/NXcanSAS.nxdl.xml: cp -a contributed/canSAS ./
    category = os.path.basename(os.getcwd())
    path = os.path.join('../../../../', category)
    basename = os.path.basename(nxdl_file)
    corename = basename[2:].split('.')[0]
    source = os.path.join(path, corename)
    if os.path.exists(source):
        target = os.path.join('.', corename)
        replicate(source, target)


if __name__ == '__main__':
    main()


# NeXus - Neutron and X-ray Common Data Format
#
# Copyright (C) 2008-2022 NeXus International Advisory Committee (NIAC)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org
