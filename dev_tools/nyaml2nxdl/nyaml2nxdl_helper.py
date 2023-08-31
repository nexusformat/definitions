#!/usr/bin/env python3
"""Main file of yaml2nxdl tool.
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


# Yaml library does not except the keys (escapechar "\t" and yaml separator ":")
# So the corresponding value is to skip them and
# and also carefull about this order
import hashlib

from yaml.composer import Composer
from yaml.constructor import Constructor
from yaml.loader import Loader
from yaml.nodes import ScalarNode
from yaml.resolver import BaseResolver

# NOTE: If any one change one of the bellow dict please change it for both
ESCAPE_CHAR_DICT_IN_YAML = {"\t": "    ", "':'": ":"}

ESCAPE_CHAR_DICT_IN_XML = {"    ": "\t", "':'": ":"}


def remove_namespace_from_tag(tag):
    """Helper function to remove the namespace from an XML tag."""

    return tag.split("}")[-1]


class LineLoader(Loader):  # pylint: disable=too-many-ancestors
    """
    LineLoader parses a yaml into a python dictionary extended with extra items.
    The new items have as keys __line__<yaml_keyword> and as values the yaml file line number
    """

    def compose_node(self, parent, index):
        # the line number where the previous token has ended (plus empty lines)
        node = Composer.compose_node(self, parent, index)
        node.__line__ = self.line + 1
        return node

    def construct_mapping(self, node, deep=False):
        node_pair_lst = node.value
        node_pair_lst_for_appending = []

        for key_node in node_pair_lst:
            shadow_key_node = ScalarNode(
                tag=BaseResolver.DEFAULT_SCALAR_TAG,
                value="__line__" + key_node[0].value,
            )
            shadow_value_node = ScalarNode(
                tag=BaseResolver.DEFAULT_SCALAR_TAG, value=key_node[0].__line__
            )
            node_pair_lst_for_appending.append((shadow_key_node, shadow_value_node))

        node.value = node_pair_lst + node_pair_lst_for_appending
        return Constructor.construct_mapping(self, node, deep=deep)


def get_yaml_escape_char_dict():
    """Get escape char and the way to skip them in yaml."""
    return ESCAPE_CHAR_DICT_IN_YAML


def get_yaml_escape_char_reverter_dict():
    """To revert yaml escape char in xml constructor from yaml."""

    return ESCAPE_CHAR_DICT_IN_XML


def type_check(nx_type):
    """
    Check for nexus type if type is NX_CHAR get '' or get as it is.
    """

    if nx_type in ["NX_CHAR", ""]:
        nx_type = ""
    else:
        nx_type = f"({nx_type})"
    return nx_type


def get_node_parent_info(tree, node):
    """
    Return tuple of (parent, index) where:
    parent = node of parent within tree
    index = index of node under parent
    """

    parent_map = {c: p for p in tree.iter() for c in p}
    parent = parent_map[node]
    return parent, list(parent).index(node)


def cleaning_empty_lines(line_list):
    """
    Cleaning up empty lines on top and bottom.
    """
    if not isinstance(line_list, list):
        line_list = line_list.split("\n") if "\n" in line_list else [""]

    # Clining up top empty lines
    while True:
        if line_list[0].strip():
            break
        line_list = line_list[1:]
        if len(line_list) == 0:
            line_list.append("")
            return line_list

    # Clining bottom empty lines
    while True:
        if line_list[-1].strip():
            break
        line_list = line_list[0:-1]
        if len(line_list) == 0:
            line_list.append("")
            return line_list

    return line_list


def nx_name_type_resolving(tmp):
    """
    extracts the eventually custom name {optional_string}
    and type {nexus_type} from a YML section string.
    YML section string syntax: optional_string(nexus_type)
    """
    if tmp.count("(") == 1 and tmp.count(")") == 1:
        # we can safely assume that every valid YML key resolves
        # either an nx_ (type, base, candidate) class contains only 1 '(' and ')'
        index_start = tmp.index("(")
        index_end = tmp.index(")", index_start + 1)
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
            lines = f2_obj.readlines()
            for line in lines:
                f1_obj.write(f"# {line}")


def separate_hash_yaml_and_nxdl(yaml_file, sep_yaml, sep_xml):
    """Separate the provided yaml file into yaml, nxdl and hash if yaml was extended with
    nxdl at the end of yaml by
        '\n# ++++++++++++++++++++++++++++++++++ SHA HASH \
            ++++++++++++++++++++++++++++++++++\n'
         # <has value>'
    """
    sha_hash = ""
    with open(yaml_file, "r", encoding="utf-8") as inp_file:
        lines = inp_file.readlines()
        # file to write yaml part
        with open(sep_yaml, "w", encoding="utf-8") as yml_f_ob, open(
            sep_xml, "w", encoding="utf-8"
        ) as xml_f_ob:
            last_line = ""
            write_on_yaml = True
            for ind, line in enumerate(lines):
                if ind == 0:
                    last_line = line
                # Write in file when ensured that the nest line is not with '++ SHA HASH ++'
                elif "++ SHA HASH ++" not in line and write_on_yaml:
                    yml_f_ob.write(last_line)
                    last_line = line
                elif "++ SHA HASH ++" in line:
                    write_on_yaml = False
                    last_line = ""
                elif not write_on_yaml and not last_line:
                    # The first line of xml file has been found. Onward write lines directly
                    # into xml file.
                    if not sha_hash:
                        sha_hash = line.split("# ", 1)[-1].strip()
                    else:
                        xml_f_ob.write(line[2:])
            # If the yaml fiile does not contain any hash for nxdl then we may have last line.
            if last_line:
                yml_f_ob.write(last_line)

    return sha_hash
