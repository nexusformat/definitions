from contextlib import contextmanager
from typing import Optional

import lxml.etree
import xmlschema

from ..globals import errors
from ..globals.directories import get_xsd_file
from ..utils.types import PathLike


def nxdl_schema() -> lxml.etree.XMLSchema:
    return lxml.etree.XMLSchema(lxml.etree.parse(get_xsd_file()))


def validate_nxdl():
    """Validate the NXDL schema itself.

    :raises XMLSchemaParseError:
    """
    xsd_path = get_xsd_file()
    _ = xmlschema.XMLSchema(xsd_path)


def validate_definition(
    xml_path: PathLike,
    xml_schema: Optional[lxml.etree.XMLSchema] = None,
):
    """Validate an NXDL instance (NeXus definition)."""
    xml_path = str(xml_path)
    with _handle_xml_error(xml_path, lxml.etree.XMLSyntaxError):
        xml_tree = lxml.etree.parse(xml_path)
    if xml_schema is None:
        xml_schema = nxdl_schema()
    with _handle_xml_error(xml_path, lxml.etree.DocumentInvalid):
        xml_schema.assertValid(xml_tree)


@contextmanager
def _handle_xml_error(xml_path: str, *exception_types):
    try:
        yield
    except exception_types as e:
        raise errors.XMLSyntaxError(
            "\n  " + "\n  ".join([xml_path] + str(e).rsplit(":", 1))
        ) from e
