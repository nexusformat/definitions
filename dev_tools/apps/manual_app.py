from ..docs import AnchorRegistry
from ..docs import NXClassDocGenerator
from ..docs import XSDDocGenerator
from ..docs.nxdl_index import nxdl_indices
from ..docs.xsd_units import generate_xsd_units_doc
from ..globals import directories
from ..nxdl import iter_definitions
from ..nxdl import validate_definition
from ..utils.copy import copy_files
from ..utils.copy import copydir
from ..utils.diff import diff_ascii
from .nxclass_app import diff_nxclass_docs
from .nxclass_app import save_nxclass_docs


def manual_args(parser):
    parser.add_argument(
        "--test",
        action="store_true",
        help="Validate all NeXus class definitions",
    )
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Create the build files for the NeXus Impatient Guide",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Print all changes in the generated documentation",
    )


def manual_exec(args):
    # Copy the documentation source files to the build directory
    if args.prepare:
        copydir(directories.manual_source_root(), directories.manual_build_root())

    # XSD and NXDL document generators
    generate_docs = args.prepare or args.diff
    if generate_docs:
        generator = NXClassDocGenerator()
        xsdgenerator = XSDDocGenerator()
        if args.prepare:
            output_path = directories.manual_build_staticroot()
        else:
            output_path = None
        anchor_registry = AnchorRegistry(output_path=output_path)

    # Generate the NeXus class documentation files in the build directory
    for subdir in ("base_classes", "applications", "contributed_definitions"):
        for nxdl_file in iter_definitions(subdir):
            if args.test:
                validate_definition(nxdl_file)
            if generate_docs:
                rst_lines = generator(nxdl_file, anchor_registry=anchor_registry)
            if args.diff:
                diff_nxclass_docs(nxdl_file, rst_lines)
            if args.prepare:
                save_nxclass_docs(nxdl_file, rst_lines)

    # Generate the NXDL XSD documentation in the build directory
    if generate_docs:
        xsd_file = directories.get_xsd_file()
        rst_lines = xsdgenerator(xsd_file)
        nxdl_desc = directories.manual_build_sphinxroot() / "nxdl_desc.rst"
    if args.diff:
        diff_ascii(xsd_file, rst_lines, nxdl_desc)
    if args.prepare:
        print("generate XSD documentation", nxdl_desc)
        with open(nxdl_desc, "w") as fh:
            fh.writelines(rst_lines)

    if generate_docs:
        xsd_file = directories.get_xsd_units_file()
        rst_lines = generate_xsd_units_doc(xsd_file, "anyUnitsAttr", "units")
        nxdl_desc = directories.manual_build_sphinxroot() / "units.table"
    if args.diff:
        diff_ascii(xsd_file, rst_lines, nxdl_desc)
    if args.prepare:
        print("generate XSD documentation (units)", nxdl_desc)
        with open(nxdl_desc, "w") as fh:
            fh.writelines(rst_lines)

    if generate_docs:
        xsd_file = directories.get_xsd_units_file()
        rst_lines = generate_xsd_units_doc(xsd_file, "primitiveType", "data")
        nxdl_desc = directories.manual_build_sphinxroot() / "types.table"
    if args.diff:
        diff_ascii(xsd_file, rst_lines, nxdl_desc)
    if args.prepare:
        print("generate XSD documentation (types)", nxdl_desc)
        with open(nxdl_desc, "w") as fh:
            fh.writelines(rst_lines)

    # Generate the NeXus class documentation index files in the
    # build directory so the files generated above are included in the docs.
    if generate_docs:
        for name, adict in nxdl_indices().items():
            index_file = adict["index_file"]
            rst_lines = adict["rst_lines"]
            if args.diff:
                diff_ascii(name, rst_lines, index_file)
            if args.prepare:
                print("generate NXDL index", index_file)
                if args.prepare:
                    with open(index_file, "w") as fh:
                        fh.writelines(rst_lines)

    # Generate the anchor list in several format
    if args.prepare:
        print("generate anchor list files in", output_path)
        anchor_registry.write()
        copy_files(EXTRA_FILES)


# Path relative to source directory,
# Path relative to build directory,
# Overwrite (boolean)
EXTRA_FILES = [["NXDL_VERSION", "NXDL_VERSION", True], ["LGPL.txt", "LGPL.txt", True]]
