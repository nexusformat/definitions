#=============================================================================
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
#==============================================================================

set(FILES Coordinates.png
          data-linking.png
          data-post-nexus.jpg
          data-pre-nexus.jpg
          ex_writer_1_3.png
          ex_writer_2_1.png
          Hierarchy.png
          mcstascoord.png
          mcstas.png
          missing.jpg
          NeXus-logo.png
          NeXus.png
          NXinstrument.png
          NXtechnical_data_nexpy.jpg
          NXtechnical_data_nxdl.jpg
          nxvalidate.png
          polplane.png
          rssfeed.jpg
          Simple.png
          translation-orientation-geometry-2.jpg
          translation-orientation-geometry.jpg
          woni-powderimage.png
          detector_origin.png
          detector_axes.png
          woni-schematic.png)

add_subdirectory(nxdl)

foreach(F ${FILES})
    configure_file(${F} ${F} COPYONLY)
endforeach()
