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
	specifications of Application Definitionsinto XML Schema (.xsd) files 
	for use in validating candidate NeXus data files and also in preparing
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
    
    <xsl:import href="nxdl2xsd.xsl"/>
    
    <!-- comment specific to this NXDL category -->
    <xsl:template name="nxdl-category-comment">
        <xsl:comment> **** This is an Application Class **** </xsl:comment>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template match="nxdl:group">
        <!-- reference to another NX object (requires that object's XSD) -->
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">application: group declaration (NOT YET READY)</xsl:with-param>
        </xsl:call-template>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <xsl:template name="groupGroup">
        <xsl:for-each select="*">
            <xsl:choose>
                <xsl:when test="name()='doc'">
                    <xsl:apply-templates select="."/>
                </xsl:when>
                <xsl:when test="name()='field'">
                    <xsl:apply-templates select="."/>
                </xsl:when>
                <xsl:when test="name()='group'">
                    <xsl:call-template name="comment">
                        <xsl:with-param name="msg">group: <xsl:value-of select="@type"/>_app</xsl:with-param>
                    </xsl:call-template>
                    <xsl:apply-templates select="."/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:call-template name="comment">
                        <xsl:with-param name="msg">
                            <xsl:value-of select="name()"/>
                        </xsl:with-param>
                    </xsl:call-template>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template name="groupGroup_ORIG">
        <xsl:apply-templates select="nxdl:group">
            <xsl:sort select="@type"/><!-- sort by group type -->
            <xsl:sort select="@name"/><!-- then sort by field names -->
        </xsl:apply-templates>
        <xsl:call-template name="comment">
            <xsl:with-param name="msg">application: more stuff here</xsl:with-param>
        </xsl:call-template>
        <xsl:apply-templates select="nxdl:field">
            <xsl:sort select="@name"/><!-- sort by field names -->
        </xsl:apply-templates>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <!-- Override: set the default minOccurs="1" -->
    <xsl:template match="nxdl:field">
        <!-- named element declaration -->
        <xsl:element name="xs:element">
            <xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
            <xsl:attribute name="minOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@minOccurs)>0"><xsl:value-of select="@minOccurs"/></xsl:when>
                    <!-- in Applications, each named field is required -->
                    <!-- default --><xsl:otherwise>1</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="maxOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@maxOccurs)>0"><xsl:value-of select="@maxOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>1</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:call-template name="comment">
                <xsl:with-param name="msg"><xsl:value-of select="name()"/> declaration: <xsl:value-of select="@name"/></xsl:with-param>
            </xsl:call-template>
            <!-- documentation comes before the sequence -->
            <xsl:apply-templates select="nxdl:doc"/>
            <xsl:choose>
                <xsl:when test="count(nxdl:enumeration)>0">
                    <xsl:apply-templates select="nxdl:enumeration" mode="standard"/>
                </xsl:when>
                <xsl:otherwise><!-- no nxdl:enumeration -->
                    <xsl:element name="xs:complexType">
                        <xsl:element name="xs:simpleContent">
                            <xsl:element name="xs:extension">
                                <!-- @name is handled already -->
                                <xsl:call-template name="typeAttributeDefaultHandler" >
                                    <!-- handle @type attribute -->
                                    <xsl:with-param name="item">base</xsl:with-param>
                                </xsl:call-template>
                                <!-- need to handle the dimensions declaration -->
                                <xsl:call-template name="groupGroup"/>    <!-- special sort order for fields & groups -->
                            </xsl:element><!-- xs:extension -->
                        </xsl:element><!-- xs:simpleContent -->
                    </xsl:element><!-- xs:complexType -->
                </xsl:otherwise><!-- no nxdl:enumeration -->
            </xsl:choose>
        </xsl:element>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    
    <!-- Override: set the default minOccurs="1" -->
    <xsl:template match="nxdl:group_developing">
        <!-- reference to another NX object (requires that object's XSD) -->
        <xsl:element name="xs:element">
            <xsl:attribute name="name">
                <xsl:choose>
                    <!-- @name was specified, use it (to avoid multiple elements with same name) -->
                    <xsl:when test="count(@name)>0"><xsl:value-of select="@name"/>_app</xsl:when>
                    <!-- default -->
                    <xsl:otherwise><xsl:value-of select="@type"/>_app</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="minOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@minOccurs)>0"><xsl:value-of select="@minOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>1</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="maxOccurs">
                <xsl:choose>
                    <!-- specified --><xsl:when test="count(@maxOccurs)>0"><xsl:value-of select="@maxOccurs"/></xsl:when>
                    <!-- default --><xsl:otherwise>unbounded</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:choose>
                <xsl:when test="count(nxdl:field)+count(nxdl:group)>0">
                    <!-- if there are fields or groups, then documentation comes afterwards ?????(then why is it before?)????? -->
                    <xsl:apply-templates select="nxdl:doc"/>
                    <!-- fields or groups within this group element  -->
                    <xsl:comment> this is part of an <xsl:value-of select="@type"/> object </xsl:comment>
                    <xsl:element name="xs:complexType">
                        <!--xsl:attribute name="mixed">true</xsl:attribute-->
                        <xsl:element name="xs:complexContent">
                            <xsl:element name="xs:extension">
                                <xsl:attribute name="base">
                                    <xsl:text>nxsd:</xsl:text><xsl:value-of select="@type"/>
                                </xsl:attribute>
                                <xsl:element name="xs:sequence">
                                    <xsl:apply-templates select="nxdl:field|nxdl:group"/>
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

</xsl:stylesheet>
