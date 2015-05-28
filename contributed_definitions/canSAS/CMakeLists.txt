#=============================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2015 Eugen Wintersberger
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
#=============================================================================

set(FILES minimum.png
          Q-geometry.jpg
          SAScollimation.png
          SASdata.png
          SASdetector.png
          SASinstrument.png
          SASprocess.png
          SASroot.png
          SASsample.png
          SASsource.png
          SAStransmission_spectrum.png)

set(IMGPATH "${CMAKE_BINARY_DIR}/manual/source/classes/contributed_definitions/canSAS")

foreach(F ${FILES})
    configure_file(${F} ${IMGPATH}/${F} COPYONLY)
endforeach()
