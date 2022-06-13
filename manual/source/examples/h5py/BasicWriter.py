#!/usr/bin/env python
'''Writes a NeXus HDF5 file using h5py and numpy'''

import h5py    # HDF5 support
import numpy

print("Write a NeXus HDF5 file")
fileName = "prj_test.nexus.hdf5"
timestamp = "2010-10-18T17:17:04-0500"

# load data from two column format
data = numpy.loadtxt("input.dat").T
mr_arr = data[0]
i00_arr = numpy.asarray(data[1],'int32')

# create the HDF5 NeXus file
f = h5py.File(fileName, "w")
# point to the default data to be plotted
f.attrs['default']          = 'entry'
# give the HDF5 root some more attributes
f.attrs['file_name']        = fileName
f.attrs['file_time']        = timestamp
f.attrs['instrument']       = 'APS USAXS at 32ID-B'
f.attrs['creator']          = 'BasicWriter.py'
f.attrs['NeXus_version']    = '4.3.0'
f.attrs['HDF5_Version']     = h5py.version.hdf5_version
f.attrs['h5py_version']     = h5py.version.version

# create the NXentry group
nxentry = f.create_group('entry')
nxentry.attrs['NX_class'] = 'NXentry'
nxentry.attrs['default'] = 'mr_scan'
nxentry.create_dataset('title', data='1-D scan of I00 v. mr')

# create the NXentry group
nxdata = nxentry.create_group('mr_scan')
nxdata.attrs['NX_class'] = 'NXdata'
nxdata.attrs['signal'] = 'I00'      # Y axis of default plot
nxdata.attrs['axes'] = 'mr'         # X axis of default plot
nxdata.attrs['mr_indices'] = [0,]   # use "mr" as the first dimension of I00

# X axis data
ds = nxdata.create_dataset('mr', data=mr_arr)
ds.attrs['units'] = 'degrees'
ds.attrs['long_name'] = 'USAXS mr (degrees)'    # suggested X axis plot label

# Y axis data
ds = nxdata.create_dataset('I00', data=i00_arr)
ds.attrs['units'] = 'counts'
ds.attrs['long_name'] = 'USAXS I00 (counts)'    # suggested Y axis plot label

f.close()	# be CERTAIN to close the file

print("wrote file:", fileName)
