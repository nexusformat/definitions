#!/usr/bin/env python
from argparse import ArgumentError

########### SVN repository information ###################
# $Date: 2011-11-02 15:27:36 -0500 (Wed, 02 Nov 2011) $
# $Author: Pete Jemian $
# $Revision: 995 $
# $URL: https://svn.nexusformat.org/definitions/trunk/sphinx/nxdl2rst.py $
# $Id: nxdl2rst.py 995 2011-11-02 20:27:36Z Pete Jemian $
########### SVN repository information ###################

'''
construct a table in reST
'''


class Table:
    '''
    Construct a table in reST (no row or column spans).
    Each cell may have multiple lines, separated by "\n"
    
    EXAMPLE
    
    These commands::
    
        t = Table()
        t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
        t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", ""] )
        t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
        print t.reST()

    build this table:
    
    +------------+-----------+--------+-------------------+
    + Name       + Type      + Units  + Description       +
    + and        +           +        + (and Occurrences) +
    + Attributes +           +        +                   +
    +============+===========+========+===================+
    + one,       + buckle my + shoe.  +                   +
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
    
    def reST(self, indentation = ''):
        '''return the table in reST format'''
        
        # maximum column widths, considering possible line breaks in each cell
        width = [max(map(len, _.split("\n"))) for _ in self.labels]
        for row in self.rows:
            row_width = [max(map(len, _.split("\n"))) for _ in row]
            width = map( max, zip(width, row_width) )
        
        # build the row separators
        separator = '+' + "".join(['-'*(w+2) + '+' for w in width]) + '\n'
        labelSep  = '+' + "".join(['='*(w+2) + '+' for w in width]) + '\n'
        fmt = '+' + "".join([" %%-%ds +" % w for w in width]) + '\n'
        
        reST = '%s%s' % (indentation, separator)         # top line
        reST += self._row(self.labels, fmt, indentation) # labels
        reST += '%s%s' % (indentation, labelSep)         # end of the labels
        for row in self.rows:
            reST += self._row(row, fmt, indentation)     # each row
            reST += '%s%s' % (indentation, separator)    # row separator
        return reST
    
    def _row(self, row, fmt, indentation = ''):
        text = ""
        for lineNum in range( max(map(len, [_.split("\n") for _ in row])) ):
            L = [self.pick_line(T.split("\n"), lineNum) for T in row]
            text += indentation + fmt % tuple(L)
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


if __name__ == '__main__':
    t = Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", ""] )
    t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
    print t.reST()
