"""This is a code that performs several tests on nexus tool"""

from pathlib import Path

import lxml.etree as ET
import pytest

from ..utils import nxdl_utils as nexus


def test_get_nexus_classes_units_attributes():
    """Check the correct parsing of a separate list for:
    Nexus classes (base_classes)
    Nexus units (memberTypes)
    Nexus attribute type (primitiveTypes)
    the tested functions can be found in nexus.py file"""

    # Test 1
    nexus_classes_list = nexus.get_nx_classes()

    assert "NXbeam" in nexus_classes_list

    # Test 2
    nexus_units_list = nexus.get_nx_units()
    assert "NX_TEMPERATURE" in nexus_units_list

    # Test 3
    nexus_attribute_list = nexus.get_nx_attribute_type()
    assert "NX_FLOAT" in nexus_attribute_list


@pytest.fixture(scope="module")
def nxdl_files():
    """Fixture to load NXDL files once."""
    local_dir = Path(__file__).resolve().parent
    return {
        "NXtest.nxdl.xml": ET.parse(local_dir / "NXtest.nxdl.xml").getroot(),
        "NXiv_temp.nxdl.xml": ET.parse(
            local_dir.parent.parent / "contributed_definitions" / "NXiv_temp.nxdl.xml"
        ).getroot(),
        "NXem.nxdl.xml": ET.parse(
            local_dir.parent.parent / "applications" / "NXem.nxdl.xml"
        ).getroot(),
    }


@pytest.mark.parametrize(
    "file_name, nxdl_path, expected",
    [
        # NXtest.nxdl.xml test cases
        (
            "NXtest.nxdl.xml",
            "/ENTRY/NXODD_name",
            {"type": "NXdata", "name": "NXODD_name"},
        ),
        (
            "NXtest.nxdl.xml",
            "/ENTRY/NXODD_name/float_value",
            {"type": "NX_FLOAT", "name": "float_value"},
        ),
        (
            "NXtest.nxdl.xml",
            "/ENTRY/NXODD_name/AXISNAME/long_name",
            {"name": "long_name"},
        ),
        # NXiv_temp.nxdl.xml test cases
        (
            "NXiv_temp.nxdl.xml",
            "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller",
            {"name": "voltage_controller"},
        ),
        (
            "NXiv_temp.nxdl.xml",
            "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller/calibration_time",
            {"name": "calibration_time"},
        ),
        # NXem.nxdl.xml test cases
        (
            "NXem.nxdl.xml",
            "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/end_time",
            {"name": "end_time"},
        ),
        ("NXem.nxdl.xml", "/ENTRY/measurement", {"type": "NXem_msr"}),
        (
            "NXem.nxdl.xml",
            "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d",
            {"type": "NXdata"},
        ),
        (
            "NXem.nxdl.xml",
            "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d/AXISNAME_indices",
            {"name": "AXISNAME_indices"},
        ),
        (
            "NXem.nxdl.xml",
            "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d/axis_j",
            {"type": "NX_NUMBER"},
        ),
        (
            "NXem.nxdl.xml",
            "/ENTRY/coordinate_system_set",
            {"type": "NXcoordinate_system_set"},
        ),
    ],
)
def test_get_node_at_nxdl_path(nxdl_files, file_name, nxdl_path, expected):
    """Test to verify if we receive the right XML element for a given NXDL path."""
    elem = nxdl_files[file_name]
    node = nexus.get_node_at_nxdl_path(nxdl_path, elem=elem)
    for key, value in expected.items():
        assert node.attrib[key] == value


@pytest.mark.parametrize(
    "file_name, nxdl_path, nx_name, expected_length",
    [
        # NXtest.nxdl.xml test cases
        ("NXtest.nxdl.xml", "/ENTRY/NXODD_name", None, 3),
        # NXiv_temp.nxdl.xml test cases
        ("NXiv_temp.nxdl.xml", "/ENTRY/INSTRUMENT/ENVIRONMENT", None, 3),
        (
            "NXiv_temp.nxdl.xml",
            "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller",
            None,
            4,
        ),
        (
            "NXiv_temp.nxdl.xml",
            "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller",
            "NXiv_temp",
            4,
        ),
    ],
)
def test_get_inherited_nodes(
    nxdl_files, file_name, nxdl_path, nx_name, expected_length
):
    """Test to verify if we receive the right XML element list for a given NXDL path."""
    elem = nxdl_files[file_name]
    (_, _, elist) = nexus.get_inherited_nodes(
        nxdl_path=nxdl_path, elem=elem, nx_name=nx_name
    )
    assert len(elist) == expected_length


