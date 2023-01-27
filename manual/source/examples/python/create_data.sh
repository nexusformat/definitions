#!/bin/bash

# (re)build all data files and text descriptions of data files


function remove_punx_lines() {
    # Remove all lines that do not start with a space
    local filename=$1
    sed -i "/^ /!d" $filename
}


ORIGINAL_WD=$(pwd)
SCRIPT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PUNX_REMOVE_HEADER="+5"

ROOT=$SCRIPT_ROOT/simple_example_basic
cd $ROOT
python simple_example_basic_write.py
punx tree simple_example_basic.nexus.hdf5 > simple_example_basic.nexus_structure.txt
remove_punx_lines simple_example_basic.nexus_structure.txt
h5dump simple_example_basic.nexus.hdf5 > simple_example_basic.nexus_h5dump.txt
python simple_example_basic_read.py

ROOT=$SCRIPT_ROOT/simple_example_test
cd $ROOT
python simple_example_test_write.py
python simple_example_test_read.py
rm simple_example_test.nexus.hdf5

ROOT=$SCRIPT_ROOT/simple_example_write1
cd $ROOT
python simple_example_write1.py
punx tree simple_example_write1.hdf5 > simple_example_write1_structure.txt
remove_punx_lines simple_example_write1_structure.txt
h5dump simple_example_write1.hdf5 > simple_example_write1_h5dump.txt

ROOT=$SCRIPT_ROOT/simple_example_write2
cd $ROOT
python simple_example_write2.py
punx tree simple_example_write2.hdf5 > simple_example_write2_structure.txt
remove_punx_lines simple_example_write2_structure.txt
h5dump simple_example_write2.hdf5 > simple_example_write2_h5dump.txt

ROOT=$SCRIPT_ROOT/external_example_write
cd $ROOT
python external_example_write.py
punx tree external_angles.hdf5 > external_angles_structure.txt
remove_punx_lines external_angles_structure.txt
h5dump external_angles.hdf5 > external_angles_h5dump.txt
punx tree external_counts.hdf5 > external_counts_structure.txt
remove_punx_lines external_counts_structure.txt
h5dump external_counts.hdf5 > external_counts_h5dump.txt
punx tree external_master.hdf5 > external_master_structure.txt
remove_punx_lines external_master_structure.txt
h5dump external_master.hdf5 > external_master_h5dump.txt

cd $ORIGINAL_WD
