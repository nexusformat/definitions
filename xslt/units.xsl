<?xml version="1.0" encoding="UTF-8" ?>
<!--
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

Purpose:
	This stylesheet is used to translate the NeXus Definition Language
	base class specifications into an HTML file showing various
	units declarations.

Usage:
	xsltproc units.xsl $(NX_CLASS).nxdl >> units.html

-->

<xs:stylesheet version="1.0"
	xmlns:xs="http://www.w3.org/1999/XSL/Transform" 
	xmlns:nx="http://www.nexusformat.org"
	xmlns:fn="http://www.w3.org/2005/02/xpath-functions">

	<!-- http://www.w3schools.com/xsl/xsl_transformation.asp -->

	<xs:output method="html" omit-xml-declaration="yes" indent="yes" />

	<xs:template match="/">
		<table border="2">
			<caption style="color: white; background: black;">
				<xs:value-of select="/nx:definition/@name" />
			</caption>
			<tr>
				<th>parent</th>
				<th>field</th>
				<th>type</th>
				<th>units</th>
			</tr>
			<xs:for-each select="//nx:field/@units">
				<tr>
					<td>
						<xs:value-of select="../../@name" />
					</td>
					<td>
						<xs:value-of select="../@name" />
					</td>
					<td>
						<xs:value-of select="../@type" />
					</td>
					<td>
						<xs:value-of select="." />
					</td>
				</tr>
			</xs:for-each>
		</table>
	</xs:template>

</xs:stylesheet>
