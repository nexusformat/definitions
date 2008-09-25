<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:nx="http://definition.nexusformat.org/schema/3.0"
	xmlns:fn="http://www.w3.org/2005/02/xpath-functions"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	>
              <xsl:output  method="html" />
	
	<xsl:template match="/">
		<html>
			<head>
				<title></title>
			</head>
			<body>
				<xsl:apply-templates select="xs:schema" />
			</body>
		</html>
	</xsl:template>
	<xsl:template match="xs:schema">
		<xsl:apply-templates select="xs:complexType" />
	</xsl:template>
	
	<xsl:template match="xs:complexType">
		<h1><xsl:value-of select="@name"/></h1> 
		<table>
		<tr>
			<td><b>Element</b></td><td><b>Type</b></td>
		</tr>
		<xsl:apply-templates select=".//xs:element" />
		</table>
	</xsl:template>
	
	<xsl:template match="xs:element">
		<tr>
			<td> <xsl:value-of select="@name"/> </td>  
			<td> <xsl:value-of select="@type"/> </td>
		</tr>
	</xsl:template>
	
</xsl:stylesheet>
