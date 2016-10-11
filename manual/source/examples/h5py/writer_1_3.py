#!/usr/bin/env python
'''
Writes the simplest NeXus HDF5 file using h5py 

Uses method accepted at 2014NIAC
according to the example from Figure 1.3 
in the Introduction chapter
'''

import h5py
import numpy

buffer = numpy.loadtxt('input.dat').T
tthData = buffer[0]                             # float[]
countsData = numpy.asarray(buffer[1],'int32')   # int[]

f = h5py.File('writer_1_3.hdf5', "w")  # create the HDF5 NeXus file
# since this is a simple example, no attributes are used at this point

nxentry = f.create_group('Scan')
nxentry.attrs["NX_class"] = 'NXentry'

nxdata = nxentry.create_group('data')
nxdata.attrs["NX_class"] = 'NXdata'
nxdata.attrs['signal'] = "counts"
nxdata.attrs['axes'] = "two_theta"
nxdata.attrs['two_theta_indices'] = [0,]

tth = nxdata.create_dataset("two_theta", data=tthData)
tth.attrs['units'] = "degrees"

counts = nxdata.create_dataset("counts", data=countsData)
counts.attrs['units'] = "counts"

f.close()	# be CERTAIN to close the file
