#!/usr/bin/env python
"""Writes a NeXus HDF5 file using h5py and numpy"""

from pathlib import Path
from re import X
import numpy

from nexusformat.nexus import NXdata, NXentry, NXfield, nxopen

print("Write a NeXus HDF5 file")
fileName = "simple_example_basic.nexus.hdf5"

# load data from two column format
data_filename = str(Path(__file__).absolute().parent.parent / "simple_example.dat")
data = numpy.loadtxt(data_filename).T
mr_arr = data[0]
i00_arr = numpy.asarray(data[1], "int32")

# create the HDF5 NeXus file
with nxopen(fileName, "w") as f:

    # create the NXentry group
    f["entry"] = NXentry()
    f["entry/title"] = "1-D scan of I00 v. mr"

    # create the NXdata group
    x = NXfield(mr_arr, name="mr", units="degrees", long_name="USAXS mr (degrees)")
    y = NXfield(i00_arr, name="I00", units="counts",
                long_name="USAXS I00 (counts)")
    f["entry/mr_scan"] = NXdata(y, x)

print("wrote file:", fileName)
