## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
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

#foreach(NXDL_FILE ${NXDL_APPLICATIONS})
#    file (APPEND schema.tmp "  <xs:include schemaLocation=\"classes/${NXDL_FILE}\"/>\n")
#endforeach(NXDL_FILE)

set(NXDL_SUFFIX nxdl.xml)

# relative locations for the NXDL instance files
set (BASE_CLASS_PATH ${MY_BINARY_DIR}/dist/base_classes)
set (APPLICATIONS_CLASS_PATH ${MY_BINARY_DIR}/dist/applications)
set (CONTRIBUTED_CLASS_PATH ${MY_BINARY_DIR}/dist/contributed_definitions)

# make lists of all the NXDL instances 
# (useful to make separate lists for category)
file(GLOB NXDL_BASE_CLASSES ${BASE_CLASS_PATH}/*.${NXDL_SUFFIX})
file(GLOB NXDL_APPLICATIONS ${APPLICATIONS_CLASS_PATH}/*.${NXDL_SUFFIX})
file(GLOB NXDL_CONTRIBUTED ${CONTRIBUTED_CLASS_PATH}/*.${NXDL_SUFFIX})

# put them all together in one big list
# be careful, empty directories will return the $(DIR)/*.$(NXDL_SUFFIX) search pattern
set (ALL_NXDL ${NXDL_BASE_CLASSES} ${NXDL_APPLICATIONS} ${NXDL_CONTRIBUTED})

file(WRITE ${MY_BINARY_DIR}/schema/all_base.nxdl.xml "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
file(APPEND ${MY_BINARY_DIR}/schema/all_base.nxdl.xml "<definitions>\n")

foreach(NXDL_FILE ${NXDL_BASE_CLASSES})
    file (READ ${NXDL_FILE} IN_FILE)
    string (REPLACE "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" ""  IN_FILE2 "${IN_FILE}")
    string (REPLACE "<?xml-stylesheet type=\"text/xsl\" href=\"nxdlformat.xsl\" ?>" ""  IN_FILE3 "${IN_FILE2}")
    file(APPEND ${MY_BINARY_DIR}/schema/all_base.nxdl.xml "${IN_FILE3}")
endforeach(NXDL_FILE)
file(APPEND ${MY_BINARY_DIR}/schema/all_base.nxdl.xml "</definitions>\n")

file(WRITE ${MY_BINARY_DIR}/schema/all.nxdl.xml "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
file(APPEND ${MY_BINARY_DIR}/schema/all.nxdl.xml "<definitions>\n")

foreach(NXDL_FILE ${ALL_NXDL})
    file (READ ${NXDL_FILE} IN_FILE)
    string (REPLACE "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" ""  IN_FILE2 "${IN_FILE}")
    string (REPLACE "<?xml-stylesheet type=\"text/xsl\" href=\"nxdlformat.xsl\" ?>" ""  IN_FILE3 "${IN_FILE2}")
    file(APPEND ${MY_BINARY_DIR}/schema/all.nxdl.xml "${IN_FILE3}")
endforeach(NXDL_FILE)
file(APPEND ${MY_BINARY_DIR}/schema/all.nxdl.xml "</definitions>\n")


