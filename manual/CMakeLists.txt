#=========================================================================----
#  NeXus - Neutron & X-ray Common Data Format
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

add_subdirectory(source)

#-----------------------------------------------------------------------------
# list of targets which have to be available before anything else can be 
# built
#-----------------------------------------------------------------------------
set(RST_TARGETS xds-manual-source 
                base-class-manual-sources
                applications-manual-sources 
                contributed-manual-sources
                )

#-----------------------------------------------------------------------------
# Build and install the HTML documentation
#-----------------------------------------------------------------------------
add_custom_target(htmldoc ALL 
    COMMAND sphinx-build -b html source html 
    DEPENDS  ${RST_TARGETS}   
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/html
        DESTINATION ${NEXUS_MANUAL})

#-----------------------------------------------------------------------------
# Build PDF documentation
#-----------------------------------------------------------------------------
add_custom_target(latexdoc 
    COMMAND sphinx-build -b latex source pdf
    DEPENDS  ${RST_TARGETS}   
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

add_custom_target(pdfdoc  
    COMMAND make
    DEPENDS  ${RST_TARGETS} latexdoc
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/pdf)


