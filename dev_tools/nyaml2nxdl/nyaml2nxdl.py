#!/usr/bin/env python3
"""Main file of nyaml2nxdl tool.
Users create NeXus instances by writing a YAML file
which details a hierarchy of data/metadata elements

"""
# -*- coding: utf-8 -*-
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
import xml.etree.ElementTree as ET

import click

from .nyaml2nxdl_backward_tools import Nxdl2yaml
from .nyaml2nxdl_backward_tools import compare_niac_and_my
from .nyaml2nxdl_forward_tools import nyaml2nxdl
from .nyaml2nxdl_forward_tools import pretty_print_xml
from .nyaml2nxdl_helper import extend_yamlfile_by_nxdl_as_comment
from .nyaml2nxdl_helper import get_sha256_hash
from .nyaml2nxdl_helper import separate_hash_yaml_and_nxdl

DEPTH_SIZE = 4 * " "

# NOTE: Some handful links for nyaml2nxdl converter:
# https://manual.nexusformat.org/nxdl_desc.html?highlight=optional


def generate_nxdl_or_retrieve_nxdl(yaml_in, xml_out, verbose):
    """
    Generate yaml, nxdl, and hash.
        If the extracted hash is exactly the same as generated from input yaml then
        retrieve the nxdl part from provided yaml and return nxdl as output.
        Else, generate nxdl from input yaml with the help of nyaml2nxdl function
    """

    file_path, rel_file = os.path.split(yaml_in)
    sep_yaml = os.path.join(file_path, f"temp_{rel_file}")
    hash_found = separate_hash_yaml_and_nxdl(yaml_in, sep_yaml, xml_out)

    if hash_found:
        gen_hash = get_sha256_hash(sep_yaml)
        if hash_found == gen_hash:
            os.remove(sep_yaml)
            return

    nyaml2nxdl(sep_yaml, xml_out, verbose)
    os.remove(sep_yaml)


