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
	xmlns:nx="http://definition.nexusformat.org/nxdl/3.1"
	xmlns:xi="http://www.w3.org/2001/XInclude"
	xmlns:xlink="http://www.w3.org/1999/xlink"
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
        
        <xsl:call-template name="nxdl-category-comment"/><!-- comment -->
<xsl:comment>
##########################################################
######	 This XML file was auto-generated from      ######
######	 an NXDL file by an XSLT transformation.    ######
######	 Do NOT edit this DocBook XML file.         ######
##########################################################
##### $Id$
##########################################################
</xsl:comment>

 <xsl:comment><!-- NeXus license comes next -->
# NeXus - Neutron, X-ray, and Muon Science Common Data Format
# 
# Copyright (C) 2008-10 NeXus International Advisory Committee (NIAC)
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
        <xsl:apply-templates select="//nx:definition"/>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:definition">
        <xsl:element name="section"><!-- root element -->
            <xsl:attribute name="xml:id"><xsl:value-of select="@name"/></xsl:attribute>
            <xsl:attribute name="xmlns">http://docbook.org/ns/docbook</xsl:attribute>
            <!-- 
                These namespaces will be added to the document (by xsltproc) if they are used.
                xmlns:xi="http://www.w3.org/2001/XInclude"
                xmlns:xlink="http://www.w3.org/1999/xlink"
            -->
            <xsl:attribute name="version">5.0</xsl:attribute><!-- required, matches NeXusManual.xml -->
            <!-- ...................................................... -->
            <xsl:element name="title"><xsl:value-of select="@name"/></xsl:element>
            <!--  mark this class in the index -->
            <xsl:element name="indexterm">
                <xsl:element name="primary">classes</xsl:element>
                <xsl:element name="secondary">
                    <xsl:choose>
                        <xsl:when test="/nx:definition/@category='base'">base classes</xsl:when>
                        <xsl:when test="/nx:definition/@category='application'">application definitions</xsl:when>
                        <xsl:when test="/nx:definition/@category='contributed'">contributed definitions</xsl:when>
                    </xsl:choose>
                </xsl:element>
                <xsl:element name="tertiary"><xsl:value-of select="@name"/></xsl:element>
            </xsl:element>
            <!-- ...................................................... -->
            <xsl:call-template name="headerList"/>
            <!-- ...................................................... -->
            <xsl:choose>
                <xsl:when test="count(nx:field)+count(nx:group)">
                    <xsl:call-template name="makeTable"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:element name="para">
                        No fields or groups are defined (nothing to show in a table at this point).
                    </xsl:element>
                </xsl:otherwise>
            </xsl:choose>
            <!-- ...................................................... -->
            <!-- listing of the NXDL source file -->
            <!-- 2009-10-16,PRJ: lighten the document, remove NXDL source -->
            <!--<section>
                <title><literal><xsl:value-of select="@name"/>.nxdl.xml</literal>: NXDL specification</title>
                <programlisting language="xml" linenumbering="numbered">___COPY_NXDL_HERE___</programlisting>
            </section>-->
            <!-- ...................................................... -->
            <xsl:apply-templates select="nx:group" mode="checkHierarchy"/>
            <!-- ...................................................... -->
        </xsl:element><!-- section -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:group" mode="checkHierarchy">
        <xsl:if test="count(nx:field)+count(nx:group)">
                <xsl:element name="para">
                    <xsl:call-template name="makeTable"/>
                </xsl:element>
        </xsl:if>
        <xsl:if test="count(nx:group)">
            <xsl:apply-templates select="nx:group" mode="checkHierarchy"/>
        </xsl:if>
    </xsl:template>

    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

    <xsl:template match="nx:field|nx:group" mode="tableRow">
        <xsl:element name="row">
            <xsl:if test="count(nx:attribute)">
                <xsl:attribute name="rowsep">0</xsl:attribute>
            </xsl:if>
            <!-- +++++++++++++++++++++
                +++ column: Name
                +++++++++++++++++++++ -->
            <xsl:element name="entry">
                <xsl:if test="count(@name)">
                    <xsl:element name="literal">
                        <xsl:value-of select="@name"/>
                    </xsl:element>
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
                                >#<xsl:value-of select="@type"/>
                            </xsl:attribute>
                            <xsl:value-of select="@type"/>
                        </xsl:element>
                    </xsl:when>
                    <xsl:when test="count(nx:enumeration)">
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
            <xsl:element name="entry">
                <xsl:if test="count(nx:doc)">
                    <xsl:element name="para">
                        <xsl:apply-templates select="nx:doc"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(@minOccurs)+count(@maxOccurs)">
                    <xsl:element name="para">
                        <xsl:call-template name="showOccurencesEntry"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(nx:dimensions)">
                    <xsl:element name="para"> Dimensions:
                        <xsl:apply-templates select="nx:dimensions" mode="showDimensionsEntry"/>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(nx:link)">
                    <xsl:element name="variablelist">
                        <xsl:element name="para">List of links:</xsl:element>
                        <xsl:for-each select="nx:link">
                            <xsl:apply-templates select="." mode="showLinkAttribute"/>
                        </xsl:for-each>
                    </xsl:element>
                </xsl:if>
                <xsl:if test="count(./nx:group)+count(./nx:field)">
                    <xsl:element name="para"
                        >See table: <xsl:element name="emphasis"
                            ><xsl:attribute name="role">bold</xsl:attribute
                            ><xsl:apply-templates select="." mode="showParentChild"
                            /></xsl:element
                        ></xsl:element>
                </xsl:if>
                <!-- perhaps forward reference to hierarchy at this point -->
            </xsl:element>
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
        <xsl:if test="count(nx:attribute)">
            <xsl:apply-templates select="nx:attribute" mode="newRow"/>
        </xsl:if>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nx:doc">
        <!--<xsl:value-of select="."/>-->
        <!-- xmlns:db="http://docbook.org/ns/docbook" -->
        <xsl:apply-templates />
    </xsl:template>
    
    <!-- default rule: copy any node beneath <nx:doc> -->
    <!-- thanks to: http://stackoverflow.com/questions/1525285/xslt-mixed-content-node -->
    <xsl:template match="nx:doc//*">
        <xsl:copy>
            <xsl:copy-of select="@*" />
            <xsl:apply-templates />
        </xsl:copy>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

    <xsl:template match="nx:attribute" mode="newRow">
        <xsl:element name="row">
            <xsl:if test="position()!=last()">
                <xsl:attribute name="rowsep">0</xsl:attribute>
            </xsl:if>
            <xsl:element name="entry">
                <xsl:element name="literal"
                    >  @<xsl:value-of select="@name"
                /></xsl:element>
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
        <xsl:if test="position()>1">, </xsl:if>        <!-- comma-separated list -->
        <xsl:element name="link">
            <xsl:attribute name="xlink:href"
                >#<xsl:value-of select="@type"/>
            </xsl:attribute>
            <xsl:value-of select="@type"/>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="*" mode="showParentChild">
        <xsl:if test="name()!='definition'"
            ><xsl:value-of select="/nx:definition/@name"
            />: <xsl:apply-templates select=".." 
                mode="showNameType"/>/</xsl:if>
        <xsl:apply-templates select="." mode="showNameType"/>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="*" mode="showNameType">
        <xsl:choose>
            <xsl:when test="name()='definition'"><xsl:value-of select="@name"/></xsl:when>
            <xsl:when test="name()='group'"><xsl:if test="count(@name)"
                ><xsl:value-of select="@name"/>:</xsl:if
                ><xsl:value-of select="@type"/></xsl:when>
            <xsl:when test="name()='field'"><xsl:value-of select="@name"/></xsl:when>
            <xsl:otherwise>
                <!-- should only get to this template for the above tests -->
                <pre>
                    DEBUG: Unexpected use of showNameType template:
                    DEBUG: name() *<xsl:value-of select="name()"/>*
                    DEBUG: @name *<xsl:value-of select="@name"/>*
                    DEBUG: @type *<xsl:value-of select="@type"/>*
                </pre>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="*" mode="showDimensionsEntry">
        <xsl:choose>
            <xsl:when test="count(@rank)">rank="<xsl:value-of select="@rank"/>"</xsl:when>
            <xsl:when test="count(nx:dim)">apparent rank="<xsl:value-of select="count(nx:dim)"/>"</xsl:when>
        </xsl:choose>
        <xsl:if test="count(nx:dim)">
            <xsl:element name="itemizedlist">
                <xsl:for-each select="nx:dim">
                    <xsl:element name="listitem"> <xsl:element name="para"> dim: 
                        <xsl:for-each select="@*">
                            <xsl:value-of select="name()"/>="<xsl:value-of select="."/>"
                        </xsl:for-each>
                        <xsl:if test="count(.)"> value="<xsl:value-of select="."/>"</xsl:if>
                    </xsl:element></xsl:element>
                </xsl:for-each>
            </xsl:element>
        </xsl:if>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="*" mode="showLinkAttribute">
        <xsl:element name="varlistentry">
            <xsl:element name="term">
                <xsl:element name="code">
                    <xsl:value-of select="@name"/>
                </xsl:element>
            </xsl:element>
            <xsl:element name="listitem">
                <xsl:element name="para">
                    <xsl:element name="code">
                        <xsl:value-of select="@target"/>
                    </xsl:element>
                </xsl:element>
            </xsl:element>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <!-- 
        +++++++++++++++
        named templates
        +++++++++++++++
    -->
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template name="headerList">
        <xsl:element name="variablelist">
            <xsl:element name="varlistentry"><!-- show the category: base, application, or contributed -->
                <xsl:element name="term">category</xsl:element>
                <xsl:element name="listitem">
                    <xsl:element name="para">
                        <xsl:element name="literal"><xsl:value-of select="/nx:definition/@category"/></xsl:element>
                        <xsl:choose>
                            <xsl:when test="/nx:definition/@category='base'">
                                (base class)
                            </xsl:when>
                            <xsl:when test="/nx:definition/@category='application'">
                                (application definition)
                            </xsl:when>
                            <xsl:when test="/nx:definition/@category='contributed'">
                                (contributed definition)
                            </xsl:when>
                        </xsl:choose>
                    </xsl:element>
                </xsl:element>
            </xsl:element><!-- varlistentry -->
            <xsl:element name="varlistentry"><!-- show where to find the source -->
                <xsl:element name="term">NXDL source:</xsl:element>
                <xsl:element name="listitem">
                    <xsl:element name="para">
                        <!-- !!! line breaks are VERY important here, don't bust them !!! -->
                        <xsl:element name="link"
                            ><xsl:attribute name="xlink:href"
                                ><xsl:call-template name="makeURL" >
                                    <xsl:with-param name="name">
                                        <xsl:value-of select="@name"/>
                                    </xsl:with-param>
                                    <xsl:with-param name="category">
                                        <xsl:value-of select="/nx:definition/@category"/>
                                    </xsl:with-param>
                                </xsl:call-template></xsl:attribute
                            ><xsl:value-of select="@name"/></xsl:element>
                        (<xsl:element name="link"
                            ><xsl:attribute name="xlink:href"
                                ><xsl:call-template name="makeURL" 
                                    ><xsl:with-param name="name"
                                        ><xsl:value-of select="@name"/>
                                    </xsl:with-param
                                    ><xsl:with-param name="category"
                                        ><xsl:value-of select="/nx:definition/@category"
                                        /></xsl:with-param
                                    ></xsl:call-template></xsl:attribute
                            ><xsl:call-template name="makeURL" >
                                <xsl:with-param name="name">
                                    <xsl:value-of select="@name"/>
                                </xsl:with-param>
                                <xsl:with-param name="category">
                                    <xsl:value-of select="/nx:definition/@category"/>
                                </xsl:with-param>
                            </xsl:call-template></xsl:element>)
                    </xsl:element>
                </xsl:element>
            </xsl:element><!-- varlistentry -->
            <xsl:element name="varlistentry"><!-- show the version of the NXDL instance -->
                <xsl:element name="term">version</xsl:element>
                <xsl:element name="listitem">
                    <xsl:element name="para">
                        <xsl:value-of select="@version"/>
                    </xsl:element>
                </xsl:element>
            </xsl:element><!-- varlistentry -->
            <xsl:element name="varlistentry"><!-- show the SVN Id of the NXDL instance -->
                <xsl:element name="term">SVN Id</xsl:element>
                <xsl:element name="listitem">
                    <xsl:element name="para">
                        <!-- strip the $ signs so SVN does not change the SVN Id in the target DocBook XML file -->
                        <xsl:value-of select="substring-before(substring-after(@svnid,'$'),'$')"/>
                    </xsl:element>
                </xsl:element>
            </xsl:element><!-- varlistentry -->
            <xsl:element name="varlistentry">
                <!-- show how to learn more about NXDL -->
                <xsl:element name="term">NeXus Definition Language</xsl:element>
                <xsl:element name="listitem">
                    <xsl:element name="para">
                        <xsl:element name="link"
                            ><xsl:attribute name="xlink:href"
                                >http://download.nexusformat.org/doc/html/NXDL.html</xsl:attribute
                            >NXDL</xsl:element>
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
                <xsl:choose>
                    <xsl:when test="count(nx:group)">
                        <xsl:element name="listitem">
                            <xsl:element name="para">
                                <xsl:apply-templates 
                                    mode="group-include"
                                    select="  //nx:group[generate-id(.) = generate-id(key('group-include', @type)[1])]  " >
                                    <!-- advice: http://sources.redhat.com/ml/xsl-list/2000-07/msg00458.html -->
                                    <!-- Muenchian method to sort+unique on group/@type -->
                                    <xsl:sort select="@type"/>
                                </xsl:apply-templates>
                            </xsl:element>
                        </xsl:element>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:element name="listitem">
                            <xsl:element name="para">no included classes</xsl:element>
                        </xsl:element>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:element><!-- varlistentry -->
            <xsl:element name="varlistentry"><!-- doc element of this class -->
                <xsl:element name="term">documentation</xsl:element>
                <xsl:element name="listitem">
                    <xsl:comment>count(nx:doc/child::*): <xsl:value-of select="count(nx:doc/child::*)"/></xsl:comment>
                    <xsl:choose>
                        <xsl:when test="count(nx:doc/child::*)=0">
                            <xsl:comment>branch-A</xsl:comment>
                            <xsl:element name="para">
                                <xsl:comment>+++</xsl:comment>
                                <xsl:apply-templates select="nx:doc"/>
                            </xsl:element>
                        </xsl:when>
                        <xsl:when test="count(nx:doc/child::*)>0">
                            <xsl:comment>branch-B</xsl:comment>
                            <xsl:apply-templates select="nx:doc"/>
                        </xsl:when>
                    </xsl:choose>
                </xsl:element>
            </xsl:element><!-- varlistentry -->
        </xsl:element><!-- variablelist -->
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template name="makeTable">
        <xsl:element name="table">
            <!--  This is markup for dblatex: -->
            <xsl:attribute name="orient">port</xsl:attribute> <!-- portrait -->
            <xsl:attribute name="role">small</xsl:attribute> <!-- smaller font -->
            <!-- describe what is defined -->
            <xsl:element name="title"
                ><xsl:apply-templates 
                    select="." mode="showParentChild"
                /></xsl:element>
            <xsl:element name="tgroup">
                <xsl:attribute name="cols">4</xsl:attribute>
                <!-- all columns *should* have adjustable width
                    So far, the PDF table columns all have fixed width.
                    How to change this? 
                    So far, the next set of instructions result in fixed column widths, but the widths are tuned somewhat.
                    The numbers are "weightings": the sum of all will be divided into each to get proportional width.
                    Asterisk (*) is necessary.
					
					http://dblatex.sourceforge.net/html/manual/ch03s04.html
                -->
                <xsl:element name="colspec"><xsl:attribute name="colwidth">15*</xsl:attribute></xsl:element>
                <xsl:element name="colspec"><xsl:attribute name="colwidth">15*</xsl:attribute></xsl:element>
                <xsl:element name="colspec"><xsl:attribute name="colwidth">20*</xsl:attribute></xsl:element>
                <xsl:element name="colspec"><xsl:attribute name="colwidth">30*</xsl:attribute></xsl:element>
                <xsl:element name="thead">
                    <xsl:element name="row">
                        <!-- more dblatex markup to set the background color of the column labels -->
                        <!--<?dblatex bgcolor="[gray]{0.8}"?>-->
                        <xsl:element name="entry"><xsl:processing-instruction name="dblatex"
                            >bgcolor="[gray]{0.8}"</xsl:processing-instruction>Name and Attributes</xsl:element>
                        <xsl:element name="entry"><xsl:processing-instruction name="dblatex"
                            >bgcolor="[gray]{0.8}"</xsl:processing-instruction>Type</xsl:element>
                        <xsl:element name="entry"><xsl:processing-instruction name="dblatex"
                            >bgcolor="[gray]{0.8}"</xsl:processing-instruction>Units</xsl:element>
                        <xsl:element name="entry"><xsl:processing-instruction name="dblatex"
                            >bgcolor="[gray]{0.8}"</xsl:processing-instruction>Description (and Occurrences)</xsl:element>
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
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template name="showOccurencesEntry">
        <!--<xsl:comment>
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            To properly populate the column for "Occurrences," we need
            to also parse the nxdl.xsd file.  Is this easy?  
            Otherwise, can only list apparent restrictions at this point.
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            </xsl:comment>-->
        Occurences: 
        <xsl:choose>
            <xsl:when test="count(@minOccurs)"><xsl:value-of select="@minOccurs"/></xsl:when>
            <xsl:otherwise>
                <xsl:element name="emphasis">
                    <xsl:attribute name="role">italic</xsl:attribute>
                    default
                </xsl:element>
            </xsl:otherwise>
        </xsl:choose>
        :
        <xsl:choose>
            <xsl:when test="count(@maxOccurs)"><xsl:value-of select="@maxOccurs"/></xsl:when>
            <xsl:otherwise>
                <xsl:element name="emphasis">
                    <xsl:attribute name="role">italic</xsl:attribute>
                    default
                </xsl:element>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <!-- http://svn.nexusformat.org/definitions/trunk -->
    <!-- http://trac.nexusformat.org/definitions/browser -->
    <!-- !!! line breaks are VERY important here, don't bust them !!! -->
    <xsl:template name="makeURL">
        <xsl:param name="name"/>
        <xsl:param name="category"
        />http://svn.nexusformat.org/definitions/trunk/<xsl:choose>
            <xsl:when test="$category='base'">base_classes</xsl:when
            ><xsl:when test="$category='application'">applications</xsl:when
            ><xsl:when test="$category='contributed'">contributed_definitions</xsl:when
            ></xsl:choose>/<xsl:value-of select="$name"/>.nxdl.xml</xsl:template>

    <!-- override these templates in each NXDL's specific XSLT file -->
    <xsl:template name="nxdl-category-comment"/> <!--  *** override for each NXDL category ***  -->

</xsl:stylesheet>
