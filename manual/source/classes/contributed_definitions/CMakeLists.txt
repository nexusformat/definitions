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

add_custom_target(manual-contributed ALL)

set(NXDL2RST ${CMAKE_SOURCE_DIR}/utils/nxdl2rst.py)
set(NXDL_SUFFIX nxdl.xml)
set(SRCDIR ${CMAKE_SOURCE_DIR}/contributed_definitions)

FILE(GLOB SRCs RELATIVE "${SRCDIR}" "${SRCDIR}/NX*.${NXDL_SUFFIX}")

FILE(COPY "${SRCDIR}/" DESTINATION "${CMAKE_CURRENT_BINARY_DIR}")

foreach(VAR ${SRCs})
    string(REPLACE ${NXDL_SUFFIX} rst RST ${VAR})
    set_property(DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ${RST})
    add_dependencies(manual-contributed contributed-${RST})
    add_custom_command(
        OUTPUT ${RST} 
	    COMMAND ${PYTHON} 
	    ARGS ${NXDL2RST} ${SRCDIR}/${VAR} > ${RST} 
	    DEPENDS ${SRCDIR}/${VAR} ${NXDL2RST}
	)
    add_custom_target(contributed-${RST} DEPENDS ${RST})
endforeach(VAR)

