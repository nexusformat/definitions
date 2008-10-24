<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:nx="http://definition.nexusformat.org/schema/3.0"
	xmlns:fn="http://www.w3.org/2005/02/xpath-functions"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	>
	<xsl:output method="html" />
	
	<xsl:variable name="nxfiles" select="document('filelist.xml')/filelist/file/@name" />
		
	<xsl:variable name="nxnodes" select="document($nxfiles)//xs:complexType"/>
		
	<xsl:key name="nxtype-key" match="xs:complexType" use="@name" />
	
	<xsl:variable name="nxnod" select="document(//xs:include/@schemaLocation)//xs:complexType"/>
	
	<xsl:template name="clean-type">
		<xsl:param name="var"/>
		<xsl:variable name="first">
		<xsl:choose >
			<xsl:when  test="contains($var, 'nx:')">
				<xsl:value-of select="substring-after($var, 'nx:')"/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$var" />
			</xsl:otherwise>
		</xsl:choose>
		</xsl:variable>
		<xsl:variable name="second">
			<xsl:choose >
				<xsl:when  test="contains($first, 'Type')">
					<xsl:value-of select="substring-before($first, 'Type')"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$first" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
		<xsl:value-of select="$second"/>
	</xsl:template>
	
	<xsl:template match="/">
		<html>
			<head>
				<title></title>
			</head>
			<body>
			   <xsl:variable name="nxtypes">
				  <xsl:apply-templates select="xs:schema" mode="process"/>
			   </xsl:variable>
			   <xsl:apply-templates select="xs:schema" mode="output" />			   
			</body>
		</html>
	</xsl:template>
	
	<xsl:template match="xs:schema" mode="process">
		<xsl:apply-templates select="*" mode="process"/>
	</xsl:template>

	<xsl:template match="xs:schema" mode="output">
		<xsl:apply-templates select="*" mode="output"/>
	</xsl:template>
	
	<xsl:template match="xs:include" mode="output" />
	
	<xsl:template match="xs:include" mode="process">
      <xsl:comment>
        <xsl:text>Loading </xsl:text><xsl:value-of select="@schemaLocation" />
      </xsl:comment>
      <xsl:apply-templates select="document(@schemaLocation)/xs:schema" mode="process" />
      <xsl:comment>
        <xsl:text>Finished </xsl:text><xsl:value-of select="@schemaLocation" />
      </xsl:comment>
    </xsl:template>

	<xsl:template match="xs:complexType" mode="output">
		<h1><xsl:call-template name="clean-type">
			<xsl:with-param name="var" select="@name"></xsl:with-param>
		</xsl:call-template></h1> 
		<table border="2" cellpadding="5">
		<tr>
			<td><b>Element</b></td><td><b>Type</b></td><td><b>Defined In</b></td><td><b>Description</b></td>
		</tr>
		<xsl:apply-templates select="./xs:complexContent/xs:extension" mode="inherited"/>
		<xsl:apply-templates select=".//xs:element" mode="output" />
		</table>
	</xsl:template>
	
	<xsl:template match="xs:complexType" mode="inherited">
		<xsl:apply-templates select="./xs:complexContent/xs:extension" mode="inherited"/>
		<xsl:apply-templates select=".//xs:element" mode="output" />
	</xsl:template>
	
	<xsl:template match="xs:complexType" mode="process">
		<xsl:copy-of select="*" />
	</xsl:template>

	<xsl:template match="xs:extension" mode="inherited">
		<xsl:variable name="yyy" select="substring-after(@base,'nx:')"/>
		<xsl:for-each select="$nxnodes">
			<xsl:variable name="y" select="."/>
			<xsl:choose>
				<xsl:when test="@name = $yyy">
				<xsl:choose>
					<xsl:when test="xs:complexContent">
						<xsl:apply-templates select="$y" mode="inherited" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			</xsl:choose>
		</xsl:for-each>
	</xsl:template>
	

	<xsl:template match="xs:element" mode="output">
		<tr>
			<td> <xsl:value-of select="@name"/> </td>  
			<td> <xsl:call-template name="clean-type">
				<xsl:with-param name="var" select="@type" />
			</xsl:call-template> </td>
			<td> <xsl:call-template name="clean-type">
				<xsl:with-param name="var" select="../../../../@name" />
			</xsl:call-template> </td>
			<td> <xsl:value-of select="xs:annotation/xs:documentation"/> </td>
		</tr>
	</xsl:template>
	
</xsl:stylesheet>
