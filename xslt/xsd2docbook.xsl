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
        
      <xsl:comment>###########################################################</xsl:comment>
      <xsl:comment>######    This XML file was auto-generated from      ######</xsl:comment>
      <xsl:comment>######    an NXDL file by an XSLT transformation.    ######</xsl:comment>
      <xsl:comment>######    Do NOT edit this DocBook XML file.         ######</xsl:comment>
      <xsl:comment>###########################################################</xsl:comment>

        <xsl:comment>NeXus license comes here</xsl:comment>

       <!-- TODO so far, thsi does nothing -->
        <xsl:for-each select="groupType|fieldType">
            <xsl:value-of select="name()"/>
            <xsl:apply-templates/>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="groupType">
        <xsl:value-of select="name()"/>
    </xsl:template>
    
</xsl:stylesheet>
