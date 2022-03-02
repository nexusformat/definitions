#!/usr/bin/env python

'''
Read the NXDL field types specification and find
all the valid data types.  Write a restructured
text (.rst) document for use in the NeXus manual in 
the NXDL chapter.
'''


import os, sys
import lxml.etree
import textwrap


TITLE_MARKERS = '- + ~ ^ * @'.split()  # used for underscoring section titles
INDENTATION = ' '*4


ELEMENT_DICT = {
                'attribute': '''
An ``attribute`` element can *only* be a child of a 
``field`` or ``group`` element.
It is used to define *attribute* elements to be used and their data types
and possibly an enumeration of allowed values.

For more details, see: 
:ref:`NXDL.data.type.attributeType`
                ''',
                
                'definition': '''
A ``definition`` element can *only* be used
at the root level of an NXDL specification.
Note:  Due to the large number of attributes of the ``definition`` element,
they have been omitted from the figure below.

For more details, see: 
:ref:`NXDL.data.type.definition`,
:ref:`NXDL.data.type.definitionType`, and
:ref:`NXDL.data.type.definitionTypeAttr`
                ''',
                
                'dimensions': '''
The ``dimensions`` element describes the *shape* of an array.
It is used *only* as a child of a ``field`` element.

For more details, see: 
:ref:`NXDL.data.type.dimensionsType`
                ''',
                
                'doc': '''
A ``doc`` element can be a child of most NXDL elements.  In most cases, the
content of the ``doc`` element will also become part of the NeXus manual.

:element: {any}:

In documentation, it may be useful to
use an element that is not directly specified by the NXDL language. 
The *any* element here says that one can use any element
at all in a ``doc`` element and NXDL will not process it but pass it through.

For more details, see: 
:ref:`NXDL.data.type.docType`
                ''',
                
                'enumeration': '''
An ``enumeration`` element can *only* be a child of a 
``field`` or ``attribute`` element.
It is used to restrict the available choices to a predefined list,
such as to control varieties in spelling of a controversial word (such as
*metre* vs. *meter*).

For more details, see: 
:ref:`NXDL.data.type.enumerationType`
                ''',
                
                'field': '''
The ``field`` element provides the value of a named item.  Many different attributes
are available to further define the ``field``.  Some of the attributes are not
allowed to be used together (such as ``axes`` and ``axis``); see the documentation
of each for details.
It is used *only* as a child of a ``group`` element.

For more details, see: 
:ref:`NXDL.data.type.fieldType`
                ''',
                
                'choice': '''
A ``choice`` element is used when a named group might take one
of several possible NeXus base classes.  Logically, it must
have at least two group children.

For more details, see: 
:ref:`NXDL.data.type.choiceType`
                ''',
                
                'group': '''
A ``group`` element can *only* be a child of a 
``definition`` or ``group`` element.
It describes a common level of organization in a NeXus data file, similar
to a subdirectory in a file directory tree.

For more details, see: 
:ref:`NXDL.data.type.groupType`
                ''',
                
                'link': '''
.. index:: 
    single: link target

A ``link`` element can *only* be a child of a 
``definition``,
``field``, or ``group`` element.
It describes the path to the original source of the parent
``definition``,
``field``, or ``group``.

For more details, see: 
:ref:`NXDL.data.type.linkType`
                ''',
                
                'symbols': '''
A ``symbols`` element can *only* be a child of a ``definition`` element.
It defines the array index symbols to be used when defining arrays as
``field`` elements with common dimensions and lengths.

For more details, see: 
:ref:`NXDL.data.type.symbolsType`
                ''',
                }

DATATYPE_DICT = {
                 'basicComponent': '''/xs:schema//xs:complexType[@name='basicComponent']''',
                 'validItemName': '''/xs:schema//xs:simpleType[@name='validItemName']''',
                 'validNXClassName': '''/xs:schema//xs:simpleType[@name='validNXClassName']''',
                 'validTargetName': '''/xs:schema//xs:simpleType[@name='validTargetName']''',
                 'nonNegativeUnbounded': '''/xs:schema//xs:simpleType[@name='nonNegativeUnbounded']''',
                 }

