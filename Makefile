# File: Makefile

# purpose:
#	build resources in NeXus definitions tree

# ref: http://www/gnu.org/software/make/manual/make.html

SUBDIRS = manual impatient-guide

.PHONY: subdirs $(SUBDIRS) builddir pdfdoc

subdirs: $(SUBDIRS)

#$(SUBDIRS):
#	$(MAKE) -C $@

manual ::
	$(MAKE) html -C $@

impatient-guide ::
	$(MAKE) html -C $@

#pdfdoc ::
#	$(MAKE) latexpdf -C $(SUBDIRS)

clean:
	$(MAKE) clean -C $(SUBDIRS)

builddir :: 
	mkdir -p build
	python utils/build_preparation.py . build

makebuilddir :: builddir
	$(MAKE) -C build

remakebuilddir :: makebuilddir

cleanbuilddir ::
	$(MAKE) -C build clean

rmbuilddir ::
	$(RM) -r build


# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2018 NeXus International Advisory Committee (NIAC)
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
