#   File: Makefile

# NeXus - Neutron & X-ray Common Data Format
# 
# Copyright (C) 2008-2010 NeXus International Advisory Committee (NIAC)
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
ALL_NXDL = $(NXDL_BASE_CLASSES) $(NXDL_APPLICATIONS) $(NXDL_CONTRIBUTED)

# list of all classes without path and without the trailing .$(NXDL_SUFFIX) suffix
ALL_CLASS_NAMES = $(notdir $(ALL_NXDL) )
ALL_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), classes/%.xml, $(ALL_CLASS_NAMES) )

BASE_CLASS_NAMES          = $(notdir $(NXDL_BASE_CLASSES) )
APPLICATION_CLASS_NAMES   = $(notdir $(NXDL_APPLICATIONS) )
CONTRIBUTED_CLASS_NAMES   = $(notdir $(NXDL_CONTRIBUTED) )
BASE_CLASS_TARGETS        = $(patsubst %.$(NXDL_SUFFIX), classes/%.xml, $(BASE_CLASS_NAMES) )
APPLICATION_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), classes/%.xml, $(APPLICATION_CLASS_NAMES) )
CONTRIBUTED_CLASS_TARGETS = $(patsubst %.$(NXDL_SUFFIX), classes/%.xml, $(CONTRIBUTED_CLASS_NAMES) )

# XSLT definitions
XSLT_PATH = ../xslt
XSLT = $(XSLT_PATH)/nxdl2docbook.xsl

DYNAMIC_DOCBOOK_SECTIONS  = classes/BaseClassSections.xml 
DYNAMIC_DOCBOOK_SECTIONS += classes/ApplicationClassSections.xml 
DYNAMIC_DOCBOOK_SECTIONS += classes/ContributedClassSections.xml
DYNAMIC_DOCBOOK_SECTIONS += types.xml
DYNAMIC_DOCBOOK_SECTIONS += units.xml
DYNAMIC_DOCBOOK_SECTIONS += subtitle.xml

CLEANING_LIST =
CLEANING_LIST += NeXusManual.pdf
CLEANING_LIST += NeXusManual.html
CLEANING_LIST += NeXusManual_one_chunk.html
CLEANING_LIST += html/
CLEANING_LIST += NeXusManual.ps
CLEANING_LIST += classes/
CLEANING_LIST += types.xml
CLEANING_LIST += units.xml

CLASS_HEAD_PYTHON = ../utils/classSectionHead.py

# for details, see: http://dblatex.sourceforge.net/doc/sec-custom.html
DBLATEX_OPTS =  -P table.in.float=0
DBLATEX_OPTS += -P doc.lot.show="figure"
#DBLATEX_OPTS += -P toc.section.depth=2
#DBLATEX_OPTS += -P draft.watermark=1
DBLATEX_OPTS += -b pdftex -tpdf

# === Rules ===

#all: NeXusManual.pdf NeXusManual.html NeXusManual_one_chunk.html html/index.html
all: NeXusManual.pdf NeXusManual.html html/index.html

docbook : $(ALL_CLASS_TARGETS) $(DYNAMIC_DOCBOOK_SECTIONS) NeXusManual.xml

# This uses VPATH to locate the source directory for the target
classes/%.xml: %.$(NXDL_SUFFIX) Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<

test ::
	@echo $(CLEANING_LIST)


subtitle.xml ::
	../utils/setsubtitle.csh > $@


classes/BaseClassSections.xml : $(BASE_CLASS_TARGETS) Makefile $(CLASS_HEAD_PYTHON)
	python $(CLASS_HEAD_PYTHON) 'Base' $(BASE_CLASS_TARGETS) > $@
	@echo "(Re)created $@"

classes/ApplicationClassSections.xml : $(APPLICATION_CLASS_TARGETS) Makefile $(CLASS_HEAD_PYTHON)
	python $(CLASS_HEAD_PYTHON) 'Application' $(APPLICATION_CLASS_TARGETS) > $@
	@echo "(Re)created $@"

classes/ContributedClassSections.xml : $(CONTRIBUTED_CLASS_TARGETS) Makefile $(CLASS_HEAD_PYTHON)
	python $(CLASS_HEAD_PYTHON) 'Contributed' $(CONTRIBUTED_CLASS_TARGETS) > $@
	@echo "(Re)created $@"


types.xml : ../nxdlTypes.xsd Makefile $(XSLT_PATH)/nxdl_types2docbook.xsl
	xsltproc $(XSLT_PATH)/nxdl_types2docbook.xsl ../nxdlTypes.xsd > $@
	@echo "(Re)created $@"

units.xml : ../nxdlTypes.xsd Makefile $(XSLT_PATH)/nxdl_units2docbook.xsl
	xsltproc $(XSLT_PATH)/nxdl_units2docbook.xsl ../nxdlTypes.xsd > $@
	@echo "(Re)created $@"


NeXusManual.pdf : docbook
	# dblatex.sf.net is used to build a PDF version of the NeXus Manual
	dblatex -V $(DBLATEX_OPTS) NeXusManual.xml


###############################################################################

# installation root directory for docbook xslt stylesheets
#    http://sourceforge.net/projects/docbook/
DBXSL:=$(abspath ..)/xslt/docbook-xsl-1.75.2

# for xslt options, see: http://docbook.sourceforge.net/release/xsl/current/doc/html/
NeXusManual.html : docbook
	xsltproc --xinclude --output $@ \
	  --stringparam use.extensions 0 \
	  --stringparam callout.graphics.path "img/callouts/" \
	  $(DBXSL)/html/docbook.xsl \
	  NeXusManual.xml

NeXusManual_one_chunk.html : docbook
	xsltproc --xinclude \
	  --stringparam use.extensions 0 \
	  --stringparam callout.graphics.path "img/callouts/" \
	  $(DBXSL)/html/onechunk.xsl \
	  NeXusManual.xml
	mv index.html $@

html/index.html : docbook
	[ -d html ] || mkdir html
	( cd html; xsltproc --xinclude \
	  --stringparam use.extensions 0 \
	  --stringparam callout.graphics.path "../img/callouts/" \
	  $(DBXSL)/html/chunk.xsl \
	  ../NeXusManual.xml; )

###############################################################################

NeXusManual.ps :: NeXusManual.pdf
	pdftops $<

clean ::
	/bin/rm -rf $(CLEANING_LIST)

rebuild :: clean all
