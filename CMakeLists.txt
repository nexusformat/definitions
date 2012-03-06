## Process this file with cmake
# $Id$
#====================================================================
#  NeXus - A common data format for neutron, x-ray and muon science.
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
if(WIN32)
    cmake_minimum_required (VERSION 2.8.7)
else()
    cmake_minimum_required (VERSION 2.8.3)
    set(CMAKE_LEGACY_CYGWIN_WIN32 0) # Remove this line when CMake >= 2.8.4 is required
endif()
project(NeXusDefinitions)

# include NXDL release number information
include(cmake_include/nxdl_release.cmake)

function(configure_release TARGET INFILE OUTFILE)
	get_filename_component(F ${INFILE} NAME)
	add_custom_command(OUTPUT "${OUTFILE}" COMMAND ${CMAKE_COMMAND} -DINPUT_FILE="${INFILE}" -DOUTPUT_FILE="${OUTFILE}" -DMATCH_STRING="\@NXDL_RELEASE\@" -DREPLACE_STRING="${NXDL_RELEASE}" -P "${CMAKE_SOURCE_DIR}/cmake_include/replace.cmake" DEPENDS "${INFILE}" "${CMAKE_BINARY_DIR}/CMakeCache.txt" COMMENT "Rebuilding ${F}")
	add_custom_target(${TARGET}-${F} DEPENDS "${OUTFILE}")
	add_dependencies(${TARGET} ${TARGET}-${F})
endfunction()

function(configure_nxdl TARGET NXDL_DIR DIST_DIR NXDL_FILES)
    foreach(F ${NXDL_FILES})
	set(NXDL ${NXDL_DIR}/${F})
	configure_release(${TARGET} ${NXDL} ${DIST_DIR}/${F})
    endforeach()
    configure_release(${TARGET} ${NXDL_DIR}/nxdlformat.xsl ${DIST_DIR}/nxdlformat.xsl)
endfunction()

set(XSD_FILES NeXus.xsd nxdl.xsd nxdlTypes.xsd BASE.xsd)
add_custom_target("DoXSD" ALL)
foreach(F ${XSD_FILES})
    configure_release("DoXSD" ${CMAKE_SOURCE_DIR}/${F} ${CMAKE_BINARY_DIR}/dist/${F})
endforeach()

# 2012-02-18,PRJ: sphinx directory is not ready for cmake yet
#option (BUILD_SPHINX "Build documentation using sphinx" OFF)

set(NEXUS_DEFINITIONS share/nexus/definitions)
set(NEXUS_MANUAL share/nexus/manual)

find_package(LATEX)
find_package(PythonInterp)

if (WIN32)
    find_program(XSLTPROC xsltproc PATHS "${CMAKE_SOURCE_DIR}/utils/win32")
else(WIN32)
    find_program(XSLTPROC xsltproc )
endif()
find_program(SVNVERSION svnversion)

# Recurse into the subdirectories.
#add_subdirectory (tutorial)
add_subdirectory (base_classes)
add_subdirectory (contributed_definitions)
add_subdirectory (applications)
add_subdirectory (schema)
add_subdirectory (manual)
# 2012-02-18,PRJ: sphinx directory is not ready for cmake yet
#if(BUILD_SPHINX)
#    add_subdirectory (sphinx)
#endif(BUILD_SPHINX)

foreach(F ${XSD_FILES})
    INSTALL(FILES ${CMAKE_BINARY_DIR}/dist/${F} DESTINATION ${NEXUS_DEFINITIONS} COMPONENT definitions)
endforeach()
INSTALL(FILES LGPL DESTINATION ${NEXUS_DEFINITIONS} COMPONENT definitions)

#
# set CPack packaging options
#
configure_file("${PROJECT_SOURCE_DIR}/CPackOptions.cmake.in"
                                "${PROJECT_BINARY_DIRECTORY}CPackOptions.cmake"
                                @ONLY)
set(CPACK_PROJECT_CONFIG_FILE "${PROJECT_BINARY_DIRECTORY}CPackOptions.cmake")
set (CPACK_GENERATOR TGZ) # not use ZIP on UNIX as problem with symlinks
set (CPACK_SOURCE_GENERATOR TGZ) # not use ZIP on UNIX as problem with symlinks
if(UNIX)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};DEB;RPM)
endif(UNIX)
if(WIN32)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};ZIP;NSIS)
    set (CPACK_SOURCE_GENERATOR ${CPACK_SOURCE_GENERATOR};ZIP) 
endif(WIN32)
if(APPLE)
    set (CPACK_GENERATOR ${CPACK_GENERATOR};PackageMaker)
endif(APPLE)
if(CYGWIN)
endif(CYGWIN)
# Include of CPack must always be last
include(CPack)
