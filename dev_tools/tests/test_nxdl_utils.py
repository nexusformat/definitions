"""This is a code that performs several tests on nexus tool"""

#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

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

    nxdl_file_path = os.path.join(
        local_dir, "../../contributed_definitions/NXem.nxdl.xml"
    )
    elem = ET.parse(nxdl_file_path).getroot()
    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/end_time", elem=elem
    )
    assert node.attrib["name"] == "end_time"

    node = nexus.get_node_at_nxdl_path("/ENTRY/measurement", elem=elem)
    assert node.attrib["type"] == "NXem_msr"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_C_SET/image_threed",
        elem=elem,
    )
    assert node.attrib["type"] == "NXdata"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_C_SET/image_threed/AXISNAME_indices",
        elem=elem,
    )
    assert node.attrib["name"] == "AXISNAME_indices"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/measurement/EVENT_DATA_EM_SET/EVENT_DATA_EM/IMAGE_C_SET/image_threed/axis_j",
        elem=elem,
    )
    assert node.attrib["type"] == "NX_NUMBER"

    node = nexus.get_node_at_nxdl_path("/ENTRY/coordinate_system_set", elem=elem)
    assert node.attrib["type"] == "NXcoordinate_system_set"

    nxdl_file_path = os.path.join(
        local_dir, "../../contributed_definitions/NXiv_temp.nxdl.xml"
    )
    elem = ET.parse(nxdl_file_path).getroot()
    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller", elem=elem
    )
    assert node.attrib["name"] == "voltage_controller"

    node = nexus.get_node_at_nxdl_path(
        "/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller/calibration_time", elem=elem
    )
    assert node.attrib["name"] == "calibration_time"


def test_get_inherited_nodes():
    """Test to verify if we receive the right XML element list for a given NXDL path."""
    local_dir = os.path.abspath(os.path.dirname(__file__))
    nxdl_file_path = os.path.join(
        local_dir, "../../contributed_definitions/NXiv_temp.nxdl.xml"
    )
    elem = ET.parse(nxdl_file_path).getroot()
    (_, _, elist) = nexus.get_inherited_nodes(
        nxdl_path="/ENTRY/INSTRUMENT/ENVIRONMENT", elem=elem
    )
    assert len(elist) == 3

    (_, _, elist) = nexus.get_inherited_nodes(
        nxdl_path="/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller", elem=elem
    )
    assert len(elist) == 4

    (_, _, elist) = nexus.get_inherited_nodes(
        nxdl_path="/ENTRY/INSTRUMENT/ENVIRONMENT/voltage_controller",
        nx_name="NXiv_temp",
    )
    assert len(elist) == 4


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
        assert nexus.get_nx_namefit(hdf_name, concept_name) > -1
    else:
        assert nexus.get_nx_namefit(hdf_name, concept_name) == -1


@pytest.mark.parametrize(
    "hdf_name,concept_name, score",
    [
        ("test_name", "TEST_name", 9),
        ("te_name", "TEST_name", 7),
        ("my_other_name", "TEST_name", 5),
        ("test_name", "test_name", 18),
        ("test_other", "test_name", -1),
        ("my_fancy_yet_long_name", "my_SOME_name", 8),
    ],
)
def test_namefitting_scores(hdf_name, concept_name, score):
    """Test namefitting of nexus concept names"""
    assert nexus.get_nx_namefit(hdf_name, concept_name) == score


@pytest.mark.parametrize(
    "better_fit,better_ref,worse_fit,worse_ref",
    [
        ("sourcetype", "sourceTYPE", "source_pump", "sourceTYPE"),
        ("source_pump", "sourceTYPE", "source_pump", "TEST"),
    ],
)
def test_namefitting_precedence(better_fit, better_ref, worse_fit, worse_ref):
    """Test if namefitting follows proper precedence rules"""

    assert nexus.get_nx_namefit(better_fit, better_ref) > nexus.get_nx_namefit(
        worse_fit, worse_ref
    )
