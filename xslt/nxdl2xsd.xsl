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
	xmlns:xmlns="http://www.w3.org/2001/XMLSchema"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns:nxdl="http://www.nexusformat.org"
	xmlns:nx="http://definition.nexusformat.org/schema/3.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:fn="http://www.w3.org/2005/02/xpath-functions">

	<!-- http://www.w3schools.com/xsl/xsl_transformation.asp -->

	<xsl:output method="xml" indent="yes" version="1.0" encoding="UTF-8" />

	<!-- root element is complete except for a few headers/comments/disclaimers -->
	<xsl:template match="/">
		<xsl:comment>
			This xsd file was auto-generated from an NXDL file by an XSLT transformation.
			Do NOT edit this XML Schema file.
		</xsl:comment>
		<xsl:element name="xs:schema" >
			<!-- 
			  define nx:{something} here so the "nx" namespace prefix will be 
			  added automatically to the schema element declaration
			  Perhaps this might be useful to define a nx:version here?
			-->
			<xsl:attribute name="nx:name">NXDL-Schema</xsl:attribute>
			<xsl:attribute name="nx:version"> $Id: <!-- SVN ID --></xsl:attribute>
			<xsl:attribute name="targetNamespace">http://definition.nexusformat.org/schema/3.0</xsl:attribute>
			<xsl:attribute name="elementFormDefault">qualified</xsl:attribute>
			<xsl:comment>The NXDL extends the <xsl:value-of select="./*/@extends" /> class</xsl:comment>
			<xsl:element name="xs:include" >
				<xsl:attribute name="schemaLocation"><xsl:value-of select="./*/@extends" />.xsd</xsl:attribute>
			</xsl:element>
			<xsl:comment>These classes were called out in group elements from the NXDL</xsl:comment>
			<xsl:for-each select="//nxdl:group">
				<xsl:element name="xs:include" >
					<xsl:attribute name="schemaLocation"><xsl:value-of select="@type" />.xsd</xsl:attribute>
				</xsl:element>
			</xsl:for-each>
			<xsl:comment> +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ </xsl:comment>
			<xsl:apply-templates select="*"/> 
		</xsl:element>
	</xsl:template>

	<!-- nxdl:definition is complete -->
	<xsl:template match="nxdl:definition">
		<xsl:element name="xs:complexType" >
			<xsl:attribute name="name" >type_<xsl:value-of select="@name" /></xsl:attribute>
			<xsl:element name="xs:sequence" >
				<xsl:apply-templates select="*"/>
			</xsl:element>
		</xsl:element>
	</xsl:template>

	<!-- nxdl:field needs work -->
	<xsl:template match="nxdl:field">
		<xsl:element name="xs:element" >
			<xsl:attribute name="name" ><xsl:value-of select="@name" /></xsl:attribute>
			<xsl:attribute name="type" >nx:type_<xsl:value-of select="@type" /></xsl:attribute>
			<!-- 
			This is NOT the place to put the units.
			Put it in an attribute element after the sequence
			<xsl:if test="@units!=''">
				<xsl:attribute name="units" ><xsl:value-of select="@units" /></xsl:attribute>
			</xsl:if>
			-->
			<xsl:apply-templates select="*"/>
		</xsl:element>
	</xsl:template>

	<!-- nxdl:group needs work, mostly complete -->
	<xsl:template match="nxdl:group">
		<xsl:element name="xs:element" >
			<xsl:attribute name="name" ><xsl:value-of select="@name" /></xsl:attribute>
			<xsl:attribute name="type" >nx:type_<xsl:value-of select="@type" /></xsl:attribute>
			<xsl:choose>
				<!-- every xs:element needs a name, make a choice -->
				<xsl:when test="@name!=''">
					<!-- name is given in the NXDL -->
					<xsl:attribute name="name" ><xsl:value-of select="@name" /></xsl:attribute>
				</xsl:when>
				<xsl:otherwise>
					<!-- use @type as the name -->
					<xsl:attribute name="name" ><xsl:value-of select="@type" /></xsl:attribute>
				</xsl:otherwise>
			</xsl:choose>
			<!-- Can the next two attributes be more efficient? -->
			<xsl:if test="@minOccurs!=''">
				<xsl:attribute name="minOccurs" ><xsl:value-of select="@minOccurs" /></xsl:attribute>
			</xsl:if>
			<xsl:if test="@maxOccurs!=''">
				<xsl:attribute name="maxOccurs" ><xsl:value-of select="@maxOccurs" /></xsl:attribute>
			</xsl:if>
			<xsl:apply-templates select="*"/>
		</xsl:element>
	</xsl:template>

	<!-- nxdl:attribute needs work -->
	<xsl:template match="nxdl:attribute">
		<xsl:comment><xsl:value-of select="name()" />: <xsl:value-of select="@name" /></xsl:comment>
	</xsl:template>

	<!-- nxdl:dimensions needs work -->
	<xsl:template match="nxdl:dimensions">
		<xsl:comment><xsl:value-of select="name()" />: <xsl:value-of select="." /></xsl:comment>
	</xsl:template>

	<!-- nxdl:enumeration needs work -->
	<xsl:template match="nxdl:enumeration">
		<xsl:comment><xsl:value-of select="name()" /></xsl:comment>
	</xsl:template>

	<!-- nxdl:doc is complete -->
	<xsl:template match="nxdl:doc">
		<xsl:element name="xs:annotation" >
			<xsl:element name="xs:documentation" >
				<xsl:value-of select="." />
			</xsl:element>
		</xsl:element>
	</xsl:template>

</xsl:stylesheet>
