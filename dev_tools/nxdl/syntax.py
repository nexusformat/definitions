from contextlib import contextmanager
from functools import lru_cache
from typing import Optional

import lxml.etree
import xmlschema

from ..globals import errors
from ..globals.directories import get_nxdl_root
from ..globals.directories import get_xsd_file
from ..globals.nxdl import NXDL_NAMESPACE
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
    _validate_value_from(xml_path, xml_tree)
    _validate_field_attributes(xml_path, xml_tree)
    _validate_group_types(xml_path, xml_tree)


def _validate_value_from(xml_path: str, xml_tree: lxml.etree._ElementTree) -> None:
    """Raise when an attribute has both ``valueFrom`` and an ``enumeration``."""
    for node in xml_tree.xpath(
        "//nx:attribute[@valueFrom][nx:enumeration]", namespaces={"nx": NXDL_NAMESPACE}
    ):
        raise errors.NXDLSyntaxError(
            f"\n  {xml_path}\n  line {node.sourceline}: attribute"
            f" '{node.get('name')}' has both 'valueFrom' and an 'enumeration'"
        )


def _validate_field_attributes(
    xml_path: str, xml_tree: lxml.etree._ElementTree
) -> None:
    """Raise when an application definition has ``fieldAttributes`` as a direct child."""
    for node in xml_tree.xpath(
        "/nx:definition[@category='application']/nx:fieldAttributes",
        namespaces={"nx": NXDL_NAMESPACE},
    ):
        raise errors.NXDLSyntaxError(
            f"\n  {xml_path}\n  line {node.sourceline}: 'fieldAttributes' is not"
            " allowed directly in an application definition"
        )


def _validate_group_types(xml_path: str, xml_tree: lxml.etree._ElementTree) -> None:
    """Raise when the type of a group is an application definition."""
    application_definitions = _application_definitions()
    for node in xml_tree.xpath("//nx:group[@type]", namespaces={"nx": NXDL_NAMESPACE}):
        if node.get("type") in application_definitions:
            raise errors.NXDLSyntaxError(
                f"\n  {xml_path}\n  line {node.sourceline}: group type"
                f" '{node.get('type')}' is an application definition, not a base class"
            )


@lru_cache(maxsize=None)
def _application_definitions() -> frozenset:
    """Names of the application definitions in the repository."""
    names = set()
    for path in get_nxdl_root().glob("*/*.nxdl.xml"):
        root = lxml.etree.parse(str(path)).getroot()
        if root.get("category") == "application":
            names.add(root.get("name"))
    return frozenset(names)


@contextmanager
def _handle_xml_error(xml_path: str, *exception_types):
    try:
        yield
    except exception_types as e:
        raise errors.XMLSyntaxError(
            "\n  " + "\n  ".join([xml_path] + str(e).rsplit(":", 1))
        ) from e
