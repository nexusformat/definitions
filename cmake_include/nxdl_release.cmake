##
## change these to specify nxdl release
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
