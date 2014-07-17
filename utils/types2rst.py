#!/usr/bin/env python

'''
Read the the NeXus NXDL types specification and find
all the valid data types.  Write a restructured
text (.rst) document for use in the NeXus manual in 
the NXDL chapter.
'''


import units2rst


if __name__ == '__main__':
    units2rst.worker('NAPI', section = 'data')
