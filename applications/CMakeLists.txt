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


set(APPLICATION_FILES 
	NXarchive.nxdl.xml 
	NXdirecttof.nxdl.xml 
	NXfluo.nxdl.xml 
	NXindirecttof.nxdl.xml 
	NXiqproc.nxdl.xml 
	NXlauetof.nxdl.xml 
	NXmonopd.nxdl.xml 
	NXrefscan.nxdl.xml 
	NXreftof.nxdl.xml 
	NXsas.nxdl.xml 
	NXsastof.nxdl.xml 
	NXscan.nxdl.xml 
	NXspe.nxdl.xml 
	NXsqom.nxdl.xml 
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

set(APPLICATION_SOURCE ${CMAKE_SOURCE_DIR}/applications)

set(APPLICATION_DIST ${CMAKE_BINARY_DIR}/dist/applications)

add_custom_target(CheckApplicationClasses ALL COMMENT "Checking application classes")

configure_nxdl(CheckApplicationClasses "${APPLICATION_SOURCE}" "${APPLICATION_DIST}" "${APPLICATION_FILES}")

foreach(F ${APPLICATION_FILES})
    install(FILES ${APPLICATION_DIST}/${F} DESTINATION ${NEXUS_DEFINITIONS}/applications COMPONENT definitions)
endforeach()