# pylint: disable=too-many-locals
def append_yml(input_file, append, verbose):
    """Append to an existing NeXus base class new elements provided in YML input file \
and print both an XML and YML file of the extended base class.

"""
    nexus_def_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../../definitions"
    )
    assert [
        s
        for s in os.listdir(os.path.join(nexus_def_path, "base_classes"))
        if append.strip() == s.replace(".nxdl.xml", "")
    ], "Your base class extension does not match any existing NeXus base classes"
    tree = ET.parse(
        os.path.join(nexus_def_path + "/base_classes", append + ".nxdl.xml")
    )
    root = tree.getroot()
    # warning: tmp files are printed on disk and removed at the ends!!
    pretty_print_xml(root, "tmp.nxdl.xml")
    input_tmp_xml = "tmp.nxdl.xml"
    out_tmp_yml = "tmp_parsed.yaml"
    converter = Nxdl2yaml([], [])
    converter.print_yml(input_tmp_xml, out_tmp_yml, verbose)
    nyaml2nxdl(input_file=out_tmp_yml, out_file="tmp_parsed.nxdl.xml", verbose=verbose)
    tree = ET.parse("tmp_parsed.nxdl.xml")
    tree2 = ET.parse(input_file)
    root_no_duplicates = ET.Element(
        "definition",
        {
            "xmlns": "http://definition.nexusformat.org/nxdl/3.1",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
    for attribute_keys in root.attrib.keys():
        if (
            attribute_keys
            != "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"
        ):
            attribute_value = root.attrib[attribute_keys]
            root_no_duplicates.set(attribute_keys, attribute_value)
    for elems in root.iter():
        if "doc" in elems.tag:
            root_doc = ET.SubElement(root_no_duplicates, "doc")
            root_doc.text = elems.text
            break
    group = "{http://definition.nexusformat.org/nxdl/3.1}group"
    root_no_duplicates = compare_niac_and_my(
        tree, tree2, verbose, group, root_no_duplicates
    )
    field = "{http://definition.nexusformat.org/nxdl/3.1}field"
    root_no_duplicates = compare_niac_and_my(
        tree, tree2, verbose, field, root_no_duplicates
    )
    attribute = "{http://definition.nexusformat.org/nxdl/3.1}attribute"
    root_no_duplicates = compare_niac_and_my(
        tree, tree2, verbose, attribute, root_no_duplicates
    )
    pretty_print_xml(
        root_no_duplicates,
        f"{input_file.replace('.nxdl.xml', '')}" f"_appended.nxdl.xml",
    )

    input_file_xml = input_file.replace(".nxdl.xml", "_appended.nxdl.xml")
    out_file_yml = input_file.replace(".nxdl.xml", "_appended_parsed.yaml")
    converter = Nxdl2yaml([], [])
    converter.print_yml(input_file_xml, out_file_yml, verbose)
    nyaml2nxdl(
        input_file=out_file_yml,
        out_file=out_file_yml.replace(".yaml", ".nxdl.xml"),
        verbose=verbose,
    )
    os.rename(
        f"{input_file.replace('.nxdl.xml', '_appended_parsed.yaml')}",
        f"{input_file.replace('.nxdl.xml', '_appended.yaml')}",
    )
    os.rename(
        f"{input_file.replace('.nxdl.xml', '_appended_parsed.nxdl.xml')}",
        f"{input_file.replace('.nxdl.xml', '_appended.nxdl.xml')}",
    )
    os.remove("tmp.nxdl.xml")
    os.remove("tmp_parsed.yaml")
    os.remove("tmp_parsed.nxdl.xml")


def split_name_and_extension(file_name):
    """
    Split file name into extension and rest of the file name.
    return file raw nam and extension
    """
    path = file_name.rsplit("/", 1)
    (pathn, filen) = ["", path[0]] if len(path) == 1 else [path[0] + "/", path[1]]
    parts = filen.rsplit(".", 2)
    raw = ext = ""
    if len(parts) == 2:
        raw = parts[0]
        ext = parts[1]
    elif len(parts) == 3:
        raw = parts[0]
        ext = ".".join(parts[1:])

    return pathn + raw, ext


@click.command()
@click.option(
    "--input-file",
    required=True,
    prompt=True,
    help="The path to the XML or YAML input data file to read and create \
a YAML or XML file from, respectively.",
)
@click.option(
    "--append",
    help="Parse xml file and append to base class, given that the xml file has same name \
of an existing base class",
)
@click.option(
    "--check-consistency",
    is_flag=True,
    default=False,
    help=(
        "Check wether yaml or nxdl has followed general rules of scema or not"
        "check whether your comment in the right place or not. The option render an "
        "output file of the same extension(*_consistency.yaml or *_consistency.nxdl.xml)"
    ),
)
@click.option(
    "--do-not-store-nxdl",
    is_flag=True,
    default=True,
    help=(
        "Whether the input nxdl file will be stored as a comment"
        " at the end of output yaml file."
    ),
)
@click.option(
    "--verbose",
    is_flag=True,
    default=False,
    help="Print in standard output keywords and value types to help \
possible issues in yaml files",
)
def launch_tool(input_file, verbose, append, do_not_store_nxdl, check_consistency):
    """
    Main function that distiguishes the input file format and launches the tools.
    """
    if os.path.isfile(input_file):
        raw_name, ext = split_name_and_extension(input_file)
    else:
        raise ValueError("Need a valid input file.")

    if ext == "yaml":
        xml_out_file = raw_name + ".nxdl.xml"
        generate_nxdl_or_retrieve_nxdl(input_file, xml_out_file, verbose)
        if append:
            append_yml(raw_name + ".nxdl.xml", append, verbose)
        # For consistency running
        if check_consistency:
            yaml_out_file = raw_name + "_consistency." + ext
            converter = Nxdl2yaml([], [])
            converter.print_yml(xml_out_file, yaml_out_file, verbose)
            os.remove(xml_out_file)
    elif ext == "nxdl.xml":
        if not append:
            yaml_out_file = raw_name + "_parsed" + ".yaml"
            converter = Nxdl2yaml([], [])
            converter.print_yml(input_file, yaml_out_file, verbose)
            # Store nxdl.xml file in output yaml file under SHA HASH
            yaml_hash = get_sha256_hash(yaml_out_file)
            # Lines as divider between yaml and nxdl
            top_lines = [
                (
                    "\n# ++++++++++++++++++++++++++++++++++ SHA HASH"
                    " ++++++++++++++++++++++++++++++++++\n"
                ),
                f"# {yaml_hash}\n",
            ]
            if do_not_store_nxdl:
                extend_yamlfile_by_nxdl_as_comment(
                    yaml_file=yaml_out_file,
                    file_to_be_appended=input_file,
                    top_lines_list=top_lines,
                )
        else:
            append_yml(input_file, append, verbose)
        # Taking care of consistency running
        if check_consistency:
            xml_out_file = raw_name + "_consistency." + ext
            generate_nxdl_or_retrieve_nxdl(yaml_out_file, xml_out_file, verbose)
            os.remove(yaml_out_file)
    else:
        raise ValueError("Provide correct file with extension '.yaml or '.nxdl.xml")


if __name__ == "__main__":
    launch_tool().parse()  # pylint: disable=no-value-for-parameter
