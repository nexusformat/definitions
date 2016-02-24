#!/bin/bash

# (re)build all data files and text descriptions of data files

#python BasicReader.py
#python TestReader.py
#python TestWriter.py

# h5toText comes from the spec2nexus package

python BasicWriter.py
h5toText prj_test.nexus.hdf5 > prj_test.nexus_structure.txt
h5dump prj_test.nexus.hdf5 > prj_test.nexus_h5dump.txt

python externalExample.py
h5toText external_angles.hdf5 > external_angles_structure.txt
h5dump external_angles.hdf5 > external_angles_h5dump.txt
h5toText external_counts.hdf5 > external_counts_structure.txt
h5dump external_counts.hdf5 > external_counts_h5dump.txt
h5toText external_master.hdf5 > external_master_structure.txt
h5dump external_master.hdf5 > external_master_h5dump.txt

python writer_1_3.py
h5toText writer_1_3.hdf5 > writer_1_3_structure.txt
h5dump writer_1_3.hdf5 > writer_1_3_h5dump.txt

python writer_2_1.py
h5toText writer_2_1.hdf5 > writer_2_1_structure.txt
h5dump writer_2_1.hdf5 > writer_2_1_h5dump.txt
