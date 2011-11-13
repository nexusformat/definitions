#!/usr/bin/env python

########### SVN repository information ###################
# $Date: 2011-11-02 15:27:36 -0500 (Wed, 02 Nov 2011) $
# $Author: Pete Jemian $
# $Revision: 995 $
# $URL: https://svn.nexusformat.org/definitions/trunk/sphinx/nxdl2rst.py $
# $Id: nxdl2rst.py 995 2011-11-02 20:27:36Z Pete Jemian $
########### SVN repository information ###################

'''
construct a restructured text table
'''


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
    
    def reST(self, indentation = '', fmt = 'simple'):
        '''return the table in reST format'''
        return {'simple': self.simple_table,
                'complex': self.complex_table,}[fmt](indentation)
    
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
                item = [self.pick_line(r.split("\n"), line_num) for r in row]
                text += indentation + fmt % tuple(item)
        return text
    
    def pick_line(self, text, lineNum):
        '''
        pick the specific line of text or supply an empty string
        '''
        if lineNum < len(text):
            s = text[lineNum]
        else:
            s = ""
        return s
    
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


if __name__ == '__main__':
    t = Table()
    t.labels = ('Name\nand\nAttributes', 
                'Type', 
                'Units', 
                'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", ""] )
    t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
    print t.reST()
