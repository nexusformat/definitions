#!/usr/bin/env python
'''
Writes a NeXus HDF5 file using h5py with links to data in other HDF5 files.

This example is based on ``writer_2_1``.
'''

import h5py
import numpy

FILE_HDF5_MASTER = u"external_master.hdf5"
FILE_HDF5_ANGLES = u"external_angles.hdf5"
FILE_HDF5_COUNTS = u"external_counts.hdf5"

#---------------------------

# get some data
buffer = numpy.loadtxt("input.dat").T
tthData = buffer[0]                             # float[]
countsData = numpy.asarray(buffer[1],'int32')   # int[]

# put the angle data in an external (non-NeXus) HDF5 data file
f = h5py.File(FILE_HDF5_ANGLES, "w")
ds = f.create_dataset(u"angles", data=tthData)
ds.attrs[u"units"] = u"degrees"
f.close()    # be CERTAIN to close the file


# put the detector counts in an external HDF5 data file 
# with *incomplete* NeXus structure (no NXdata group)
f = h5py.File(FILE_HDF5_COUNTS, "w")
nxentry = f.create_group(u"entry")
nxentry.attrs[u"NX_class"] = u"NXentry"
nxinstrument = nxentry.create_group(u"instrument")
nxinstrument.attrs[u"NX_class"] = u"NXinstrument"
nxdetector = nxinstrument.create_group(u"detector")
nxdetector.attrs[u"NX_class"] = u"NXdetector"
ds = nxdetector.create_dataset(u"counts", data=countsData)
ds.attrs[u"units"] = u"counts"
# link the "two_theta" data stored in separate file
local_addr = nxdetector.name + u"/two_theta"
f[local_addr] = h5py.ExternalLink(FILE_HDF5_ANGLES, u"/angles")
f.close()

# create a master NeXus HDF5 file
f = h5py.File(FILE_HDF5_MASTER, "w")
f.attrs[u"default"] = u"entry"
nxentry = f.create_group(u"entry")
nxentry.attrs[u"NX_class"] =u"NXentry"
nxentry.attrs[u"default"] = u"data"
nxdata = nxentry.create_group(u"data")
nxdata.attrs[u"NX_class"] = u"NXdata"

# link in the signal data
local_addr = '/entry/data/counts'
external_addr = u"/entry/instrument/detector/counts"
f[local_addr] = h5py.ExternalLink(FILE_HDF5_COUNTS, external_addr)
nxdata.attrs[u"signal"] = u"counts"

# link in the axes data
local_addr = u"/entry/data/two_theta"
f[local_addr] = h5py.ExternalLink(FILE_HDF5_ANGLES, u"/angles")
nxdata.attrs[u"axes"] = u"two_theta"
nxdata.attrs[u"two_theta_indices"] = [0,]

local_addr = u"/entry/instrument"
f[local_addr] = h5py.ExternalLink(FILE_HDF5_COUNTS, u"/entry/instrument")

f.close()
