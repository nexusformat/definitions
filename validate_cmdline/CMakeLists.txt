## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011 Freddie Akeroyd
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

if (WIN32)
    configure_file(nxvalidate_cli.bat.in nxvalidate_cli.bat @ONLY)
	install (PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/nxvalidate_cli.bat DESTINATION bin COMPONENT definitions)
else(WIN32)
	configure_file(nxvalidate_cli.in nxvalidate_cli @ONLY)
	install (PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/nxvalidate_cli DESTINATION bin COMPONENT definitions)
endif(WIN32)

install (FILES saxon9he.jar DESTINATION ${NEXUS_DEFINITIONS}/java COMPONENT
definitions)

FILE(GLOB SCHEMATRON_FILES "schematron/*")
INSTALL(FILES ${SCHEMATRON_FILES} DESTINATION ${NEXUS_DEFINITIONS}/schematron COMPONENT definitions)
