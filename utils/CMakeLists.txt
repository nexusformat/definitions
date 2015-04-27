#=============================================================================
#  NeXus - A common data format for neutron, x-ray and muon science.
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2014 NeXus International Advisory Committee (NIAC)
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

set(FILES dev_nxdl2rst.py
          nxdl2rst.py
          nxdl_desc2rst.py
          nxxref.py
          showtree.py
          types2rst.py
          xmlstrip.py
          partmerge.py
          units2rst.py)

foreach(F ${FILES})
    configure_file(${F} ${F} @ONLY)
endforeach()

