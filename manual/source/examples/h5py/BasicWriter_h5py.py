#!/usr/bin/env python
'''Writes a NeXus HDF5 file using the h5py and numpy packages'''

import numpy
import h5py

fileName = "prj_test.nexus.hdf5"

# load data from two column format
data = numpy.loadtxt("input.dat").T
mr_arr = data[0]
I00_arr = numpy.asarray(data[1],'int32')

# create the HDF5 NeXus file (with statement will ensure that file is closed)
with h5py.File(fileName, "w") as f:
	# give the HDF5 root some basic attributes
	f.attrs['file_name']        = fileName
	f.attrs['file_time']        = datetime.datetime.now().isoformat()
	f.attrs['HDF5_Version']     = h5py.version.hdf5_version
	f.attrs['h5py_version']     = h5py.version.version
	f.attrs['instrument']       = 'APS USAXS at 32ID-B'
	f.attrs['creator']          = 'BasicWriter_h5py.py'
	f.attrs['NeXus_version']    = '4.4.3'

	# create the NXentry group
	f['entry'].attrs['NX_class'] = 'NXentry'

	# create the NXdata group
	f['entry/data'].attrs['NX_class'] = 'NXdata'
	f['entry/data'].attrs['signal'] = 'I00'      # Y axis of default plot
	f['entry/data'].attrs['axes'] = 'mr'         # X axis of default plot

	# X axis data
	f['entry/data/mr'] = mr_arr
	f['entry/data/mr'].attrs['units'] = 'degrees'
	f['entry/data/mr'].attrs['long_name'] = 'USAXS mr (degrees)' # X axis plot label

	# Y axis data
	f['entry/data/I00'] = I00_arr
	f['entry/data/I00'].attrs['units'] = 'counts'
	f['entry/data/I00'].attrs['long_name'] = 'USAXS I00 (counts)' # Y axis plot label

	# give a title to the plot
	f['entry/title'] = '1-D scan of I00 v. mr'
	
	# point to the default data to be plotted
	f.attrs['default']          = 'entry'
	f['entry'].attrs['default'] = 'data'

