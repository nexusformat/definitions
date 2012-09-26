# Makefile for NeXus manual custom pages

# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2012 NeXus International Advisory Committee (NIAC)
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
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

all :: NXcrystal.rst NXentry.rst NXdata.rst

NXDL2RST = ../../../../utils/nxdl2rst.py
SRCDIR = ../../../../base_classes

NXcrystal.rst: $(SRCDIR)/NXcrystal.nxdl.xml $(NXDL2RST) Makefile
	$(NXDL2RST) $(SRCDIR)/NXcrystal.nxdl.xml > $@
	#echo "----------------------"
	#echo $(NXDL2RST)
	#echo $@
	#echo $<
	#echo "----------------------"

NXentry.rst: $(NXDL2RST) $(SRCDIR)/NXentry.nxdl.xml
	$(NXDL2RST) $(SRCDIR)/NXentry.nxdl.xml > $@

NXdata.rst: $(NXDL2RST) $(SRCDIR)/NXdata.nxdl.xml
	$(NXDL2RST) $(SRCDIR)/NXdata.nxdl.xml > $@

%.rst: $(SRCDIR)%.nxdl.xml Makefile $(NXDL2RST)
	echo $(NXDL2RST) $@ $<

clean ::
	$(RM) NX*.rst
