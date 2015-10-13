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

set(IFBASE_FILES 
    NXaperture.nxdl.xml
    NXattenuator.nxdl.xml
    NXbeam.nxdl.xml
    NXbeam_stop.nxdl.xml
    NXbending_magnet.nxdl.xml
    NXcapillary.nxdl.xml
    NXcharacterization.nxdl.xml
    NXcite.nxdl.xml
    NXcollection.nxdl.xml
    NXcollimator.nxdl.xml
    NXcrystal.nxdl.xml
    NXdata.nxdl.xml
    NXdetector_group.nxdl.xml
    NXdetector_module.nxdl.xml
    NXdetector.nxdl.xml
    NXdisk_chopper.nxdl.xml
    NXentry.nxdl.xml
    NXenvironment.nxdl.xml
    NXevent_data.nxdl.xml
    NXfermi_chopper.nxdl.xml
    NXfilter.nxdl.xml
    NXflipper.nxdl.xml
    NXfresnel_zone_plate.nxdl.xml
    NXgeometry.nxdl.xml
    NXgrating.nxdl.xml
    NXguide.nxdl.xml
    NXinsertion_device.nxdl.xml
    NXinstrument.nxdl.xml
    NXlog.nxdl.xml
    NXmirror.nxdl.xml
    NXmoderator.nxdl.xml
    NXmonitor.nxdl.xml
    NXmonochromator.nxdl.xml
    NXnote.nxdl.xml
    NXobject.nxdl.xml
    NXorientation.nxdl.xml
    NXparameters.nxdl.xml
    NXpinhole.nxdl.xml
    NXpolarizer.nxdl.xml
    NXpositioner.nxdl.xml
    NXprocess.nxdl.xml
    NXroot.nxdl.xml
    NXsample.nxdl.xml
    NXsensor.nxdl.xml
    NXshape.nxdl.xml
    NXslit.nxdl.xml
    NXsource.nxdl.xml
    NXsubentry.nxdl.xml
    NXtransformations.nxdl.xml
    NXtranslation.nxdl.xml
    NXuser.nxdl.xml
    NXvelocity_selector.nxdl.xml
    NXxraylens.nxdl.xml
)

set(IFBASE_CLASS_RST_FILES)
set(IFBASE_CLASS_RST_DIR "${CMAKE_BINARY_DIR}/manual/source/classes/ifbase_classes")


foreach(F ${IFBASE_FILES})
    # copy the file to the binary directory
    configure_file(${F} ${F} @ONLY)

    #assemble the name of the base class file
    string(REPLACE ".nxdl.xml" ".rst" IFBASE_CLASS_RST_FILE ${F})
    set(IFBASE_CLASS_RST_FILE "${IFBASE_CLASS_RST_DIR}/${IFBASE_CLASS_RST_FILE}")
    list(APPEND IFBASE_CLASS_RST_FILES ${IFBASE_CLASS_RST_FILE})

    # build the RST file from the NXDL file
    add_custom_command(
        OUTPUT ${IFBASE_CLASS_RST_FILE}
        COMMAND python ${NXDL2RST} ${F} > ${IFBASE_CLASS_RST_FILE}
        DEPENDS ${F} ${NXDL2RST}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

    #install the XML file
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${F}
            DESTINATION ${NEXUS_DEFINITIONS}/ifbase_classes
            COMPONENT definitions)
endforeach()

add_custom_target(ifbase-class-manual-sources
                  DEPENDS ${IFBASE_CLASS_RST_FILES})

#-----------------------------------------------------------------------------
# configure and install the nxdlformat.xsl file
#-----------------------------------------------------------------------------
configure_file(nxdlformat.xsl nxdlformat.xsl @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/nxdlformat.xsl 
        DESTINATION ${NEXUS_DEFINITIONS}/ifbase_classes
        COMPONENT definitions)



