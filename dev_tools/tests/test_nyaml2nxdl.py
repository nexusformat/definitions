from pathlib import Path

import lxml.etree as ET
import pytest
from click.testing import CliRunner

from ..nyaml2nxdl import nyaml2nxdl as conv
from ..nyaml2nxdl.nyaml2nxdl_forward_tools import handle_each_part_doc
from ..nyaml2nxdl.nyaml2nxdl_helper import LineLoader
from ..nyaml2nxdl.nyaml2nxdl_helper import remove_namespace_from_tag
from ..utils.nxdl_utils import find_definition_file


def test_conversion():
    root = find_definition_file("NXentry")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", root])
    assert result.exit_code == 0
    # Replace suffixes
    yaml = root.parent / Path(root.with_suffix("").stem + "_parsed.yaml")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", yaml])
    assert result.exit_code == 0
    new_root = yaml.with_suffix(".nxdl.xml")
    with open(root, encoding="utf-8", mode="r") as tmp_f:
        root_content = tmp_f.readlines()
    with open(new_root, encoding="utf-8", mode="r") as tmp_f:
        new_root_content = tmp_f.readlines()
    assert root_content == new_root_content
    Path.unlink(yaml)
    Path.unlink(new_root)


def test_yaml2nxdl_doc():
    """To test the doc style from yaml to nxdl."""
    pwd = Path(__file__).parent

    doc_file = pwd / "data/doc_yaml2nxdl.yaml"
    ref_doc_file = pwd / "data/ref_doc_yaml2nxdl.nxdl.xml"
    out_doc_file = (
        pwd / "data/doc_yaml2nxdl.nxdl.xml"
    )  # doc_file.with_suffix('.nxdl.xml')
    # Test yaml2nxdl
    # Generates '../data/doc_text.nxdl.xml'
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(doc_file)])
    if result.exit_code != 0:
        Path.unlink(out_doc_file)
    assert result.exit_code == 0, f"Error: Having issue running input file {doc_file}."

    ref_nxdl = ET.parse(str(ref_doc_file)).getroot()
    out_nxdl = ET.parse(str(out_doc_file)).getroot()

    def compare_nxdl_doc(parent1, parent2):
        if len(parent1) > 0 and len(parent2) > 0:
            for par1, par2 in zip(parent1, parent2):
                compare_nxdl_doc(par1, par2)

        elif (
            remove_namespace_from_tag(parent1.tag) == "doc"
            and remove_namespace_from_tag(parent2.tag) == "doc"
        ):
            assert (
                parent1.text == parent2.text
            ), f"DOCS ARE NOT SAME: node {parent1}, node {parent2}"

    compare_nxdl_doc(ref_nxdl, out_nxdl)

    Path.unlink(out_doc_file)


def test_nxdl2yaml_doc():
    """To test the doc style from nxdl to yaml."""

    pwd = Path(__file__).parent
    nxdl_file = pwd / "data/doc_nxdl2yaml.nxdl.xml"
    ref_yaml = pwd / "data/ref_doc_nxdl2yaml.yaml"
    parsed_yaml_file = pwd / "data/doc_nxdl2yaml_parsed.yaml"

    result = CliRunner().invoke(
        conv.launch_tool, ["--input-file", str(nxdl_file), "--do-not-store-nxdl"]
    )

    if result.exit_code != 0:
        Path.unlink(parsed_yaml_file)

    assert result.exit_code == 0, "Error in converter execuation."

    with open(ref_yaml, mode="r", encoding="utf-8") as yaml1, open(
        parsed_yaml_file, mode="r", encoding="utf-8"
    ) as yaml2:
        yaml_dict1 = LineLoader(yaml1).get_single_data()
        yaml_dict2 = LineLoader(yaml2).get_single_data()

    def compare_yaml_doc(yaml_dict1, yaml_dict2):
        for k_val1, k_val2 in zip(yaml_dict1.items(), yaml_dict2.items()):
            key1, val1 = k_val1
            key2, val2 = k_val2
            if key1 == "doc" and key2 == "doc":
                assert val1 == val2, "Doc texts are not the same."
            elif isinstance(val1, dict) and isinstance(val2, dict):
                compare_yaml_doc(val1, val2)

    compare_yaml_doc(yaml_dict1, yaml_dict2)
    Path.unlink(parsed_yaml_file)


@pytest.mark.parametrize(
    "test_input,output,is_valid",
    [
        (
            """
    xref:
        spec: <spec>
        term: <term>
        url: <url>
    """,
            "    This concept is related to term `<term>`_ "
            "of the <spec> standard.\n.. _<term>: <url>",
            True,
        ),
        (
            """
    xref:
        spec: <spec>
         term: <term>
        url: <url>
    """,
            "Found invalid xref. Please make sure that your xref entries are valid yaml.",
            False,
        ),
        (
            """
    xref:
        spec: <spec>
        term: <term>
        url: <url>
        term: <term2>
    """,
            "Invalid xref. It contains nested or duplicate keys.",
            False,
        ),
        (
            """
    xref:
        spec: <spec>
        term: <term>
        url: <url>
        hallo: <term2>
    """,
            "Invalid xref. Too many keys.",
            False,
        ),
        (
            """
    xref:
        spec: <spec>
        my_key: <term>
        url: <url>
    """,
            "Invalid xref key `my_key`. Must be one of `term`, `spec` or `url`.",
            False,
        ),
        (
            """
    xref:
        spec: <spec>
        term:
            test: <nested_value>
        url: <url>
    """,
            "Invalid xref. It contains nested or duplicate keys.",
            False,
        ),
    ],
)
def test_handle_xref(test_input, output, is_valid):
    """
    Tests whether the xref generates a correct docstring.
    """
    if is_valid:
        assert handle_each_part_doc(test_input) == output
        return

    with pytest.raises(ValueError) as err:
        handle_each_part_doc(test_input)

    assert output == err.value.args[0]
