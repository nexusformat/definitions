from click.testing import CliRunner

from ..nyaml2nxdl import nyaml2nxdl as conv
from ..utils.nxdl_utils import find_definition_file


def test_conversion():
    root = find_definition_file("NXentry")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(root)])
    assert result.exit_code == 0
    # Replace suffixes
    yaml = root.with_suffix("").with_suffix(".yaml")  # replace .nxdl.xml
    yaml = yaml.with_name(yaml.stem + "_parsed.yaml")  # extend file name with _parsed
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(yaml)])
    assert result.exit_code == 0
    new_root = yaml.with_suffix(".nxdl.xml")  # replace yaml
    with open(root, encoding="utf-8", mode="r") as tmp_f:
        root_content = tmp_f.readlines()
    with open(new_root, encoding="utf-8", mode="r") as tmp_f:
        new_root_content = tmp_f.readlines()
    assert root_content == new_root_content
    yaml.unlink()
    new_root.unlink()
