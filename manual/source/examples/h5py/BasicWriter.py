#!/usr/bin/env python
'''Writes a NeXus HDF5 file using h5py and numpy'''

import h5py    # HDF5 support
import numpy
import my_lib  # uses h5py

print "Write a NeXus HDF5 file"
fileName = "prj_test.nexus.hdf5"
timestamp = "2010-10-18T17:17:04-0500"

# load data from two column format
data = numpy.loadtxt('input.dat').T
mr_arr = data[0]
i00_arr = numpy.asarray(data[1],'int32')

# create the HDF5 NeXus file
f = my_lib.makeFile(fileName, file_name=fileName,
        file_time=timestamp,
        instrument="APS USAXS at 32ID-B",
        creator="$Id$",
        NeXus_version="4.3.0",
        HDF5_Version=h5py.version.hdf5_version,
        h5py_version=h5py.version.version)

nxentry = my_lib.makeGroup(f, "entry", "NXentry")
my_lib.makeDataset(nxentry, 'title', data='1-D scan of I00 v. mr')

nxdata = my_lib.makeGroup(nxentry, "mr_scan", "NXdata")

my_lib.makeDataset(nxdata,  "mr",  mr_arr, units='degrees', 
                   long_name='USAXS mr (degrees)')

my_lib.makeDataset(nxdata,  "I00",  i00_arr, units='counts',
      signal='1',     # Y axis of default plot
      axes='mr',	     # name "mr" as X axis
      long_name='USAXS I00 (counts)')

f.close()	# be CERTAIN to close the file

print "wrote file:", fileName
