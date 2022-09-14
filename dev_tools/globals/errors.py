class XMLSyntaxError(Exception):
    """XML file has a syntax error"""

    pass


class NXDLSyntaxError(XMLSyntaxError):
    """XML file written in NXDL has a syntax error"""

    pass


class NXDLParseError(Exception):
    """XML file written in NXDL cannot be parsed"""
