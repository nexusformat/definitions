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
#	make all	builds docbook
#	make clean	removes files built in this directory
#	make rebuild	does a make clean then make all

BASE_CLASSES  = NXaperture NXattenuator NXbeam NXbeam_stop NXbending_magnet 
BASE_CLASSES += NXcharacterization NXcollimator NXcrystal NXdata NXdetector NXdetector_group
BASE_CLASSES += NXdisk_chopper NXentry NXenvironment NXevent_data NXfermi_chopper 
BASE_CLASSES += NXfilter NXflipper NXgeometry NXguide NXinsertion_device NXinstrument 
BASE_CLASSES += NXlog NXmirror NXmoderator NXmonitor NXmonochromator NXnote 
BASE_CLASSES += NXorientation NXpolarizer NXpositioner NXprocess NXroot NXsample 
BASE_CLASSES += NXsensor NXshape NXsource NXtranslation NXuser NXvelocity_selector 

EXTENSION = xml
TARGETS =  $(BASE_CLASSES:%= %.xml)
NXDL = $(BASE_CLASS_PATH)/%.nxdl.xml

XSLT_PATH = ../xslt

XSLT = $(XSLT_PATH)/nxdl2docbook.xsl

# === Rules ===

docbook : $(TARGETS)

all: docbook

#  docbook2html -d docbook-utils.dsl#html myfile.docbook

%.xml: $(NXDL) Makefile $(XSLT)
	xsltproc -o $@ $(XSLT) $<

clean ::
	/bin/rm -f $(TARGETS)

rebuild :: clean all
