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


add_subdirectory(applications)
add_subdirectory(base_classes)
add_subdirectory(contributed_definitions)

add_custom_command(
    OUTPUT all_base.nxdl.xml
    COMMAND python ${XMLMERGE} base_classes > all_base.nxdl.xml
    DEPENDS base-class-schema-sources
    COMMENT "Generating all_base.nxdl.xml")

add_custom_target(all-base-nxdl DEPENDS all_base.nxdl.xml)

add_custom_command(
    OUTPUT all.nxdl.xml
    COMMAND python ${XMLMERGE} base_classes applications contributed_definitions
    > all.nxdl.xml
    DEPENDS applications-schema-sources 
            base-class-schema-sources
            contributed-schema-sources
    COMMENT "Generating all.nxdl.xml")

add_custom_target(all-nxdl DEPENDS all.nxdl.xml)

add_custom_command(
    OUTPUT all_unsorted.xsd
    COMMAND ${XSLTPROC} -o all_unsorted.xsd ${XSLTPATH}/nxdl2xsd.xsl
    all.nxdl.xml
    DEPENDS all-nxdl
    COMMENT "Building all_unsorted.xsd"
    )

add_custom_command(
    OUTPUT all.xml
    COMMAND ${XSLTPROC} -o all.xml ${XSLTPATH}/sort_nxdl.xsl all.nxdl.xml
    DEPENDS all-nxdl
    COMMENT "Building all.xml"
    )

add_custom_command(
    OUTPUT all_base.sch
    COMMAND ${XSLTPROC} -o all_base.sch ${XSLTPATH}/nxdl2sch.xsl
    all_base.nxdl.xml
    DEPENDS all-base-nxdl
    COMMENT "Building all_base.sch"
    )

add_custom_command(
    OUTPUT all.sch
    COMMAND ${XSLTPROC} -o all.sch ${XSLTPATH}/nxdl2sch.xsl all.nxdl.xml
    DEPENDS all-nxdl
    COMMENT "Building all.sch"
    )


install(FILES ${CMAKE_CURRENT_BINARY_DIR}/all.xml
              ${CMAKE_CURRENT_BINARY_DIR}/all_unsorted.xsd 
              ${CMAKE_CURRENT_BINARY_DIR}/all_base.sch 
              ${CMAKE_CURRENT_BINARY_DIR}/all.sch
        DESTINATION ${NEXUS_DEFINITIONS}/schema)

add_custom_target(nxdl_schema ALL
                  DEPENDS all.xml all_unsorted.xsd all_base.sch all.sch)

