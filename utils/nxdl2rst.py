#!/usr/bin/env python

'''
Read the the NeXus NXDL class specification and describe it.  
Write a restructured text (.rst) document for use in the NeXus manual in 
the NeXus NXDL Classes chapter.
'''

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################


import os, sys
import lxml.etree
import rst_table


TITLE_MARKERS = '# - + ~ ^ * @'.split()  # used for underscoring section titles
INDENTATION = ' '*4
# find the directory of this python file
BASEDIR = os.path.split(os.path.abspath(__file__))[0]


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





def _indent(indentLevel):
    return INDENTATION*indentLevel


def getDocFromNode(ns, node, retval=None):
    docnodes = node.xpath('nx:doc', namespaces=ns)
    if docnodes == None:
        return retval
    if not len(docnodes) == 1:
        return retval
    
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
                raise "Something wrong with indentation on this line:\n" + line
            text += '\n' + line[indent:]
    return text.lstrip()


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
    print
    print '.. _%s:\n' % name
    print '='*len(title)
    print title
    print '='*len(title) 
       
    t = rst_table.Table()
    t.labels = ['version', 'category', 'extends', ]
    parts = [
             root.get('version').strip(),
             root.get('category').strip(),
             ':ref:`%s`' % root.get('extends').strip(),
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
    print t.reST(format='complex')

    # documentation
    print
    doc = getDocFromNode(ns, root)
    for line in doc.splitlines():
        print '%s' % line

    # TODO: change instances of \t to proper indentation
    fmt = '\n%s:\n\t%s'
    html_root = 'http://svn.nexusformat.org/definitions/trunk'
        
    # symbol table
    node_list = root.xpath('nx:symbols', namespaces=ns)
    if len(node_list) == 0:
        print fmt % ('symbol list', 'No symbol table.')
    elif len(node_list) > 1:
        print fmt % ('symbol list', 'Invalid symbol table.')
    else:
        print '\nsymbol list:'
        doc = getDocFromNode(ns, node_list[0])
        for line in doc.splitlines():
            print '\t%s' % line
        print
        for node in node_list[0].xpath('nx:symbol', namespaces=ns):
            doc = getDocFromNode(ns, node)
            print '\t:%s:' % node.get('name')
            for line in doc.splitlines():
                print '\t\t%s' % line
            print
    
#    # other NeXus groups used by this specification
#    node_list = root.xpath('//nx:group', namespaces=ns)
#    groups = []
#    for node in node_list:
#        t = node.get('type')
#        t_ref = ':ref:`%s`' % t
#        if t.startswith('NX') and t_ref not in groups:
#            groups.append(t_ref)
#    if len(groups) > 0:
#        print fmt % ('other classes included', ', '.join(sorted(groups)))
#    else:
#        print fmt % ('other classes included', 'none')

    # structure of NXDL specification
    print '\n%s:' % ':ref:`NXDL <NXDL>` source'
    print '\t%s/%s/%s.nxdl.xml' % (html_root, subdir, name)
    print fmt % ('svnid', str(root.get('svnid')).strip('$').strip())
    
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

    # TODO: show a table listing the attributes, groups, and fields, use subtables as required
    #  At each level, iterate over the children at each level to build one table.  If there is a group, then append another level and repeat.
    
    # table(s) describing the specification
    t = rst_table.Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.alignment = ('p{0.2\linewidth}', 'p{0.2\linewidth}', 'p{0.2\linewidth}', 'p{0.4\linewidth}', )
    #t.longtable = True
    for node in root.xpath('nx:field', namespaces=ns):
        t.rows.append( getFieldData(ns, node) )
        for subnode in node.xpath('nx:attribute', namespaces=ns):
            t.rows.append( getAttributeData(ns, subnode) )
    for node in root.xpath('nx:group', namespaces=ns):
        t.rows.append( getGroupData(ns, node) )
        for subnode in node.xpath('nx:attribute', namespaces=ns):
            t.rows.append( getAttributeData(ns, subnode) )
    print
    print t.reST(format='complex')


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
    return [name, typ, units, doc]


def getFieldData(ns, node):
    name = node.get('name')
    typ  = node.get('type', '(:ref:`NX_CHAR <NX_CHAR>`)')
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ':ref:`%s <%s>`' % (units, units)
    doc = getDocFromNode(ns, node, retval='')
    return [name, typ, units, doc]


def getAttributeData(ns, node):
    name = '@' + node.get('name')
    typ  = node.get('type', '(:ref:`NX_CHAR <NX_CHAR>`)')
    if typ.startswith('NX_'):
        typ = ':ref:`%s <%s>`' % (typ, typ)
    units = node.get('units', '')
    if units.startswith('NX_'):
        units = ':ref:`%s <%s>`' % (units, units)
    doc = getDocFromNode(ns, node, retval='')
    return [name, typ, units, doc]


if __name__ == '__main__':
    developermode =True
    if developermode and len(sys.argv) != 2:
        NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'applications', 'NXarchive.nxdl.xml')
        #NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'base_classes', 'NXcrystal.nxdl.xml')
        NXDL_SCHEMA_FILE = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXarpes.nxdl.xml')
    else:
        if len(sys.argv) != 2:
            print "usage: %s someclass.nxdl.xml" % sys.argv[0]
            exit()
        NXDL_SCHEMA_FILE = sys.argv[1]
    if not os.path.exists(NXDL_SCHEMA_FILE):
        print "Cannot find %s" % NXDL_SCHEMA_FILE
        exit()
        
    tree = lxml.etree.parse(NXDL_SCHEMA_FILE)
    NAMESPACE = 'http://definition.nexusformat.org/nxdl/@NXDL_RELEASE@'
    ns = {'nx': NAMESPACE}
    
    main(tree, ns)
