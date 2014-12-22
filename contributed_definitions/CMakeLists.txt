## Process this file with cmake
#====================================================================
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
#====================================================================

set(CONTRIBUTED_FILES 
    NXarpes.nxdl.xml
    NXcanSAS.nxdl.xml
    NXelectrostatic_kicker.nxdl.xml
    NXfresnel_zone_plate.nxdl.xml
    NXgrating.nxdl.xml
    NXmagnetic_kicker.nxdl.xml
    NXquadrupole_magnet.nxdl.xml
    NXseparator.nxdl.xml
    NXsnsevent.nxdl.xml
    NXsnshisto.nxdl.xml
    NXsolenoid_magnet.nxdl.xml
    NXspin_rotator.nxdl.xml
    NXstxm.nxdl.xml
)

set(CONTRIBUTED_SOURCE ${CMAKE_SOURCE_DIR}/contributed_definitions)

set(CONTRIBUTED_DIST ${CMAKE_BINARY_DIR}/dist/contributed_definitions)

add_custom_target(CheckContributedClasses ALL COMMENT "Checking contributed classes")
configure_nxdl(CheckContributedClasses "${CONTRIBUTED_SOURCE}" "${CONTRIBUTED_DIST}" "${CONTRIBUTED_FILES}")

foreach(F ${CONTRIBUTED_FILES})
    install(FILES ${CONTRIBUTED_DIST}/${F} DESTINATION ${NEXUS_DEFINITIONS}/contributed_definitions  COMPONENT definitions)
endforeach()
