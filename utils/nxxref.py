#!/usr/bin/env python

'''
Created on Feb 15, 2011

@summary: Read all the NeXus NXDL specifications and find
          all the group, field, attribute, and link
          specifications.  Write an XML document
          with enough information to build a cross-reference.
@author: jemian
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
    #
    # @note: It is non-standard to prepend the NXDL class name to the path
    #
    pathStartIndex = 0   # NXDL class prepended to path
    pathStartIndex = 1   # normal path
    for level in range(pathStartIndex, len(structuralPath)):
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
            if element == 'link':
                default = None      # keeps the type of its link source
            else:
                default = 'NX_CHAR'
            dict['type'] = item.get("type", default)
            dict['NXDL_path'] = constructNxdlPath(tree, item, ns['nx'])
            # now, build a key to help sorting in the XSLT
            # easier to build the sort key here
            if element == 'group':
                if dict['name'] == None:
                    key = dict['type']
                else:
                    key = "%s:%s" % (dict['name'], dict['type'])
            else:
                key = dict['name']
                if element == 'link':
                    key += "~~" + element  # links should sort later
                    key += "~~" + nxdlName
            if element == 'link':
                dict['target'] = item.get("target", None)
            dict['key'] = key
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
    NEXUS_ROOT = ".."  # code is in [definitions]/trunk/utils directory

    root = lxml.etree.Element("NXDL_cross_reference")
    owd = os.getcwd()
	
    categoryDict = {'base_classes': 'base_class', 
		'applications': 'application', 
		'contributed_definitions': 'contributed'}
    NXDLnode = lxml.etree.SubElement(root, 'NXDL')
    declarations = lxml.etree.SubElement(root, 'declarations')

    dirEntries = {}
    classes = {}
    for dir, category in categoryDict.items():
        os.chdir( os.path.join(NEXUS_ROOT, dir) )
        dirEntries[dir] = 0
        classes[dir] = []
        for nxdlFile in os.listdir('.'):
            if nxdlFile.endswith('.nxdl.xml'):
                nxdlList = processFile( nxdlFile )
                nxdlName = nxdlFile[:nxdlFile.find('.nxdl.xml')]
                print "%s: %d entries" % (nxdlFile, len(nxdlList))
                dirEntries[dir] += len(nxdlList)
                classes[dir].append( nxdlName )
                node = lxml.etree.SubElement(NXDLnode, 'class')
                node.set('name', nxdlName)
                node.set('file', nxdlFile)
                node.set('category', category)
                node.set('entries', str(len(nxdlList)))
                for dict in nxdlList:
                    node = lxml.etree.SubElement(declarations, dict['tag'])
                    for k, v in dict.items():
                        if v != None and k != 'tag':
                            node.set(k, v)

    os.chdir(owd)
    
    summary = lxml.etree.SubElement(NXDLnode, 'summary')
    totalEntries = 0
    totalClasses = 0
    for dir, n in dirEntries.items():
        category = lxml.etree.SubElement(summary, 'category')
        category.set('name', categoryDict[dir])
        category.set('entries', str(n))
        category.set('count', str(len(classes[dir])))
        totalEntries += n
        totalClasses += len(classes[dir])
    print "%d entries total, %d classes total" % (totalEntries, totalClasses)
    category = lxml.etree.SubElement(summary, 'category')
    category.set('name', 'total')
    category.set('entries', str(totalEntries))
    category.set('count', str(totalClasses))

    f = open('nxdlxref.xml', 'w')
    f.write( '<?xml version="1.0" encoding="UTF-8"?>' + "\n")
    f.write( '<?xml-stylesheet type="text/xsl" href="nxdlxref.xsl" ?>' + "\n")
    f.write( lxml.etree.tostring(root, pretty_print=True) )
    f.close()
