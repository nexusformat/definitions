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

set(XSLT_PATH ${CMAKE_SOURCE_DIR}/xslt)

set(NXDL_SUFFIX nxdl.xml)

### start of choose your xslt processor 
# xsltproc has arguments os         "xsl file"
# others such as msxsl, nxslt have  "file xsl"
# so XSL_TYPE needs to be set to BEFORE or AFTER as appropriate

find_program(XSLTPROC_FIND xsltproc)
#find_program(XSLTPROC xsltproc)
# set up approariate _BEFORE or _AFTER variables
if(XSLTPROC_FIND)
    set (XSL_TYPE BEFORE)
    set (XSL_BEFORE ${XSLT_PATH}/nxdl2xsd.xsl)
    set (XSLSORT_BEFORE ${XSLT_PATH}/sort_xsd.xsl)
    set (XSLSCH_BEFORE ${XSLT_PATH}/nxdl2sch.xsl)
    set (XSLTPROC ${XSLTPROC_FIND})
endif(XSLTPROC_FIND)

# msxsl
find_program(MSXSL msxsl)
# set up approariate _BEFORE or _AFTER variables
if(MSXSL)
    set (XSL_TYPE AFTER)
    set (XSL_AFTER ${XSLT_PATH}/nxdl2xsd.xsl)
    set (XSLSORT_AFTER ${XSLT_PATH}/sort_xsd.xsl)
    set (XSLSCH_AFTER ${XSLT_PATH}/nxdl2sch.xsl)
    set (XSLTPROC ${MSXSL})
endif(MSXSL)

# nxslt
find_program(NXSLT nxslt)
# set up approariate _BEFORE or _AFTER variables
if(NXSLT)
    set (XSL_TYPE AFTER)
    set (XSL_AFTER ${XSLT_PATH}/nxdl2xsd.xsl)
    set (XSLSORT_AFTER ${XSLT_PATH}/sort_xsd.xsl)
    set (XSLSCH_AFTER ${XSLT_PATH}/nxdl2sch.xsl)
    set (XSLTPROC ${NXSLT})
endif(NXSLT)

### end of choose your xslt processor 

# relative locations for the NXDL instance files
#set (BASE_CLASS_PATH ${CMAKE_SOURCE_DIR}/base_classes)
#set (APPLICATIONS_CLASS_PATH ${CMAKE_SOURCE_DIR}/applications)
#set (CONTRIBUTED_CLASS_PATH ${CMAKE_SOURCE_DIR}/contributed_definitions)

# make lists of all the NXDL instances 
# (useful to make separate lists for category)
#file(GLOB NXDL_BASE_CLASSES ${BASE_CLASS_PATH}/*.${NXDL_SUFFIX})
#file(GLOB NXDL_APPLICATIONS ${APPLICATIONS_CLASS_PATH}/*.${NXDL_SUFFIX})
#file(GLOB NXDL_CONTRIBUTED ${CONTRIBUTED_CLASS_PATH}/*.${NXDL_SUFFIX})

# put them all together in one big list
# be careful, empty directories will return the $(DIR)/*.$(NXDL_SUFFIX) search pattern
#set (ALL_NXDL ${NXDL_BASE_CLASSES} ${NXDL_APPLICATIONS} ${NXDL_CONTRIBUTED})

if(XSLTPROC AND (XSL_TYPE STREQUAL "BEFORE"))

    message("BEFORE")
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        COMMAND ${CMAKE_COMMAND}
        ARGS -DMY_SOURCE_DIR="${CMAKE_SOURCE_DIR}" -DMY_BINARY_DIR="${CMAKE_BINARY_DIR}" -P ${CMAKE_SOURCE_DIR}/schema/GenerateBASE.cmake
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml and ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml"
    ) 

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd ${XSL_BEFORE} ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        DEPENDS   ${XSL_BEFORE} ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all.xsd
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all.xsd ${XSLSORT_BEFORE} ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd
        DEPENDS   ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all.xsd"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all_base.sch
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all_base.sch ${XSLSCH_BEFORE} ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml
        DEPENDS   ${CMAKE_BINARY_DIR}/schema/all.xsd
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all_base.sch"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all.sch
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all.sch ${XSLSCH_BEFORE} ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        DEPENDS   ${CMAKE_BINARY_DIR}/schema/all_base.sch
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all.sch"
    )

    add_custom_target(BuildSchemaFiles ALL DEPENDS ${CMAKE_BINARY_DIR}/schema/all.sch)

else (XSLTPROC AND (XSL_TYPE STREQUAL "BEFORE"))

    message(AFTER)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        COMMAND ${CMAKE_COMMAND}
        ARGS -DMY_SOURCE_DIR="${CMAKE_SOURCE_DIR}" -DMY_BINARY_DIR="${CMAKE_BINARY_DIR}" -P ${CMAKE_SOURCE_DIR}/schema/GenerateBASE.cmake
        COMMENT   "Generating all_base.nxdl.xml and all.nxdl.xml"
    ) 

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml ${XSL_AFTER}
        DEPENDS   ${XSL_BEFORE} ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all.xsd
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all.xsd ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd ${XSLSORT_AFTER}
        DEPENDS   ${CMAKE_BINARY_DIR}/schema/all_unsorted.xsd
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all.xsd"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all_base.sch
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all_base.sch ${CMAKE_BINARY_DIR}/schema/all_base.nxdl.xml ${XSLSCH_AFTER}
        DEPENDS   ${CMAKE_SOURCE_DIR}/schema/all.xsd
        COMMENT   "Generating ${CMAKE_SOURCE_DIR}/schema/all_base.sch"
    )

    add_custom_command( 
        OUTPUT    ${CMAKE_BINARY_DIR}/schema/all.sch
        COMMAND   ${XSLTPROC}
        ARGS      -o ${CMAKE_BINARY_DIR}/schema/all.sch ${CMAKE_BINARY_DIR}/schema/all.nxdl.xml ${XSLSCH_AFTER}
        DEPENDS   ${CMAKE_BINARY_DIR}/schema/all_base.sch
        COMMENT   "Generating ${CMAKE_BINARY_DIR}/schema/all.sch"
    )

    add_custom_target(BuildSchemaFiles ALL DEPENDS ${CMAKE_BINARY_DIR}/schema/all.sch)


endif(XSLTPROC AND (XSL_TYPE STREQUAL "BEFORE"))

#set(NXDL_FILES all_base.nxdl.xml all_base.sch all.nxdl.xml all.sch all_unsorted.xsd  all.xsd)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} DESTINATION ${NEXUS_DEFINITIONS} COMPONENT definitions FILES_MATCHING PATTERN "*.xml" PATTERN "*.sch" PATTERN "*.xsd")

