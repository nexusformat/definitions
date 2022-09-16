"""Namespace of the schema in which NXDL is defined
(the XSD namespace) and the namespace of the NeXus
class definitions (the NXDL namespace).

Namespaces are URL's solely to be globally unique.
Do not use these URL's for validation. That's what
"xsi:schemaLocation" is for. Currently this is the
relative URI "../nxdl.xsd" which means validation
can only be done for NXDL files in subdirectories.
"""

from .directories import get_nxdl_version_file

XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
NXDL_NAMESPACE = "http://definition.nexusformat.org/nxdl/3.1"


def get_nxdl_version() -> str:
    """The version of the NeXus standard and the NeXus Definition language"""
    with open(get_nxdl_version_file(), "r") as fh:
        return fh.read().strip()
