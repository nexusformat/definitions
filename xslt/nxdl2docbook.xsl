<?xml version="1.0" encoding="UTF-8"?>

<!--
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

<xsl:stylesheet
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	version="1.0"
	xmlns:nx="http://definition.nexusformat.org/schema/3.1"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <xsl:output method="xml" indent="yes" version="1.0" encoding="UTF-8"/>

    <!-- 
        +++++++++++++++++
          grouping keys
        +++++++++++++++++
    -->

    <!-- identify all group elements by @type for the include statements -->
    <!-- advice: http://sources.redhat.com/ml/xsl-list/2000-07/msg00458.html -->
    <xsl:key name="group-include" match="//nx:group" use="@type"/>
    

    <!-- 
        +++++++++++++++++
        matched templates
        +++++++++++++++++
    -->
    
    
    <xsl:template match="/">

<xsl:comment>
##########################################################
######	 This XML file was auto-generated from      ######
######	 an NXDL file by an XSLT transformation.    ######
######	 Do NOT edit this XML Schema file.          ######
##########################################################
</xsl:comment>

        <xsl:element name="xs:schema">
            <xsl:attribute name="nx:xslt_name">nxdl2xsd.xsl</xsl:attribute>
            <xsl:attribute name="nx:xslt_id">$Id$</xsl:attribute>
            <!-- XSLT v2.0 feature: <xsl:attribute name="nx:xsd_created"><xsl:value-of select="fn:current-dateTime()" /></xsl:attribute>-->
            <xsl:attribute name="targetNamespace">http://definition.nexusformat.org/schema/3.1</xsl:attribute>
            <!--<xsl:attribute name="elementFormDefault">qualified</xsl:attribute>-->
            <!--<xsl:attribute name="attributeFormDefault">qualified</xsl:attribute>-->
            <!-- special case for nx:attribute elements because they have to come before documentation -->
            <xsl:for-each select="nx:attribute">
                <xsl:attribute name="{name()}"><xsl:value-of select="."/></xsl:attribute>
                <xsl:apply-templates select="*"/>
            </xsl:for-each>
            <xsl:comment><!-- NeXus license comes next -->
# NeXus - Neutron, X-ray, and Muon Science Common Data Format
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
            </xsl:comment>
		    <xsl:apply-templates select="nx:definition"/>
		</xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:definition">
        <xsl:element name="section">
            <xsl:element name="title"><xsl:value-of select="@name"/></xsl:element>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
 
</xsl:stylesheet>
