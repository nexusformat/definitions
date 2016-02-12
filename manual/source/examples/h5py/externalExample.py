#!/usr/bin/env python
'''
Writes a NeXus HDF5 file using h5py with links to data in other HDF5 files.

This example is based on ``writer_2_1``.
'''

import my_lib

FILE_INPUT = 'input.dat'
FILE_HDF5_MASTER = 'external_master.hdf5'
FILE_HDF5_ANGLES = 'external_angles.hdf5'
FILE_HDF5_COUNTS = 'external_counts.hdf5'

#---------------------------

# get some data
tthData, countsData = my_lib.get2ColumnData(FILE_INPUT)

# put the angle data in an external (non-NeXus) HDF5 data file
f = my_lib.makeFile(FILE_HDF5_ANGLES)  # create an HDF5 file (non-NeXus)
tth = my_lib.makeDataset(f, "angles", tthData, units='degrees')
f.close()    # be CERTAIN to close the file


# put the detector counts in an external NeXus HDF5 data file
f = my_lib.makeFile(FILE_HDF5_COUNTS)
nxentry = my_lib.makeGroup(f, 'entry', 'NXentry')
nxinstrument = my_lib.makeGroup(nxentry, 'instrument', 'NXinstrument')
nxdetector = my_lib.makeGroup(nxinstrument, 'detector', 'NXdetector')
counts = my_lib.makeDataset(nxdetector, "counts", countsData, units='counts')
# make a link since "two_theta" has not been stored here
my_lib.makeExternalLink(f, FILE_HDF5_ANGLES, 
                        '/angles', nxdetector.name+'/two_theta')
f.close()

# create a master NeXus HDF5 file
f = my_lib.makeFile(FILE_HDF5_MASTER, default='entry')
nxentry = my_lib.makeGroup(f, 'entry', 'NXentry', default='data')
nxdata = my_lib.makeGroup(nxentry, 'data', 'NXdata')

ds = my_lib.makeExternalLink(f, FILE_HDF5_COUNTS, 
                        '/entry/instrument/detector/counts', 
                        nxdata.name+'/counts')
nxdata.attrs["signal"] = 'counts'

ds = my_lib.makeExternalLink(f, 
                             FILE_HDF5_ANGLES, 
                             '/angles', 
                             nxdata.name+'/two_theta')
nxdata.attrs["axes"] = 'two_theta'
nxdata.attrs["two_theta_indices"] = [0,]

my_lib.makeExternalLink(f, FILE_HDF5_COUNTS, 
                        '/entry/instrument', 
                        nxentry.name+'/instrument')
f.close()
