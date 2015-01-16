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

ROOTDIR = ../../../..
NXDL2RST = $(ROOTDIR)/utils/nxdl2rst.py
NXDL_SUFFIX = nxdl.xml

SRCDIR = $(ROOTDIR)/applications

SRCs = $(wildcard $(SRCDIR)/NX*.$(NXDL_SUFFIX) )
RSTs := $(SRCs:.$(NXDL_SUFFIX)=.rst)
RSTs := $(patsubst $(SRCDIR)/%, ./%, $(RSTs) )

vpath %.$(NXDL_SUFFIX) $(SRCDIR)

.PHONY: all clean test

all :: $(RSTs)

%.rst : %.$(NXDL_SUFFIX) $(NXDL2RST) Makefile
	$(NXDL2RST) $< > $@

clean ::
	$(RM) NX*.rst

test ::
	# $(SRCs)
	# $(RSTs)
