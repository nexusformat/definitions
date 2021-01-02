# Makefile for NeXus manual custom pages

# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2021 NeXus International Advisory Committee (NIAC)
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
NXDLSUMMARY= $(ROOTDIR)/utils/nxdl_summary.py
NXDL_SUFFIX = nxdl.xml

SRCDIR = $(ROOTDIR)/base_classes

SRCs = $(wildcard $(SRCDIR)/NX*.$(NXDL_SUFFIX) )
RSTs := $(SRCs:.$(NXDL_SUFFIX)=.rst)
RSTs := $(patsubst $(SRCDIR)/%, ./%, $(RSTs) )
TARGET_NXDLs = $(patsubst $(SRCDIR)/%, ./%, $(SRCs) )

#vpath %.$(NXDL_SUFFIX) $(SRCDIR)

.PHONY: all clean test

all :: index.rst $(RSTs) $(TARGET_NXDLs)

%.nxdl.xml : $(SRCDIR)/%.$(NXDL_SUFFIX)  Makefile
	cp $(SRCDIR)/$@   ./$@

index.rst :: 
	echo "Adding summaries to base_classes/index.rst"
	python $(NXDLSUMMARY) base_classes

%.rst : %.$(NXDL_SUFFIX) $(NXDL2RST) Makefile
	python $(NXDL2RST) $< > $@

clean ::
	$(RM) NX*.rst NX*.nxdl.xml

test ::
	# $(SRCs)
	# -----------
	# $(RSTs)
