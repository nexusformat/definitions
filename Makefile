# File: Makefile

# purpose:
#	build resources in NeXus definitions tree

# ref: http://www/gnu.org/software/make/manual/make.html

SUBDIRS = manual impatient-guide

.PHONY: subdirs $(SUBDIRS) builddir all

subdirs: $(SUBDIRS)

#$(SUBDIRS):
#	$(MAKE) -C $@

manual :: nxdl2rst
	$(MAKE) html -C $@

all :: 
	$(MAKE) rmbuilddir builddir
	$(MAKE) impatient-guide manual -C build
	# expect next make (PDF) to fail (thus exit 0) since nexus.ind not found first time
	# extra option needed to satisfy "levels nested too deeply" error
	($(MAKE) latexpdf LATEXOPTS="--interaction=nonstopmode" -C build/manual || exit 0)
	# make that missing file
	makeindex build/manual/build/latex/nexus.idx
	# build the PDF, still a failure will be noted but we can ignore it without problem
	($(MAKE) latexpdf LATEXOPTS="--interaction=nonstopmode" -C build/manual || exit 0)
	# finally, report what was built
	@echo "HTML built: `ls -lAFgh build/manual/build/html/index.html`"
	@echo "PDF built: `ls -lAFgh build/manual/build/latex/nexus.pdf`"

impatient-guide ::
	$(MAKE) html -C $@

#pdfdoc ::
#	$(MAKE) latexpdf -C $(SUBDIRS)

clean:
	$(MAKE) clean -C $(SUBDIRS)

nxdl2rst:
	$(MAKE) -C manual/source

builddir :: 
	mkdir -p build
	python utils/build_preparation.py . build

makebuilddir :: builddir
	$(MAKE) -C build

remakebuilddir :: makebuilddir

rebuildall :: rmbuilddir makebuilddir

cleanbuilddir ::
	$(MAKE) -C build clean

rmbuilddir ::
	$(RM) -r build

# for developer's use on local build host
local ::
	python utils/test_suite.py
	$(RM) -r build
	mkdir -p build
	python utils/build_preparation.py . build
	$(MAKE) -C build

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
