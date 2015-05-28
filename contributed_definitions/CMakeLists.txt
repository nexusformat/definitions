## Process this file with cmake
#=============================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011-2012 Freddie Akeroyd
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

set(CONTRIBUTED_FILES 
    NXcanSAS.nxdl.xml
    NXelectrostatic_kicker.nxdl.xml
    NXmagnetic_kicker.nxdl.xml
    NXquadrupole_magnet.nxdl.xml
    NXseparator.nxdl.xml
    NXsnsevent.nxdl.xml
    NXsnshisto.nxdl.xml
    NXsolenoid_magnet.nxdl.xml
    NXspin_rotator.nxdl.xml
)

add_subdirectory(canSAS)

set(CONTRIBUTED_RST_FILES)
set(CONTRIBUTED_RST_DIR
    "${CMAKE_BINARY_DIR}/manual/source/classes/contributed_definitions")

foreach(F ${CONTRIBUTED_FILES})
    configure_file(${F} ${F} @ONLY)
    
    #assemble the name of the constributed class file
    string(REPLACE ".nxdl.xml" ".rst" CONTRIBUTED_RST_FILE ${F})
    set(CONTRIBUTED_RST_FILE "${CONTRIBUTED_RST_DIR}/${CONTRIBUTED_RST_FILE}")
    list(APPEND CONTRIBUTED_RST_FILES ${CONTRIBUTED_RST_FILE})


    # build the RST file from the NXDL file
    add_custom_command(
        OUTPUT ${CONTRIBUTED_RST_FILE}
        COMMAND python ${NXDL2RST} ${F} > ${CONTRIBUTED_RST_FILE}
        DEPENDS ${F} ${NXDL2RST}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
    

    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${F}
            DESTINATION ${NEXUS_DEFINITIONS}/contributed_definitions
            COMPONENT definitions)
endforeach()

add_custom_target(contributed-manual-sources DEPENDS ${CONTRIBUTED_RST_FILES})

