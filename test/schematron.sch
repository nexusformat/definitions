<?xml version="1.0" encoding="UTF-8"?>
<sch:schema 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
    queryBinding="xslt2">

    <sch:pattern fpi="check NX.... class">
        <sch:rule abstract="true" id="rule_check_NXclass">
            <!-- make sure this test is applied properly -->
            <sch:assert 
                test="starts-with(name(),'NX') and @name or not(starts-with(name(),'NX')) or not(NXroot)"
                >NX groups must a @name attribute.</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern>
        <sch:rule context="//*">
            <sch:extends rule="rule_check_NXclass"/>
        </sch:rule>
    </sch:pattern>
    
</sch:schema>