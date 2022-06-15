#!/usr/bin/env python
"""
Writes a NeXus HDF5 file using h5py with links to data in other HDF5 files.

This example is based on ``writer_2_1``.
"""

from pathlib import Path
import h5py
import numpy

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
with h5py.File(FILE_HDF5_COUNTS, "w") as f:
    nxentry = f.create_group("entry")
    nxentry.attrs["NX_class"] = "NXentry"
    nxinstrument = nxentry.create_group("instrument")
    nxinstrument.attrs["NX_class"] = "NXinstrument"
    nxdetector = nxinstrument.create_group("detector")
    nxdetector.attrs["NX_class"] = "NXdetector"
    ds = nxdetector.create_dataset("counts", data=countsData)
    ds.attrs["units"] = "counts"
    # link the "two_theta" data stored in separate file
    local_addr = nxdetector.name + "/two_theta"
    f[local_addr] = h5py.ExternalLink(FILE_HDF5_ANGLES, "/angles")

# create a master NeXus HDF5 file
with h5py.File(FILE_HDF5_MASTER, "w") as f:
    f.attrs["default"] = "entry"
    nxentry = f.create_group("entry")
    nxentry.attrs["NX_class"] = "NXentry"
    nxentry.attrs["default"] = "data"
    nxdata = nxentry.create_group("data")
    nxdata.attrs["NX_class"] = "NXdata"

    # link in the signal data
    local_addr = "/entry/data/counts"
    external_addr = "/entry/instrument/detector/counts"
    f[local_addr] = h5py.ExternalLink(FILE_HDF5_COUNTS, external_addr)
    nxdata.attrs["signal"] = "counts"

    # link in the axes data
    local_addr = "/entry/data/two_theta"
    f[local_addr] = h5py.ExternalLink(FILE_HDF5_ANGLES, "/angles")
    nxdata.attrs["axes"] = "two_theta"
    nxdata.attrs["two_theta_indices"] = [
        0,
    ]

    local_addr = "/entry/instrument"
    f[local_addr] = h5py.ExternalLink(FILE_HDF5_COUNTS, "/entry/instrument")
