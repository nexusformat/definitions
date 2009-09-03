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
	specifications of Base Class Definitions into DocBook (.xml) files 
	for use in assembling NeXus about the class definitions from NXDL.

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
    
    <xsl:import href="nxdl2docbook.xsl"/>
    
    <!-- comment specific to this NXDL category -->
    <xsl:template name="nxdl-category-comment">
        <xsl:comment> **** This is a BASE Class **** </xsl:comment>
    </xsl:template>

</xsl:stylesheet>
