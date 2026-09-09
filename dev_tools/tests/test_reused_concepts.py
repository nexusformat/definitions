"""Showing concepts of other classes in the documentation of a NeXus class."""

from pathlib import Path
from typing import List
from typing import Optional

import pytest

from ..docs import NXClassDocGenerator
from ..globals.errors import NXDLParseError
from ..nxdl import nxdl_schema
from ..nxdl import validate_definition

_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<definition name="NXtest_reused_concepts" extends="NXobject" type="group" category="application"
    xmlns="http://definition.nexusformat.org/nxdl/3.1"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://definition.nexusformat.org/nxdl/3.1 ../nxdl.xsd">
{symbols}{reused}    <doc>Definition to test the reuse of concepts of other classes.</doc>
    <group type="NXentry">
        <doc>The entry.</doc>
{content}    </group>
</definition>
"""


def _count_reused(rst: str) -> int:
    """Number of concepts marked as reused, excluding the legend."""
    return rst.count("*(reused)*") - 1


@pytest.fixture(scope="module")
def doc_generator():
    return NXClassDocGenerator()


@pytest.fixture(scope="module")
def xml_schema():
    return nxdl_schema()


@pytest.fixture
def generate_doc(tmp_path, doc_generator, xml_schema, monkeypatch):
    """Generate the documentation of a test definition."""
    monkeypatch.setattr("dev_tools.docs.nxdl.get_nxdl_root", lambda: tmp_path)

    def generate(
        reuse: Optional[List[str]] = None,
        symbols: Optional[List[str]] = None,
        content: str = "",
    ) -> str:
        if reuse:
            lines = "".join(f"        {line}\n" for line in reuse)
            reused = f"    <reused_concepts>\n{lines}    </reused_concepts>\n"
        else:
            reused = ""
        if symbols:
            lines = "".join(f"        {line}\n" for line in symbols)
            symbols = f"    <symbols>\n{lines}    </symbols>\n"
        else:
            symbols = ""
        nxdl_file = Path(tmp_path) / "NXtest_reused_concepts.nxdl.xml"
        nxdl_file.write_text(
            _TEMPLATE.format(symbols=symbols, reused=reused, content=content)
        )
        validate_definition(nxdl_file, xml_schema)
        return "".join(doc_generator(nxdl_file))

    return generate


def test_reused_ancestors(generate_doc):
    """Groups in between are documented as well, without their documentation."""
    rst = generate_doc(['<reuse path="/ENTRY/INSTRUMENT/SOURCE/type"/>'])

    assert ":bolditalic:`INSTRUMENT`: (optional) :ref:`NXinstrument`" in rst
    assert ":bolditalic:`SOURCE`: (optional) :ref:`NXsource`" in rst
    assert "**type**: (optional) :ref:`NX_CHAR <NX_CHAR>`" in rst
    assert _count_reused(rst) == 3
    assert ":ref:`⤆ </NXsource/type-field>`" in rst

    # only the listed concept is documented
    assert "type of radiation source" in rst
    assert "Collection of the components of the instrument" not in rst


def test_reused_no_children(generate_doc):
    rst = generate_doc(['<reuse path="/ENTRY/INSTRUMENT/SOURCE"/>'])

    assert ":bolditalic:`SOURCE`: (optional) :ref:`NXsource`" in rst
    assert "**type**" not in rst


def test_reused_direct_children(generate_doc):
    rst = generate_doc(
        ['<reuse path="/ENTRY/INSTRUMENT/SOURCE/geometry" children="direct"/>']
    )

    assert "**component_index**: (optional)" in rst
    # the children of NXgeometry/SHAPE are not documented
    assert ":bolditalic:`SHAPE`: (optional) :ref:`NXshape`" in rst
    assert "**size**" not in rst


def test_reused_all_children(generate_doc):
    rst = generate_doc(
        ['<reuse path="/ENTRY/INSTRUMENT/SOURCE/geometry" children="all"/>'],
        symbols=[
            '<symbol name="numobj" reused_from="NXshape"/>',
            '<symbol name="nshapepar" reused_from="NXshape"/>',
        ],
    )

    assert ":bolditalic:`SHAPE`: (optional) :ref:`NXshape`" in rst
    assert "**size**: (optional)" in rst


def test_reused_too_many_children(generate_doc):
    with pytest.raises(NXDLParseError, match="concepts are reused"):
        generate_doc(['<reuse path="/ENTRY/INSTRUMENT/SOURCE" children="all"/>'])


def test_reused_subset_of_children(generate_doc):
    rst = generate_doc(
        [
            '<reuse path="/ENTRY/INSTRUMENT/SOURCE/type"/>',
            '<reuse path="/ENTRY/INSTRUMENT/SOURCE/probe"/>',
        ]
    )

    assert "**type**: (optional)" in rst
    assert "**probe**: (optional)" in rst
    assert "**name**: (optional)" not in rst


def test_reused_attribute(generate_doc):
    rst = generate_doc(['<reuse path="/ENTRY@default"/>'])

    assert "**@default**: (optional) :ref:`NX_CHAR <NX_CHAR>`" in rst
    assert ":ref:`⤆ </NXentry@default-attribute>` *(reused)*" in rst


def test_reused_below_defined_group(generate_doc):
    """A concept is documented below the group that defines it."""
    content = """        <group name="instrument" type="NXinstrument">
            <doc>The instrument.</doc>
        </group>
