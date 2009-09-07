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
	specifications of Base Class Definitions into XML Schema (.xsd) files 
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
        <xsl:comment> **** This is a BASE Class **** </xsl:comment>
    </xsl:template>
    
    <!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

</xsl:stylesheet>
