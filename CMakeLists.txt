## Process this file with cmake
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

#=============================================================================
#                   BUILD CONFIGURATION
#=============================================================================

# we need 2.8.8 for correct component install with CPACK for archives
if(WIN32)
    cmake_minimum_required (VERSION 2.8.8)
else()
    cmake_minimum_required (VERSION 2.8.0)
    if (${CMAKE_VERSION} VERSION_LESS 2.8.4)
        # Remove this line when CMake >= 2.8.4 is required
        set(CMAKE_LEGACY_CYGWIN_WIN32 0) 
    endif()
endif()

project(NeXusDefinitions)

#-----------------------------------------------------------------------------
# Search for required packages
#-----------------------------------------------------------------------------
find_package(LATEX)
find_package(PythonInterp)

#-----------------------------------------------------------------------------
# Search for required programs
#-----------------------------------------------------------------------------
find_program(DBLATEX dblatex)
if (WIN32)
    find_program(XSLTPROC xsltproc PATHS "${CMAKE_SOURCE_DIR}/utils/win32")
else(WIN32)
    find_program(XSLTPROC xsltproc )
endif()

#-----------------------------------------------------------------------------
# include NXDL release number information
# This file provides three variables: 
# -> NXDL_MAJOR_RELEASE
# -> NXDL_MINOR_RELEASE
# -> NXDL_RELEASE
#-----------------------------------------------------------------------------
include(cmake_include/nxdl_release.cmake)

#set cmake module path
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake_include)

option (BUILD_SPHINX "Build documentation using sphinx" ON)

include(GNUInstallDirs)

set(NEXUS_DEFINITIONS "${CMAKE_INSTALL_DATADIR}/nexus/definitions")
set(NEXUS_MANUAL "${CMAKE_INSTALL_DATADIR}/doc/nexus-reference")


#==============================================================================
#              DEALING WITH FILES IN THE ROOT DIRECTORY
#==============================================================================

#------------------------------------------------------------------------------
# configure and install xsd files
#------------------------------------------------------------------------------
set(XSD_FILES NeXus.xsd nxdl.xsd nxdlTypes.xsd BASE.xsd)
add_custom_target("DoXSD" ALL)
foreach(F ${XSD_FILES})
    configure_file(${F} ${F} @ONLY)
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${F} 
            DESTINATION ${NEXUS_DEFINITIONS}
            COMPONENT definitions)
endforeach()


#-----------------------------------------------------------------------------
# Recurse into the subdirectories.
#-----------------------------------------------------------------------------
add_subdirectory (xslt)
add_subdirectory (base_classes)
add_subdirectory (contributed_definitions)
add_subdirectory (applications)
add_subdirectory (schema)
#add_subdirectory (manual)
#add_subdirectory (validate_cmdline)

#-----------------------------------------------------------------------------
# install license for definitions and manual
#-----------------------------------------------------------------------------
install(FILES LGPL.txt 
        DESTINATION ${NEXUS_DEFINITIONS} 
        COMPONENT definitions)
install(FILES LGPL.txt 
        DESTINATION ${NEXUS_MANUAL} 
        COMPONENT manual)