@pytest.mark.parametrize(
    "hdf_name,concept_name,should_fit",
    [
        ("source_pump", "sourceType", False),
        ("source_pump", "sourceTYPE", True),
        ("source pump", "sourceTYPE", False),
        ("source", "sourceTYPE", False),
        ("source123", "SOURCE", True),
        ("1source", "SOURCE", True),
        ("_source", "SOURCE", True),
        ("same_name", "same_name", True),
        ("angular_energy_resolution", "angularNresolution", True),
        ("angularresolution", "angularNresolution", False),
        ("Name with some whitespaces in it", "ENTRY", False),
        ("simple_name", "TEST", True),
        (".test", "TEST", False),
    ],
)
def test_namefitting(hdf_name, concept_name, should_fit):
    """Test namefitting of nexus concept names"""
    if should_fit:
        assert nexus.get_nx_namefit(hdf_name, concept_name, name_partial=True) > -1
    else:
        assert nexus.get_nx_namefit(hdf_name, concept_name, name_partial=True) == -1


@pytest.mark.parametrize(
    "hdf_name,concept_name, score",
    [
        ("test_name", "TEST_name", 9),
        ("te_name", "TEST_name", 7),
        ("my_other_name", "TEST_name", 5),
        ("test_name", "test_name", 18),
        ("test_other", "test_name", -1),
        ("my_fancy_yet_long_name", "my_SOME_name", 8),
        ("something", "XXXX", 0),
        ("something", "OTHER", 1),
    ],
)
def test_namefitting_scores(hdf_name, concept_name, score):
    """Test namefitting of nexus concept names"""
    assert nexus.get_nx_namefit(hdf_name, concept_name, name_partial=True) == score


@pytest.mark.parametrize(
    "better_fit,better_ref,worse_fit,worse_ref",
    [
        ("sourcetype", "sourceTYPE", "source_pump", "sourceTYPE"),
        ("source_pump", "sourceTYPE", "source_pump", "TEST"),
    ],
)
def test_namefitting_precedence(better_fit, better_ref, worse_fit, worse_ref):
    """Test if namefitting follows proper precedence rules"""

    assert nexus.get_nx_namefit(
        better_fit, better_ref, name_partial=True
    ) > nexus.get_nx_namefit(worse_fit, worse_ref)


@pytest.mark.parametrize(
    "string_obj, decode, expected",
    [
        # Test with lists of bytes and strings
        ([b"bytes", "string"], True, ["bytes", "string"]),
        ([b"bytes", "string"], False, [b"bytes", "string"]),
        ([b"bytes", b"more_bytes", "string"], True, ["bytes", "more_bytes", "string"]),
        (
            [b"bytes", b"more_bytes", "string"],
            False,
            [b"bytes", b"more_bytes", "string"],
        ),
        ([b"fixed", b"length", b"strings"], True, ["fixed", "length", "strings"]),
        ([b"fixed", b"length", b"strings"], False, [b"fixed", b"length", b"strings"]),
        # Test with nested lists
        ([[b"nested1"], [b"nested2"]], True, [["nested1"], ["nested2"]]),
        ([[b"nested1"], [b"nested2"]], False, [[b"nested1"], [b"nested2"]]),
        # Test with bytes
        (b"single", True, "single"),
        (b"single", False, b"single"),
        # Test with str
        ("single", True, "single"),
        ("single", False, "single"),
        # Test with int
        (123, True, 123),
        (123, False, 123),
    ],
)
def test_decode_or_not(string_obj, decode, expected):
    # Handle normal cases
    result = nexus.decode_or_not(elem=string_obj, decode=decode)
    if isinstance(expected, list):
        assert isinstance(result, list), f"Expected list, but got {type(result)}"
    # Handle all other cases
    else:
        assert result == expected, f"Failed for {string_obj} with decode={decode}"
