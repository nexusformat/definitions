#!/usr/bin/env python
'''Reads a NeXus HDF5 file using the nexusformat module and plots the contents'''

from nexusformat.nexus import *

f = nxload('example.nxs')
print('Path to default plot is ', f.plottable_data.nxpath)
if f.plottable_data.ndim > 2:
  f.plottable_data[0].plot()
else:
  f.plot()
