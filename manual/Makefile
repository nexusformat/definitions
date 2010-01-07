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

VPATH = $(BASE_CLASS_PATH) $(APPLICATIONS_CLASS_PATH) $(CONTRIBUTED_CLASS_PATH)5

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
ALL_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xml, $(ALL_CLASS_NAMES) )

BASE_CLASS_NAMES          = $(notdir $(NXDL_BASE_CLASSES) )
APPLICATION_CLASS_NAMES   = $(notdir $(NXDL_APPLICATIONS) )
CONTRIBUTED_CLASS_NAMES   = $(notdir $(NXDL_CONTRIBUTED) )
BASE_CLASS_TARGETS        = $(patsubst %.$(NXDL_SUFFIX), %.xml, $(BASE_CLASS_NAMES) )
APPLICATION_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xml, $(APPLICATION_CLASS_NAMES) )
CONTRIBUTED_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), %.xml, $(CONTRIBUTED_CLASS_NAMES) )

# XSLT definitions
XSLT_PATH = ../xslt
XSLT = $(XSLT_PATH)/nxdl2docbook.xsl

DYNAMIC_DOCBOOK_SECTIONS  = BaseClassSections.xml 
DYNAMIC_DOCBOOK_SECTIONS += ApplicationClassSections.xml 
DYNAMIC_DOCBOOK_SECTIONS += ContributedClassSections.xml

CLEANING_LIST = $(ALL_CLASS_TARGETS) 
CLEANING_LIST += $(DYNAMIC_DOCBOOK_SECTIONS)
CLEANING_LIST += $(patsubst %.xml, %.pdf, $(ALL_CLASS_TARGETS))
CLEANING_LIST += $(patsubst %.xml, %.html, $(ALL_CLASS_TARGETS))
#CLEANING_LIST += $(patsubst %.xml, %.ps, $(ALL_CLASS_TARGETS))
CLEANING_LIST += NeXusManual.pdf
CLEANING_LIST += NeXusManual.html
CLEANING_LIST += NeXusManual.ps

# === Rules ===

all: docbook

docbook : $(ALL_CLASS_TARGETS) $(DYNAMIC_DOCBOOK_SECTIONS) NeXusManual.pdf

# This uses VPATH to locate the source directory for the target
%.xml: %.$(NXDL_SUFFIX) Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<
	python ./addnxdlcode.py $< $@

test ::
	@echo $(CLEANING_LIST)


BaseClassSections.xml : $(BASE_CLASS_TARGETS) Makefile classSectionHead.py
	python ./classSectionHead.py 'Base' $(BASE_CLASS_TARGETS) > $@
	@echo "(Re)Created $@"

ApplicationClassSections.xml : $(APPLICATION_CLASS_TARGETS) Makefile classSectionHead.py
	python ./classSectionHead.py 'Application' $(APPLICATION_CLASS_TARGETS) > $@
	@echo "(Re)Created $@"

ContributedClassSections.xml : $(CONTRIBUTED_CLASS_TARGETS) Makefile classSectionHead.py
	python ./classSectionHead.py 'Contributed' $(CONTRIBUTED_CLASS_TARGETS) > $@
	@echo "(Re)Created $@"


# dblatex.sf.net is used to build a PDF version of the NeXus Manual
dblatex NeXusManual.pdf ::
	@#dblatex -P table.in.float=0 -ttex NeXusManual.xml
	dblatex -V -P table.in.float=0 -b pdftex -tpdf NeXusManual.xml
	@#pdftops $< temporaryNeXusManual.ps
	@#ps2pdf temporaryNeXusManual.ps $<

NeXusManual.ps ::NeXusManual.pdf
	pdftops $<

clean ::
	/bin/rm -f $(CLEANING_LIST)

rebuild :: clean all
