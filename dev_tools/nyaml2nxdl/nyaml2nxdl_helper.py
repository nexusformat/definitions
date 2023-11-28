#!/usr/bin/env python3
"""File consists of helping functions and variables.

The functions and variables are utilised in the converting tool
to convert from nyaml to nxdl and vice versa.
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

import hashlib
from typing import Callable

from yaml.composer import Composer
from yaml.constructor import Constructor
from yaml.loader import Loader
from yaml.nodes import ScalarNode
from yaml.resolver import BaseResolver

# Yaml library does not except the keys (escape char "\t" and yaml separator ":")
ESCAPE_CHAR_DICT_IN_YAML = {"\t": "    "}
ESCAPE_CHAR_DICT_IN_XML = {val: key for key, val in ESCAPE_CHAR_DICT_IN_YAML.items()}

# Set up attributes for nxdl version
NXDL_GROUP_ATTRIBUTES = (
    "optional",
    "recommended",
    "name",
    "type",
    "maxOccurs",
    "minOccurs",
    "deprecated",
)
NXDL_FIELD_ATTRIBUTES = (
    "optional",
    "recommended",
    "name",
    "type",
    "axes",
    "axis",
    "data_offset",
    "interpretation",
    "long_name",
    "maxOccurs",
    "minOccurs",
    "nameType",
    "primary",
    "signal",
    "stride",
    "required",
    "deprecated",
    "units",
)

NXDL_ATTRIBUTES_ATTRIBUTES = (
    "name",
    "type",
    "recommended",
    "optional",
    "deprecated",
)

NXDL_LINK_ATTRIBUTES = ("name", "target", "napimount")

# Set up attributes for yaml version
YAML_GROUP_ATTRIBUTES = (*NXDL_GROUP_ATTRIBUTES, "exists")

YAML_FIELD_ATTRIBUTES = (*NXDL_FIELD_ATTRIBUTES[0:-1], "unit", "exists")

YAML_ATTRIBUTES_ATTRIBUTES = (
    *NXDL_ATTRIBUTES_ATTRIBUTES,
    "minOccurs",
    "maxOccurs",
    "exists",
)

YAML_LINK_ATTRIBUTES = NXDL_LINK_ATTRIBUTES


def remove_namespace_from_tag(tag):
    """Helper function to remove the namespace from an XML tag."""
    if isinstance(tag, Callable) and tag.__name__ == "Comment":
        return "!--"
    else:
        return tag.split("}")[-1]


class LineLoader(Loader):  # pylint: disable=too-many-ancestors
    """Class to load yaml file with extra non yaml items.

    LineLoader parses a yaml into a python dictionary extended with extra items.
    The new items have as keys __line__<yaml_keyword> and as values the yaml file line number
    """

    def compose_node(self, parent, index):
        """Compose node and return node."""
        # the line number where the previous token has ended (plus empty lines)
        node = Composer.compose_node(self, parent, index)
        node.__line__ = self.line + 1
        return node

    def construct_mapping(self, node, deep=False):
        """Construct mapping between node info and line info."""
        node_pair_lst_for_appending = []

        # Visit through node-pair list
        for key_node in node.value:
            shadow_key_node = ScalarNode(
                tag=BaseResolver.DEFAULT_SCALAR_TAG,
                value="__line__" + key_node[0].value,
            )
            shadow_value_node = ScalarNode(
                tag=BaseResolver.DEFAULT_SCALAR_TAG, value=key_node[0].__line__
            )
            node_pair_lst_for_appending.append((shadow_key_node, shadow_value_node))

        node.value = node.value + node_pair_lst_for_appending
        return Constructor.construct_mapping(self, node, deep=deep)


def get_yaml_escape_char_dict():
    """Get escape char and the way to skip them in yaml."""
    return ESCAPE_CHAR_DICT_IN_YAML


def get_yaml_escape_char_reverter_dict():
    """To revert yaml escape char in xml constructor from yaml."""

    return ESCAPE_CHAR_DICT_IN_XML


def type_check(nx_type):
    """Check for nexus type if type is NX_CHAR get '' or get as it is."""

    if nx_type in ["NX_CHAR", ""]:
        nx_type = ""
    else:
        nx_type = f"({nx_type})"
    return nx_type


def get_node_parent_info(tree, node):
    """Return tuple of (parent, index).

    parent = parent node is the first level node under tree node
    index = index of grand child node of tree
    """

    # map from grand child to parent which is child of tree
    parent_map = {c: p for p in tree.iter() for c in p}
    parent = parent_map[node]
    return parent, list(parent).index(node)


def clean_empty_lines(line_list):
    """Clean up empty lines by top part and bottom and part."""
    if not isinstance(line_list, list):
        line_list = line_list.split("\n") if "\n" in line_list else [""]

    start_non_empty_line = -1
    ends_non_empty_line = None
    # Find the index of first non-empty line
    for ind, line in enumerate(line_list):
        if len(line.strip()) > 1:
            start_non_empty_line = ind
            break

    # Find the index of the last non-empty line
    for ind, line in enumerate(reversed(line_list)):
        if len(line.strip()) > 1:
            ends_non_empty_line = -ind
            break

    if ends_non_empty_line == 0:
        ends_non_empty_line = None
    return line_list[start_non_empty_line:ends_non_empty_line]


def nx_name_type_resolving(tmp):
    """Separate name and NeXus type

    Extracts the eventual custom name {optional_string}
    and type {nexus_type} from a YML section string.
    YML section string syntax: optional_string(nexus_type)
    """
    if tmp.count("(") == 1 and tmp.count(")") == 1:
        # we can safely assume that every valid YML key resolves
        # either an nx_ (type, base, candidate) class contains only 1 '(' and ')'
        index_start = tmp.index("(")
        index_end = tmp.index(")", index_start + 1)
        if index_start > index_end:
            raise ValueError(
                f"Check name and type combination {tmp} which can not be resolved."
            )
        if index_end - index_start == 1:
            raise ValueError(
                f"Check name(type) combination {tmp}, properly not defined."
            )
        typ = tmp[index_start + 1 : index_end]
        nam = tmp.replace("(" + typ + ")", "")
        return nam, typ

    # or a name for a member
    typ = ""
    nam = tmp
    return nam, typ


def get_sha256_hash(file_name):
    """Generate a sha256_hash for a given file."""
    sha_hash = hashlib.sha256()

    with open(
        file=file_name,
        mode="rb",
    ) as file_obj:
        # Update hash for each 4k block of bytes
        for b_line in iter(lambda: file_obj.read(4096), b""):
            sha_hash.update(b_line)
    return sha_hash.hexdigest()


def extend_yamlfile_by_nxdl_as_comment(
    yaml_file, file_to_be_appended, top_lines_list=None
):
    """Extend yaml file by the file_to_be_appended as comment."""

    with open(yaml_file, mode="a+", encoding="utf-8") as f1_obj:
        if top_lines_list:
            for line in top_lines_list:
                f1_obj.write(line)

        with open(file_to_be_appended, mode="r", encoding="utf-8") as f2_obj:
            for line in f2_obj:
                f1_obj.write(f"# {line}")


def separate_hash_yaml_and_nxdl(yaml_file, sep_yaml, sep_xml):
    """Separate yaml, SHA hash and nxdl parts.

    Separate the provided yaml file into yaml, nxdl and hash if yaml was extended with
    nxdl at the end of yaml as

                    <yaml part>
        '\n# ++++++++++++++++++++++++++++++++++ SHA HASH \
            ++++++++++++++++++++++++++++++++++\n'
         # <has value>'
                    <nxdl part>
    """
    sha_hash = ""
    with open(yaml_file, "r", encoding="utf-8") as inp_file:
        lines = inp_file.readlines()
        # file to write yaml part
        with open(sep_yaml, "w", encoding="utf-8") as yml_f_ob, open(
            sep_xml, "w", encoding="utf-8"
        ) as xml_f_ob:
            write_on_yaml = True

            last_line = lines[0]
            for line in lines[1:]:
                # Write in file when ensured that the next line is not with '++ SHA HASH ++'
                if "++ SHA HASH ++" not in line and write_on_yaml:
                    yml_f_ob.write(last_line)
                    last_line = line
                elif "++ SHA HASH ++" in line:
                    write_on_yaml = False
                    last_line = ""
                elif not write_on_yaml and not last_line:
                    # The first line of xml file has been found so in future write lines directly
                    # into xml file.
                    if not sha_hash:
                        sha_hash = line.split("# ", 1)[-1].strip()
                    else:
                        xml_f_ob.write(line[2:])
            # If the yaml fiile does not contain any hash for nxdl then we may have last line.
            if last_line:
                yml_f_ob.write(last_line)

    return sha_hash


def is_dom_comment(text):
    """Analyze a comment, whether it is a dom comment or not.

    Return true if dom comment.
    """

    # some signature keywords to distingush dom comments from other comments.
    signature_keyword_list = [
        "NeXus",
        "GNU Lesser General Public",
        "Free Software Foundation",
        "Copyright (C)",
        "WITHOUT ANY WARRANTY",
    ]
    for keyword in signature_keyword_list:
        if keyword not in text:
            return False

    return True
