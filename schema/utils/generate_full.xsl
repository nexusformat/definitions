<?xml version="1.0"?> 
<!--
Generate a full definition by processing the includes

Freddie Akeroyd, 15/10/2008

-->
<xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
     xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xsl:output method="xml" />
<xsl:preserve-space elements="*"/>
 
 <xsl:key name="file_key" match="xs:include" use="@schemaLocation" />
 
 <xsl:variable name="files" select="document(//xs:incude/@schemalocation)" />
 
<xsl:template match="/">
 <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="http://definition.nexusformat.org/schema/3.0" 
  xmlns:nx="http://definition.nexusformat.org/schema/3.0"
  elementFormDefault="qualified">
  <xsl:apply-templates select="xs:schema" />
</xs:schema>
</xsl:template>

<xsl:template match="xs:schema">
  <xsl:apply-templates select="*" />
</xsl:template>

<xsl:template name="process-includes">
 <xsl:param name="input"/>
</xsl:template>
 <xsl:template match="xs:include">
 <xsl:variable name="test" select="key('file_key',@schemaLocation)" />
 <xsl:value-of select="$test" />
 <xsl:choose>
 <xsl:when test="key('file_key',@schemaLocation)">
  <xsl:comment>
   <xsl:text>Starting </xsl:text><xsl:value-of select="@schemaLocation" />
  </xsl:comment>
  <xsl:apply-templates select="document(@schemaLocation)/xs:schema" />
  <xsl:comment xml:lang="en">
   <xsl:text>Finished </xsl:text><xsl:value-of select="@schemaLocation" />
  </xsl:comment>
  </xsl:when>
  <xsl:otherwise>
   <xsl:comment xml:lang="en">
    <xsl:text>Skipping </xsl:text><xsl:value-of select="@schemaLocation" />
   </xsl:comment>
  </xsl:otherwise>
 </xsl:choose>
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
