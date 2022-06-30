#!/usr/bin/env python
"""
Writes a simple NeXus HDF5 file using h5py with links
according to the example from Figure 2.1 in the Design chapter
"""

from pathlib import Path

import numpy

from nexusformat.nexus import (NXdata, NXdetector, NXentry, NXfield,
                               NXinstrument, NXlink, nxopen)

filename = str(Path(__file__).absolute().parent.parent / "simple_example.dat")
buffer = numpy.loadtxt(filename).T
tthData = buffer[0]  # float[]
countsData = numpy.asarray(buffer[1], "int32")  # int[]

with nxopen("simple_example_write2.hdf5", "w") as f:  # create the HDF5 NeXus file
    f["entry"] = NXentry()
    f["entry/instrument"] = NXinstrument()
    f["entry/instrument/detector"] = NXdetector()

    # store the data in the NXdetector group
    f["entry/instrument/detector/two_theta"] = NXfield(tthData, units="degrees")
    f["entry/instrument/detector/counts"] = NXfield(countsData, units="counts")

    f["entry/data"] = NXdata(NXlink("/entry/instrument/detector/counts"),
                             NXlink("/entry/instrument/detector/two_theta"))
    f["entry/data"].set_default()
