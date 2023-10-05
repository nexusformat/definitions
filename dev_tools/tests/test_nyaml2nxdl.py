import os

from click.testing import CliRunner

from ..nyaml2nxdl import nyaml2nxdl as conv
from ..utils.nxdl_utils import find_definition_file


def test_conversion():
    root = find_definition_file("NXentry")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", root])
    assert result.exit_code == 0
    # Replace suffixes
    yaml = root.with_suffix('').with_suffix('.yaml')
    yaml = yaml.with_stem(yaml.stem + "_parsed")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", yaml])
    assert result.exit_code == 0
    new_root = yaml.with_suffix(".nxdl.xml")
    with open(root, encoding="utf-8", mode="r") as tmp_f:
        root_content = tmp_f.readlines()
    with open(new_root, encoding="utf-8", mode="r") as tmp_f:
        new_root_content = tmp_f.readlines()
    assert root_content == new_root_content
    os.remove(yaml)
    os.remove(new_root)
