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
        <!-- Needs this on 2nd line of XML file: 
            <?oxygen RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"?>
        -->
        <xsl:processing-instruction 
            name="oxygen">RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbook.rng" type="xml"</xsl:processing-instruction>
        <xsl:comment/><!-- tricks XSLT to start a new line -->
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
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:definition">
        <xsl:element name="section"><!-- root element -->
            <xsl:attribute name="xml:id"><xsl:value-of select="@name"/>Section</xsl:attribute>
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
                            <xsl:element name="link"
                                ><xsl:attribute  name="xlink:href"
                                        >http://svn.nexusformat.org/definitions/trunk/base_classes/<xsl:value-of
                                        select="@name"/>.nxdl.xml</xsl:attribute
                                ><xsl:value-of select="@name"/></xsl:element>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
                <xsl:element name="varlistentry">
                    <!-- show how to learn more about NXDL -->
                    <xsl:element name="term">NeXus Definitional Language</xsl:element>
                    <xsl:element name="listitem">
                        <xsl:element name="para">
                            <xsl:element name="link">
                                <xsl:attribute name="xlink:href"
                                    >http://www.nexusformat.org/NXDL</xsl:attribute> NXDL
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
                                <xsl:element name="para">
                                    <xsl:value-of select="@extends"/>
                                </xsl:element>
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
                        <xsl:element name="para">
                            <xsl:comment>empty list</xsl:comment>
                            <xsl:apply-templates select="nx:doc"/>
                        </xsl:element>
                    </xsl:element>
                </xsl:element><!-- varlistentry -->
            </xsl:element><!-- variablelist -->
            <!-- ...................................................... -->
            <!--
                table formatting suggestion: examine http://www.nexusformat.org/TOFRaw#NXentry
                for hierarchical groups, link to subgroup in parent table row
                    and display subgroup in table below.
                For attributes, remove from last column and place on new row in last n-1 columns.
                Add column for # of occurrences:
                Occurrences Name Type Units Description
            -->
            <xsl:element name="table">
                <!-- describe what is defined -->
                <xsl:element name="title">Tabular representation of <xsl:value-of select="@name"
                    />:</xsl:element>
                <xsl:element name="tgroup">
                    <xsl:attribute name="cols">5</xsl:attribute>
		    <!-- all columns *should* have adjustable width
		    So far, the PDF table columns all have fixed width.
		    How to change this? 
		    So far, the next set of instructions result in fixed column widths, but the widths are tuned somewhat.
		    The numbers are "weightings": the sum of all will be divided into each to get proportional width.
		    Asterisk (*) is necessary.
		    -->
		   
                    <xsl:element name="colspec"><xsl:attribute name="colnum">1</xsl:attribute><xsl:attribute name="colwidth">1.5*</xsl:attribute></xsl:element>
                    <xsl:element name="colspec"><xsl:attribute name="colnum">2</xsl:attribute><xsl:attribute name="colwidth">1.5*</xsl:attribute></xsl:element>
                    <xsl:element name="colspec"><xsl:attribute name="colnum">3</xsl:attribute><xsl:attribute name="colwidth">1.5*</xsl:attribute></xsl:element>
                    <xsl:element name="colspec"><xsl:attribute name="colnum">4</xsl:attribute><xsl:attribute name="colwidth">1*</xsl:attribute></xsl:element>
                    <xsl:element name="colspec"><xsl:attribute name="colnum">5</xsl:attribute><xsl:attribute name="colwidth">3*</xsl:attribute></xsl:element>
                    <xsl:element name="thead">
                        <xsl:element name="row">
                            <xsl:element name="entry">Name</xsl:element>
                            <xsl:element name="entry">
			        <para>Occurrences</para>
				<para>/ Attributes</para>
			    </xsl:element>
                            <xsl:element name="entry">Type</xsl:element>
                            <xsl:element name="entry">Units</xsl:element>
                            <xsl:element name="entry">Description</xsl:element>
                        </xsl:element>
                        <!-- row -->
                    </xsl:element>
                    <!-- thead -->
                    <xsl:element name="tbody">
                        <xsl:apply-templates select="nx:field|nx:group" mode="tableRow"/>
                        <!-- row -->
                    </xsl:element>
                    <!-- tbody -->
                </xsl:element>
                <!-- tgroup -->
            </xsl:element><!-- table -->
            <!-- ...................................................... -->
        </xsl:element><!-- section -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:field|nx:group" mode="tableRow">
        <xsl:element name="row">
            <!-- +++++++++++++++++++++
                +++ column: Name
                +++++++++++++++++++++ -->
            <xsl:element name="entry">
                <xsl:if test="count(nx:attribute)!=0">
                    <xsl:attribute name="morerows"><xsl:value-of select="count(nx:attribute)"/></xsl:attribute>
                </xsl:if>
                <xsl:value-of select="@name"/>
            </xsl:element>
            <!-- +++++++++++++++++++++
                +++ column: Occurrences/Attributes
                +++++++++++++++++++++ -->
            <xsl:element name="entry">
                <!--<xsl:comment>
                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                    To properly populate the column for "Occurrences," we need
                    to also parse the nxdl.xsd file.  Is this easy?  Otherwise,
                    can only list apparent restrictions at this point.
                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                </xsl:comment>-->
                <xsl:if test="count(@minOccurs)!=0"><xsl:value-of select="@minOccurs"/>:</xsl:if>
                <xsl:if test="count(@maxOccurs)!=0">
                    <xsl:if test="count(@minOccurs)=0">:</xsl:if>
                    <xsl:value-of select="@maxOccurs"/>
                </xsl:if>
            </xsl:element>
            <!-- +++++++++++++++++++++
                +++ column: Type
                +++++++++++++++++++++ -->
            <xsl:element name="entry">
                <xsl:choose>
                    <xsl:when test="name()='group'">
                        <xsl:element name="link">
                            <xsl:attribute name="xlink:href"
                                    >http://www.nexusformat.org/<xsl:value-of select="@type"
                                /></xsl:attribute>
                            <xsl:value-of select="@type"/>
                        </xsl:element>
                    </xsl:when>
                    <xsl:when test="count(nx:enumeration)!=0">
                        <xsl:apply-templates select="nx:enumeration"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:choose>
                            <xsl:when test="count(@type)=0">NX_CHAR</xsl:when>
                            <xsl:otherwise><xsl:value-of select="@type"/></xsl:otherwise>
                        </xsl:choose>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:element>
            <!-- +++++++++++++++++++++
                +++ column: Units
                +++++++++++++++++++++ -->
            <xsl:element name="entry"><xsl:value-of select="@units"/></xsl:element>
            <!-- +++++++++++++++++++++
                +++ column: Description
                +++++++++++++++++++++ -->
            <xsl:element name="entry"><xsl:apply-templates select="nx:doc"/></xsl:element>
            <!-- +++++++++++++++++++++
                +++ situation: Hierarchy of group elements
                +++++++++++++++++++++ -->
            <xsl:for-each select="nx:group|nx:field">
                <xsl:comment
                    >subitem: <xsl:value-of select="name()"/>, <xsl:value-of select="@name"/>, <xsl:value-of select="@type"/>
                </xsl:comment>
            </xsl:for-each>
        </xsl:element><!-- row -->
        <!-- +++++++++++++++++++++
            +++ situation: attribute declarations
            +++++++++++++++++++++ -->
        <xsl:if test="count(nx:attribute)!=0">
            <xsl:apply-templates select="nx:attribute" mode="newRow"/>
        </xsl:if>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:doc">
        <xsl:value-of select="."/>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:attribute" mode="newRow">
        <xsl:element name="row">
            <xsl:element name="entry">
                <xsl:element name="emphasis">
                    <xsl:attribute name="role">italic</xsl:attribute
                    >@<xsl:value-of select="@name"/>
                </xsl:element>
            </xsl:element>
            <xsl:element name="entry">
                <xsl:choose>
                    <xsl:when test="count(@type)=0">NX_CHAR</xsl:when>
                    <xsl:otherwise><xsl:value-of select="@type"/></xsl:otherwise>
                </xsl:choose></xsl:element>
            <xsl:element name="entry"/>
            <xsl:element name="entry"><xsl:apply-templates select="nx:doc"/></xsl:element>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:enumeration">
        <!-- report each item in a list such as [ a | "b b" | c | d] -->
        <!--<xsl:element name="para">enumeration:</xsl:element>-->
            <xsl:apply-templates select="nx:item"/>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:item">
        <!-- 
            Q: How do we report documentation on any item?  
            A: Ignore it for this table.  No space to report it.
            Q: Then why have it?  
            A: So schema-aware editors can describe the item.
        -->
        <xsl:element name="para">
            <!--<xsl:if test="position()=1">
                [ 
            </xsl:if>-->
            <xsl:if test="position()!=1">
                |
            </xsl:if>
            <xsl:choose>
                <xsl:when test="contains(@value, ' ')">
                    <!-- surround with quotes when there is white-space -->
                    "<xsl:value-of select="@value"/>"
                </xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select="@value"/>
                </xsl:otherwise>
            </xsl:choose>
            <!--<xsl:if test="position()=last()">
                ]
            </xsl:if>-->
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:group" mode="group-include">
        <!-- show a class included by this class  -->
        <!-- http://www.nexusformat.org/NXclassname -->
        <xsl:element name="para">
            <xsl:element name="link">
                <xsl:attribute name="xlink:href"
                    >http://www.nexusformat.org/<xsl:value-of select="@type"/>
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

    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
 
</xsl:stylesheet>
