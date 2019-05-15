#!/usr/bin/env python
'''
Writes the simplest NeXus HDF5 file using h5py 

Uses method accepted at 2014NIAC
according to the example from Figure 1.3 
in the Introduction chapter
'''

import h5py
import numpy

buffer = numpy.loadtxt("input.dat").T
tthData = buffer[0]                             # float[]
countsData = numpy.asarray(buffer[1],'int32')   # int[]

f = h5py.File("writer_1_3.hdf5", "w")  # create the HDF5 NeXus file
# since this is a simple example, no attributes are used at this point

nxentry = f.create_group(u"Scan")
nxentry.attrs[u"NX_class"] = u"NXentry"

nxdata = nxentry.create_group(u"data")
nxdata.attrs["NX_class"] = u"NXdata"
nxdata.attrs[u"signal"] = u"counts"
nxdata.attrs[u"axes"] = u"two_theta"
nxdata.attrs[u"two_theta_indices"] = [0,]

tth = nxdata.create_dataset(u"two_theta", data=tthData)
tth.attrs[u"units"] = u"degrees"

counts = nxdata.create_dataset(u"counts", data=countsData)
counts.attrs[u"units"] = u"counts"

f.close()	# be CERTAIN to close the file
