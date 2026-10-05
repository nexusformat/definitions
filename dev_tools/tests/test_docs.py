import pytest

from ..docs import AnchorRegistry
from ..docs import NXClassDocGenerator
from ..docs import XSDDocGenerator
from ..docs import nxdl_indices
from ..globals.directories import get_xsd_file
from ..nxdl import find_definition
from ..nxdl import iter_definitions
from .utils import pytest_path_param_id


@pytest.fixture(scope="module")
def doc_generator():
    return NXClassDocGenerator()


@pytest.fixture(scope="module")
def anchor_registry():
    return AnchorRegistry()


@pytest.fixture(scope="module")
def anchor_registry_write(tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("registry")
    reg = AnchorRegistry(output_path=tmpdir)
    yield reg
    reg.write()


@pytest.mark.parametrize(
    "nxdl_file", list(iter_definitions()), ids=pytest_path_param_id
)
def test_nxdl_generate_doc(nxdl_file, doc_generator):
    assert doc_generator(nxdl_file)


@pytest.mark.parametrize(
    "nxdl_file", list(iter_definitions()), ids=pytest_path_param_id
)
def test_nxdl_anchor_list(nxdl_file, doc_generator, anchor_registry):
    assert doc_generator(nxdl_file, anchor_registry=anchor_registry)


@pytest.mark.parametrize(
    "nxdl_file", list(iter_definitions()), ids=pytest_path_param_id
)
def test_nxdl_anchor_write_list(nxdl_file, doc_generator, anchor_registry_write):
    assert doc_generator(nxdl_file, anchor_registry=anchor_registry_write)


def test_nxdl_indices():
    sections = nxdl_indices(write_rst=False)
    expected = {"base_classes", "applications", "contributed_definitions"}
    assert set(sections) == expected


def test_xsd_generate_doc():
    generator = XSDDocGenerator()
    assert generator(get_xsd_file())


def test_nxdl_generate_doc_field_attributes(doc_generator):
    rst = "".join(doc_generator(find_definition("NXobject")))
    assert "**Attributes of every field**:" in rst
    assert ".. _/NXobject/fieldAttributes@target-attribute:" in rst


def test_nxdl_generate_doc_value_from(doc_generator):
    rst = "".join(doc_generator(find_definition("NXroot")))
    assert "Obligatory value: ``NXroot``" in rst


def test_nxdl_generate_doc_inherited_value_from(doc_generator):
    rst = "".join(doc_generator(find_definition("NXdetector")))
    assert ".. _/NXdetector@NX_class-attribute:" in rst
    assert "Obligatory value: ``NXdetector``" in rst


def test_nxdl_generate_doc_link(doc_generator):
    rst = "".join(doc_generator(find_definition("NXtomo")))
    assert ".. _/NXtomo/ENTRY/data/image_key-link:" in rst
