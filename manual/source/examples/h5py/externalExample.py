#!/usr/bin/env python
'''
Writes a NeXus HDF5 file using h5py with links to data in other HDF5 files.

This example is based on ``writer_2_1``.
'''

import h5py
import numpy

FILE_INPUT = 'input.dat'
FILE_HDF5_MASTER = 'external_master.hdf5'
FILE_HDF5_ANGLES = 'external_angles.hdf5'
FILE_HDF5_COUNTS = 'external_counts.hdf5'

#---------------------------

# get some data
buffer = numpy.loadtxt(FILE_INPUT).T
tthData = buffer[0]                             # float[]
countsData = numpy.asarray(buffer[1],'int32')   # int[]

# put the angle data in an external (non-NeXus) HDF5 data file
f = h5py.File(FILE_HDF5_ANGLES, "w")
ds = f.create_dataset('angles', tthData)
ds.attrs['units'] = 'degrees'
f.close()    # be CERTAIN to close the file


# put the detector counts in an external HDF5 data file 
# with *incomplete* NeXus structure (no NXdata group)
f = h5py.File(FILE_HDF5_COUNTS, "w")
nxentry = f.create_group('entry')
nxentry.attrs['NX_class'] = 'NXentry'
nxinstrument = nxentry.create_group('instrument')
nxinstrument.attrs['NX_class'] = 'NXinstrument'
nxentry = nxinstrument.create_group('detector')
nxdetector.attrs['NX_class'] = 'NXdetector'
ds = nxdetector.create_dataset('counts', countsData)
ds.attrs['units'] = 'counts'
# link the "two_theta" data stored in separate file
local_name = nxdetector.name+'/two_theta'
f[local_name] = h5py.ExternalLink(FILE_HDF5_ANGLES, '/angles')
f.close()

# create a master NeXus HDF5 file
f = h5py.File(FILE_HDF5_MASTER, "w")
f.attrs['default'] = 'entry'
nxentry = f.create_group('entry')
nxentry.attrs['NX_class'] = 'NXentry'
nxentry.attrs["default"] = 'entry'
nxdata = nxentry.create_group('data')
nxdata.attrs['NX_class'] = 'NXdata'

# link in the signal data
local_name = nxdata.name+'/counts'
f[local_name] = h5py.ExternalLink(FILE_HDF5_COUNTS, 
                                   '/entry/instrument/detector/counts')
nxdata.attrs['signal'] = 'counts'

# link in the axes data
local_name = nxdata.name+'/two_theta'
f[local_name] = h5py.ExternalLink(FILE_HDF5_ANGLES, '/angles')
nxdata.attrs['axes'] = 'two_theta'
nxdata.attrs['two_theta_indices'] = [0,]

local_name = nxentry.name+'/instrument'
f[local_name] = h5py.ExternalLink(FILE_HDF5_COUNTS, '/entry/instrument')

f.close()
