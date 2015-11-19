##
## change these to specify nxdl release
##
## Be __VERY__ judicious about updating NXDL_MAJOR_RELEASE and/or NXDL_MINOR_RELEASE
##  They are used to define the XML namespace for the NXDL files.  
##  This namespace is used in:
##    * NXDL documents
##    * NeXus data file validation
##    * XSLT transformations
##    * XSD specifications
##    * SCH specifications
##    * client source code files
##    * examples in the manual
##    * possibly other places, as well
##
set(NXDL_MAJOR_RELEASE 3)
set(NXDL_MINOR_RELEASE 1)
#set(NXDL_NAMESPACE_BASE "http://definition.nexusformat.org/nxdl")
##
## items below are derived from above
## force value into cache so we know to rebuild nxdl by checking cache
##
set(NXDL_RELEASE "${NXDL_MAJOR_RELEASE}.${NXDL_MINOR_RELEASE}" CACHE STRING "NXDL release" FORCE)
mark_as_advanced(NXDL_RELEASE)
#set(NXDL_NAMESPACE "${NXDL_NAMESPACE_BASE}/${NXDL_RELEASE}" CACHE STRING "NXDL namespace" FORCE)
#mark_as_advanced(NXDL_NAMESPACE)
