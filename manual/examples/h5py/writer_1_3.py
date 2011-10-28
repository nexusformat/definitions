#!/usr/bin/env python
'''
Writes the simplest NeXus HDF5 file using h5py
according to the example from Figure 1.3 
in the Introduction chapter
'''

import my_lib

INPUT_FILE = 'input.dat'
HDF5_FILE = 'writer_1_3.hdf5'

#---------------------------

tthData, countsData = my_lib.get_2column_data(INPUT_FILE)

f = my_lib.makeFile(HDF5_FILE)  # create the HDF5 NeXus file

nxentry = my_lib.makeGroup(f, 'entry', 'NXentry')
nxdata = my_lib.makeGroup(nxentry, 'data', 'NXdata')

# call h5py library routine directly rather than our my_lib support
tth = nxdata.create_dataset("two_theta", data=tthData)
tth.attrs['units'] = "degrees"

counts = nxdata.create_dataset("counts", data=countsData)
counts.attrs['units'] = "counts"
counts.attrs['signal'] = "1"
counts.attrs['axes'] = "two_theta"

f.close()	# be CERTAIN to close the file
