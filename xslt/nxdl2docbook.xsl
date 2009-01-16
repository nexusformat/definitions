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

    <!-- identify all group elements by @type -->
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
            <!-- ...................................................... -->
            <xsl:element name="variablelist">
                 <xsl:element name="varlistentry"><!-- show the SVN Id of the NXDL instance -->
                    <xsl:element name="term">SVN Id</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:element name="para">
                            <!-- strip the $ signs so SVN does not change the SVN Id in the target DocBook XML file -->
                            <xsl:value-of select="substring-before(substring-after(@svnid,'$'),'$')"/>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry"><!-- show where to find the source -->
                    <xsl:element name="term">NXDL source</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:element name="para">
                            <xsl:element name="link">
                                <xsl:attribute name="xlink:href">
                                    http://svn.nexusformat.org/definitions/trunk/base_classes/<xsl:value-of select="@name"/>.nxdl.xml
                                </xsl:attribute>
                                <xsl:value-of select="@name"/>
                            </xsl:element>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry"><!-- show how to learn more about NXDL -->
                    <xsl:element name="term">NeXus Definitional Language</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:element name="para">
                            <xsl:element name="link">
                                <xsl:attribute name="xlink:href">http://www.nexusformat.org/NXDL</xsl:attribute>
                                NXDL
                            </xsl:element>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry"><!-- show what this class extends -->
                    <xsl:element name="term">extends class:</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:choose>
                            <xsl:when test="@extends='../nxdl'">
                                <xsl:element name="para">NeXus base class</xsl:element>
                            </xsl:when>
                            <xsl:otherwise>
                                <xsl:element name="para"><xsl:value-of select="@extends"/></xsl:element>
                            </xsl:otherwise>
                        </xsl:choose>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry"><!-- show other classes included by this class -->
                    <xsl:element name="term">other classes included:</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:apply-templates 
                            mode="group-include"
                            select="  //nx:group[generate-id(.) = generate-id(key('group-include', @type)[1])]  " >
                            <!-- advice: http://sources.redhat.com/ml/xsl-list/2000-07/msg00458.html -->
                            <!-- Muenchian method to sort+unique on group/@type -->
                            <xsl:sort select="@type"/>
                        </xsl:apply-templates>
                        <xsl:element name="para">
                            <!-- should code against this situation instead -->
                            <xsl:comment>formatting placeholder in case this list is empty</xsl:comment>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry"><!-- doc element of this class -->
                    <xsl:element name="term">documentation</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:for-each select="nx:doc">
                            <xsl:element name="literallayout"><xsl:copy-of select="node()"/></xsl:element><!-- para -->
                        </xsl:for-each>
                        <xsl:element name="para">
                            <!-- should code against this situation instead (missing documentation: NXdisk_chopper) -->
                            <xsl:comment>formatting placeholder in case this list is empty</xsl:comment>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
            </xsl:element><!-- variablelist -->
            <!-- ...................................................... -->
            <xsl:element name="table"><!-- describe what is defined -->
                <xsl:element name="title">Tabular representation of <xsl:value-of select="@name"/>:</xsl:element>
                <xsl:element name="tgroup">
                    <xsl:attribute name="cols">5</xsl:attribute>
                    <xsl:element name="thead">
                        <xsl:element name="row">
                            <xsl:element name="entry">Name</xsl:element>
                            <xsl:element name="entry">Type</xsl:element>
                            <xsl:element name="entry">Description</xsl:element>
                            <xsl:element name="entry">Units</xsl:element>
                            <xsl:element name="entry">Attributes</xsl:element>
                        </xsl:element><!-- row -->
                    </xsl:element><!-- thead -->
                    <xsl:element name="tbody">
                        <xsl:apply-templates select="nx:field|nx:group" mode="tableRow"/><!-- row -->
                    </xsl:element><!-- tbody -->
                </xsl:element><!-- tgroup -->
            </xsl:element><!-- table -->
            <!-- ...................................................... -->
        </xsl:element><!-- section -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:field|nx:group" mode="tableRow">
        <xsl:call-template name="tableRowNTDUA">
            <xsl:with-param name="name"><xsl:value-of select="@name"/></xsl:with-param>
            <xsl:with-param name="type">
                <xsl:choose>
                    <xsl:when test="name()='group'">
                        <!-- this does not work in this context -->
                        <xsl:element name="link">
                            <xsl:attribute name="xlink:href">
                                http://www.nexusformat.org/<xsl:value-of select="@type"/>
                            </xsl:attribute>
                            <xsl:value-of select="@type"/>
                        </xsl:element>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="@type"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:with-param>
            <xsl:with-param name="desc"><xsl:copy-of select="nx:doc"/></xsl:with-param>
            <xsl:with-param name="units"><xsl:value-of select="@units"/></xsl:with-param>
            <!-- next line does not work correctly -->
            <xsl:with-param name="attr"><xsl:apply-templates select="nx:attribute"/></xsl:with-param>
        </xsl:call-template><!-- row -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:attribute">
        <xsl:comment><xsl:value-of select="count(.)"/></xsl:comment>
        <xsl:element name="para">
            <xsl:comment> A new para? </xsl:comment>
            @<xsl:value-of select="@name"/> 
            (<xsl:value-of select="@type"/>):
            <xsl:copy-of select="nx:doc"/>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:group" mode="group-include">
        <!-- show a class included by this class  -->
        <!-- http://www.nexusformat.org/NXclassname -->
        <xsl:element name="para">
            <xsl:element name="link">
                <xsl:attribute name="xlink:href">
                    http://www.nexusformat.org/<xsl:value-of select="@type"/>
                </xsl:attribute>
                <xsl:value-of select="@type"/>
            </xsl:element>
        </xsl:element>
    </xsl:template>
    
    <!-- 
        +++++++++++++++
        named templates
        +++++++++++++++
    -->
    
    <xsl:template name="tableRowNTDUA" mode="tableRow">
        <xsl:param name="name"/>
        <xsl:param name="type"/>
        <xsl:param name="desc"/>
        <xsl:param name="units"/>
        <xsl:param name="attr"/>
        <!-- add a row to the open table -->
        <xsl:element name="row">
            <xsl:element name="entry"><xsl:value-of select="$name"/></xsl:element>
            <xsl:element name="entry"><xsl:value-of select="$type"/></xsl:element>
            <xsl:element name="entry"><xsl:value-of select="$desc"/></xsl:element>
            <xsl:element name="entry"><xsl:value-of select="$units"/></xsl:element>
            <xsl:element name="entry"><xsl:value-of select="$attr"/></xsl:element>
        </xsl:element><!-- row -->
    </xsl:template>

    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
 
</xsl:stylesheet>
