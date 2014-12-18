## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2012 NeXus International Advisory Committee (NIAC)
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

add_subdirectory(classes)

file(COPY "${CMAKE_SOURCE_DIR}/LGPL.txt" DESTINATION "${CMAKE_CURRENT_BINARY_DIR}")

add_custom_target(manual-source ALL)
add_dependencies(manual-source manual-classes types.table-manual-source units.table-manual-source nxdl_desc.rst-manual-source)

add_custom_command(
    OUTPUT types.table 
	COMMAND ${PYTHON} 
	ARGS ${CMAKE_SOURCE_DIR}/utils/types2rst.py ${CMAKE_SOURCE_DIR}/nxdlTypes.xsd > types.table 
	DEPENDS ${CMAKE_SOURCE_DIR}/nxdlTypes.xsd ${CMAKE_SOURCE_DIR}/utils/types2rst.py
)
add_custom_target(types.table-manual-source DEPENDS types.table)
set_target_properties(types.table-manual-source PROPERTIES OUTPUT_NAME types.table)

add_custom_command(
    OUTPUT units.table 
	COMMAND ${PYTHON} 
	ARGS ${CMAKE_SOURCE_DIR}/utils/units2rst.py ${CMAKE_SOURCE_DIR}/nxdlTypes.xsd > units.table 
	DEPENDS ${CMAKE_SOURCE_DIR}/nxdlTypes.xsd ${CMAKE_SOURCE_DIR}/utils/units2rst.py
)
add_custom_target(units.table-manual-source DEPENDS units.table)
set_target_properties(units.table-manual-source PROPERTIES OUTPUT_NAME units.table)

add_custom_command(
    OUTPUT nxdl_desc.rst 
	COMMAND ${PYTHON} 
	ARGS ${CMAKE_SOURCE_DIR}/utils/nxdl_desc2rst.py ${CMAKE_SOURCE_DIR}/nxdl.xsd > nxdl_desc.rst 
	DEPENDS ${CMAKE_SOURCE_DIR}/nxdl.xsd ${CMAKE_SOURCE_DIR}/utils/nxdl_desc2rst.py
)
add_custom_target(nxdl_desc.rst-manual-source DEPENDS nxdl_desc.rst)
set_target_properties(nxdl_desc.rst-manual-source PROPERTIES OUTPUT_NAME nxdl_desc.rst)

SET_DIRECTORY_PROPERTIES(PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES types.table;units.table;nxdl_desc.rst)
