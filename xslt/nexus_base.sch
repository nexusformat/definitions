<?xml version="1.0" encoding="UTF-8"?>
<!-- 
########### SVN repository information ###################
# $LastChangedDate$
# $LastChangedBy$
# $LastChangedRevision$
# $HeadURL$
########### SVN repository information ###################
-->
<sch:schema 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    queryBinding="xslt2">

    <!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
    <!-- This file is automatically included in the final all.sch -->
    <!-- by the nxdl2sch.xsl transform                            -->
    <!-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

    <!--xsl:comment>Processing $Id$</xsl:comment-->
    
    <sch:ns uri="http://definition.nexusformat.org/schema/3.1" prefix="nx"/>
    <sch:ns uri="http://www.w3.org/1999/XSL/Transform" prefix="xsl"/>
    <sch:ns uri="http://www.w3.org/2001/XMLSchema-instance" prefix="xsi" />

    <xsl:key name="targets" match="//*[not(name()='NAPIlink')]" use="@target" />
    
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    <!-- defined variables -->
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    
    <sch:let name="NAPItype_INT" value="'NX_INT(8|16|32|64)'"/>
    <sch:let name="NAPItype_FLOAT" value="'NX_FLOAT(32|64)'"/>
    <sch:let name="ARRAY_regexp" value="'(\[0-9\])?'"/> <!-- this is not complete -->
    <sch:let name="NAPItype_regexp" 
        value="concat('NX_CHAR|',$NAPItype_INT,'|',$NAPItype_FLOAT)"/>
    
    <sch:let name="ValidItemName_regexp" value="'[A-Za-z_][A-Za-z0-9_]*'" />
    <sch:let name="ValidNXClassName_regexp" value="'NX[A-Za-z0-9_]*'" />

    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    <!-- abstract rules -->
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    
    <sch:pattern fpi="check for name attributes">
        <sch:rule abstract="true" id="rule_check_NXclass">
            <!-- ensure NXclass groups have a @name -->
            <sch:assert 
                diagnostics="diag_NXclass_needs_name_attr"
                test="@name"
            />
            <sch:assert 
				test="matches(@name,$ValidNXClassName_regexp)"
				diagnostics="diag_NXclass_needs_valid_name"
			/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NAPIlink element">
        <sch:rule abstract="true" id="rule_check_NAPIlink_element">
            <sch:assert 
                diagnostics="diag_NAPIlink_needs_target_attr" 
                test="@target"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern fpi="check NAPItype attributes">
        <sch:rule abstract="true" id="rule_check_NAPItype_attribute">
            <!--<sch:report test="true()">
                ::<sch:value-of select="name(..)"/>/@<sch:value-of select="name()"/>::
            </sch:report>-->
            <!-- NAPItype MUST start with "NX_" -->
            <sch:assert test="starts-with(@NAPItype,'NX_')"
                >NAPItype value should start with 'NX_'.</sch:assert>
            <sch:assert test="matches(@NAPItype,$NAPItype_regexp)">
                NAPItype attribute must be one of the allowed data types.
                Value '<sch:value-of select="@NAPItype"/>' was found in 
                <sch:value-of select="name()"/>.
            </sch:assert>
        </sch:rule>
        <sch:rule abstract="true" id="rule_check_field">
            <sch:extends rule="rule_check_NAPItype_attribute"/>
            <sch:assert test="matches(name(),$ValidItemName_regexp)">
                Field name <sch:value-of select="name()"/> contains invalid characters.
            </sch:assert>
        </sch:rule>
        <sch:rule abstract="true" id="rule_check_group">
            <sch:extends rule="rule_check_NXclass"/>
        </sch:rule>
    </sch:pattern>
    
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    <!-- diagnostics -->
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    
    <sch:diagnostics>
        <sch:diagnostic id="diag_NXclass_needs_name_attr"
            ><sch:value-of select="name()"
            />: An NX... group must have a name="" attribute</sch:diagnostic>
        <sch:diagnostic id="diag_NXclass_needs_valid_name"
            ><sch:value-of select="name()"
            />: An NX... group must have a valid name="" attribute</sch:diagnostic>
        <sch:diagnostic id="diag_NAPIlink_needs_target_attr"
            ><sch:value-of select="name(../@name)"
            />[<sch:value-of select="name(..)"/>]: 
            A NAPIlink element must have a target="" attribute.</sch:diagnostic>
    </sch:diagnostics>
    
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    <!-- patterns to match nodes in instance document -->
    <!-- ++++++++++++++++++++++++++++++++++++++ -->
    
    <sch:pattern>
        <sch:rule context="/nx:NXroot//*[count(child::*) > 0]">
            <sch:extends rule="rule_check_NXclass"/>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern>
        <sch:rule context="//nx:NAPIlink">
            <sch:extends rule="rule_check_NAPIlink_element"/>
            <!--
                Evaluate each NAPIlink element to verify that its @target 
                attribute points to one and only one data elements (field 
                that is not NAPIlink) with the same attribute and value.
                This does not evaluate if the value of the target (a path in the 
                NXentry) is correct.  That will come.
            -->
            <sch:let name="t" value="count(key('targets',@target))"/>
            <sch:assert test="$t > 0">Target not found in file</sch:assert>
            <sch:assert test="$t &lt;= 1">Multiple targets found in file</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern>
        <sch:rule context="/nx:NXroot//*[count(child::*) = 0 and not(name() = 'NAPIlink')]">
            <sch:extends rule="rule_check_field"/>
        </sch:rule>
    </sch:pattern>
        
</sch:schema>
