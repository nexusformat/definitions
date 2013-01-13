#!/usr/bin/env python
'''
Writes a simple NeXus HDF5 file using h5py with links
according to the example from Figure 2.1 in the Design chapter
'''

import my_lib

INPUT_FILE = 'input.dat'
HDF5_FILE = 'writer_2_1.hdf5'

#---------------------------

tthData, countsData = my_lib.get2ColumnData(INPUT_FILE)

f = my_lib.makeFile(HDF5_FILE)  # create the HDF5 NeXus file

nxentry = my_lib.makeGroup(f, 'entry', 'NXentry')
nxinstrument = my_lib.makeGroup(nxentry, 'instrument', 'NXinstrument')
nxdetector = my_lib.makeGroup(nxinstrument, 'detector', 'NXdetector')

tth = my_lib.makeDataset(nxdetector, "two_theta", tthData, units='degrees')
counts = my_lib.makeDataset(nxdetector, "counts", countsData, 
                   units='counts', signal=1, axes='two_theta')

nxdata = my_lib.makeGroup(nxentry, 'data', 'NXdata')
my_lib.makeLink(nxdetector, tth, nxdata.name+'/two_theta')
my_lib.makeLink(nxdetector, counts, nxdata.name+'/counts')

f.close()	# be CERTAIN to close the file