"""
    rst = generate_doc(['<reuse path="/ENTRY/instrument/SOURCE"/>'], content=content)

    _, _, below = rst.partition("**instrument**: (required) :ref:`NXinstrument`")
    assert ":bolditalic:`SOURCE`: (optional) :ref:`NXsource`" in below
    assert _count_reused(rst) == 1


def test_reused_defined_concept(generate_doc):
    content = """        <field name="title" type="NX_CHAR">
            <doc>The title.</doc>
        </field>
"""
    with pytest.raises(
        NXDLParseError, match="is defined by NXtest_reused_concepts itself"
    ):
        generate_doc(['<reuse path="/ENTRY/title"/>'], content=content)


def test_reused_unknown_concept(generate_doc):
    with pytest.raises(NXDLParseError, match="does not exist in"):
        generate_doc(['<reuse path="/ENTRY/does_not_exist"/>'])


def test_reused_renamed_concept(generate_doc):
    """A concept that this class redefines under another name is a different one."""
    content = """        <group name="my_sample" nameType="any" type="NXsample">
            <doc>The sample.</doc>
        </group>
"""
    with pytest.raises(NXDLParseError, match="is redefined by .* as 'my_sample'"):
        generate_doc(['<reuse path="/ENTRY/SAMPLE"/>'], content=content)

    # the concept as this class knows it can be reused instead
    rst = generate_doc(
        ['<reuse path="/ENTRY/my_sample/chemical_formula"/>'], content=content
    )
    assert "**chemical_formula**: (optional)" in rst


def test_reused_invalid_path(generate_doc):
    with pytest.raises(NXDLParseError, match="must start with '/'"):
        generate_doc(['<reuse path="ENTRY/INSTRUMENT"/>'])


def test_reused_wrong_separator(generate_doc):
    with pytest.raises(NXDLParseError, match="is a group"):
        generate_doc(['<reuse path="/ENTRY@INSTRUMENT"/>'])


def test_reused_listed_twice(generate_doc):
    with pytest.raises(NXDLParseError, match="reused more than once"):
        generate_doc(
            [
                '<reuse path="/ENTRY/INSTRUMENT/SOURCE"/>',
                '<reuse path="/ENTRY/INSTRUMENT/SOURCE"/>',
            ]
        )


def test_symbols_of_reused_concept(generate_doc):
    reuse = ['<reuse path="/ENTRY/INSTRUMENT/DETECTOR/dead_time"/>']

    with pytest.raises(NXDLParseError, match="missing from its symbol table"):
        generate_doc(reuse)

    rst = generate_doc(
        reuse,
        symbols=[
            '<symbol name="nP" reused_from="NXdetector"/>',
            '<symbol name="i" reused_from="NXdetector"/>',
            '<symbol name="j"><doc>Number of columns.</doc></symbol>',
        ],
    )
    assert (
        "**nP**: number of scan points (only present in scanning measurements) "
        ":ref:`⤆ </NXdetector/nP-symbol>` *(reused)*" in rst
    )
    assert ".. _/NXtest_reused_concepts/j-symbol:" in rst
    assert "**j**: Number of columns." in rst
    cls = "/NXtest_reused_concepts"
    assert (
        "(Rank: 3, Dimensions: "
        f"[:ref:`nP <{cls}/nP-symbol>`, "
        f":ref:`i <{cls}/i-symbol>`, "
        f":ref:`j <{cls}/j-symbol>`])" in rst
    )


def test_symbol_links_in_dimensions(generate_doc):
    """Symbols in a dimension size link to the symbol table."""
    content = """        <field name="data" type="NX_NUMBER">
            <doc>The data.</doc>
            <dimensions rank="2">
                <dim index="1" value="2n_data"/>
                <dim index="2" value="n_data+1"/>
            </dimensions>
        </field>
"""
    rst = generate_doc(
        content=content,
        symbols=['<symbol name="n_data"><doc>Number of points.</doc></symbol>'],
    )

    ref = ":ref:`n_data </NXtest_reused_concepts/n_data-symbol>`"
    # the escapes keep the inline markup valid next to a digit and a "+"
    assert f"(Rank: 2, Dimensions: [2\\ {ref}, {ref}\\ +1])" in rst


def test_symbols_of_defined_concept(generate_doc):
    content = """        <field name="data" type="NX_NUMBER">
            <doc>The data.</doc>
            <dimensions rank="1">
                <dim index="1" value="n_data"/>
            </dimensions>
        </field>
"""
    with pytest.raises(NXDLParseError, match="'n_data' \\(dimension of 'data'\\)"):
        generate_doc(content=content)

    rst = generate_doc(
        symbols=['<symbol name="n_data"><doc>Number of points.</doc></symbol>'],
        content=content,
    )
    assert "**n_data**: Number of points." in rst


def test_symbol_reused_from_unknown_class(generate_doc):
    with pytest.raises(NXDLParseError, match="unknown class 'NXdoes_not_exist'"):
        generate_doc(symbols=['<symbol name="nP" reused_from="NXdoes_not_exist"/>'])


def test_symbol_not_in_reused_class(generate_doc):
    with pytest.raises(NXDLParseError, match="does not define the symbol 'nP'"):
        generate_doc(symbols=['<symbol name="nP" reused_from="NXsource"/>'])


def test_symbol_reused_with_doc(generate_doc):
    with pytest.raises(
        NXDLParseError, match="has a 'doc' element as well as reused_from"
    ):
        generate_doc(
            symbols=[
                '<symbol name="nP" reused_from="NXdetector"><doc>Points.</doc></symbol>'
            ]
        )
