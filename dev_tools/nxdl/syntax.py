from contextlib import contextmanager
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
    with _handle_xml_error(xml_file_name, lxml.etree.XMLSyntaxError):
        xml_tree = lxml.etree.parse(xml_file_name)
    if xml_schema is None:
        xml_schema = nxdl_schema()
    with _handle_xml_error(xml_file_name, lxml.etree.DocumentInvalid):
        xml_schema.assertValid(xml_tree)


@contextmanager
def _handle_xml_error(xml_file_name: str, *exception_types):
    try:
        yield
    except exception_types as e:
        raise errors.XMLSyntaxError(
            "\n  " + "\n  ".join([xml_file_name] + str(e).rsplit(":", 1))
        ) from e
