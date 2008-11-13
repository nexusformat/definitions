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
	specifications into XML Schema (.xsd) files for use in
	validating candidate NeXus data files and also in preparing
	additional application definitions and XML schemas for use by NeXus.

Usage:
	xsltproc nxdl2xsd.xsl $(NX_CLASS).nxdl > $(NX_CLASS).xsd

-->

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:nx="http://www.nexusformat.org"
	xmlns:fn="http://www.w3.org/2005/02/xpath-functions">

	<!-- http://www.w3schools.com/xsl/xsl_transformation.asp -->

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" />

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

<!-- no indentation for this template -->
<xsl:template match="/">
<xsl:comment>
<xsl:text>
</xsl:text>
<xsl:value-of select="/nx:definition/nx:doc" />
<xsl:text>
</xsl:text>
extends: <xsl:value-of select="/nx:definition/@extends" />
<xsl:text>
</xsl:text>
</xsl:comment>
<xsl:apply-templates select="*" />
</xsl:template>

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

<!-- no indentation for this template -->
<xsl:template match="nx:definition">
<xsl:text>
</xsl:text>
<xsl:element name="{@name}">
<xsl:attribute name="name" />
<!-- Do not forget attribute elements! -->
<xsl:apply-templates select="nx:attribute" />
<xsl:apply-templates select="*" />
<xsl:text>
</xsl:text>
</xsl:element>
</xsl:template>

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

	<xsl:template match="nx:field">
		<xsl:text>
		</xsl:text>
		<xsl:element name="{@name}">
			<xsl:attribute name="type">
				<xsl:value-of select="@type" />
				<xsl:if test="nx:dimensions!=''">[<xsl:value-of select="nx:dimensions" />]</xsl:if>
			</xsl:attribute>
			<xsl:if test="@units!=''">
				<xsl:attribute name="units">
					<xsl:value-of select="@units" />
				</xsl:attribute>
			</xsl:if>
			<!-- Do not forget attribute elements! -->
			<xsl:apply-templates select="nx:attribute" />
			<!-- Do not forget enumeration elements! -->
			<xsl:if test="nx:doc!=''">
				{<xsl:value-of select="nx:doc" />}
			</xsl:if>
			<xsl:if test="nx:enumeration!=''">
				<!-- leave next line unbroken -->
				{<xsl:for-each select="nx:enumeration/nx:item"><xsl:if test="position()>1"> | </xsl:if>"<xsl:value-of select="@value" />"<xsl:if test=".!=''"> (<xsl:value-of select="." />)</xsl:if></xsl:for-each>}
			</xsl:if>
		</xsl:element>
	</xsl:template>

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

	<!-- prevent default match from generating output -->
	<xsl:template match="nx:doc" />

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

	<!-- no further indentation for this template -->
	<xsl:template match="nx:attribute">
		<xsl:attribute name="{@name}"><xsl:if test="nx:enumeration!=''"><xsl:value-of select="nx:enumeration/nx:item[1]/@value" /></xsl:if><xsl:if test="nx:enumeration=''"><xsl:value-of select="." /></xsl:if></xsl:attribute>
	</xsl:template>

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

	<xsl:template match="nx:group">
		<xsl:text>
		</xsl:text>
		<xsl:element name="{@type}">
			<!-- name will be empty if @name is undefined - that is OK -->
			<xsl:attribute name="name"><xsl:value-of select="@name" /></xsl:attribute>
			<!-- Do not forget attribute elements! -->
			<xsl:apply-templates select="nx:attribute" />
			<xsl:if test="nx:doc!=''">
				{<xsl:value-of select="nx:doc" />}
			</xsl:if>
			<xsl:if test="@minOccurs!=''">
				<xsl:comment>minOccurs = <xsl:value-of select="@minOccurs" /></xsl:comment>
			</xsl:if>
			<xsl:if test="@maxOccurs!=''">
				<xsl:comment>maxOccurs = <xsl:value-of select="@maxOccurs" /></xsl:comment>
			</xsl:if>
		</xsl:element>
	</xsl:template>

<!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

</xsl:stylesheet>
