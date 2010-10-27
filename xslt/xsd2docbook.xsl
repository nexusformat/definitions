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
	nxdl.xsd schema into an DocBook (.xml) file for use in
	part of the NXDL chapter.

Usage:
    xsltproc $(XSLT_PATH)/xsd2docbook.xsl ../nxdl.xsd > nxdl_xsd.xml
-->

<xsl:stylesheet
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	version="1.0"
	xmlns:nx="http://definition.nexusformat.org/nxdl/3.1"
	xmlns:xi="http://www.w3.org/2001/XInclude"
	xmlns:xlink="http://www.w3.org/1999/xlink" 
	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    >

    <!-- 
        The CDATA section does not work the same when this XSLT is "xsl:import"ed.
        Modify the Python code to provide the proper syntax.
     -->
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
        <!-- Needs this on 2nd line of XML file: 
            <?oxygen RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"?>
        -->
        <xsl:processing-instruction 
            name="oxygen">RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"</xsl:processing-instruction>
        <xsl:comment/><!-- tricks XSLT to start a new line -->
        <xsl:comment/><!-- tricks XSLT to start a new line -->
        
      <xsl:comment>###########################################################</xsl:comment>
      <xsl:comment>######    This XML file was auto-generated from      ######</xsl:comment>
      <xsl:comment>######    an NXDL file by an XSLT transformation.    ######</xsl:comment>
      <xsl:comment>######    Do NOT edit this DocBook XML file.         ######</xsl:comment>
      <xsl:comment>###########################################################</xsl:comment>
        
        <xsl:comment>There has been no effort to make this file easy to read for humans.</xsl:comment>
        
        <xsl:comment/><!-- tricks XSLT to start a new line -->

        <xsl:comment>
# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2010 NeXus International Advisory Committee (NIAC)
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
        </xsl:comment>
        
        <xsl:comment/><!-- tricks XSLT to start a new line -->
        
        <xsl:element name="section">
            <xsl:attribute name="xmlns">http://docbook.org/ns/docbook</xsl:attribute>
            <xsl:attribute name="xml:id">NXDL-xsd2docbook</xsl:attribute>
            <xsl:attribute name="version">5.0</xsl:attribute><!-- required, matches NeXusManual.xml -->
            <xsl:element name="title">Structures of the NXDL language</xsl:element>
            <xsl:element name="para">
                The text and figures of this section have been auto-generated from the 
                documentation and structures
                <indexterm>
                    <primary>NXDL</primary>
                    <secondary>structures</secondary>
                </indexterm>
                found in the
                XML Schema file (<code>nxdl.xsd</code>) that defines the rules for NXDL files.
            </xsl:element>
                
            <xsl:apply-templates select="xsd:schema"/>
    
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="xsd:schema">
        <!--<xsl:for-each select="xsd:element">
            <!-\- should only match the "definition" element -\->
            <xsl:element name="para">
                element: <xsl:value-of select="./@name"/>
                <xsl:apply-templates select="xsd:annotation/xsd:documentation"/>
            </xsl:element>
            </xsl:for-each>-->
        
        <xsl:for-each select="xsd:complexType">
            <xsl:if test="contains(./@name,'Type')">
                <!-- TODO Don't forget the index entries -->
                <xsl:call-template name="doSection">
                    <xsl:with-param name="short"
                        ><xsl:value-of select="substring-before(./@name,'Type')"
                    /></xsl:with-param>
                </xsl:call-template>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template name="doSection">
        <xsl:param name="short"/>
        <xsl:element name="section">
            <xsl:element name="title"
                >NXDL <code><xsl:value-of select="$short"
                /></code> structure</xsl:element>
            <!-- first, the element documentation -->
            <xsl:apply-templates select="xsd:annotation/xsd:documentation" mode="typeDocs">
                <xsl:with-param name="short"
                    ><xsl:value-of select="$short"
                    /></xsl:with-param>
            </xsl:apply-templates>
            <indexterm>
                <primary>NXDL</primary>
                <secondary>structures</secondary>
                <tertiary><xsl:value-of select="$short" /></tertiary>
            </indexterm>
            <!-- now the attributes' documentation -->
            <xsl:choose>
                <xsl:when test="$short='field'">
                    <para>
                    <code>field</code> attributes are buried in a <code>complexContent</code> node
                    and will take more work to extract automatically.</para>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:if test="count(xsd:attribute)">
                      <xsl:element name="variablelist">
                          <xsl:apply-templates select="xsd:attribute" mode="attributeDocs">
                              <!-- TODO Don't forget the index entries -->
                             <xsl:with-param name="short"
                                 ><xsl:value-of select="$short"
                                 /></xsl:with-param>
                         </xsl:apply-templates>
                      </xsl:element>
                  </xsl:if>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="xsd:documentation" mode="typeDocs">
        <!-- pull out all the documentation -->
        <xsl:param name="short"/>
        <xsl:element name="para"
            ><xsl:copy-of select="node()"
            /></xsl:element>
        <!-- show the structure diagram -->
        <xsl:choose>
            <!-- TODO Don't forget the index entries -->
            <xsl:when test="$short='dims'"/><!-- do nothing -->
            <xsl:when test="$short='enumItem'"/><!-- do nothing -->
            <xsl:otherwise>
                <xsl:element name="figure">
                    <xsl:attribute name="xml:id"
                        >fig.nxdl.<xsl:value-of select="$short"
                        /></xsl:attribute>
                    <xsl:element name="title"
                        >Graphical representation of the NXDL <code
                        ><xsl:value-of select="$short"/></code> element</xsl:element>
                    <xsl:element name="mediaobject">
                        <xsl:element name="imageobject">
                            <xsl:element name="imagedata">
                                <xsl:attribute name="fileref"
                                    ><xsl:value-of 
                                        select="concat('img/nxdl/nxdl_xsd_Element_nx_',$short,'.jpg')"
                                    /></xsl:attribute>
                                <xsl:attribute name="width">200pt</xsl:attribute>
                                <xsl:attribute name="scalefit">1</xsl:attribute>
                            </xsl:element>
                        </xsl:element>
                    </xsl:element>
                </xsl:element>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="xsd:documentation" mode="attributeDocs">
        <xsl:param name="short"/>
        <!-- TODO Don't forget the index entries -->
        <varlistentry>
            <term>@<xsl:value-of 
                select="parent::xsd:annotation/parent::xsd:attribute/@name"
            /></term>
            <listitem>
                <para><xsl:copy-of select="node()"
                /></para>
            </listitem>
        </varlistentry>
    </xsl:template>
    
</xsl:stylesheet>
