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
# $Date$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################

# purpose:
#	manage various resources in this directory

# Usage:
#	make		default (1st) rule: same as "make xsd"
#	make xsd	builds all XML Schemas from NeXus base class NXDL files
#	make all	builds xsd
#	make clean	removes files built in this directory
#	make rebuild	does a make clean then make all


NXDL_SUFFIX = nxdl.xml

### start of choose your xslt processor 
# xsltproc has arguments os         "xsl file"
# others such as msxsl, nxslt have  "file xsl"
# so XSL_TYPE needs to be set to BEFORE or AFTER as appropriate

# xsltproc
XSLTPROC=xsltproc # xsltproc, Linux
#XSLTPROC="/c/Program Files/Oxygen XML Editor 10/xsltproc" # xsltproc, Windows/MinGW
XSL_TYPE=BEFORE

# msxsl
#XSLTPROC="/c/Program Files/Oxygen XML Editor 10/msxsl"
#XSL_TYPE=AFTER

# nxslt
#XSLTPROC="/c/Program Files/Oxygen XML Editor 10/nxslt"
#XSL_TYPE=AFTER

### end of choose your xslt processor 

# set up approariate _BEFORE or _AFTER variables
XSL_$(XSL_TYPE)=$(XSLT_PATH)/nxdl2xsd.xsl
XSLSORT_$(XSL_TYPE)=$(XSLT_PATH)/sort_xsd.xsl
XSLSCH_$(XSL_TYPE)=$(XSLT_PATH)/nxdl2sch.xsl

# relative locations for the NXDL instance files
BASE_CLASS_PATH          = ../base_classes
APPLICATIONS_CLASS_PATH  = ../applications
CONTRIBUTED_CLASS_PATH   = ../contributed_definitions

# make lists of all the NXDL instances 
# (useful to make separate lists for category)
NXDL_BASE_CLASSES = $(wildcard $(BASE_CLASS_PATH)/*.$(NXDL_SUFFIX) )
NXDL_APPLICATIONS = $(wildcard $(APPLICATIONS_CLASS_PATH)/*.$(NXDL_SUFFIX) )
NXDL_CONTRIBUTED  = $(wildcard $(CONTRIBUTED_CLASS_PATH)/*.$(NXDL_SUFFIX) )

# put them all together in one big list
# be careful, empty directories will return the $(DIR)/*.$(NXDL_SUFFIX) search pattern
ALL_NXDL = $(NXDL_BASE_CLASSES) $(NXDL_APPLICATIONS) $(NXDL_CONTRIBUTED)

# list of all classes without path and without the trailing .$(NXDL_SUFFIX) suffix
ALL_CLASS_NAMES = $(notdir $(ALL_NXDL) )
APPLICATION_CLASS_NAMES = $(notdir $(NXDL_APPLICATIONS) )
ALL_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xsd, $(ALL_CLASS_NAMES) )
APPLICATION_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xsd, $(APPLICATION_CLASS_NAMES) )
# additional target for cleanup
ALL_CLASS_TARGETS += BASE.xsd


XSLT_PATH = ../xslt

# === Rules ===

all: all.xsd all_base.sch all.sch # all.docbook

xsd : $(ALL_CLASS_TARGETS)

BASE.xsd : ../BASE.xsd $(APPLICATION_CLASS_TARGETS)
	rm -f schema.tmp
	for i in $(APPLICATION_CLASS_TARGETS); do\
	    echo "  <xs:include schemaLocation=\"$$i\"/>" >> schema.tmp; \
	done
	rm -f BASE.xsd
	sed -e "/SCHEMA_INCLUDE_SUB_START/ r schema.tmp" < ../BASE.xsd > BASE.xsd
	rm -f schema.tmp

all_unsorted.xsd : all.nxdl.xml Makefile $(XSL_BEFORE) $(XSL_AFTER)
	$(XSLTPROC) -o $@ $(XSL_BEFORE) $< $(XSL_AFTER)

all.xsd : all_unsorted.xsd Makefile $(XSLSORT_BEFORE) $(XSLSORT_AFTER)
	$(XSLTPROC) -o $@ $(XSLSORT_BEFORE) $< $(XSLSORT_AFTER)

all_base.sch : all_base.nxdl.xml Makefile $(XSLSCH_BEFORE) $(XSLSCH_AFTER)
	$(XSLTPROC) -o $@ $(XSLSCH_BEFORE) $< $(XSLSCH_AFTER)

all.sch : all.nxdl.xml Makefile $(XSLSCH_BEFORE) $(XSLSCH_AFTER)
	$(XSLTPROC) -o $@ $(XSLSCH_BEFORE) $< $(XSLSCH_AFTER)

all_base.nxdl.xml : Makefile $(NXDL_BASE_CLASSES)
	echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?> " > all_base.nxdl.xml
	echo "<definitions>" >> all_base.nxdl.xml
	for i in $(NXDL_BASE_CLASSES); do \
	    sed -e '/^<?xml/d' < $$i >> all_base.nxdl.xml; \
	done
	echo "</definitions>" >> all_base.nxdl.xml

all.nxdl.xml : Makefile $(ALL_NXDL)
	echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?> " > all.nxdl.xml
	echo "<definitions>" >> all.nxdl.xml
	for i in $(ALL_NXDL); do \
	    sed -e '/^<?xml/d' < $$i >> all.nxdl.xml; \
	done
	echo "</definitions>" >> all.nxdl.xml

# NXDL files come from three source directories 
#   but end up in one schema directory.  This means 
#   that no two NXDL files can have the same class name. 
%.xsd: $(BASE_CLASS_PATH)/%.nxdl.xml Makefile $(XSLT_PATH)/nxdl2xsd.xsl
	$(XSLTPROC) -o $@ $(XSL_BEFORE) $< $(XSL_AFTER)
%.xsd: $(APPLICATIONS_CLASS_PATH)/%.nxdl.xml Makefile $(XSLT_PATH)/nxdl2xsd.xsl
	$(XSLTPROC) -o $@ $(XSL_BEFORE) $< $(XSL_AFTER)
%.xsd: $(CONTRIBUTED_CLASS_PATH)/%.nxdl.xml Makefile $(XSLT_PATH)/nxdl2xsd.xsl
	$(XSLTPROC) -o $@ $(XSL_BEFORE) $< $(XSL_AFTER)

clean ::
	rm -f $(ALL_CLASS_TARGETS)
	rm -f all.xsd all_unsorted.xsd all_base.nxdl.xml all.nxdl.xml \
		all_base.sch all.sch

rebuild :: clean all

NeXus.xsd :
	echo "NeXus.xsd is manually-generated.  Do not remove or rebuild it."
