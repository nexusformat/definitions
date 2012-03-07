## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011-2012 NeXus International Advisory Committee (NIAC)
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

#if (LATEX_FOUND)

    set (TUTORIAL_SOURCE ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.tex)

    set (IMAGE_FILES ${CMAKE_SOURCE_DIR}/tutorial/dmc.eps
                     ${CMAKE_SOURCE_DIR}/tutorial/dmc.png
                     ${CMAKE_SOURCE_DIR}/tutorial/polplane.eps
                     ${CMAKE_SOURCE_DIR}/tutorial/polplane.png
                     ${CMAKE_SOURCE_DIR}/tutorial/powderimage.eps
                     ${CMAKE_SOURCE_DIR}/tutorial/powderimage.png)

    ADD_CUSTOM_COMMAND( 
        OUTPUT    ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.aux ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.log
        COMMAND   ${LATEX_COMPILER}
        ARGS      ${TUTORIAL_SOURCE}
        DEPENDS   ${TUTORIAL_SOURCE} ${IMAGE_FILES}
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/tutorial
        COMMENT   "Generating Definitions Tutorial AUX"
    )

    ADD_CUSTOM_COMMAND( 
        OUTPUT    ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.dvi
        COMMAND   ${LATEX_COMPILER}
        ARGS      ${TUTORIAL_SOURCE}
        DEPENDS   ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.aux ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.log
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/tutorial
        COMMENT   "Generating Definitions Tutorial DVI"
    )

    ADD_CUSTOM_COMMAND( 
        OUTPUT    ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.ps
        COMMAND   ${DVIPS_CONVERTER}
        ARGS      -o ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.ps ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.dvi
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/tutorial
        DEPENDS   ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.dvi
        COMMENT   "Generating Definitions Tutorial PS"
    )

    ADD_CUSTOM_COMMAND( 
        OUTPUT    ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.pdf
        COMMAND   ${PS2PDF_CONVERTER}
        ARGS      ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.ps ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.pdf
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/tutorial
        DEPENDS   ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.ps
        COMMENT   "Generating Definitions Tutorial PDF"
    )

    ADD_CUSTOM_TARGET(NexusDefinitionsTutorialBuild ALL echo
        DEPENDS   ${CMAKE_SOURCE_DIR}/tutorial/NXDLTutorial.pdf
    )

#endif (LATEX_FOUND)

