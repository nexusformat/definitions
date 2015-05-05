set(FILES nxdl2nx.xsl
          nxdl2rst.xsl
          nxdl2sch.xsl
          nxdl2xsd.xsl
          nxdl_desc2rst.xsl
          sort_nxdl.xsl)

foreach(F ${FILES})
    configure_file(${F} ${F} COPYONLY)
endforeach()


install(FILES ${FILES} 
        DESTINATION ${NEXUS_DEFINITIONS}/xslt 
        COMPONENT definitions)