ELEMENT_PREAMBLE = '''
=============================
NXDL Elements and Field Types
=============================

The documentation in this section has been obtained directly 
from the NXDL Schema file:  *nxdl.xsd*.
First, the basic elements are defined in alphabetical order.  
Attributes to an element are indicated immediately following the element
and are preceded with an "@" symbol, such as
**@attribute**.
Then, the common data types used within the NXDL specification are defined.
Pay particular attention to the rules for *validItemName*
and  *validNXClassName*.

..
    2010-11-29,PRJ:
    This contains a lot of special case code to lay out the NXDL chapter.
    It could be cleaner but that would also involve some cooperation on 
    anyone who edits nxdl.xsd which is sure to break.  The special case ensures
    the parts come out in the chosen order.  BUT, it is possible that new
    items in nxdl.xsd will not automatically go in the manual.
    Can this be streamlined with some common methods?
    Also, there is probably too much documentation in nxdl.xsd.  Obscures the function.

.. index::
    see: attribute; NXDL attribute
    ! single: NXDL elements

.. _NXDL.elements:

NXDL Elements
=============

    '''

DATATYPE_PREAMBLE = '''

.. _NXDL.data.types.internal:

NXDL Field Types (internal)
===========================

Field types that define the NXDL language are described here.
These data types are defined in the XSD Schema (``nxdl.xsd``)
and are used in various parts of the Schema to define common structures
or to simplify a complicated entry.  While the data types are not intended for
use in NXDL specifications, they define structures that may be used in NXDL specifications. 

'''

DATATYPE_POSTAMBLE = '''
**The** ``xs:string`` **data type**
    The ``xs:string`` data type can contain characters, 
    line feeds, carriage returns, and tab characters.
    See https://www.w3schools.com/xml/schema_dtypes_string.asp
    for more details.

**The** ``xs:token`` **data type**
    The ``xs:string`` data type is derived from the 
    ``xs:string`` data type.

    The ``xs:token`` data type also contains characters, 
    but the XML processor will remove line feeds, carriage returns, tabs, 
    leading and trailing spaces, and multiple spaces.
    See https://www.w3schools.com/xml/schema_dtypes_string.asp
    for more details.
'''


def _tagMatch(ns, parent, match_list):
    '''match this tag to a list'''
    if parent is None:
        raise ValueError("Must supply a valid parent node")
    parent_tag = parent.tag
    tag_found = False
    for item in match_list:
        # this routine only handles certain XML Schema components
        tag_found = parent_tag == '{%s}%s' % (ns['xs'], item)
        if tag_found:
            break
    return tag_found


def _indent(indentLevel):
    return INDENTATION*indentLevel


def printTitle(title, indentLevel):
    print(title)
    print(TITLE_MARKERS[indentLevel]*len(title) + '\n')


def generalHandler(ns, parent=None, indentLevel=0):
    '''Handle XML nodes like the former XSLT template'''
    # ignore things we don't know how to handle
    known_tags = ('complexType', 'simpleType', 'group', 'element', 'attribute')
    if not _tagMatch(ns, parent, known_tags):
        return
    
    parent_name = parent.get('name')
    if parent_name is None:
        return
    
    simple_tag = parent.tag[parent.tag.find('}')+1:]    # cut off the namespace identifier
    
    # <varlistentry> ...
    name = parent_name  # + ' data type'
    if simple_tag == 'attribute':
        name = '@' + name
    
    if indentLevel == 0 and not simple_tag in ('attribute'):
        print('.. index:: ! %s (NXDL data type)\n' % name)
        print('\n.. _%s:\n' % ('NXDL.data.type.'+name))

    printTitle(name, indentLevel)
    
    printDocs(ns, parent, indentLevel)
    
    if len(parent.xpath('xs:attribute', namespaces=ns)) > 0:
        printTitle("Attributes of "+name, indentLevel+1)
        applyTemplates(ns, parent, 'xs:attribute', indentLevel+1)

    node_list = parent.xpath('xs:restriction', namespaces=ns)
    if len(node_list) > 0:
        #printTitle("Restrictions of "+name, indentLevel+1)
        restrictionHandler(ns, node_list[0], indentLevel+1)
    node_list = parent.xpath('xs:simpleType/xs:restriction/xs:enumeration', namespaces=ns)
    if len(node_list) > 0:
