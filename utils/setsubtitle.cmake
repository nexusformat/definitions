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
#  For further information, see <http://www.neutron.anl.gov/NeXus/>
#
#
#====================================================================

file(WRITE subtitle.xml "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
file(APPEND subtitle.xml "<?oxygen \n")
file(APPEND subtitle.xml "    RNGSchema=\"http://www.oasis-open.org/docbook/xml/5.0/rng/docbookxi.rng\" \n")
file(APPEND subtitle.xml "    type=\"xml\"?>\n")
file(APPEND subtitle.xml "<subtitle \n")
file(APPEND subtitle.xml "    xmlns=\"http://docbook.org/ns/docbook\" \n")
file(APPEND subtitle.xml "    version=\"5.0\">\n")
file(APPEND subtitle.xml "    <!-- manual was last rebuilt on this date/time -->\n")
#file(APPEND subtitle.xml "    Id:' ${svnid}, `date\n")
file(APPEND subtitle.xml "</subtitle>\n")


