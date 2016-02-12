#!/usr/bin/env python
'''
Writes the simplest NeXus HDF5 file using 
a simple helper library with h5py and numpy calls
according to the example from Figure 1.3 
in the Introduction chapter
'''

import my_lib

INPUT_FILE = 'input.dat'
HDF5_FILE = 'writer_1_3.hdf5'

#---------------------------

tthData, countsData = my_lib.get2ColumnData(INPUT_FILE)

f = my_lib.makeFile(HDF5_FILE)
# since this is a simple example, no attributes are used at this point

nxentry = my_lib.makeGroup(f, 'Scan', 'NXentry')
nxdata = my_lib.makeGroup(nxentry, 'data', 'NXdata', 
                          signal='counts', 
                          axes='two_theta',
                          two_theta_indices = [0,],
                          )

my_lib.makeDataset(nxdata, "two_theta", tthData, units='degrees')
my_lib.makeDataset(nxdata, "counts", countsData, units='counts')

f.close()	# be CERTAIN to close the file
