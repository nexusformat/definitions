import pytest

from ..nxdl import find_definition
from ..nxdl import iter_definitions
from ..nxdl import nxdl_schema
from ..nxdl import validate_definition


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


@pytest.mark.parametrize("nxdl_file", list(iter_definitions()))
def test_nxdl_syntax(nxdl_file, xml_schema):
    validate_definition(nxdl_file, xml_schema)
