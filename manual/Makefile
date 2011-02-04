#   File: Makefile

# NeXus - Neutron & X-ray Common Data Format
# 
# Copyright (C) 2008-2011 NeXus International Advisory Committee (NIAC)
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
ALL_CLASS_SUMMARIES = $(patsubst %.$(NXDL_SUFFIX), classes/%.txt, $(ALL_CLASS_NAMES) )

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
DYNAMIC_DOCBOOK_SECTIONS += nxdl_desc.xml
DYNAMIC_DOCBOOK_SECTIONS += subtitle.xml

BUILT_NEXUSMANUAL  = NeXusManual.pdf
BUILT_NEXUSMANUAL += NeXusManual.html
#BUILT_NEXUSMANUAL += NeXusManual.ps

BUILT_NEXUSREFDOC  = NeXusRefDoc.pdf
#BUILT_NEXUSREFDOC += NeXusRefDoc.ps

CLEANING_LIST =
CLEANING_LIST += $(BUILT_NEXUSMANUAL)
CLEANING_LIST += $(BUILT_NEXUSREFDOC)
CLEANING_LIST += html/
CLEANING_LIST += classes/
CLEANING_LIST += types.xml
CLEANING_LIST += units.xml
CLEANING_LIST += nxdl_desc.xml

CLASS_HEAD_PYTHON = ../utils/classSectionHead.py

# for details, see: http://dblatex.sourceforge.net/doc/sec-custom.html
DBLATEX_OPTS =  -P table.in.float=0
DBLATEX_OPTS += -P doc.lot.show="figure"
#DBLATEX_OPTS += -P toc.section.depth=2
#DBLATEX_OPTS += -P draft.watermark=1
DBLATEX_OPTS += -b pdftex -tpdf
#  http://dblatex.sourceforge.net/doc/manual/sec-pub-output.html#sec-book-set
#DBLATEX_OPTS += -Pset.book.num=all
#DBLATEX_OPTS += -Puse.id.as.filename=1

###############################################################################

# === Rules ===

#all: NeXusManual.pdf NeXusManual.html NeXusManual_one_chunk.html html/index.html
all: $(BUILT_NEXUSMANUAL) $(BUILT_NEXUSREFDOC) html/index.html 

docbook : $(ALL_CLASS_TARGETS) $(ALL_CLASS_SUMMARIES) $(DYNAMIC_DOCBOOK_SECTIONS) NeXusManual.xml

# build the DocBook documentation of each NXDL
# This uses VPATH to locate the source directory for the target
classes/%.xml: %.$(NXDL_SUFFIX) Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<

# build the simple view of the structure of each NXDL
# This uses VPATH to locate the source directory for the target
classes/%.txt: %.$(NXDL_SUFFIX) Makefile
	xsltproc -o $@ $<

test ::
	@echo $(CLEANING_LIST)


subtitle.xml ::
	/bin/sh ../utils/setsubtitle.sh > $@


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

nxdl_desc.xml : ../nxdl.xsd Makefile $(XSLT_PATH)/nxdl_desc2docbook.xsl
	xsltproc $(XSLT_PATH)/nxdl_desc2docbook.xsl ../nxdl.xsd > $@
	@echo "(Re)created $@"


NeXusManual.pdf : docbook
	# dblatex.sf.net is used to build a PDF version of the NeXus Manual
	# build two separate PDF documents
	dblatex -V -Pset.book.num=1 $(DBLATEX_OPTS) NeXusManual.xml -o $@

NeXusRefDoc.pdf : docbook
	# dblatex.sf.net is used to build a PDF version of the NeXus Manual
	# build two separate PDF documents
	dblatex -V -Pset.book.num=2 $(DBLATEX_OPTS) NeXusManual.xml -o $@

pdf :: NeXusManual.pdf NeXusRefDoc.pdf

###############################################################################

# installation root directory for docbook xslt stylesheets
#    http://sourceforge.net/projects/docbook/
DBXSL:=$(abspath ..)/xslt/docbook-xsl-1.75.2

# for xslt options, see: http://docbook.sourceforge.net/release/xsl/current/doc/html/
# for single html page we have choice of docbook.xsl and onechunk.xsl
# onechunk.xsl looks better at the moment

#NeXusManual.html : docbook
#	xsltproc --xinclude --output $@ \
#	  --stringparam use.extensions 0 \
#	  --stringparam callout.graphics.path "img/callouts/" \
#	  $(DBXSL)/html/docbook.xsl \
#	  NeXusManual.xml
#	sed -i -e 's/\o240/ /g' $@

NeXusManual.html : docbook
	xsltproc --xinclude \
	  --stringparam use.extensions 0 \
	  --stringparam callout.graphics.path "img/callouts/" \
	  --stringparam chunker.output.encoding UTF-8 \
	  $(DBXSL)/html/onechunk.xsl \
	  NeXusManual.xml
	mv index.html $@

html/index.html : docbook
	[ -d html ] || mkdir html
	( cd html; xsltproc --xinclude \
	  --stringparam use.id.as.filename 1 \
	  --stringparam use.extensions 0 \
	  --stringparam callout.graphics.path "../img/callouts/" \
	  --stringparam chunker.output.encoding UTF-8 \
	  $(DBXSL)/html/chunk.xsl \
	  ../NeXusManual.xml; )

###############################################################################

NeXusManual.ps :: NeXusManual.pdf
	pdftops $<

NeXusRefDoc.ps :: NeXusRefDoc.pdf
	pdftops $<

clean ::
	/bin/rm -rf $(CLEANING_LIST)

rebuild :: clean all
