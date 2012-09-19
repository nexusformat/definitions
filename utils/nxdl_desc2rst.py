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
    print '%s\n%s\n' % (name, '='*len(name))
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
    print '''
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

    '''
    
    NAMESPACE = 'http://www.w3.org/2001/XMLSchema'
    ns = {'xs': NAMESPACE}

    #    describeElement(ns, name, node)
    for name in sorted(ELEMENT_LIST):
        fmt = '''/xs:schema//xs:complexType[@name='%sType']'''
        docpath = fmt % name
        describeElement(ns, name=name, docpath=docpath)
        
    # TODO: What about the common data types?
