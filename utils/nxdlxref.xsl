<?xml version="1.0" encoding="UTF-8"?>

<!--
  Stylesheet to provide a view of the NeXus NXDL cross-reference XML document
  
  ########### SVN repository information ###################
  # $Date$
  # $Author$
  # $Revision$
  # $HeadURL$
  # $Id$
  ########### SVN repository information ###################
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:output method="html"/>
  
  <xsl:template match="/">
    <xsl:apply-templates select="NXDL_cross_reference" mode="list"/>
  </xsl:template>
  
  <xsl:template match="NXDL_cross_reference" mode="table">
    <table border="2">
      <tr>
        <th>element</th>
        <th>item</th>
        <th>link</th>
      </tr>
      <xsl:apply-templates select="*" mode="table"/>
    </table>
  </xsl:template>
  
  <xsl:template match="group" mode="table">
    <tr>
      <td><xsl:value-of select="name()"/></td>
      <td><xsl:value-of select="@type"/></td>
      <td><xsl:value-of select="@NXDL_path"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="field|attribute|link" mode="table">
    <tr>
      <td><xsl:value-of select="name()"/></td>
      <td><xsl:value-of select="@name"/></td>
      <td><xsl:value-of select="@NXDL_path"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="NXDL_cross_reference" mode="list">
    <dl>
      <xsl:apply-templates select="*" mode="list">
        <xsl:sort case-order="upper-first" select="@key"/>
      </xsl:apply-templates>
    </dl>
  </xsl:template>
  
  <xsl:template match="*" mode="list">
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
      <xsl:text>, </xsl:text>
      <b><xsl:value-of select="@NXDL"/></b>
      <xsl:text>, </xsl:text>
      <tt><xsl:value-of select="@NXDL_path"/></tt>
      <xsl:if test="name()='link'">
        <xsl:text>, </xsl:text>
        <b>==&gt;</b>:<tt><xsl:value-of select="@target"/></tt>
      </xsl:if>
      <xsl:if test="name()!='group' and name()!='link'">
        <xsl:text>, </xsl:text>
        <b>type</b>:<tt><xsl:value-of select="@type"/></tt>
      </xsl:if>
    </dd>
  </xsl:template>
  
</xsl:stylesheet>
