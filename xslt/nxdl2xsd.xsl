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
	xmlns:nxsd="http://definition.nexusformat.org/schema/3.1"
	xmlns:nxdl="http://definition.nexusformat.org/nxdl/3.1"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <xsl:output method="xml" indent="yes" version="1.0" encoding="UTF-8"/>

    <!-- 
        +++++++++++++++++
          grouping keys
        +++++++++++++++++
    -->

    <!-- identify all group elements by @type for the include statements -->
    <!-- advice: http://sources.redhat.com/ml/xsl-list/2000-07/msg00458.html -->
    <xsl:key name="group-include" match="//nxdl:group" use="@type"/>

    <xsl:key name="def-name" match="//nxdl:definition" use="@name"/>
    <xsl:key name="def-extends" match="//nxdl:definition" use="@extends"/>
    <xsl:key name="def-restricts" match="//nxdl:definition" use="@restricts"/>    

    <xsl:key name="link-target" match="//nxdl:link" use="@target"/>
    
    <!-- 
        +++++++++++++++++
        matched templates
        +++++++++++++++++
    -->
    
        
    <xsl:template match="/">

<xsl:comment>
##########################################################
######	 This xsd file was auto-generated from      ######
######	 an NXDL file by an XSLT transformation.    ######
######	 Do NOT edit this XML Schema file.          ######
##########################################################
</xsl:comment>

        <xsl:element name="xs:schema">
            <xsl:attribute name="nxdl:xslt_name">nxdl2xsd.xsl</xsl:attribute>
            <xsl:attribute name="nxdl:xslt_id">$Id$</xsl:attribute>
            <!-- XSLT v2.0 feature: <xsl:attribute name="nxdl:xsd_created"><xsl:value-of select="fn:current-dateTime()" /></xsl:attribute>-->
            <xsl:attribute name="targetNamespace">http://definition.nexusformat.org/schema/3.1</xsl:attribute>
            <xsl:attribute name="elementFormDefault">qualified</xsl:attribute>
            <xsl:attribute name="nxsd:something">1<!-- force the namespace to be present --></xsl:attribute>
            <!--<xsl:attribute name="attributeFormDefault">qualified</xsl:attribute>-->
            <!-- special case for nxdl:attribute elements because they have to come before documentation -->
            <xsl:for-each select="nxdl:attribute">
                <xsl:attribute name="{name()}"><xsl:value-of select="."/></xsl:attribute>
                <xsl:apply-templates select="*"/>
            </xsl:for-each>
            <xsl:element name="xs:annotation">
                <xsl:element name="xs:documentation"><!-- NeXus license comes next -->
