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
#	make		default (1st) rule: same as "make docbook"
#	make docbook	builds DocBook sections from all NeXus base class NXDL files
#	make all	builds docbook and BaseClassSections.xml
#	make clean	removes files built in this directory
#	make rebuild	does a make clean then make all

NXDL_SUFFIX = nxdl.xml

# relative locations for the NXDL instance files
BASE_CLASS_PATH          = ../base_classes
APPLICATIONS_CLASS_PATH  = ../applications
CONTRIBUTED_CLASS_PATH   = ../contributed_definitions

# make lists of all the NXDL instances 
# (useful to make separate lists for category)
NXDL_BASE_CLASSES = $(BASE_CLASS_PATH)/*.$(NXDL_SUFFIX)
NXDL_APPLICATIONS = $(APPLICATIONS_CLASS_PATH)/*.$(NXDL_SUFFIX)
NXDL_CONTRIBUTED  = $(CONTRIBUTED_CLASS_PATH)/*.$(NXDL_SUFFIX)

# put them all together in one big list
# be careful, empty directories will return the $(DIR)/*.$(NXDL_SUFFIX) search pattern
ALL_NXDL = $(wildcard $(NXDL_BASE_CLASSES) $(NXDL_APPLICATIONS) $(NXDL_CONTRIBUTED))

# list of all classes without path and without the trailing .$(NXDL_SUFFIX) suffix
BASE_CLASS_NAMES = $(patsubst $(BASE_CLASS_PATH)/%.$(NXDL_SUFFIX), %, $(ALL_NXDL) )
XML_BASE_CLASS_TARGETS =  $(BASE_CLASS_NAMES:%= %.xml)

# XSLT definitions
XSLT_PATH = ../xslt
XSLT = $(XSLT_PATH)/nxdl2docbook.xsl

# === Rules ===

docbook : $(XML_BASE_CLASS_TARGETS)

all: docbook BaseClassSections.xml

# need to revise this rule once there NXDL instances
# in applications and contributed_definitions
%.xml: $(BASE_CLASS_PATH)/%.nxdl.xml Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<

test ::
	@echo $(XML_BASE_CLASS_TARGETS) > BaseClassSections


BaseClassSections.xml :: $(ALL_NXDL) Makefile
	@echo '<?xml version="1.0" encoding="UTF-8"?>' > $@
	@echo '<?oxygen RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"?>' >> $@
	@echo '<section xmlns="http://docbook.org/ns/docbook" version="5.0" xmlns:xi="http://www.w3.org/2001/XInclude">' >> $@
	@echo '<title>Base Classes</title>' >> $@
	@echo $(patsubst %,  "<xi:include href=\""%"\"/>", $(wildcard $(XML_BASE_CLASS_TARGETS)) ) >> $@
	@echo '</section>' >> $@
	@echo "(Re)Created $@"

clean ::
	/bin/rm -f $(XML_BASE_CLASS_TARGETS) BaseClassSections.xml

rebuild :: clean all
