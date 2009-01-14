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
	specifications into DocBook (.xml) files for use in
	assembling NeXus about the class definitions from NXDL.

Usage:
    xsltproc -o $(NX_CLASS).xml  nxdl2docbook.xsl $(NX_CLASS).nxdl.xml
-->

<xsl:stylesheet
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	version="1.0"
	xmlns:nx="http://definition.nexusformat.org/schema/3.1"
	xmlns:xi="http://www.w3.org/2001/XInclude"
	xmlns:xlink="http://www.w3.org/1999/xlink"
    >

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
        <xsl:processing-instruction name="oxygen">RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"</xsl:processing-instruction>

        <xsl:comment/><!-- Puts the ID string on a new line. -->
        <xsl:comment><xsl:text> $</xsl:text>Id: <xsl:text>$ </xsl:text></xsl:comment>
<xsl:comment>
##########################################################
######	 This XML file was auto-generated from      ######
######	 an NXDL file by an XSLT transformation.    ######
######	 Do NOT edit this DocBook XML file.         ######
##########################################################
</xsl:comment>

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
        <!-- Needs this on 2nd line of XML file: 
            <?oxygen RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"?>
        -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:definition">
        <xsl:element name="section"><!-- root element -->
            <xsl:attribute name="xmlns">http://docbook.org/ns/docbook</xsl:attribute>
            <!-- 
                These namespaces will be added to the document (by xsltproc) if they are used.
                xmlns:xi="http://www.w3.org/2001/XInclude"
                xmlns:xlink="http://www.w3.org/1999/xlink"
            -->
            <xsl:attribute name="version">5.0</xsl:attribute><!-- required, matches NeXusManual.xml -->
            <xsl:element name="title"><xsl:value-of select="@name"/></xsl:element>
            <!-- show where to find the source -->
            <xsl:element name="para">
                <xsl:value-of select="@name"/> source:
                <xsl:element name="link">
                    <xsl:attribute name="xlink:href">http://svn.nexusformat.org/definitions/trunk/base_classes/<xsl:value-of select="@name"/>.nxdl.xml</xsl:attribute>
                    http://svn.nexusformat.org/definitions/trunk/base_classes/<xsl:value-of select="@name"/>.nxdl.xml
                </xsl:element>
            </xsl:element><!-- para -->
            <!-- show how to learn more about NXDL -->
            <xsl:element name="para">
                NXDL description:
                <xsl:element name="link">
                    <xsl:attribute name="xlink:href">http://www.nexusformat.org/NXDL</xsl:attribute>
                    NXDL: NeXus Definitional Language
                </xsl:element>
            </xsl:element>
            <!-- describe what is defined -->
            <xsl:element name="table">
                <xsl:element name="title">Tabular representation of <xsl:value-of select="@name"/>:</xsl:element>
                <xsl:element name="tgroup">
                    <xsl:attribute name="cols">4</xsl:attribute>
                    <xsl:element name="thead">
                        <xsl:element name="row">
                            <xsl:element name="entry">Name</xsl:element>
                            <xsl:element name="entry">Type</xsl:element>
                            <xsl:element name="entry">Description</xsl:element>
                            <xsl:element name="entry">Attributes</xsl:element>
                        </xsl:element><!-- row -->
                    </xsl:element><!-- thead -->
                    <xsl:element name="tbody">
                        <xsl:element name="row">
                            <xsl:element name="entry">Name content</xsl:element>
                            <xsl:element name="entry">Type content</xsl:element>
                            <xsl:element name="entry">Description content</xsl:element>
                            <xsl:element name="entry">Attributes content</xsl:element>
                        </xsl:element><!-- row -->
                    </xsl:element><!-- thead -->
                </xsl:element><!-- tgroup -->
            </xsl:element><!-- table -->
        </xsl:element><!-- section -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
 
</xsl:stylesheet>