#        printTitle("Enumerations of "+name, indentLevel+1)
        applyTemplates(ns, parent, 'xs:simpleType/xs:restriction', 
                       indentLevel+1, handler=restrictionHandler)
    
    if len(parent.xpath('xs:sequence/xs:element', namespaces=ns)) > 0:
        printTitle("Elements of "+name, indentLevel+1)
        applyTemplates(ns, parent, 'xs:sequence/xs:element', indentLevel+1)
    
    node_list = parent.xpath('xs:sequence/xs:group', namespaces=ns)
    if len(node_list) > 0:
        printTitle("Groups under "+name, indentLevel+1)
        printDocs(ns, node_list[0], indentLevel+1)

    applyTemplates(ns, parent, 'xs:simpleType', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexType', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexType/xs:attribute', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexContent/xs:extension/xs:attribute', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexType/xs:sequence/xs:attribute', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexType/xs:sequence/xs:element', indentLevel+1)
    applyTemplates(ns, parent, 'xs:complexContent/xs:extension/xs:sequence/xs:element', indentLevel+1)


def restrictionHandler(ns, parent=None, indentLevel=0):
    '''Handle XSD restriction nodes like the former XSLT template'''
    if not _tagMatch(ns, parent, ('restriction',)):
        return
    printDocs(ns, parent, indentLevel)
    print('\n')
    print(_indent(indentLevel) + 'The value may be any')
    base = parent.get('base')
    pattern_nodes = parent.xpath('xs:pattern', namespaces=ns)
    enumeration_nodes = parent.xpath('xs:enumeration', namespaces=ns)
    if len(pattern_nodes) > 0:
        print(_indent(indentLevel) + '``%s``' % base + ' that *also* matches the regular expression::\n')
        print(_indent(indentLevel) + ' '*4 + pattern_nodes[0].get('value'))
    elif len(pattern_nodes) > 0:
        # how will this be reached?  Perhaps a deprecated procedure
        print(_indent(indentLevel) + '``%s``' % base + ' from this list:')
        for node in enumeration_nodes:
            enumerationHandler(ns, node, indentLevel)
            printDocs(ns, node, indentLevel)
        print(_indent(indentLevel))
    elif len(enumeration_nodes) > 0:
        print(_indent(indentLevel) + 'one from this list only:\n')
        for node in enumeration_nodes:
            enumerationHandler(ns, node, indentLevel)
            printDocs(ns, parent, indentLevel)
        print(_indent(indentLevel))
    else:
        print('@' + base)
    print('\n')


def enumerationHandler(ns, parent=None, indentLevel=0):
    '''Handle XSD enumeration nodes like the former XSLT template'''
    if not _tagMatch(ns, parent, ['enumeration']):
        return
    print(_indent(indentLevel) + '* ``%s``' % parent.get('value'))
    printDocs(ns, parent, indentLevel)


def applyTemplates(ns, parent, path, indentLevel, handler=generalHandler):
    '''iterate the nodes found on the supplied XPath expression'''
    db = {}
    for node in parent.xpath(path, namespaces=ns):
        name = node.get('name') or node.get('ref') or node.get('value')
        if name is not None:
            if name in ('nx:groupGroup',):
                print(">"*45, name)
            if name in db:
                raise KeyError("Duplicate name found: " + name)
            db[name] = node
    for name in sorted(db):
        node = db[name]
        handler(ns, node, indentLevel)
        #printDocs(ns, node, indentLevel)


def printDocs(ns, parent, indentLevel=0):
    docs = getDocFromNode(ns, parent)
    if docs is not None:
        print(_indent(indentLevel) + '\n')
        for line in docs.splitlines():
            print(_indent(indentLevel) + line)
        print(_indent(indentLevel) + '\n')


def getDocFromNode(ns, node, retval=None):
    annotation_node = node.find('xs:annotation', ns)
    if annotation_node is None:
        return retval
    documentation_node = annotation_node.find('xs:documentation', ns)
    if documentation_node is None:
        return retval
    
    # Be sure to grab _all_ content in the <xs:documentation> node.
    # In the documentation nodes, use XML entities ("&lt;"" instead of "<")
    # for documentation characters that would otherwise be considered as XML.
    s = lxml.etree.tostring(documentation_node, method="text", pretty_print=True)
    rst = s.decode().lstrip('\n')  # remove any leading blank lines
    rst = rst.rstrip()  # remove any trailing white space
    text = textwrap.dedent(rst)  # remove common leading space

    # substitute HTML entities in markup: "<" for "&lt;"
    # thanks: http://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
    try:		# see #661
        import html
        text = html.unescape(text)
    except (ImportError, AttributeError):
        from html import parser as HTMLParser
        htmlparser = HTMLParser.HTMLParser()
        text = htmlparser.unescape(text)

    return text.lstrip()


def addFigure(name, indentLevel=0):
    fmt = '''
.. compound::

    .. _%s:

    .. figure:: %s
        :alt: fig.nxdl/nxdl_%s
        :width: %s

        Graphical representation of the NXDL ``%s`` element

    .. Images of NXDL structure are generated from nxdl.xsd source
        using the Eclipse XML Schema Editor (Web Tools Platform).  Open the nxdl.xsd file and choose the
        "Design" tab.  Identify the structure to be documented and double-click to expand
        as needed to show the detail.  Use the XSD > "Export Diagram as Image ..." menu item (also available
        as button in top toolbar).
        Set the name: "nxdl_%s.png" and move the file into the correct location using
        your operating system's commands.  Commit the revision to version control.
    '''
    imageFile = 'img/nxdl/nxdl_%s.png' % name
    figure_id = 'fig.nxdl_%s' % name
    if not os.path.exists(os.path.abspath(imageFile)):
        return
    text = fmt % (figure_id, imageFile, name, '80%', name, name, )
    indent = _indent(indentLevel)
    for line in text.splitlines():
        print(indent + line)
    print('\n')


def pickNodesFromXpath(ns, parent, path):
    return parent.xpath(path, namespaces=ns)


def main(tree, ns):
    print(".. auto-generated by script: " + sys.argv[0])
    print(ELEMENT_PREAMBLE)

    for name in sorted(ELEMENT_DICT):
        print("")
        print('.. index:: ! %s (NXDL element)\n' % name)
        print('.. _%s:\n' % name)
        printTitle(name, indentLevel=0)
        print('\n')
        print(ELEMENT_DICT[name])
        print('\n')
        addFigure(name, indentLevel=0)
        

    print(DATATYPE_PREAMBLE)

    path_list = (
                 "/xs:schema/xs:complexType[@name='attributeType']",
                 "/xs:schema/xs:element[@name='definition']",
                 "/xs:schema/xs:complexType[@name='definitionType']",
                 "/xs:schema/xs:simpleType[@name='definitionTypeAttr']",
                 "/xs:schema/xs:complexType[@name='dimensionsType']",
                 "/xs:schema/xs:complexType[@name='docType']",
                 "/xs:schema/xs:complexType[@name='enumerationType']",
                 "/xs:schema/xs:complexType[@name='fieldType']",
                 "/xs:schema/xs:complexType[@name='choiceType']",
                 "/xs:schema/xs:complexType[@name='groupType']",
                 "/xs:schema/xs:complexType[@name='linkType']",
                 "/xs:schema/xs:complexType[@name='symbolsType']",
                 "/xs:schema/xs:complexType[@name='basicComponent']",
                 "/xs:schema/xs:simpleType[@name='validItemName']",
                 "/xs:schema/xs:simpleType[@name='validNXClassName']",
                 "/xs:schema/xs:simpleType[@name='validTargetName']",
                 "/xs:schema/xs:simpleType[@name='nonNegativeUnbounded']",
                 )
    for path in path_list:
        nodes = pickNodesFromXpath(ns, tree, path)
        print("\n.. Xpath = %s\n" % path)
        generalHandler(ns, parent=nodes[0])

    print(DATATYPE_POSTAMBLE)


if __name__ == '__main__':
    developermode = True
    developermode = False
    if developermode and len(sys.argv) != 2:
        path = os.path.dirname(__file__)
        NXDL_SCHEMA_FILE = os.path.join(path, '..', 'nxdl.xsd')
    else:
        if len(sys.argv) != 2:
            print("usage: %s nxdl.xsd" % sys.argv[0])
            exit()
        NXDL_SCHEMA_FILE = sys.argv[1]
    if not os.path.exists(NXDL_SCHEMA_FILE):
        print("Cannot find %s" % NXDL_SCHEMA_FILE)
        exit()
        
    tree = lxml.etree.parse(NXDL_SCHEMA_FILE)
    NAMESPACE = 'http://www.w3.org/2001/XMLSchema'
    ns = {'xs': NAMESPACE}
    
    main(tree, ns)


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
