#!/usr/bin/env python
"""Reads NeXus HDF5 files using nexusformat and prints the contents"""

from nexusformat.nexus import nxopen

fileName = "simple_example_basic.nexus.hdf5"
with nxopen(fileName) as f:
    print(f.tree)
