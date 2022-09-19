from typing import Optional

import lxml.etree

from ..globals import errors
from ..globals.directories import get_xsd_file
from ..utils.types import PathLike


def nxdl_schema() -> lxml.etree.XMLSchema:
    return lxml.etree.XMLSchema(lxml.etree.parse(get_xsd_file()))


def validate_definition(
    xml_file_name: PathLike,
    xml_schema: Optional[lxml.etree.XMLSchema] = None,
):
    xml_file_name = str(xml_file_name)
    try:
        xml_tree = lxml.etree.parse(xml_file_name)
    except lxml.etree.XMLSyntaxError:
        raise errors.XMLSyntaxError(xml_file_name)
    if xml_schema is None:
        xml_schema = nxdl_schema()
    try:
        xml_schema.assertValid(xml_tree)
    except lxml.etree.DocumentInvalid:
        raise errors.NXDLSyntaxError(xml_file_name)
