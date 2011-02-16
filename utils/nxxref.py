#!/usr/bin/env python

'''
Created on Feb 15, 2011

@summary: Read all the NeXus NXDL specifications and find
          all the group, field, attribute, and link 
          specifications.  Write an XML document
          with enough information to build a cross-reference.
@author: jemian
########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
'''


import os
import lxml.etree


def constructNxdlPath(tree, node, ns):
    '''
    @param tree: lxml.etree structure
    @param node: node to identify with text path
    @param ns: NXDL namespace string
    '''
    structuralPath = tree.getpath(node).split('/')[1:]
    cut = len(ns)+2
    result = ""
    for level in range(len(structuralPath)):
        path = '/' + '/'.join(structuralPath[0:level+1])
        n = tree.xpath(path)[0]
        cut = len(n.nsmap[None])+2
        tag = n.tag[cut:]
        name = n.get('name', '')
        typ_ = n.get('type', '')
        result += "/"
        if tag == 'definition' and typ_ == 'group':
            result += name
        else:
            if len(name) > 0:
                if tag == 'attribute':
                    result += "@"
                result += name
                if len(typ_) > 0 and tag not in ('field', 'attribute'):
                    result += ":"
            if len(typ_) > 0 and tag not in ('field', 'attribute'):
                result += typ_
    return result


def processFile(nxdlFile):
    results = []
    ns = {'nx': 'http://definition.nexusformat.org/nxdl/3.1'}
    cut = len( ns['nx'] ) + 2
    nxdlName = nxdlFile[:nxdlFile.find('.nxdl.xml')]
    
    tree = lxml.etree.parse(nxdlFile)
    root = tree.xpath("//nx:definition", namespaces=ns)[0]
    category = root.get('category', 'None')
    
    for element in ('group', 'field', 'attribute', 'link'):
        for item in tree.xpath("//nx:" + element, namespaces=ns):
            dict = {'NXDL': nxdlName, 'category': category}
            dict['tag'] = item.tag[cut:]
            dict['name'] = item.get("name", None)
            dict['type'] = item.get("type", "NX_CHAR")
            dict['NXDL_path'] = constructNxdlPath(tree, item, ns['nx'])
            results.append( dict )
    
    return results

def xrefTable(tree):
    '''
    @param tree: XML root node
    '''
    for item in tree.xpath("/NXDL_cross_reference//*"):
        p = '/' + '/'.join( item.get('NXDL_path').split('/')[2:] )
        nxdl = item.get('NXDL')
        print nxdl, p
    pass


if __name__ == '__main__':
    #NEXUS_ROOT = "/home/oxygen/JEMIAN/Documents/eclipse/NeXus/definitions/trunk"
    NEXUS_ROOT = ".."

    root = lxml.etree.Element("NXDL_cross_reference")
    owd = os.getcwd()

    for dir in ('base_classes', 'applications', 'contributed_definitions'):
        os.chdir( os.path.join(NEXUS_ROOT, dir) )
        for nxdlFile in os.listdir('.'):
            if nxdlFile.endswith('.nxdl.xml'):
                nxdlList = processFile( nxdlFile )
                print "%s: %d entries" % (nxdlFile, len(nxdlList))
                for dict in nxdlList:
                    #node = lxml.etree.SubElement(root, "item")
                    node = lxml.etree.SubElement(root, dict['tag'])
                    for k, v in dict.items():
                        if v != None and k != 'tag':
                            node.set(k, v)

    os.chdir(owd)

    f = open('nxdlxref.xml', 'w')
    f.write( lxml.etree.tostring(root, pretty_print=True) )
    f.close()
    
    #xrefTable(root)
    #paths = [item.get('NXDL_path') for item in root.xpath("/NXDL_cross_reference//*")]
    #paths.sort()
    #print "\n".join(paths)
