<?xml version="1.0" encoding="UTF-8"?>

<!--
  Provides a view of the NeXus NXDL cross-reference XML document
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:output method="html"/>
  
  <xsl:template match="/">
  	<h1>NXDL Cross-reference</h1>
    <xsl:apply-templates select="NXDL_cross_reference" mode="list"/>
  </xsl:template>
  
  <xsl:template match="NXDL_cross_reference" mode="list">
  	<h2>Summary table of NXDL categories</h2>
  	<table border = "2">
  		<tr bgcolor="black" >
  		  <th><font color="white">category</font></th>
  		  <th><font color="white">classes</font></th>
  		  <th><font color="white">entries</font></th>
  		</tr>
      <xsl:for-each select="NXDL/summary/category">
        <tr>
          <td><xsl:value-of select="@name"/></td>
          <td><xsl:value-of select="@count"/></td>
          <td><xsl:value-of select="@entries"/></td>
        </tr>
      </xsl:for-each>
  	</table>
  	
  	<h2>Table of NXDL classes</h2>
     	<table border="2">
     		<tr bgcolor="black">
     		  <th><font color="white">class</font></th>
     		  <th><font color="white">category</font></th>
     		  <th><font color="white">entries</font></th>
     		</tr>
     		<xsl:for-each select="NXDL/class">
     			<xsl:sort select="@name"/>
     			<tr>
     				<td><xsl:value-of select="@name"/></td>
     				<td><xsl:value-of select="@category"/></td>
     				<td><xsl:value-of select="@entries"/></td>
     			</tr>
     		</xsl:for-each>
     	</table>

    <h2>List of defined names</h2>
      <dl>
        <xsl:apply-templates select="declarations/*" mode="list">
          <xsl:sort select="@key"/>
        </xsl:apply-templates>
      </dl>
  </xsl:template>
  
  <xsl:template match="group|field|attribute|link" mode="list">
    <dt>
      <xsl:choose>
        <xsl:when test="name()='group'">
          <xsl:if test="count(@name)>0">
            <tt><xsl:value-of select="@name"/>:</tt>
          </xsl:if>
          <tt><xsl:value-of select="@type"/></tt>
        </xsl:when>
        <xsl:otherwise>
          <tt><xsl:value-of select="@name"/></tt>
        </xsl:otherwise>
      </xsl:choose>
     <!-- <xsl:text>, </xsl:text>
      <em>@key</em>=<tt><xsl:value-of select="@key"/></tt>-->
    </dt>
    <dd>
      <em><xsl:value-of select="name()"/></em>
      <xsl:if test="name()='field' or name()='attribute'">
        <xsl:text> </xsl:text>
        (<tt><xsl:value-of select="@type"/></tt>)
      </xsl:if>
      <xsl:text>, </xsl:text>
      <b><xsl:value-of select="@NXDL"/></b>
      <xsl:text>, </xsl:text>
      <tt><xsl:value-of select="@NXDL_path"/></tt>
      <xsl:if test="name()='link'">
        <xsl:text>, </xsl:text>
        <b>==&gt;</b> <em><tt><xsl:value-of select="@target"/></tt></em>
      </xsl:if>
    </dd>
  </xsl:template>
  
</xsl:stylesheet>
