## Process this file with cmake
#=============================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011-2014 NIAC
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

set(INTERFACE_FILES 
NXIFarea_detector.nxdl.xml
NXIFarea_detector_scanned.nxdl.xml
NXIFarea_detector_tof.nxdl.xml
NXIFBeamline_component.nxdl.xml
NXIFcount_time.nxdl.xml
NXIFcount_time_scanned.nxdl.xml
NXIFgasdetector.nxdl.xml
NXIFgeneric_detector.nxdl.xml
NXIFgeneric_detector_scanned.nxdl.xml
NXIFGeneric_detector_tof.nxdl.xml
NXIFlinear_detector.nxdl.xml
NXIFlinear_detector_scanned.nxdl.xml
NXIFlinear_detector_tof.nxdl.xml
NXIFmetadata.nxdl.xml
NXIFmonochromator.nxdl.xml
NXIFphoton_counter.nxdl.xml
NXIFsinglecrystal.nxdl.xml
NXIFsingle_detector.nxdl.xml
NXIFsingle_detector_scanned.nxdl.xml
NXIF_single_detector_tof.nxdl.xml
)

set(INTERFACE_CLASS_RST_FILES)
set(INTERFACE_CLASS_RST_DIR "${CMAKE_BINARY_DIR}/manual/source/classes/interfaces")


foreach(F ${INTERFACE_FILES})
    # copy the file to the binary directory
    configure_file(${F} ${F} @ONLY)

    #assemble the name of the base class file
    string(REPLACE ".nxdl.xml" ".rst" INTERFACE_CLASS_RST_FILE ${F})
    set(INTERFACE_CLASS_RST_FILE "${INTERFACE_CLASS_RST_DIR}/${INTERFACE_CLASS_RST_FILE}")
    list(APPEND INTERFACE_CLASS_RST_FILES ${INTERFACE_CLASS_RST_FILE})

    # build the RST file from the NXDL file
    add_custom_command(
        OUTPUT ${INTERFACE_CLASS_RST_FILE}
        COMMAND python ${NXDL2RST} ${F} > ${INTERFACE_CLASS_RST_FILE}
        DEPENDS ${F} ${NXDL2RST}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

    #install the XML file
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${F}
            DESTINATION ${NEXUS_DEFINITIONS}/interfaces
            COMPONENT definitions)
endforeach()

add_custom_target(interfaces-class-manual-sources
                  DEPENDS ${INTERFACE_CLASS_RST_FILES})

#-----------------------------------------------------------------------------
# configure and install the nxdlformat.xsl file
#-----------------------------------------------------------------------------
configure_file(nxdlformat.xsl nxdlformat.xsl @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/nxdlformat.xsl 
        DESTINATION ${NEXUS_DEFINITIONS}/interfaces
        COMPONENT definitions)



