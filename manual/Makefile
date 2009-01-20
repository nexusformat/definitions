#   File: Makefile

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
# $Date: 2008$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################

# purpose:
#	manage various resources in this directory

# Usage:
#	make		default (1st) rule: same as "make all"
#	make docbook	builds DocBook sections from all NeXus base class NXDL files
#	make all	builds docbook and BaseClassSections.xml
#	make clean	removes files built in this directory
#	make rebuild	does a make clean then make all

NXDL_SUFFIX = nxdl.xml

# relative locations for the NXDL instance files
BASE_CLASS_PATH          = ../base_classes
APPLICATIONS_CLASS_PATH  = ../applications
CONTRIBUTED_CLASS_PATH   = ../contributed_definitions

VPATH = $(BASE_CLASS_PATH) $(APPLICATIONS_CLASS_PATH) $(CONTRIBUTED_CLASS_PATH)

# make lists of all the NXDL instances 
# (useful to make separate lists for category)
NXDL_BASE_CLASSES = $(wildcard $(BASE_CLASS_PATH)/*.$(NXDL_SUFFIX) )
NXDL_APPLICATIONS = $(wildcard $(APPLICATIONS_CLASS_PATH)/*.$(NXDL_SUFFIX) )
NXDL_CONTRIBUTED  = $(wildcard $(CONTRIBUTED_CLASS_PATH)/*.$(NXDL_SUFFIX) )

# put them all together in one big list
# be careful, empty directories will return the $(DIR)/*.$(NXDL_SUFFIX) search pattern
ALL_NXDL = $(NXDL_BASE_CLASSES) # $(NXDL_APPLICATIONS) $(NXDL_CONTRIBUTED)

# list of all classes without path and without the trailing .$(NXDL_SUFFIX) suffix
ALL_CLASS_NAMES = $(notdir $(ALL_NXDL) )
ALL_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xml, $(ALL_CLASS_NAMES) )

# XSLT definitions
XSLT_PATH = ../xslt
XSLT = $(XSLT_PATH)/nxdl2docbook.xsl

# === Rules ===

all: docbook BaseClassSections.xml

docbook : $(ALL_CLASS_TARGETS)

# This uses VPATH to locate the source directory for the target
%.xml: %.$(NXDL_SUFFIX) Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<

test ::
	@echo $(ALL_CLASS_TARGETS)


BaseClassSections.xml :: $(ALL_NXDL) Makefile
	@echo '<?xml version="1.0" encoding="UTF-8"?>' > $@
	@echo '<?oxygen RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"?>' >> $@
	@echo '<section xmlns="http://docbook.org/ns/docbook" version="5.0" xmlns:xi="http://www.w3.org/2001/XInclude">' >> $@
	@echo '<title>Base Classes</title>' >> $@
	@echo '<para>A description of each NeXus Base Class is given.</para>' >> $@
	@echo $(patsubst %,  "<xi:include href=\""%"\"/>", $(wildcard $(ALL_CLASS_TARGETS)) ) >> $@
	@echo '</section>' >> $@
	@echo "(Re)Created $@"

clean ::
	/bin/rm -f $(ALL_CLASS_TARGETS) BaseClassSections.xml

rebuild :: clean all
