<?xml version="1.0" encoding="UTF-8"?>
<!--
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
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
    
    <xsl:output method="xml" indent="yes" version="1.0" encoding="UTF-8"/>
    
<!-- 
     sort nodes based on name attribute if present - this should catch 
     all xs:element nodes within xs:sequence and orer them alphabetically 
-->
    
    
    <xsl:template match="/">
        <xsl:apply-templates select="*">
            <xsl:sort select="@name"/>
        </xsl:apply-templates>
    </xsl:template>
    
    <xsl:template match="*">
        <xsl:copy>
            <xsl:copy-of select="@*" />
            <xsl:apply-templates>
                <xsl:sort select="@name"/>
            </xsl:apply-templates>
        </xsl:copy>
    </xsl:template>
    
    <!--
    <xsl:template match="text()">
        <xsl:value-of select="normalize-space()"/>
    </xsl:template>
    -->
    
    <!-- if we are a sequence, copy in a sorted way - use name attribute from xs:element -->

    <!--
    <xsl:template match="xs:sequence">
        <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:for-each select="*">
                <xsl:sort select="@name"/>
                <xsl:apply-templates/>
            </xsl:for-each>
        </xsl:copy>
    </xsl:template>
    -->
            
</xsl:stylesheet>
