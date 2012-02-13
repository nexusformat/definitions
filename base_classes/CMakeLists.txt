## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011 Freddie Akeroyd
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

set(BASE_FILES 
	NXaperture.nxdl.xml 
	NXattenuator.nxdl.xml 
	NXbeam.nxdl.xml 
	NXbeam_stop.nxdl.xml 
	NXbending_magnet.nxdl.xml 
	NXcapillary.nxdl.xml 
	NXcharacterization.nxdl.xml 
	NXcollection.nxdl.xml 
	NXcollimator.nxdl.xml 
	NXcrystal.nxdl.xml 
	NXdata.nxdl.xml 
	NXdetector_group.nxdl.xml 
	NXdetector.nxdl.xml 
	NXdisk_chopper.nxdl.xml 
	NXentry.nxdl.xml 
	NXenvironment.nxdl.xml 
	NXevent_data.nxdl.xml 
	NXfermi_chopper.nxdl.xml 
	NXfilter.nxdl.xml 
	NXflipper.nxdl.xml 
	NXgeometry.nxdl.xml 
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
	NXpolarizer.nxdl.xml 
	NXpositioner.nxdl.xml
	NXprocess.nxdl.xml 
	NXroot.nxdl.xml 
	NXsample.nxdl.xml 
	NXsensor.nxdl.xml 
	NXshape.nxdl.xml 
	NXsource.nxdl.xml 
	NXsubentry.nxdl.xml 
	NXtranslation.nxdl.xml 
	NXuser.nxdl.xml 
	NXvelocity_selector.nxdl.xml 
	NXxraylens.nxdl.xml 
)

set(BASE_SOURCE ${CMAKE_SOURCE_DIR}/base_classes)

set(BASE_DIST ${CMAKE_BINARY_DIR}/dist/base_classes)

add_custom_target(CheckBaseClasses ALL COMMENT "Checking base classes")

configure_nxdl(CheckBaseClasses "${BASE_SOURCE}" "${BASE_DIST}" "${BASE_FILES}")

foreach(F ${BASE_FILES})
    install(FILES ${BASE_DIST}/${F} DESTINATION ${NEXUS_DEFINITIONS}/base_classes COMPONENT definitions)
endforeach()
