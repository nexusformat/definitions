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


all :: types.table units.table nxdl_desc.rst subdirs

types.table: ../../utils/types2rst.py ../../utils/units2rst.py ../../nxdlTypes.xsd
	python ../../utils/types2rst.py ../../nxdlTypes.xsd > $@

units.table: ../../utils/units2rst.py ../../nxdlTypes.xsd
	python ../../utils/units2rst.py ../../nxdlTypes.xsd > $@

nxdl_desc.rst: ../../utils/nxdl_desc2rst.py ../../nxdl.xsd
	python ../../utils/nxdl_desc2rst.py ../../nxdl.xsd > $@

clean ::
	$(RM) types.table units.table nxdl_desc.rst
	$(MAKE) clean -C $(SUBDIRS)

SUBDIRS = classes

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@
