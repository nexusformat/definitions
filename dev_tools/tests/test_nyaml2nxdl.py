import os

from click.testing import CliRunner

from ..nyaml2nxdl import nyaml2nxdl as conv
from ..utils.nxdl_utils import find_definition_file

# import subprocess


def test_conversion():
    root = find_definition_file("NXentry")
    # subprocess.run(["python3","-m","dev_tools.nyaml2nxdl.nyaml2nxdl","--input-file",root])
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", root])
    assert result.exit_code == 0
    yaml = root[:-9] + "_parsed.yaml"
    # subprocess.run(["python3","-m","dev_tools.nyaml2nxdl.nyaml2nxdl","--input-file",yaml])
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", yaml])
    assert result.exit_code == 0
    new_root = yaml[:-4] + "nxdl.xml"
    with open(root, encoding="utf-8", mode="r") as tmp_f:
        root_content = tmp_f.readlines()
    with open(new_root, encoding="utf-8", mode="r") as tmp_f:
        new_root_content = tmp_f.readlines()
    assert root_content == new_root_content
    os.remove(yaml)
    os.remove(new_root)
