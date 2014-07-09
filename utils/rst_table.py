#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# 2014-07-09, copied from:  https://pypi.python.org/pypi/pyRestTable
#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

'''
Format a nice table in reST (restructured text)

Each cell may have multiple lines, separated by a newline.
The content of each cell will be rendered as str(cell).

EXAMPLE

These commands::

    import pyRestTable
    t = pyRestTable.Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.rows.append( ['class', 'NX_FLOAT', '', None, ] )
    t.rows.append( range(0,4) )
    t.rows.append( [None, t, 1.234, range(3)] )
    print t.reST(fmt='complex')

build this table source code::

    +------------+-----------------------------------------+--------+-------------------+
    | Name       | Type                                    | Units  | Description       |
    | and        |                                         |        | (and Occurrences) |
    | Attributes |                                         |        |                   |
    +============+=========================================+========+===================+
    | one,       | buckle my                               | shoe.  | ...               |
    | two        |                                         |        |                   |
    |            |                                         |        |                   |
    |            |                                         | three, |                   |
    |            |                                         | four   |                   |
    +------------+-----------------------------------------+--------+-------------------+
    | class      | NX_FLOAT                                |        | None              |
    +------------+-----------------------------------------+--------+-------------------+
    | 0          | 1                                       | 2      | 3                 |
    +------------+-----------------------------------------+--------+-------------------+
    | None       | <__main__.Table instance at 0x022B8EE0> | 1.234  | [0, 1, 2]         |
    +------------+-----------------------------------------+--------+-------------------+

'''


class Table:
    '''
    Construct a table in reST (no row or column spans).
    '''
    
    def __init__(self):
        self.rows = []
        self.labels = []
        self.use_tabular_columns = False
        self.alignment = []
        self.longtable = False
    
    def reST(self, indentation = '', fmt = 'simple'):
        '''render the table in reST format'''
        if len(self.alignment) == 0:
            #  set the default column alignments
            self.alignment = str('L '*len(self.labels)).strip().split()
        if not len(self.labels) == len(self.alignment):
            msg = "Number of column labels is different from column width specifiers"
            raise IndexError, msg
        return {'simple': self.simple_table,
                'complex': self.complex_table,}[fmt](indentation)
    
    def simple_table(self, indentation = ''):
        '''render the table in simple rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = " ".join(['='*w for w in width]) + '\n'
        fmt = " ".join(["%%-%ds" % w for w in width]) + '\n'
        
        rest = ''
        if self.use_tabular_columns:
            rest += indentation
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
        '''render the table in complex rest format'''
        # maximum column widths, considering possible line breaks in each cell
        width = self.find_widths()
        
        # build the row separators
        separator = '+' + "".join(['-'*(w+2) + '+' for w in width]) + '\n'
        label_sep = '+' + "".join(['='*(w+2) + '+' for w in width]) + '\n'
        fmt = '|' + "".join([" %%-%ds |" % w for w in width]) + '\n'
        
        rest = ''
        if self.use_tabular_columns:
            rest += indentation
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
        Demo list-table: (not implemented yet)
        
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
        '''
        raise NotImplementedError
    
    def _row(self, row, fmt, indentation = ''):
        '''
        Given a list of entry nodes in this table row, 
        build one line of the table with one text from each entry element.
        The lines are separated by line breaks.
        '''
        def pick_line(text, lineNum):
            '''
            Pick the specific line of text or supply an empty string.
            Convenience routine when analyzing tables.
            '''
            if lineNum < len(text):
                s = text[lineNum]
            else:
                s = ""
            return s
        text = ""
        if len(row) > 0:
            for line_num in range( max(map(len, [str(_).split("\n") for _ in row])) ):
                item = [pick_line(str(r).split("\n"), line_num) for r in row]
                text += indentation + fmt % tuple(item)
        return text
    
    def find_widths(self):
        '''
        measure the maximum width of each column, 
        considering possible line breaks in each cell
        '''
        width = []
        if len(self.labels) > 0:
            width = [max(map(len, str(_).split("\n"))) for _ in self.labels]
        for row in self.rows:
            row_width = [max(map(len, str(_).split("\n"))) for _ in row]
            if len(width) == 0:
                width = row_width
            width = map( max, zip(width, row_width) )
        return width


def main():
    '''test routine used to demo the code'''
    t = Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.rows.append( ['class', 'NX_FLOAT', '', None, ] )
    t.rows.append( range(0,4) )
    t.rows.append( [None, t, 1.234, range(3)] )
    print t.reST(fmt='simple')
    print ""
    print t.reST(fmt='complex')
    print ""
    t.longtable = True
    t.use_tabular_columns = True
    t.alignment = 'l L c r'.split()
    print t.reST(fmt='complex')


if __name__ == '__main__':
    main()
