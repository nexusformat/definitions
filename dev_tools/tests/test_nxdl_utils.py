"""This is a code that performs several tests on nexus tool

"""

import os

import lxml.etree as ET

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


def test_get_node_at_nxdl_path():
    """Test to verify if we receive the right XML element for a given NXDL path"""
    local_dir = os.path.abspath(os.path.dirname(__file__))
    nxdl_file_path = os.path.join(local_dir, "./NXtest.nxdl.xml")
    elem = ET.parse(nxdl_file_path).getroot()
    node = nexus.get_node_at_nxdl_path("/ENTRY/NXODD_name", elem=elem)
    assert node.attrib["type"] == "NXdata"
    assert node.attrib["name"] == "NXODD_name"

    node = nexus.get_node_at_nxdl_path("/ENTRY/NXODD_name/float_value", elem=elem)
    assert node.attrib["type"] == "NX_FLOAT"
    assert node.attrib["name"] == "float_value"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/NXODD_name/AXISNAME/long_name", elem=elem
    )
    assert node.attrib["name"] == "long_name"

    nxdl_file_path = os.path.join(local_dir, "../../applications/NXem.nxdl.xml")
    elem = ET.parse(nxdl_file_path).getroot()
    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/end_time", elem=elem
    )
    assert node.attrib["name"] == "end_time"

    node = nexus.get_node_at_nxdl_path("/ENTRY/measurement", elem=elem)
    assert node.attrib["type"] == "NXem_msr"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d",
        elem=elem,
    )
    assert node.attrib["type"] == "NXdata"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d/AXISNAME_indices",
        elem=elem,
    )
    assert node.attrib["name"] == "AXISNAME_indices"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_SET/image_3d/axis_j",
        elem=elem,
    )
    assert node.attrib["type"] == "NX_NUMBER"

    node = nexus.get_node_at_nxdl_path("/ENTRY/coordinate_system_set", elem=elem)
    assert node.attrib["type"] == "NXcoordinate_system_set"


def test_get_inherited_nodes():
    """Test to verify if we receive the right XML element list for a given NXDL path."""
    local_dir = os.path.abspath(os.path.dirname(__file__))
    nxdl_file_path = os.path.join(local_dir, "./NXtest.nxdl.xml")
    elem = ET.parse(nxdl_file_path).getroot()
    (_, _, elist) = nexus.get_inherited_nodes(nxdl_path="/ENTRY/NXODD_name", elem=elem)
    assert len(elist) == 3
