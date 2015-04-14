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


set(APPLICATION_FILES 
    NXarpes.nxdl.xml
    NXarchive.nxdl.xml
    NXdirecttof.nxdl.xml
    NXfluo.nxdl.xml
    NXindirecttof.nxdl.xml
    NXiqproc.nxdl.xml
    NXlauetof.nxdl.xml
    NXmonopd.nxdl.xml
    NXmx.nxdl.xml
    NXrefscan.nxdl.xml
    NXreftof.nxdl.xml
    NXsas.nxdl.xml
    NXsastof.nxdl.xml
    NXscan.nxdl.xml
    NXspe.nxdl.xml
    NXsqom.nxdl.xml
    NXstxm.nxdl.xml
    NXtas.nxdl.xml
    NXtofnpd.nxdl.xml
    NXtofraw.nxdl.xml
    NXtofsingle.nxdl.xml
    NXtomo.nxdl.xml
    NXtomophase.nxdl.xml
    NXtomoproc.nxdl.xml
    NXxas.nxdl.xml
    NXxasproc.nxdl.xml
    NXxbase.nxdl.xml
    NXxeuler.nxdl.xml
    NXxkappa.nxdl.xml
    NXxlaue.nxdl.xml
    NXxlaueplate.nxdl.xml
    NXxnb.nxdl.xml
    NXxrot.nxdl.xml
)


set(APPLICATIONS_RST_FILES)
set(APPLICATIONS_RST_DIR "${CMAKE_BINARY_DIR}/manual/source/classes/applications")

#need to copy this file as it is required by the documentation
configure_file(NXmonopd.nxdl.xml 
               ${APPLICATIONS_RST_DIR}/NXmonopd.nxdl.xml COPYONLY)

#-----------------------------------------------------------------------------
# process the application definition files
#-----------------------------------------------------------------------------
foreach(F ${APPLICATION_FILES})
    configure_file(${F} ${F} @ONLY)
    
    #assemble the name of the base class file
    string(REPLACE ".nxdl.xml" ".rst" APPLICATION_RST_FILE ${F})
    set(APPLICATION_RST_FILE "${APPLICATIONS_RST_DIR}/${APPLICATION_RST_FILE}")
    list(APPEND APPLICATIONS_RST_FILES ${APPLICATION_RST_FILE})
    
    # build the RST file from the NXDL file
    add_custom_command(
        OUTPUT ${APPLICATION_RST_FILE}
        COMMAND python ${NXDL2RST} ${F} > ${APPLICATION_RST_FILE}
        DEPENDS ${F} ${NXDL2RST}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${F} 
            DESTINATION ${NEXUS_DEFINITIONS}/applications 
            COMPONENT definitions)

endforeach()

#this target ensures that the application RST files are created before 
#the documentation is built
add_custom_target(applications-manual-sources 
                  DEPENDS ${APPLICATIONS_RST_FILES})

