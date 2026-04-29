"""NXDL agnostic XML helper functions."""

from functools import lru_cache
from pathlib import Path

import lxml.etree as ET


def read_xml_file(file_path: Path | str) -> ET.Element:
    """Read XML file with caching."""
    normalized_path = Path(file_path).resolve()
    return _read_xml_file(normalized_path)


@lru_cache(maxsize=None)
def _read_xml_file(normalized_path: Path) -> ET.Element:
    try:
        return ET.parse(normalized_path).getroot()
    except OSError:
        # Not sure this is still necessary
        with open(normalized_path, "r") as f:
            return ET.parse(f).getroot()


def get_local_name(element: ET.Element) -> str:
    """
    Return the local XML tag name of an element (without its namespace).

    '{http://example.org/ns}field' -> 'field'
    """
    return ET.QName(element).localname


def get_namespace(element: ET.Element) -> str:
    """
    Return the namespace URI of an XML element.

    '{http://example.org/ns}field' -> 'http://example.org/ns'
    """
    return ET.QName(element).namespace
