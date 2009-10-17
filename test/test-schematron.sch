<?xml version="1.0" encoding="UTF-8"?>
<!--
    ########### SVN repository information ###################
    # $Date$
    # $Author$
    # $Revision$
    # $HeadURL$
    # $Id$
    ########### SVN repository information ###################
    
    <sch:schema xmlns:sch="http://www.ascc.net/xml/schematron">
    
    paste this string on the second line of an XML instance
    to use Schematron schema to validate the file
    <?oxygen SCHSchema="file:test-schematron.sch" type="xml"?>
-->
<sch:schema 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
    queryBinding="xslt2">
    <sch:title>demonstration Schematron schema NeXus XML data file</sch:title>
    <!-- http://www.schematron.com/ -->

    <!--<xsl:key xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
        match="t:Participants" name="Participant" use="t:Name/@id"/>-->
    
    <sch:let name="NAPItype_INT" value="'NX_INT(8|16|32|64)'"/>
    <sch:let name="NAPItype_FLOAT" value="'NX_FLOAT(32|64)'"/>
    <sch:let name="ARRAY_regexp" value="'(\[0-9\])?'"/> <!-- this is not complete -->
    <sch:let name="NAPItype_regexp" 
        value="concat('NX_CHAR|',$NAPItype_INT,'|',$NAPItype_FLOAT)"/>

    <sch:pattern fpi="check NXroot">
        <sch:rule context="/NXroot">
            <sch:assert test="@NeXus_version">Missing "NeXus_version" attribute in <sch:name/>.</sch:assert>
            <sch:assert test="@XML_version">Missing "XML_version" attribute in <sch:name/>.</sch:assert>
            <sch:assert test="@file_name">Missing "file_name" attribute in <sch:name/>.</sch:assert>
            <sch:assert test="@file_time">Missing "file_time" attribute in <sch:name/>.</sch:assert>
        </sch:rule>
    </sch:pattern>

    <sch:pattern fpi="check NX groups">
        <sch:rule abstract="true" id="NXentry_abstract_rule">
            <!-- make sure this test is applied properly -->
            <sch:assert test="starts-with(name(),'NX')">Official NeXus classes start with 'NX'.</sch:assert>
            <!-- NX groups MUST have a "name" attribute -->
            <sch:assert test="@name">Missing "name" attribute.</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NAPI type">
        <sch:rule abstract="true" id="check_NAPItype_rule">
            <!-- make sure this test is applied properly -->
            <sch:assert test="@NAPItype">Missing "NAPItype" attribute.</sch:assert>
            <!-- NAPItype MUST start with "NX_" -->
            <sch:assert test="starts-with(@NAPItype,'NX_')">NAPItype value should start with 'NX_'.</sch:assert>
            <sch:report test="starts-with(@NAPItype,'NX_INT')">NX_INT identified.</sch:report>
            <sch:report test="substring(@NAPItype,1,10)='NX_FLOAT32'">NX_FLOAT32 identified.</sch:report>
            <sch:report test="substring(@NAPItype,1,10)='NX_FLOAT64'">NX_FLOAT64 identified.</sch:report>
            <sch:assert test="exists(index-of ((15, 40, 25, 40, 10), 40))"> something </sch:assert>
            <sch:assert test="matches(@NAPItype,$NAPItype_regexp)">
                NAPItype must be one of the allowed data types.
                '<sch:value-of select="@NAPItype"/>' was found in 
                <sch:value-of select="../@name"/>[<sch:value-of select="name(..)"/>]/<sch:name/>
            </sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXentry">
        <sch:rule context="//NXentry" id="NXentry_rule">
            <sch:extends rule="NXentry_abstract_rule"/>
            <sch:assert test="@name">Missing "name" attribute in <sch:name/>.</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXinstrument">
        <sch:rule context="//NXinstrument">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXdetector">
        <sch:rule context="//NXdetector">
            <sch:extends rule="NXentry_abstract_rule"/>
            <sch:report test="not(polar_angle)">
                Missing "polar_angle" element in <sch:name/>.
            </sch:report>
        </sch:rule>
        <sch:rule context="//NXdetector/polar_angle">
            <sch:extends rule="check_NAPItype_rule"/>
            <!-- check for link to this data in NXdata -->
            <sch:assert test="../../../NXdata/polar_angle/@NAPIlink">
                Missing @NAPIlink in "../../../NXdata/polar_angle/@NAPIlink".
                <sch:value-of select="name(../../..)"/>
            </sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXsource">
        <sch:rule context="//NXsource">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXcrystal">
        <sch:rule context="//NXcrystal">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXmonitor">
        <sch:rule context="//NXmonitor">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXdata">
        <sch:rule context="//NXdata">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXsample">
        <sch:rule context="//NXsample">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NXuser">
        <sch:rule context="//NXuser">
            <sch:extends rule="NXentry_abstract_rule"/>
        </sch:rule>
    </sch:pattern>

</sch:schema>