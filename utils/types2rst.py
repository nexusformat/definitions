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


class Table:
    '''
    Construct a table in reST (no row or column spans).
    Each cell may have multiple lines, separated by "\n"
    
    EXAMPLE
    
    These commands::
    
        t = Table()
        t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
        t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
        t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
        print t.reST(format='complex')

    build this table source code::
    
        +------------+-----------+--------+-------------------+
        + Name       + Type      + Units  + Description       +
        + and        +           +        + (and Occurrences) +
        + Attributes +           +        +                   +
        +============+===========+========+===================+
        + one,       + buckle my + shoe.  + ...               +
        + two        +           +        +                   +
        +            +           +        +                   +
        +            +           + three, +                   +
        +            +           + four   +                   +
        +------------+-----------+--------+-------------------+
        + class      + NX_FLOAT  + ..     + ..                +
        +------------+-----------+--------+-------------------+
    '''
    
    def __init__(self):
        self.rows = []
        self.labels = []
    
    def reST(self, indentation = '', format = 'simple'):
        '''return the table in reST format'''
        return {'simple': self.simple_table,
                'complex': self.complex_table,}[format](indentation)
    
    def simple_table(self, indentation = ''):
        '''return the table in simple rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = " ".join(['='*w for w in width]) + '\n'
        fmt = " ".join(["%%-%ds" % w for w in width]) + '\n'
        
        rest = '%s%s' % (indentation, separator)         # top line
        rest += self._row(self.labels, fmt, indentation) # labels
        rest += '%s%s' % (indentation, separator)        # end of the labels
        for row in self.rows:
            rest += self._row(row, fmt, indentation)     # each row
        rest += '%s%s' % (indentation, separator)        # end of table
        return rest
    
    def complex_table(self, indentation = ''):
        '''return the table in complex rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = '+' + "".join(['-'*(w+2) + '+' for w in width]) + '\n'
        label_sep = '+' + "".join(['='*(w+2) + '+' for w in width]) + '\n'
        fmt = '|' + "".join([" %%-%ds |" % w for w in width]) + '\n'
        
        rest = '%s%s' % (indentation, separator)         # top line
        rest += self._row(self.labels, fmt, indentation) # labels
        rest += '%s%s' % (indentation, label_sep)         # end of the labels
        for row in self.rows:
            rest += self._row(row, fmt, indentation)     # each row
            rest += '%s%s' % (indentation, separator)    # row separator
        return rest
    
    def _row(self, row, fmt, indentation = ''):
        '''
        Given a list of <entry nodes in this table <row, 
        build one line of the table with one text from each entry element.
        The lines are separated by line breaks.
        '''
        text = ""
        if len(row) > 0:
            for line_num in range( max(map(len, [_.split("\n") for _ in row])) ):
                item = [self._pick_line(r.split("\n"), line_num) for r in row]
                text += indentation + fmt % tuple(item)
        return text
    
    def find_widths(self):
        '''
    measure the maximum width of each column, 
    considering possible line breaks in each cell
    '''
        width = []
        if len(self.labels) > 0:
            width = [max(map(len, _.split("\n"))) for _ in self.labels]
        for row in self.rows:
            row_width = [max(map(len, _.split("\n"))) for _ in row]
            if len(width) == 0:
                width = row_width
            width = map( max, zip(width, row_width) )
        return width
    
    def _pick_line(self, text, lineNum):
        '''
        Pick the specific line of text or supply an empty string.
        Convenience routine when analyzing tables.
        '''
        if lineNum < len(text):
            s = text[lineNum]
        else:
            s = ""
        return s



TITLE = 'Data Types allowed in NXDL specifications'
if len(sys.argv) != 2:
    print "usage: %s nxdlTypes.xsd" % sys.argv[0]
    exit()
NXDL_TYPES_FILE = sys.argv[1]
if not os.path.exists(NXDL_TYPES_FILE):
    print "Cannot find %s" % NXDL_TYPES_FILE
    exit()
#NXDL_TYPES_FILE = os.path.join('..', 'nxdlTypes.xsd')

tree = lxml.etree.parse(NXDL_TYPES_FILE)

output = ['.. auto-generated -- DO NOT EDIT']
output.append('')
#output.append('.. _%s:' % 'nxdl-types')
#output.append('')
#output.append('='*len(TITLE))
#output.append(TITLE)
#output.append('='*len(TITLE))
#output.append('')

labels = ('term', 'description')
output.append('.. tabularcolumns:: %s' % '|l|L|')
output.append('')
db = {}

NAMESPACE = 'http://www.w3.org/2001/XMLSchema'
ns = {'xs': NAMESPACE}
root = tree.xpath('//xs:schema', namespaces=ns)[0]
s = '//xs:simpleType'
for node in tree.xpath("//xs:simpleType", namespaces=ns):
    if node.get('name') == 'NAPI':
        for item in node.xpath('xs:restriction//xs:enumeration', namespaces=ns):
            key = '``%s``' % item.get('value')
            words = item.xpath('xs:annotation/xs:documentation', namespaces=ns)[0]
            db[key] = words.text

print '\n'.join(output)

t = Table()
t.labels = labels
for key in sorted(db):
    t.rows.append( [key, db[key]] )
print t.reST(format='complex')
