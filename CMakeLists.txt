## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011 Stephen Rankin
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
if(WIN32)
    cmake_minimum_required (VERSION 2.8.7)
else()
    cmake_minimum_required (VERSION 2.8.3)
    set(CMAKE_LEGACY_CYGWIN_WIN32 0) # Remove this line when CMake >= 2.8.4 is required
endif()
project(NeXusDefinitions)

option (BUILD_SPHINX "Build documentation using sphinx" OFF)

set(NEXUS_DEFINITIONS share/nexus/definitions)
set(NEXUS_MANUAL share/nexus/manual)

find_package(LATEX)
find_package(PythonInterp)

if (WIN32)
    find_program(XSLTPROC xsltproc PATHS "${CMAKE_SOURCE_DIR}/utils/win32")
else(WIN32)
    find_program(XSLTPROC xsltproc )
endif()

# Recurse into the subdirectories.
#add_subdirectory (tutorial)
add_subdirectory (base_classes)
add_subdirectory (contributed_definitions)
add_subdirectory (applications)
add_subdirectory (schema)
add_subdirectory (manual)
if(BUILD_SPHINX)
    add_subdirectory (sphinx)
endif(BUILD_SPHINX)

INSTALL(FILES nxdl.xsd nxdlTypes.xsd DESTINATION ${NEXUS_DEFINITIONS} COMPONENT definitions)
INSTALL(FILES BASE.xsd NeXus.xsd DESTINATION ${NEXUS_DEFINITIONS} COMPONENT definitions)

#
# set CPack packaging options
#
configure_file("${PROJECT_SOURCE_DIR}/CPackOptions.cmake.in"
                                "${PROJECT_BINARY_DIRECTORY}CPackOptions.cmake"
                                @ONLY)
set(CPACK_PROJECT_CONFIG_FILE "${PROJECT_BINARY_DIRECTORY}CPackOptions.cmake")
set (CPACK_GENERATOR TGZ) # not use ZIP on UNIX as problem with symlinks
if(UNIX)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};DEB;RPM)
endif(UNIX)
if(WIN32)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};ZIP;NSIS)
endif(WIN32)
if(APPLE)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};PackageMaker)
endif(APPLE)
if(CYGWIN)
endif(CYGWIN)
# Include of CPack must always be last
include(CPack)
