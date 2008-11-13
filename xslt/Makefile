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
#	make xsd	builds all XML Schemas from NeXus base class NXDL files
#	make metaDTD	builds all metaDTD from NeXus base class NXDL files for comparison with existing metaDTD files
#	make all	builds xsd, metaDTD, and tables
#	make tables	builds units.html and dimensions.html
#	make clean	removes files built in this directory
#	make rebuild	does a make clean then make all

BASE_CLASSES  = NXaperture NXattenuator NXbeam NXbeam_stop NXbending_magnet 
BASE_CLASSES += NXcharacterization NXcollimator NXcrystal NXdata NXdetector 
BASE_CLASSES += NXdisk_chopper NXentry NXenvironment NXevent_data NXfermi_chopper 
BASE_CLASSES += NXfilter NXflipper NXgeometry NXguide NXinsertion_device NXinstrument 
BASE_CLASSES += NXlog NXmirror NXmoderator NXmonitor NXmonochromator NXnote 
BASE_CLASSES += NXorientation NXpolarizer NXpositioner NXprocess NXroot NXsample 
BASE_CLASSES += NXsensor NXshape NXsource NXtranslation NXuser NXvelocity_selector 

BASE_CLASS_PATH = ../base_classes

XSDS =  $(BASE_CLASSES:%= %.xsd)
META_DTDS =  $(BASE_CLASSES:%= %.metaDTD.xml)

all: xsd metaDTD tables

xsd nxdl2xsd : $(XSDS)

metaDTD nxdl2metaDTD : $(META_DTDS)

%.xsd: $(BASE_CLASS_PATH)/%.nxdl.xml Makefile nxdl2xsd.xsl
	xsltproc nxdl2xsd.xsl $< > $@

%.metaDTD.xml: $(BASE_CLASS_PATH)/%.nxdl.xml Makefile nxdl2metaDTD.xsl
	xsltproc nxdl2metaDTD.xsl $< > $@
	diff -bByW 200 $(BASE_CLASS_PATH)/$*.xml $@ || echo "# ++++++++++++++++++++++++++ #"

tables ::
	/bin/tcsh ./tables.csh

clean ::
	/bin/rm -f $(XSDS) $(META_DTDS) units.html dimensions.html

rebuild :: clean all
