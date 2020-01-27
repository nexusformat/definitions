#!/usr/bin/env python
'''
Writes a simple NeXus HDF5 file using h5py with links
according to the example from Figure 2.1 in the Design chapter
'''

import h5py
import numpy

buffer = numpy.loadtxt("input.dat").T
tthData = buffer[0]                             # float[]
countsData = numpy.asarray(buffer[1],'int32')   # int[]

f = h5py.File("writer_2_1.hdf5", "w")  # create the HDF5 NeXus file
f.attrs[u"default"] = u"entry"

nxentry = f.create_group(u"entry")
nxentry.attrs[u"NX_class"] = u"NXentry"
nxentry.attrs[u"default"] = u"data"

nxinstrument = nxentry.create_group(u"instrument")
nxinstrument.attrs[u"NX_class"] = u"NXinstrument"

nxdetector = nxinstrument.create_group(u"detector")
nxdetector.attrs[u"NX_class"] = u"NXdetector"

# store the data in the NXdetector group
ds_tth = nxdetector.create_dataset(u"two_theta", data=tthData)
ds_tth.attrs[u"units"] = u"degrees"
ds_counts = nxdetector.create_dataset(u"counts", data=countsData)
ds_counts.attrs[u"units"] = u"counts"

# create the NXdata group to define the default plot
nxdata = nxentry.create_group(u"data")
nxdata.attrs[u"NX_class"] = u"NXdata"
nxdata.attrs[u"signal"] = u"counts"
nxdata.attrs[u"axes"] = u"two_theta"
nxdata.attrs[u"two_theta_indices"] = [0,]

source_addr = u"/entry/instrument/detector/two_theta"   # existing data
target_addr = u"two_theta"                              # new location
ds_tth.attrs[u"target"] = source_addr                   # a NeXus API convention for links
nxdata[target_addr] = f[source_addr]                    # hard link
# nxdata._id.link(source_addr, target_addr, h5py.h5g.LINK_HARD)

source_addr = u"/entry/instrument/detector/counts"      # existing data
target_addr = u"counts"                                 # new location
ds_counts.attrs[u"target"] = source_addr                # a NeXus API convention for links
nxdata[target_addr] = f[source_addr]                    # hard link
# nxdata._id.link(source_addr, target_addr, h5py.h5g.LINK_HARD)

f.close()	# be CERTAIN to close the file
