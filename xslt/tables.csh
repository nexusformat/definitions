#!/usr/bin/tcsh

# NeXus - Neutron & X-ray Common Data Format
# 
# Copyright (C) 2008 NeXus International Advisory Committee (NIAC)
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################

# purpose:
#	manages XSLT translations that are used to generate HTML pages showing
#	units and dimensions used by NeXus base class definitions
#	by translating the NXDL files.

# Usage:
#	./tables.csh


/bin/cp -f /dev/null units.html
/bin/cp -f /dev/null dimensions.html
setenv BASE_CLASS_PATH "../base_classes"

foreach item (`/bin/ls --color=never ${BASE_CLASS_PATH}/*.nxdl.xml`)
	xsltproc units.xsl $item >> units.html
	xsltproc dimensions.xsl $item >> dimensions.html
end
