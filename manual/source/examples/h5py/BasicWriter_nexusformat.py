#!/usr/bin/env python
'''Writes a NeXus HDF5 file using the nexusformat and numpy packages'''

import numpy as np
from nexusformat.nexus import *

fileName = "prj_test.nexus.hdf5"

# load data from two column format
data = numpy.loadtxt("input.dat").T
mr_arr = data[0]
I00_arr = numpy.asarray(data[1],'int32')

# create hdf5 object in memory
f = NXroot()
# give the HDF5 root some basic attributes




f.attrs['instrument']       = 'APS USAXS at 32ID-B'
f.attrs['creator']          = 'BasicWriter_nexusformat.py'
f.attrs['NeXus_version']    = '4.4.3'

# create the NXentry group
f['entry'] = NXentry()

# create the NXdata group
f['entry/data'] = NXdata(
	NXfield(I00_arr, name='USAXS I00 (counts)', units='counts'), # Y axis information
	NXfield(mr_arr, name='USAXS mr (degrees)', units='degrees')  # X axis information
	)










# give a title to the plot
f['entry/title'] = '1-D scan of I00 v. mr'

# point to the default data to be plotted
f['entry/data'].set_default()

# write hdf5 object to disk
f.save(fileName, 'w')
