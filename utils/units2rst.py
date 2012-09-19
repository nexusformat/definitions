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
import rst_table


def worker(nodeMatchString):
    if len(sys.argv) != 2:
        print "usage: %s nxdlTypes.xsd" % sys.argv[0]
        exit()
    NXDL_TYPES_FILE = sys.argv[1]
    if not os.path.exists(NXDL_TYPES_FILE):
        print "Cannot find %s" % NXDL_TYPES_FILE
        exit()
        
    tree = lxml.etree.parse(NXDL_TYPES_FILE)
    
    output = ['.. auto-generated -- DO NOT EDIT']
    output.append('')
    
    labels = ('term', 'description')
    output.append('.. nodeMatchString : %s' % nodeMatchString)
    output.append('')
    db = {}
    
    NAMESPACE = 'http://www.w3.org/2001/XMLSchema'
    ns = {'xs': NAMESPACE}
    root = tree.xpath('//xs:schema', namespaces=ns)[0]
    s = '//xs:simpleType'
    for node in tree.xpath("//xs:simpleType", namespaces=ns):
        if node.get('name') == nodeMatchString:
            for item in node.xpath('xs:restriction//xs:enumeration', namespaces=ns):
                key = '``%s``' % item.get('value')
                words = item.xpath('xs:annotation/xs:documentation', namespaces=ns)[0]
                db[key] = words.text
    
    print '\n'.join(output)
    
    t = rst_table.Table()
    t.labels = labels
    t.alignment = ['l', 'L']
    for key in sorted(db):
        t.rows.append( [key, db[key]] )
    print t.reST(format='complex')


if __name__ == '__main__':
    worker('anyUnitsAttr')