# NeXus - Neutron, X-ray, and Muon Science Common Data Format
# 
# Copyright (C) 2008-2012 NeXus International Advisory Committee (NIAC)
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
                </xsl:element>
            </xsl:element>
	    <xsl:element name="xs:include">
	    <xsl:attribute name="schemaLocation">../NeXus.xsd</xsl:attribute>
	    </xsl:element>
        <!--
        <xsl:element name="xs:import">
            <xsl:attribute name="schemaLocation">../nxdlTypes.xsd</xsl:attribute>
            <xsl:attribute name="namespace">http://definition.nexusformat.org/nxdl/3.1</xsl:attribute>
            <xsl:element name="xs:annotation">
                <xsl:element name="xs:documentation"
                    >Definitions of the basic data types and unit types allowed in NXDL instance files.</xsl:element>
            </xsl:element>
        </xsl:element>
        -->
        <xsl:apply-templates select="//nxdl:field" mode="generate-types"/>
                
        <xsl:apply-templates select="//nxdl:definition"/>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nxdl:definition">
        <!-- identify all the XSD files to be included -->
	<xsl:variable name="baseClass">
	<xsl:choose>
	    <xsl:when test="@extends"><xsl:text>nxsd:</xsl:text><xsl:value-of select="@extends" /></xsl:when>
	    <xsl:when test="@restricts"><xsl:text>nxsd:</xsl:text><xsl:value-of select="@restricts" /></xsl:when>
	    <xsl:otherwise><xsl:text>nxsd:classSuperBaseType</xsl:text></xsl:otherwise>
	</xsl:choose>
	</xsl:variable>
        <xsl:variable name="extendType">
            <xsl:choose>
                <xsl:when test="@extends"><xsl:text>xs:extension</xsl:text></xsl:when>
                <xsl:when test="@restricts"><xsl:text>xs:restriction</xsl:text></xsl:when>
                <xsl:otherwise><xsl:text>xs:extension</xsl:text></xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:call-template name="groupIncludes" />
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">declarations (attributes, docs, groups, and fields)</xsl:with-param>
        </xsl:call-template>
        <xsl:element name="xs:complexType">
          <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
          <!--xsl:attribute name="mixed">true</xsl:attribute-->
          <xsl:element name="xs:complexContent">
           <xsl:element name="{$extendType}">
            <xsl:attribute name="base"><xsl:value-of select="$baseClass"/></xsl:attribute>
            <xsl:element name="xs:sequence">
                <!--<xsl:apply-templates select="*"/>-->    <!-- standard order for fields & groups from NXDL -->
                <xsl:call-template name="groupGroup">    <!-- special sort order for fields & groups -->
                    <xsl:with-param name="extendType" select="$extendType"/>
                    <xsl:with-param name="baseClass" select="substring-after($baseClass,':')"/>
                </xsl:call-template>
                <!-- fill in  missing fields from a restriction -->
                <xsl:variable name="bdef" select="key('def-name', substring-after($baseClass,':'))" />
                <xsl:variable name="cdef" select="." />
                <xsl:if test="$extendType = 'xs:restriction'">
                    <xsl:call-template name="add-inherited">
                        <xsl:with-param name="bdef" select="$bdef" />
                        <xsl:with-param name="cdef" select="$cdef" />
                        <xsl:with-param name="baseClass" select="substring-after($baseClass,':')" />
                    </xsl:call-template>
                </xsl:if>
            </xsl:element>
            <!--xsl:if test="count(nxdl:attribute/@name)=0">
                <xsl:element name="xs:attribute">
                    <xsl:attribute name="name">name</xsl:attribute>
                    <xsl:attribute name="use">optional</xsl:attribute>
                </xsl:element>
            </xsl:if-->
            <!-- special case: need to handle nxdl:attribute _after_ the sequence! -->
            <xsl:apply-templates select="nxdl:attribute" mode="after_sequence"/>
           </xsl:element>
         </xsl:element>
        </xsl:element>
    </xsl:template>
    
    <xsl:template name="add-inherited">
        <xsl:param name="bdef" />
        <xsl:param name="cdef" />
        <xsl:param name="baseClass" />
        
    <xsl:call-template name="comment">
        <xsl:with-param name="msg">begin inherited fields from <xsl:value-of select="$baseClass"/></xsl:with-param>
    </xsl:call-template>
    <xsl:for-each select="$bdef/nxdl:group">
        <xsl:sort select="@name"/>
        <xsl:sort select="@type"/>
        <xsl:variable name="ggg" select="string(@type)" />
        <xsl:choose>
            <xsl:when test="$cdef/nxdl:group[@type=$ggg]" />
            <xsl:otherwise>
                <xsl:apply-templates select="." />                                            
            </xsl:otherwise>
        </xsl:choose>
    </xsl:for-each>
        <xsl:for-each select="$bdef/nxdl:field">
            <xsl:sort select="@name"/>
            <xsl:variable name="ggg" select="string(@name)" />
            <xsl:choose>
                <xsl:when test="$cdef/nxdl:field[@name=$ggg]" />
                <xsl:otherwise>
                    <xsl:apply-templates select="." />                                            
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
        <xsl:for-each select="$bdef/nxdl:link">
            <xsl:sort select="@name"/>
            <xsl:variable name="ggg" select="string(@name)" />
            <xsl:choose>
                <xsl:when test="$cdef/nxdl:link[@name=$ggg]" />
                <xsl:otherwise>
                    <xsl:apply-templates select="." />                                            
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">end inherited fields from <xsl:value-of select="$baseClass"/></xsl:with-param>
        </xsl:call-template>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nxdl:doc">
        <!-- documentation -->
        <xsl:element name="xs:annotation">
            <xsl:element name="xs:documentation"><xsl:value-of select="."/></xsl:element>
        </xsl:element>
    </xsl:template>

    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nxdl:link">
        <xsl:element name="xs:element">
            <xsl:attribute name="name">NAPIlink</xsl:attribute>
            <xsl:element name="xs:complexType">
                <xsl:element name="xs:simpleContent">
                    <xsl:element name="xs:restriction">
                        <xsl:attribute name="base">nxsd:NAPIlinkType</xsl:attribute>
                        <xsl:element name="xs:attribute">
                            <xsl:attribute name="name">name</xsl:attribute>
                            <xsl:attribute name="use">required</xsl:attribute>
                            <xsl:attribute name="type">nxsd:validName</xsl:attribute>
                            <xsl:attribute name="fixed"><xsl:value-of select="@name"/></xsl:attribute>
                        </xsl:element>
                        <xsl:element name="xs:attribute">
                            <xsl:attribute name="name">target</xsl:attribute>
                            <xsl:attribute name="use">required</xsl:attribute>
                            <xsl:attribute name="type">nxsd:validTarget</xsl:attribute>
                            <xsl:attribute name="fixed"><xsl:value-of select="@target"/></xsl:attribute>
                        </xsl:element>
                    </xsl:element>
                 </xsl:element>   
            </xsl:element>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="nxdl:field">
        <!-- named element declaration -->
        <xsl:param name="extendType" />
        <xsl:param name="baseClass"/>
        
        <xsl:variable name="path_name">
            <xsl:call-template name="get_path_name" />
        </xsl:variable>
        
        <xsl:variable name="field_type" select="concat('nxsd:',$path_name)"/>
        
        <xsl:element name="xs:element">
            <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
            <xsl:attribute name="minOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@minOccurs)>0"><xsl:value-of select="@minOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>0</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="maxOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@maxOccurs)>0"><xsl:value-of select="@maxOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>1</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="type"><xsl:value-of select="$field_type"/></xsl:attribute>
            <xsl:call-template name="comment">
                <xsl:with-param name="msg"><xsl:value-of select="name()"/> declaration: <xsl:value-of select="@name"/></xsl:with-param>
            </xsl:call-template>
            <!-- documentation comes before the sequence -->
            <xsl:apply-templates select="nxdl:doc"/>
        </xsl:element>
    </xsl:template>

    <!-- generate a name from the absolute path to the element using _ to separate names -->
    <xsl:template name="get_path_name">
        <xsl:for-each select="ancestor-or-self::*">
            <xsl:choose>
                <xsl:when test="name()='definition'"><xsl:value-of select="@name"/></xsl:when>
                <xsl:when test="name()='field'"><xsl:value-of select="@name"/></xsl:when>
                <xsl:otherwise><xsl:value-of select="@type"/></xsl:otherwise>
            </xsl:choose>
            <xsl:if test="position() != last()">
                <xsl:text>_</xsl:text>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>
    
    <!-- old version of get_field_base_type just here for reference -->
    <xsl:template name="get_base_type_not_used">
        <xsl:for-each select="ancestor-or-self::*">
            <xsl:choose>
                <xsl:when test="name()='definition'">
                    <xsl:choose>
                        <xsl:when test="@restricts">
                            <xsl:value-of select="@restricts"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="@name"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="name()='field'"><xsl:value-of select="@name"/></xsl:when>
                <xsl:otherwise><xsl:value-of select="@type"/></xsl:otherwise>
            </xsl:choose>
            <xsl:if test="position() != last()">
                <xsl:text>_</xsl:text>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>
    
    <!-- if we are a restriction, work out what we are a restriction of and generate the
         name of that type. It assumes the same namimng convention for types
         used in "generate-types" 
    -->
    <xsl:template name="get_field_base_type">
        <xsl:text>_</xsl:text>
        <xsl:choose>
            <!-- field is part of <definition> -->
            <xsl:when test="name(..)='definition'">
                <xsl:choose>
                    <xsl:when test="../@restricts">
                        <xsl:value-of select="../@restricts"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="../@name"/>  
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:when>
            <!-- field is part of a <group> -->
            <xsl:otherwise><xsl:value-of select="../@type"/></xsl:otherwise>
        </xsl:choose>
        <xsl:text>_</xsl:text>
        <xsl:value-of select="@name"/>
    </xsl:template>
    
    <!-- search back up node tree to see if we are an extension of restriction of an existing type
          and the output the correst xsd directive -->
    <xsl:template name="get_inherit_type">
        <xsl:variable name="defnode" select="ancestor-or-self::*[name()='definition']" />
            <xsl:choose>
                <xsl:when test="$defnode/@extends"><xsl:value-of select="'xs:extension'"/></xsl:when>
                <xsl:when test="$defnode/@restricts"><xsl:value-of select="'xs:restriction'"/></xsl:when>
                <xsl:otherwise><xsl:text>unknown</xsl:text></xsl:otherwise>
            </xsl:choose>
    </xsl:template>   
    
    <xsl:template match="nxdl:field" mode="generate-types">
        <!-- named element declaration -->
        
        <xsl:variable name="field_type">
            <xsl:call-template name="get_path_name" />
        </xsl:variable>
        
        <xsl:variable name="inherit_type">
            <xsl:call-template name="get_inherit_type" />
        </xsl:variable>
        
        <xsl:variable name="base_type">
            <xsl:choose>
                <xsl:when test="$inherit_type = 'xs:restriction'">nxsd:<xsl:call-template name="get_field_base_type"/></xsl:when>
            </xsl:choose>            
        </xsl:variable>
                    
        <xsl:element name="xs:complexType">
            <xsl:attribute name="name"><xsl:value-of select="$field_type"/></xsl:attribute>
                    <xsl:choose>
                        <xsl:when test="count(nxdl:enumeration)>0">
                            <xsl:apply-templates select="nxdl:enumeration" mode="complex">
                                <xsl:with-param name="base_type" select="$base_type"/>
                            </xsl:apply-templates>
                        </xsl:when>
                        <xsl:otherwise><!-- no nxdl:enumeration -->
                            <xsl:element name="xs:simpleContent">
                                <xsl:element name="{$inherit_type}">
                                    <!-- @name is handled already -->
                                    <xsl:choose>
                                        <xsl:when test="$inherit_type = 'xs:restriction'">
                                            <xsl:attribute name="base"><xsl:value-of select="$base_type"/></xsl:attribute>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <xsl:call-template name="typeAttributeDefaultHandler" >
                                                <!-- handle @type attribute -->
                                                <xsl:with-param name="item">base</xsl:with-param>
                                            </xsl:call-template>
                                        </xsl:otherwise>
                                    </xsl:choose>                      
                                    <!-- need to handle the dimensions declaration -->
                                </xsl:element><!-- xs:extension -->
                            </xsl:element><!-- xs:simpleContent -->
                        </xsl:otherwise><!-- no nxdl:enumeration -->
                    </xsl:choose>
                    <xsl:call-template name="groupGroup"/>    <!-- special sort order for fields & groups -->
        </xsl:element><!-- xs:complexType -->
    </xsl:template>
    
    <xsl:template match="nxdl:group">
        <xsl:param name="extendType" select="'xs:extension'"/>
        <!-- reference to another NX object (requires that object's XSD) -->
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">group declaration</xsl:with-param>
        </xsl:call-template>
        <xsl:element name="xs:element">
            <xsl:attribute name="name">
                <xsl:choose>
                    <!-- @name was specified, use it (to avoid multiple elements with same name) -->
                    <xsl:when test="count(@name)>0"><xsl:value-of select="@name"/></xsl:when>
                    <!-- default -->
                    <xsl:otherwise><xsl:value-of select="@type"/></xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="minOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@minOccurs)>0"><xsl:value-of select="@minOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>0</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="maxOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@maxOccurs)>0"><xsl:value-of select="@maxOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>unbounded</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:choose>
                <xsl:when test="count(nxdl:link)+count(nxdl:field)+count(nxdl:group)>0">
                    <!-- if there are fields or groups, then documentation comes afterwards ?????(then why is it before?)????? -->
                    <xsl:apply-templates select="nxdl:doc"/>
                    <!-- fields or groups within this group element  -->
                    <xsl:comment> this is part of an <xsl:value-of select="@type"/> object </xsl:comment>
                    <xsl:element name="xs:complexType">
                    <!--xsl:attribute name="mixed">true</xsl:attribute-->
                    <xsl:element name="xs:complexContent">
                    <xsl:element name="{$extendType}">
                    <xsl:attribute name="base">
                      <xsl:text>nxsd:</xsl:text><xsl:value-of select="@type"/>
                    </xsl:attribute>
                        <xsl:element name="xs:sequence">
                            <xsl:apply-templates select="nxdl:group">
                                <xsl:with-param name="extendType" select="$extendType"></xsl:with-param>
                                <xsl:sort select="@name"/>
                                <xsl:sort select="@type"/>
                            </xsl:apply-templates>
                            <xsl:apply-templates select="nxdl:field|nxdl:link">
                                <xsl:with-param name="extendType" select="$extendType"></xsl:with-param>
                                <xsl:sort select="@name"/>
                            </xsl:apply-templates>
                            <!-- fill in missing inherited fields -->
                            <xsl:variable name="bdef" select="key('def-name', @type)" />
                            <xsl:variable name="cdef" select="." />
                            <xsl:if test="$extendType = 'xs:restriction'">
                                <xsl:if test="$extendType = 'xs:restriction'">
                                    <xsl:call-template name="add-inherited">
                                        <xsl:with-param name="bdef" select="$bdef" />
                                        <xsl:with-param name="cdef" select="$cdef" />
                                        <xsl:with-param name="baseClass" select="@type" />
                                    </xsl:call-template>
                                </xsl:if>
                            </xsl:if>
                        </xsl:element>
                        <xsl:if test="count(@name)>0">
                            <xsl:element name="xs:attribute">
                                <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
                            </xsl:element>
                        </xsl:if>
                    </xsl:element>
                    </xsl:element>
                    </xsl:element>
                </xsl:when>
                <xsl:when test="count(@name)>0">
                    <xsl:attribute name="type">nxsd:<xsl:value-of select="@type"/></xsl:attribute>
                </xsl:when>
                <xsl:otherwise>
                    <!-- no fields or groups within this group element -->
                    <xsl:call-template name="typeAttributeDefaultHandler" >
                        <xsl:with-param name="item">type</xsl:with-param>
                    </xsl:call-template>
                    <xsl:apply-templates select="nxdl:doc"/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="@units|@minOccurs|@maxOccurs">
        <xsl:attribute name="{name()}">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nxdl:enumeration" mode="standard">
        <xsl:param name="base_type" />
        <xsl:element name="xs:simpleType">
            <xsl:element name="xs:restriction">
                <xsl:attribute name="base">
                    <xsl:choose>
                        <xsl:when test="string-length($base_type) > 0"><xsl:value-of select="$base_type"/></xsl:when>
                        <!-- base or type was specified in the parent field -->
                        <xsl:when test="count(../@type)>0">nxsd:<xsl:value-of select="../@type"/></xsl:when>
                        <!-- default -->
                        <xsl:otherwise>nxsd:NX_CHAR</xsl:otherwise>
                    </xsl:choose>
                </xsl:attribute>
                <xsl:apply-templates select="nxdl:item" mode="field"/>
            </xsl:element>
        </xsl:element>
    </xsl:template>

    <xsl:template match="nxdl:enumeration" mode="complex">
        <xsl:param name="base_type" />
        <xsl:element name="xs:simpleContent">
            <xsl:element name="xs:restriction">
                <xsl:attribute name="base">
                    <xsl:choose>
                        <xsl:when test="string-length($base_type) > 0"><xsl:value-of select="$base_type"/></xsl:when>
                        <!-- base or type was specified in the parent field -->
                        <xsl:when test="count(../@type)>0">nxsd:<xsl:value-of select="../@type"/></xsl:when>
                        <!-- default -->
                        <xsl:otherwise>nxsd:NX_CHAR</xsl:otherwise>
                    </xsl:choose>
                </xsl:attribute>
                <xsl:apply-templates select="nxdl:item" mode="field"/>
            </xsl:element>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="nxdl:item" mode="field">
        <xsl:element name="xs:enumeration">
            <xsl:attribute name="value"><xsl:value-of select="@value"/></xsl:attribute>
        </xsl:element>
    </xsl:template>

    <xsl:template match="nxdl:dimensions" mode="field">
        <xsl:element name="xs:attribute">
            <xsl:attribute name="name">dimensions</xsl:attribute>
            <xsl:call-template name="typeAttributeDefaultHandler" >
                <xsl:with-param name="item">type</xsl:with-param>
            </xsl:call-template>
            <xsl:apply-templates select="nxdl:dimensions/nxdl:doc"/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="nxdl:attribute" mode="field">
        <xsl:element name="xs:attribute">
            <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
            <xsl:if test="count(nxdl:enumeration)=0">
                <xsl:call-template name="typeAttributeDefaultHandler" >
                    <xsl:with-param name="item">type</xsl:with-param>
                </xsl:call-template>
            </xsl:if>
            <xsl:apply-templates select="nxdl:doc"/>
            <xsl:apply-templates select="nxdl:enumeration" mode="standard"/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="nxdl:attribute" mode="after_sequence">
        <xsl:element name="xs:attribute">
            <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
            <xsl:apply-templates select="@*"/>
            <xsl:choose>
                <xsl:when test="count(nxdl:enumeration)>0">
                    <xsl:apply-templates select="nxdl:enumeration" mode="standard"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:apply-templates select="*"/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:element>
    </xsl:template>

    <xsl:template match="nxdl:group" mode="group-include">
        <!-- include the XSD from a group declared in the NXDL -->
    </xsl:template>
    
    <!-- 
        +++++++++++++++
        named templates
        +++++++++++++++
    -->

    <xsl:template name="comment">
        <xsl:param name="msg"/>
        <!-- put a comment into the XSD (usually before every declaration) -->
        <xsl:comment>+++++ <xsl:value-of select="$msg"/> +++++</xsl:comment>
    </xsl:template>
    
    <xsl:template name="groupIncludes">
        <!-- extends from this NeXus object -->
        <!-- ++++++++++++++++++++++++++++++++++++ -->
        <!-- ++++++++++++++++++++++++++++++++++++ -->
        <!-- ++++++++++++++++++++++++++++++++++++ -->
        <!-- calls these NeXus or application objects -->
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">other objects used by this NXDL</xsl:with-param>
        </xsl:call-template>

        <!-- Be sure to include XSD of any base_class or application elements that define this object -->
        <xsl:apply-templates 
            mode="group-include"
            select="  //nxdl:group[generate-id(.) = generate-id(key('group-include', @type)[1])]  " >
            <!-- advice: http://sources.redhat.com/ml/xsl-list/2000-07/msg00458.html -->
            <!-- Muenchian method to sort+unique on group/@type -->
            <xsl:sort select="@type"/>
        </xsl:apply-templates>
    </xsl:template>

    <xsl:template name="groupGroup">
        <xsl:param name="extendType" select="'xs:extension'"/>
        <xsl:param name="baseClass"/>
        <xsl:apply-templates select="nxdl:group">
            <xsl:with-param name="extendType" select="$extendType"/>
            <xsl:with-param name="baseClass" select="$baseClass"/>
            <xsl:sort select="@name"/><!-- then sort by field names -->
            <xsl:sort select="@type"/><!-- sort by group type -->
        </xsl:apply-templates>
        <xsl:apply-templates select="nxdl:field|nxdl:link">
            <xsl:with-param name="extendType" select="$extendType" />
            <xsl:with-param name="baseClass" select="$baseClass"/>
            <xsl:sort select="@name"/><!-- sort by field names -->
        </xsl:apply-templates>
        <xsl:for-each select="*">
            <xsl:choose>
                <!-- these declarations are handled separately -->
                <xsl:when test="name()='doc'"/>
                <xsl:when test="name()='field'"/>
                <xsl:when test="name()='group'"/>
                <!-- What might be the "otherwise" case? -->
                <xsl:otherwise>
                    <xsl:apply-templates select="."/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>

    <xsl:template name="typeAttributeDefaultHandler">
        <xsl:param name="item"/>
        <xsl:attribute name="{$item}">
            <xsl:choose>
                <xsl:when test="name()='field'">
                    <xsl:choose>
                        <xsl:when test="count(@type)=0">nxsd:NX_CHAR</xsl:when>
                        <xsl:otherwise>nxsd:<xsl:value-of select="@type"/></xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="name()='group'">nxsd:<xsl:value-of select="@type"/></xsl:when>
                <xsl:otherwise>nxsd:<xsl:value-of select="@type"/></xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>
    </xsl:template>
    
    <!--leave these templates empty, they are handled by special case code as needed	-->
    <xsl:template match="nxdl:attribute"/>
    <xsl:template match="nxdl:dimensions"/>
    <xsl:template match="nxdl:item"/>
    <xsl:template match="@name"/>
    <xsl:template match="@type"/>
    
</xsl:stylesheet>
