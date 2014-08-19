#!/usr/bin/env python

'''
Read the the NeXus NXDL class specification and describe it.  
Write a restructured text (.rst) document for use in the NeXus manual in 
the NeXus NXDL Classes chapter.
'''


import os, sys
import lxml.etree
try:
  from pyRestTable import rest_table
except:
  import rst_table as rest_table 


TITLE_MARKERS = '# - + ~ ^ * @'.split()  # used for underscoring section titles
INDENTATION = ' '*4
# find the directory of this python file
BASEDIR = os.path.split(os.path.abspath(__file__))[0]
NEXT_TABLE_NUMBER = 1
SUBTABLES = []


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# the problem with trying to improve the tables for the PDF ...
"""
This works better ...

+---------+--------+------------------------+
| name    | type   | units                  |
+---------+--------+------------------------+
|         | description                     |
+=========+========+========================+
| thing1  | small  | cat                    |
+---------+--------+------------------------+
|         | travels with big cat            |
+---------+--------+------------------------+
| ..                                        |
+---------+--------+------------------------+
| thing2  | small  | cat                    |
+---------+--------+------------------------+
| ..      | travels with big cat and thing1 |
+---------+---------------------------------+


.. than this in PDF (both are fine in HTML!)
   but both fail in PDF when description is multi-line
   and even worse if there is a bullet list in the description

+---------------------+-----------------------------+--------------------------------------+
| Name and Attributes | Type                        | Units                                |
|                     +-----------------------------+--------------------------------------+
|                     | Description (and Occurrences)                                      |
+=====================+=============================+======================================+
| variable            | NX_NUMBER                                                          |
+                     +-----------------------------+--------------------------------------+
|                     | Dimension scale defining an axis of the data.                      |
|                     | Client is responsible for defining the dimensions of the data.     |
|                     | The name of this field may be changed to fit the circumstances.    |
|                     | Standard NeXus client tools will use the attributes to determine   |
|                     | how to use this field.                                             |
+---------------------+-----------------------------+--------------------------------------+
| variable_errors     | NX_NUMBER                                                          |
+                     +-----------------------------+--------------------------------------+
|                     | Errors (uncertainties) associated with axis ``variable``           |
|                     | Client is responsible for defining the dimensions of the data.     |
|                     | The name of this field may be changed to fit the circumstances     |
|                     | but is matched with the *variable*                                 |
|                     | field with ``_errors`` appended.                                   |
+---------------------+-----------------------------+--------------------------------------+
| data                | NX_NUMBER                   |                                      |
+                     +-----------------------------+--------------------------------------+
|                     | This field contains the data values to be used as the              |
|                     | NeXus *plottable data*.                                            |
|                     | Client is responsible for defining the dimensions of the data.     |
|                     | The name of this field may be changed to fit the circumstances.    |
|                     | Standard NeXus client tools will use the attributes to determine   |
|                     | how to use this field.                                             |
+---------------------+-----------------------------+--------------------------------------+
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def _indent(indentLevel):
    return INDENTATION*indentLevel


def getDocFromNode(ns, node, retval=None):
    docnodes = node.xpath('nx:doc', namespaces=ns)
    if docnodes is None or len(docnodes)==0:
        return retval
    if len(docnodes) > 1:
        things = (node.sourceline, os.path.split(node.base)[1])
        raise Exception, "Too many doc elements: line %d, %s" % things
    
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
                msg = "Something wrong with indentation on this line:\n" + line
                raise Exception, msg
            text += '\n' + line[indent:]
    return text.lstrip()


def getNextTableXref(name):
    global NEXT_TABLE_NUMBER
    xref = 'table.%02d.%s' % (NEXT_TABLE_NUMBER, name)
    NEXT_TABLE_NUMBER += 1
    return xref


def printMemberTable(ns, parent, name, xref):
    '''
    print a table of the members in the parent node
    
    At each level, iterate over the children 
    at each level to build one table.  
    If there is a group, then append 
    another level and repeat.
    
    :param dict ns: dictionary of namespaces for use in XPath expressions
    :param lxml_element_node parent: parent node to be documented
    :param str name: name of elements, such as NXentry/NXuser
    :param str xref: cross-referencing label to use with this parent node member table
    '''
    # table(s) describing the specification
    t = rest_table.Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.alignment = ('p{0.2\linewidth}', 'p{0.2\linewidth}', 'p{0.2\linewidth}', 'p{0.4\linewidth}', )
    #t.longtable = True
    
    for node in parent.xpath('nx:field', namespaces=ns):
        t.rows.append( getFieldData(ns, node) )
        for subnode in node.xpath('nx:attribute', namespaces=ns):
            t.rows.append( getAttributeData(ns, subnode) )
    
    for node in parent.xpath('nx:group', namespaces=ns):
        # look for more levels to document
        more_nodes = 0
        for item in ('nx:group', 'nx:field', 'nx:link', ): 
            more_nodes += len(node.xpath(item, namespaces=ns))
        group_data = getGroupData(ns, node)
        if more_nodes > 0:
            addSubTable('%s/%s' % (name, node.get('type')), node, getNextTableXref(name))
            group_data[3] += '\n\nSee table :ref:`%s`.' % SUBTABLES[-1]['xref']
            group_data[3] = group_data[3].strip()
        t.rows.append( group_data )
        for subnode in node.xpath('nx:attribute', namespaces=ns):
            t.rows.append( getAttributeData(ns, subnode) )

    for node in parent.xpath('nx:link', namespaces=ns):
        t.rows.append( getLinkData(ns, node) )

    title = '**%s** Members' % name
    print
    print '.. _%s:\n' % xref
    print '%s\n%s\n' % (title, '='*len(title))
    # in PDF, the section title is printed beside the table unless some text intervenes.
    print '\nDeclarations in the *%s* group.\n' % name
    if len(t.rows) > 0:
        print t.reST(fmt='complex')
    else:
        print 'No members to be documented'


def addSubTable(name, node, xref):
    SUBTABLES.append( {
                       'name': name, 
                       'node': node, 
                       'xref': xref
                       } )


def getAttributeData(ns, node):
    name = '@' + node.get('name')
    typ  = node.get('type', '(:ref:`NX_CHAR <NX_CHAR>`)')
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ':ref:`%s <%s>`' % (units, units)
    doc = getDocFromNode(ns, node, retval='')
    
    node_list = node.xpath('nx:enumeration', namespaces=ns)
    if len(node_list) == 1:
        doc += '\n'*2 + getEnumerationDescription(ns, node_list[0])

    return [name, typ, units, doc.strip()]


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


def getFieldData(ns, node):
    name = node.get('name')
    typ  = node.get('type', '(:ref:`NX_CHAR <NX_CHAR>`)')
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ':ref:`%s <%s>`' % (units, units)
    
    # TODO: look for "deprecated" element, add to doc
    
    doc = getDocFromNode(ns, node, retval='')
    
    node_list = node.xpath('nx:enumeration', namespaces=ns)
    if len(node_list) == 1:
        doc += '\n'*2 + getEnumerationDescription(ns, node_list[0])
    
    node_list = node.xpath('nx:dimensions', namespaces=ns)
    if len(node_list) == 1:
        doc += '\n'*2 + getDimensionsDescription(ns, node_list[0])
    
    return [name, typ, units, doc.strip()]


def getGroupData(ns, node):
    name = node.get('name', '')
    typ = node.get('type', '<ERROR!>')
    if typ.startswith('NX'):
        if name is '':
            name = '(%s)' % typ.lstrip('NX')
        typ = ':ref:`%s`' % typ
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ':ref:`%s <%s>`' % (units, units)
    doc = getDocFromNode(ns, node, retval='')
    return [name, typ, units, doc.strip()]


def getLinkData(ns, node):
    name = node.get('name')
    target = node.get('target')
    typ  = ':ref:`link`'
    units = ''
    
    # TODO: look for "deprecated" element, add to doc
    
    doc = 'target = ``%s``\n\n' % target
    doc += getDocFromNode(ns, node, retval='')
    return [name, typ, units, doc.strip()]


def main(tree, ns):
    root = tree.getroot()
    name = root.get('name')
    subdir = os.path.split(os.path.split(tree.docinfo.URL)[0])[1]
    index_cat = {
                 'base_classes': 'Base Classes',
                 'applications': 'Application Definitions',
                 'contributed_definitions': 'Contributed Definitions',
                 }[subdir]
    title = name
    print '.. auto-generated by a script: %s' % sys.argv[0]
    print
    print '.. index:: ! class definition -- %s; %s' % (index_cat, name)
    print '.. index:: ! %s' % name
    print
    print '.. _%s:\n' % name
    print '='*len(title)
    print title
    print '='*len(title)
       
    # various metrics and metadata about this specification
    t = rest_table.Table()
    t.labels = ['version', 'category', 'extends', ]
    extends = root.get('extends')
    if extends is not None:
        extends = ':ref:`%s`' % extends
    else:
        extends = ''
    parts = [
             root.get('version').strip(),
             root.get('category').strip(),
             extends,
             ]
    node_list = root.xpath('//nx:group', namespaces=ns)
    t.labels.append('groups cited')
    groups = []
    for node in node_list:
        g = node.get('type')
        g_ref = ':ref:`%s`' % g
        if g.startswith('NX') and g_ref not in groups:
            groups.append(g_ref)
    if len(groups) > 0:
        parts.append(', '.join(sorted(groups)))
    else:
        parts.append('none')
    t.rows.append(parts)
    print
    print t.reST(fmt='complex')

    # documentation
    print
    doc = getDocFromNode(ns, root)
    if doc is None:
        raise Exception, "No documentation for: " + name
    for line in doc.splitlines():
        print '%s' % line

    # TODO: change instances of \t to proper indentation
    fmt = '\n%s:\n\t%s'
    html_root = 'https://github.com/nexusformat/definitions/blob/master'
        
    # symbol table
    node_list = root.xpath('nx:symbols', namespaces=ns)
    if len(node_list) == 0:
        print fmt % ('symbol list', 'No symbol table.')
    elif len(node_list) > 1:
        print fmt % ('symbol list', 'Invalid symbol table.')
    else:
        print '\nsymbol list:'
        doc = getDocFromNode(ns, node_list[0])
        if doc is not None:
            for line in doc.splitlines():
                print '\t%s' % line
            print
        for node in node_list[0].xpath('nx:symbol', namespaces=ns):
            doc = getDocFromNode(ns, node)
            print '\t:%s:' % node.get('name')
            for line in doc.splitlines():
                print '\t\t%s' % line
            print

    # structure of NXDL specification
    print '\n%s:' % ':ref:`NXDL <NXDL>` source'
    print '\t%s/%s/%s.nxdl.xml' % (html_root, subdir, name)
    
    print '\n.. compound::\n'
    print '\t.. rubric:: Structure of %s\n' % name
    print '\t.. code-block:: guess'
    print '\t\t:linenos:\n'
    # relative path to XSLT
    XSLT_FILE = os.path.join(BASEDIR, '..', subdir, 'nxdlformat.xsl')
    # absolute path
    XSLT_FILE = os.path.abspath(XSLT_FILE)
    # same as: xsltproc NXDL_FILE XSLT_FILE
    transform = lxml.etree.XSLT(lxml.etree.parse(XSLT_FILE))
    for line in str(transform(root)).splitlines():
        print '\t\t%s' % line

    printMemberTable(ns, root, name, getNextTableXref(name))
    while len(SUBTABLES) > 0:
        item = SUBTABLES.pop(0)
        if item is not None:
            printMemberTable(ns, item['node'], item['name'], item['xref'])



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
            print "usage: %s someclass.nxdl.xml" % sys.argv[0]
            exit()
        NXDL_SCHEMA_FILE = sys.argv[1]

    # parse input file into tree
    if not os.path.exists(NXDL_SCHEMA_FILE):
        print "Cannot find %s" % NXDL_SCHEMA_FILE
        exit()
    tree = lxml.etree.parse(NXDL_SCHEMA_FILE)

    NAMESPACE = 'http://definition.nexusformat.org/nxdl/@NXDL_RELEASE@'
    ns = {'nx': NAMESPACE}
    
    main(tree, ns)
