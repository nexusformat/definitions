import shutil
from pathlib import Path
from typing import List

from ..docs import AnchorRegistry
from ..docs import NXClassDocGenerator
from ..globals import directories
from ..nxdl import find_definition
from ..nxdl import validate_definition
from ..utils.diff import diff_ascii


def nxclass_args(parser):
    parser.add_argument(
        "name",
        type=str,
        help="NeXus class name (For example 'nxdata')",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Validate the NeXus class definition",
    )
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Save the NeXus class documentation in the build directory",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Print changes in the NeXus class documentation",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Print the NeXus class documentation",
    )


def nxclass_exec(args):
    nxdl_file = find_definition(args.name)
    assert nxdl_file, f"No definition found for {args.name}"

    if args.test:
        validate_definition(nxdl_file)

    if args.prepare or args.diff or args.print:
        generator = NXClassDocGenerator()
        if args.prepare:
            output_path = directories.manual_build_staticroot()
        else:
            output_path = None
        anchor_registry = AnchorRegistry(output_path=output_path)
        rst_lines = generator(nxdl_file, anchor_registry=anchor_registry)

    if args.prepare:
        save_nxclass_docs(nxdl_file, rst_lines)
        print("add to anchor list files in", output_path)
        anchor_registry.write()

    if args.diff:
        diff_nxclass_docs(nxdl_file, rst_lines)

    if args.print:
        print("".join(rst_lines))


def save_nxclass_docs(nxdl_file: Path, rst_lines: List[str]) -> None:
    """Build the NXDL file: this means prepare the documentation
    and resources in the build directory.
    """
    rst_file_name = directories.get_rst_filename(nxdl_file)

    # Save the documentation in the build directory
    print("generate", nxdl_file)
    print("      ->", rst_file_name)
    rst_file_name.parent.mkdir(parents=True, exist_ok=True)
    with open(rst_file_name, "w") as fh:
        fh.writelines(rst_lines)

    # Copy resources to the build directory
    resource_name = rst_file_name.stem[2:]  # (e.g. NXaperture -> aperture)
    nxdl_resource_dir = nxdl_file.parent / resource_name
    if nxdl_resource_dir.is_dir():
        rst_resource_dir = rst_file_name.parent / resource_name
        print("copy", nxdl_resource_dir)
        print("  ->", rst_resource_dir)
        shutil.copytree(nxdl_resource_dir, rst_resource_dir, dirs_exist_ok=True)

    # Copy the NXDL file as it might be used in a "literalinclude"
    nxdl_file2 = rst_file_name.parent / nxdl_file.name
    print("generate", nxdl_file)
    print("      ->", nxdl_file2)
    shutil.copyfile(nxdl_file, nxdl_file2)


def diff_nxclass_docs(nxdl_file: Path, rst_lines: List[str]) -> None:
    """Build the NXDL file: this means prepare the documentation
    and resources in the build directory.
    """
    rst_file_name = directories.get_rst_filename(nxdl_file)
    diff_ascii(nxdl_file, rst_lines, rst_file_name)
