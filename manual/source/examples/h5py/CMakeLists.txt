#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2015 NeXus International Advisory Committee (NIAC)
#  
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
# 
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
# 
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free 
#  Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, 
#  MA  02111-1307  USA
#             
#  For further information, see <http://www.nexusformat.org>
#
#
#====================================================================

set(FILES BasicReader.py
          BasicWriter.py
          data-model.txt
          external_angles.hdf5
          external_counts.hdf5
          externalExample.py
          external_master.hdf5
          h5toText.py
          index.rst
          input.dat
          my_lib.py
          nexpy.png
          nxvalidate.png
          output.txt
          prj_test.nexus.hdf5
          s00008.png
          TestReader.py
          TestWriter.py
          writer_1_3_h5dump.txt
          writer_1_3_h5py.py
          writer_1_3.hdf5
          writer_1_3.py
          writer_1_3.rst
          writer_1_3_structure.txt
          writer_2_1_h5dump.txt
          writer_2_1.hdf5
          writer_2_1.py
          writer_2_1.rst
          writer_2_1_structure.txt
          )

foreach(F ${FILES})
    configure_file(${F} ${F} COPYONLY)
endforeach()
