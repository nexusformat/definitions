<?xml version="1.0"?>
<!--
Generate a full definition by processing the includes

Freddie Akeroyd, 15/10/2008

-->
<xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
     xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xsl:output method="xml" />

<xsl:template match="/">
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="http://definition.nexusformat.org/schema/3.0" 
  xmlns:nx="http://definition.nexusformat.org/schema/3.0"
  elementFormDefault="qualified">
  <xsl:apply-templates select="xs:schema" />
</xs:schema>
</xsl:template>

<xsl:template match="xs:schema">
  <xsl:apply-templates match="*" />
</xsl:template>

<xsl:template match="xs:include">
 <xs:documentation>
 <xsl:text>Starting </xsl:text><xsl:value-of select="@schemaLocation" />
 </xs:documentation>
 <xsl:apply-templates select="document(@schemaLocation)/xs:schema" />
 <xs:documentation>
 <xsl:text>Finished </xsl:text><xsl:value-of select="@schemaLocation" />
 </xs:documentation>
</xsl:template>

<xsl:template match="*">
<xsl:copy>
 <xsl:for-each select="@*">
  <xsl:copy />
 </xsl:for-each>
 <xsl:apply-templates />
</xsl:copy>
</xsl:template>

</xsl:stylesheet>
