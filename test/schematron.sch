<?xml version="1.0" encoding="UTF-8"?>
<sch:schema 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
    queryBinding="xslt2">

    <sch:pattern fpi="check for name attributes">
        <sch:rule abstract="true" id="rule_check_NXclass">
            <!-- ensure NX groups have a @name -->
            <sch:assert 
                diagnostics="diag_NXgroup_needs_name_attr"
                test="(starts-with(name(),'NX') and @name)
                or not(starts-with(name(),'NX')) 
                or not(NXroot)"
                />
        </sch:rule>
    </sch:pattern>

    <sch:diagnostics>
        <sch:diagnostic id="diag_NXgroup_needs_name_attr"
            ><sch:value-of select="name()"
            />: An NX... group must have a name="" attribute</sch:diagnostic>
    </sch:diagnostics>
    
    <!-- ++++++++++++++++++++++++++++++++++++++ -->

    <sch:pattern>
        <sch:rule context="//*">
            <sch:extends rule="rule_check_NXclass"/>
        </sch:rule>
    </sch:pattern>

</sch:schema>