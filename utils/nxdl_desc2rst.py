#!/usr/bin/env python

'''
Read the the NeXus NXDL types specification and find
all the valid data types.  Write a restructured
text (.rst) document for use in the NeXus manual in 
the NXDL chapter.
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

# TODO: look at ALL the select= clauses in nxdl_desc2rst.xsl before declaring this job is complete
# replicate the function of this clause
#      <xslt:template match="xsd:complexType|xsd:simpleType|xsd:group|xsd:element|xsd:attribute">



ELEMENT_LIST = (
                'attribute',
                'definition',
                'dimensions',
                'doc',
                'enumeration',
                'field',
                'group',
                'link',
                'symbols',
                )

DATATYPE_DICT = {
                 'basicComponent': '''/xs:schema//xs:complexType[@name='basicComponent']''',
                 'validItemName': '''/xs:schema//xs:simpleType[@name='validItemName']''',
                 'validNXClassName': '''/xs:schema//xs:simpleType[@name='validNXClassName']''',
                 'validTargetName': '''/xs:schema//xs:simpleType[@name='validTargetName']''',
                 'nonNegativeUnbounded': '''/xs:schema//xs:simpleType[@name='nonNegativeUnbounded']''',
                 }

ELEMENT_PREAMBLE = '''
===============================
NXDL Elements and Data Types
===============================

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

.. _NXDL.elements:

NXDL Elements
=================

    '''

DATATYPE_PREAMBLE = '''

.. _NXDL.data.types:

NXDL Data Types (internal)
============================

Data types that define the NXDL language are described here.
These data types are defined in the XSD Schema (``nxdl.xsd``)
and are used in various parts of the Schema to define common structures
or to simplify a complicated entry.  While the data types are not intended for
use in NXDL specifications, they define structures that may be used in NXDL specifications. 

'''

DATATYPE_POSTAMBLE = '''
**The** ``xs:string`` **data type**
    The ``xs:string`` data type can contain characters, 
    line feeds, carriage returns, and tab characters.
    See http://www.w3schools.com/Schema/schema_dtypes_string.asp 
    for more details.

**The** ``xs:token`` **data type**
    The ``xs:string`` data type is derived from the 
    ``xs:string`` data type.

    The ``xs:token`` data type also contains characters, 
    but the XML processor will remove line feeds, carriage returns, tabs, 
    leading and trailing spaces, and multiple spaces.
    See http://www.w3schools.com/Schema/schema_dtypes_string.asp 
    for more details.
'''

def getDocFromNode(node, retval=None):
    docnodes = node.xpath('xs:annotation//xs:documentation', namespaces=ns)
    if docnodes == None:
        return retval
    if not len(docnodes) == 1:
        return retval
    text = docnodes[0].text
    # TODO: what about embedded tabs? v. spaces
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


def describeElement(ns, name=None, docpath=None):
    if name == None:
        raise "Must provide an element name"
    print '\n.. _NXDL.element.%s:\n' % name
    print '%s\n%s\n' % (name, '-'*len(name))
    print '.. index:: NXDL element; %s\n' % name

    # next: document this name
    node = tree.xpath(docpath, namespaces=ns)[0]
    print getDocFromNode(node)

    # next: get the image for this node
    fmt = '''
.. compound::

    .. _fig.nxdl_%s:

    .. figure:: img/nxdl/nxdl_%s.jpg
        :alt: fig.nxdl/nxdl_%s
        :width: %s

        Graphical representation of the NXDL ``%s`` element

    .. Images of NXDL structure are generated from nxdl.xsd source
        using the oXygen XML Editor.  Open the nxdl.xsd file and choose the
        "Design" tab.  Identify the structure to be documented and expand
        as needed to show the detail.  Right click and select "Save as Image ..."
        Set the name: "nxdl_%s.jpg" and move the file into the correct location using
        your operating system's commands.  Commit the revision to version control.
    '''
    print fmt % (name, name, name, '80%', name, name, )

    # next, look for attributes nodes
    attributes = node.xpath('xs:attribute', namespaces=ns)
    if attributes is not None and len(attributes) > 0:
        print '.. rubric:: List of Attributes of ``%s`` element\n' % name
        db = {}
        for item in attributes:
            item_name = '%s' % item.get('name')
            prefix = ''
            usage = item.get('use')
            if usage is not None:
                prefix = '(**%s**) ' % usage
            item_doc = prefix + getDocFromNode(item)
            db[item_name] = item_doc
        # make sure the required attributes appear first
        for k in sorted(db):
            if db[k].startswith('(**required**) '):
                print ':%s:' % k
                for line in db[k].splitlines():
                    print '    %s' % line
                print ''
        # now show the other attributes
        for k in sorted(db):
            if not db[k].startswith('(**required**) '):
                print ':%s:' % k
                for line in db[k].splitlines():
                    print '    %s' % line
                print ''

    # next, look for a sequence, it will contain nodes for variables
    variables = node.xpath('xs:sequence//xs:element', namespaces=ns)
    if variables is None:
        pass
    # TODO: also look for xs:complexContent/xs:extension/xs:sequence//xs:element
    if variables is not None and len(variables) > 0:
        print '.. rubric:: List of Variables in ``%s`` element\n' % name
        db = {}
        for item in variables:
            item_name = '%s' % item.get('name')
            item_doc = getDocFromNode(item)
            db[item_name] = item_doc
        for k in sorted(db):
            print ':%s:' % k
            for line in db[k].splitlines():
                print '    %s' % line
            print ''

        # TODO: consider all these cases?
        #    <xslt:apply-templates select="xsd:sequence//xsd:element"/>
        #    <xslt:apply-templates select="xsd:simpleType"/>
        #    <xslt:apply-templates select="xsd:complexType"/>
        #    <xslt:apply-templates select="xsd:complexType//xsd:attribute"/>


def describeDatatype(ns, name=None, docpath=None):
    if name == None:
        raise "Must provide a data type name"


if __name__ == '__main__':
    developermode =True
    if developermode and len(sys.argv) != 2:
        NXDL_SCHEMA_FILE = os.path.join('..', 'nxdl.xsd')
    else:
        if len(sys.argv) != 2:
            print "usage: %s nxdl.xsd" % sys.argv[0]
            exit()
        NXDL_SCHEMA_FILE = sys.argv[1]
    if not os.path.exists(NXDL_SCHEMA_FILE):
        print "Cannot find %s" % NXDL_SCHEMA_FILE
        exit()
        
    tree = lxml.etree.parse(NXDL_SCHEMA_FILE)
    
    print ".. auto-generated by a script"
    print ELEMENT_PREAMBLE
    
    NAMESPACE = 'http://www.w3.org/2001/XMLSchema'
    ns = {'xs': NAMESPACE}

    for name in sorted(ELEMENT_LIST):
        fmt = '''/xs:schema//xs:complexType[@name='%sType']'''
        docpath = fmt % name
        describeElement(ns, name=name, docpath=docpath)

    print DATATYPE_PREAMBLE

    for name in sorted(DATATYPE_DICT):
        docpath = DATATYPE_DICT[name]
        describeDatatype(ns, name=name, docpath=docpath)

    print DATATYPE_POSTAMBLE
