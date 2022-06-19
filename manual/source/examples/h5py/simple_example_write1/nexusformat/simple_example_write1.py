#!/usr/bin/env python
"""
Writes the simplest NeXus HDF5 file using h5py

Uses method accepted at 2014NIAC
according to the example from Figure 1.3
in the Introduction chapter
"""

from pathlib import Path

import numpy

from nexusformat.nexus import NXdata, NXentry, NXfield, nxopen

filename = str(Path(__file__).absolute().parent.parent / "simple_example.dat")
buffer = numpy.loadtxt(filename).T
tthData = buffer[0]
countsData = numpy.asarray(buffer[1], "int32")

with nxopen("simple_example_write1.hdf5", "w") as f:  # create the NeXus file
    f["Scan"] = NXentry()
    tth = NXfield(tthData, name="two_theta", units="degrees")
    counts = NXfield(countsData, name="counts", units="counts")
    f["Scan/data"] = NXdata(counts, tth)
