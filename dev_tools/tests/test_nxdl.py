import pytest

from ..globals import errors
from ..nxdl import find_definition
from ..nxdl import iter_definitions
from ..nxdl import nxdl_schema
from ..nxdl import validate_definition
from ..nxdl import validate_nxdl
from .utils import pytest_path_param_id


def test_iter_definitions():
    all_files = set(iter_definitions())
    assert all_files
    base_files = set(iter_definitions("base_classes"))
    assert base_files
    assert not (base_files - all_files)


def test_find_definition():
    assert find_definition("NXroot")
    assert not find_definition("NXwrong")
    assert not find_definition("NXroot", "applications")


@pytest.fixture(scope="module")
def xml_schema():
    return nxdl_schema()


def test_nxdl_syntax():
    validate_nxdl()


@pytest.mark.parametrize(
    "nxdl_file", list(iter_definitions()), ids=pytest_path_param_id
)
def test_nexus_syntax(nxdl_file, xml_schema):
    validate_definition(nxdl_file, xml_schema)


_FIELD_ATTRIBUTES_NXDL = """<?xml version="1.0" encoding="UTF-8"?>
<definition xmlns="http://definition.nexusformat.org/nxdl/3.1"
    name="NXtest_field_attributes" type="group" category="base">
    <doc>Test.</doc>
    <group type="NXsample">
        {group_content}
    </group>
    {definition_content}
</definition>
"""

_FIELD_ATTRIBUTES = """<fieldAttributes>
    <attribute name="long_name"/>
</fieldAttributes>"""


@pytest.mark.parametrize(
    "group_content,definition_content",
    [
        ("", _FIELD_ATTRIBUTES),
        ('<field name="x"/>' + _FIELD_ATTRIBUTES, ""),
    ],
    ids=["definition", "group"],
)
def test_field_attributes(tmp_path, xml_schema, group_content, definition_content):
    nxdl_file = tmp_path / "NXtest_field_attributes.nxdl.xml"
    nxdl_file.write_text(
        _FIELD_ATTRIBUTES_NXDL.format(
            group_content=group_content, definition_content=definition_content
        )
    )
    validate_definition(nxdl_file, xml_schema)


def test_field_attributes_must_be_last(tmp_path, xml_schema):
    nxdl_file = tmp_path / "NXtest_field_attributes.nxdl.xml"
    nxdl_file.write_text(
        _FIELD_ATTRIBUTES_NXDL.format(
            group_content=_FIELD_ATTRIBUTES + '<field name="x"/>',
            definition_content="",
        )
    )
    with pytest.raises(errors.XMLSyntaxError):
        validate_definition(nxdl_file, xml_schema)


_ENUMERATION = '<enumeration><item value="NXsample"/></enumeration>'


@pytest.mark.parametrize(
    "group_content,definition_content,valid",
    [
        ('<attribute name="NX_class" valueFrom="class"/>', "", True),
        ("", '<attribute name="NX_class" valueFrom="class"/>', True),
        ('<attribute name="NX_class" valueFrom="name"/>', "", False),
        (
            f'<attribute name="NX_class" valueFrom="class">{_ENUMERATION}</attribute>',
            "",
            False,
        ),
        (
            '<field name="x"><attribute name="a" valueFrom="class"/></field>',
            "",
            False,
        ),
        (
            '<fieldAttributes><attribute name="a" valueFrom="class"/>'
            "</fieldAttributes>",
            "",
            False,
        ),
    ],
    ids=[
        "group",
        "definition",
        "unknown-value",
        "with-enumeration",
        "field",
        "field-attributes",
    ],
)
def test_attribute_value_from(
    tmp_path, xml_schema, group_content, definition_content, valid
):
    nxdl_file = tmp_path / "NXtest_field_attributes.nxdl.xml"
    nxdl_file.write_text(
        _FIELD_ATTRIBUTES_NXDL.format(
            group_content=group_content, definition_content=definition_content
        )
    )
    if valid:
        validate_definition(nxdl_file, xml_schema)
    else:
        with pytest.raises(errors.XMLSyntaxError):
            validate_definition(nxdl_file, xml_schema)
