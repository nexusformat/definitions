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
        t.alignment = ('l', 'L', 'l', 'L', )
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
        self.alignment = []
        self.longtable = False
    
    def reST(self, indentation = '', format = 'simple'):
        '''return the table in reST format'''
        if len(self.alignment) == 0:
            #  set the default column alignments
            self.alignment = ['L' for item in self.labels]
        if not len(self.labels) == len(self.alignment):
            raise "Number of column labels is different from column width specifiers"
        return {'simple': self.simple_table,
                'complex': self.complex_table,}[format](indentation)
    
    def simple_table(self, indentation = ''):
        '''return the table in simple rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = " ".join(['='*w for w in width]) + '\n'
        fmt = " ".join(["%%-%ds" % w for w in width]) + '\n'
        
        rest = indentation
        rest += '.. tabularcolumns:: |%s|' % '|'.join(self.alignment)
        if self.longtable:
            rest += '\n%s%s' % (' '*4, ':longtable:')
        rest += '\n\n'
        rest += '%s%s' % (indentation, separator)        # top line of table
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
        
        rest = indentation
        rest += '.. tabularcolumns:: |%s|' % '|'.join(self.alignment)
        if self.longtable:
            rest += '\n%s%s' % (' '*4, ':longtable:')
        rest += '\n\n'
        rest += '%s%s' % (indentation, separator)        # top line of table
        rest += self._row(self.labels, fmt, indentation) # labels
        rest += '%s%s' % (indentation, label_sep)         # end of the labels
        for row in self.rows:
            rest += self._row(row, fmt, indentation)     # each row
            rest += '%s%s' % (indentation, separator)    # row separator
        return rest
    
    def list_table(self, indentation = ''):
        '''
            Demo list-table:
            
            .. Does this work?
            
            It was found on this page
                http://docutils.sourceforge.net/docs/ref/rst/directives.html
            
            .. list-table:: Frozen Delights!
               :widths: 15 10 30
               :header-rows: 1
            
               * - Treat
                 - Quantity
                 - Description
               * - Albatross
                 - 2.99
                 - On a stick!
               * - Crunchy Frog
                 - 1.49
                 - If we took the bones out, it wouldn't be
                   crunchy, now would it?
               * - Gannet Ripple
                 - 1.99
                 - On a stick!
            
            .. Yes, it _does_ work.  
               Use it for the tables in the NXDL description.
'''
    
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
            row_width = [max(map(len, str(_).split("\n"))) for _ in row]
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


if __name__ == '__main__':
    t = Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
    print t.reST()
    print '\n'*3
    t.alignment = ('l', 'L', 'l', 'L', )
    print t.reST(format='complex')
