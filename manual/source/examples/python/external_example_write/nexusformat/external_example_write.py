#!/usr/bin/env python
"""
Writes a NeXus HDF5 file using h5py with links to data in other HDF5 files.

This example is based on ``writer_2_1``.
"""

from pathlib import Path

import h5py
import numpy

from nexusformat.nexus import (NXdata, NXdetector, NXentry, NXfield,
                               NXinstrument, NXlink, nxopen)

FILE_HDF5_MASTER = "external_master.hdf5"
FILE_HDF5_ANGLES = "external_angles.hdf5"
FILE_HDF5_COUNTS = "external_counts.hdf5"

# ---------------------------

# get some data
filename = str(Path(__file__).absolute().parent.parent / "simple_example.dat")
buffer = numpy.loadtxt(filename).T
tthData = buffer[0]  # float[]
countsData = numpy.asarray(buffer[1], "int32")  # int[]

# put the angle data in an external (non-NeXus) HDF5 data file
with h5py.File(FILE_HDF5_ANGLES, "w") as f:
    ds = f.create_dataset("angles", data=tthData)
    ds.attrs["units"] = "degrees"

# put the detector counts in an external HDF5 data file
# with *incomplete* NeXus structure (no NXdata group)
with nxopen(FILE_HDF5_COUNTS, "w") as f:
    f["entry"] = NXentry()
    f["entry/instrument"] = NXinstrument()
    f["entry/instrument/detector"] = NXdetector()
    f["entry/instrument/detector/counts"] = NXfield(countsData, units="counts")
    f["entry/instrument/detector/two_theta"] = NXlink("/angles",
                                                      FILE_HDF5_ANGLES)

# create a master NeXus HDF5 file
with nxopen(FILE_HDF5_MASTER, "w") as f:
    f["entry"] = NXentry()
    counts = NXlink("/entry/instrument/detector/counts", FILE_HDF5_COUNTS,
                    name="counts")
    two_theta = NXlink("/angles", FILE_HDF5_ANGLES, name="two_theta")
    f["entry/data"] = NXdata(counts, two_theta)
    f["entry/data"].set_default()
    f["entry/instrument"] = NXlink("/entry/instrument", FILE_HDF5_COUNTS)
