#!/usr/bin/env python3
"""This file collects the function used in the reverse tool nxdl2yaml.

"""
import os

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
import sys
import xml.etree.ElementTree as ET
from typing import Dict
from typing import List

from .nyaml2nxdl_helper import cleaning_empty_lines
from .nyaml2nxdl_helper import get_node_parent_info
from .nyaml2nxdl_helper import get_yaml_escape_char_dict
from .nyaml2nxdl_helper import remove_namespace_from_tag

DEPTH_SIZE = "  "
CMNT_TAG = "!--"


def separate_pi_comments(input_file):
    """
    Separate PI comments from ProcessesInstruction (pi)
    """
    comments_list = []
    comment = []
    xml_lines = []

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        has_pi = True
        for line in lines:
            c_start = "<!--"
            cmnt_end = "-->"
            def_tag = "<definition"

            if c_start in line and has_pi:
                line = line.replace(c_start, "")
                if cmnt_end in line:
                    line = line.replace(cmnt_end, "")
                    comments_list.append(line)
                else:
                    comment.append(line)
            elif cmnt_end in line and len(comment) > 0 and has_pi:
                comment.append(line.replace(cmnt_end, ""))
                comments_list.append("".join(comment))
                comment = []
            elif def_tag in line or not has_pi:
                has_pi = False
                xml_lines.append(line)
            elif len(comment) > 0 and has_pi:
                comment.append(line)
            else:
                xml_lines.append(line)
    return comments_list, "".join(xml_lines)


# Collected: https://dustinoprea.com/2019/01/22/python-parsing-xml-and-retaining-the-comments/
class _CommentedTreeBuilder(ET.TreeBuilder):
    def comment(self, text):
        """
        defining comment builder in TreeBuilder
        """
        self.start("!--", {})
        self.data(text)
        self.end("--")


def parse(filepath):
    """
    Construct parse function for modified tree builder for including modified TreeBuilder
    and rebuilding XMLParser.
    """
    comments, xml_str = separate_pi_comments(filepath)
    ctb = _CommentedTreeBuilder()
    xp_parser = ET.XMLParser(target=ctb)
    root = ET.fromstring(xml_str, parser=xp_parser)
    return comments, root


def handle_mapping_char(text, depth=-1, skip_n_line_on_top=False):
    """Check for ":" char and replace it by "':'"."""

    escape_char = get_yaml_escape_char_dict()
    for esc_key, val in escape_char.items():
        if esc_key in text:
            text = text.replace(esc_key, val)
    if not skip_n_line_on_top:
        if depth > 0:
            text = add_new_line_with_pipe_on_top(text, depth)
        else:
            raise ValueError("Need depth size to co-ordinate text line in yaml file.")
    return text


def add_new_line_with_pipe_on_top(text, depth):
    """
    Return modified text for what we get error in converter, such as ':'. After adding a
    new line at the start of text the error is solved.
    """
    char_list_to_add_new_line_on_top_of_text = [":"]
    for char in char_list_to_add_new_line_on_top_of_text:
        if char in text:
            return "|" + "\n" + depth * DEPTH_SIZE + text
    return text


# pylint: disable=too-many-instance-attributes
class Nxdl2yaml:
    """
    Parse XML file and print a YML file
    """

    def __init__(
        self,
        symbol_list: List[str],
        root_level_definition: List[str],
        root_level_doc="",
        root_level_symbols="",
    ):
        # updated part of yaml_dict
        self.found_definition = False
        self.root_level_doc = root_level_doc
        self.root_level_symbols = root_level_symbols
        self.root_level_definition = root_level_definition
        self.symbol_list = symbol_list
        self.is_last_element_comment = False
        self.include_comment = True
        self.pi_comments = None
        # NOTE: Here is how root_level_comments organised for storing comments
        # root_level_comment= {'root_doc': comment,
        #                      'symbols': comment,
        #       The 'symbol_doc_comments' list is for comments from all 'symbol doc'
        #                      'symbol_doc_comments' : [comments]
        #                      'symbol_list': [symbols],
        #       The 'symbol_comments' contains comments for 'symbols doc' and all 'symbol'
        #                      'symbol_comments': [comments]}
        self.root_level_comment: Dict[str, str] = {}

    def print_yml(self, input_file, output_yml, verbose):
        """
        Parse an XML file provided as input and print a YML file
        """
        if os.path.isfile(output_yml):
            os.remove(output_yml)

        depth = 0

        self.pi_comments, root = parse(input_file)
        xml_tree = {"tree": root, "node": root}
        self.xmlparse(output_yml, xml_tree, depth, verbose)

    def handle_symbols(self, depth, node):
        """Handle symbols field and its childs symbol"""

        # pylint: disable=consider-using-f-string
        self.root_level_symbols = (
            f"{remove_namespace_from_tag(node.tag)}: "
            f"{node.text.strip() if node.text else ''}"
        )
        depth += 1
        last_comment = ""
        sbl_doc_cmnt_list = []
        # Comments that come above symbol tag
        symbol_cmnt_list = []
        for child in list(node):
            tag = remove_namespace_from_tag(child.tag)
            if tag == CMNT_TAG and self.include_comment:
                last_comment = self.comvert_to_ymal_comment(
                    depth * DEPTH_SIZE, child.text
                )
            if tag == "doc":
                symbol_cmnt_list.append(last_comment)
                # The bellow line is for handling lenth of 'symbol_comments' and
                # 'symbol_doc_comments'. Otherwise print_root_level_info() gets inconsistency
                # over for the loop while writting comment on file
                sbl_doc_cmnt_list.append("")
                last_comment = ""
                self.symbol_list.append(
                    self.handle_not_root_level_doc(depth, text=child.text)
                )
            elif tag == "symbol":
                # place holder is symbol name
                symbol_cmnt_list.append(last_comment)
                last_comment = ""
                if "doc" in child.attrib:
                    self.symbol_list.append(
                        self.handle_not_root_level_doc(
                            depth, tag=child.attrib["name"], text=child.attrib["doc"]
                        )
                    )
                else:
                    for symbol_doc in list(child):
                        tag = remove_namespace_from_tag(symbol_doc.tag)
                        if tag == CMNT_TAG and self.include_comment:
                            last_comment = self.comvert_to_ymal_comment(
                                depth * DEPTH_SIZE, symbol_doc.text
                            )
                        if tag == "doc":
                            sbl_doc_cmnt_list.append(last_comment)
                            last_comment = ""
                            self.symbol_list.append(
                                self.handle_not_root_level_doc(
                                    depth,
                                    tag=child.attrib["name"],
                                    text=symbol_doc.text,
                                )
                            )
        self.store_root_level_comments("symbol_doc_comments", sbl_doc_cmnt_list)
        self.store_root_level_comments("symbol_comments", symbol_cmnt_list)

    def store_root_level_comments(self, holder, comment):
        """Store yaml text or section line and the comments inteded for that lines or section"""

        self.root_level_comment[holder] = comment

    def handle_definition(self, node):
        """
        Handle definition group and its attributes
        NOTE: Here we tried to store the order of the xml element attributes. So that we get
        exactly the same file in nxdl from yaml.
        """
        # pylint: disable=consider-using-f-string
        # self.root_level_definition[0] = ''
        keyword = ""
        # tmp_word for reseving the location
        tmp_word = "#xx#"
        attribs = node.attrib
        # for tracking the order of name and type
        keyword_order = -1
        for item in attribs:
            if "name" in item:
                keyword = keyword + attribs[item]
                if keyword_order == -1:
                    self.root_level_definition.append(tmp_word)
                    keyword_order = self.root_level_definition.index(tmp_word)
            elif "extends" in item:
                keyword = f"{keyword}({attribs[item]})"
                if keyword_order == -1:
                    self.root_level_definition.append(tmp_word)
                    keyword_order = self.root_level_definition.index(tmp_word)
            elif "schemaLocation" not in item and "extends" != item:
                text = f"{item}: {attribs[item]}"
                self.root_level_definition.append(text)
        self.root_level_definition[keyword_order] = f"{keyword}:"

    def handle_root_level_doc(self, node):
        """
        Handle the documentation field found at root level.
        """
        # tag = remove_namespace_from_tag(node.tag)
        text = node.text
        text = self.handle_not_root_level_doc(depth=0, text=text)
        self.root_level_doc = text

    # pylint: disable=too-many-branches
    def handle_not_root_level_doc(self, depth, text, tag="doc", file_out=None):
        """
        Handle docs field along the yaml file. In this function we also tried to keep
        the track of intended indentation. E.g. the bollow doc block.
            * Topic name
                Description of topic
        """

        # Handling empty doc
        if not text:
            text = ""
        else:
            text = handle_mapping_char(text, -1, True)
        if "\n" in text:
            # To remove '\n' character as it will be added before text.
            text = cleaning_empty_lines(text.split("\n"))
            text_tmp = []
            yaml_indent_n = len((depth + 1) * DEPTH_SIZE)
            # Find indentaion in the first text line with alphabet
            tmp_i = 0
            while tmp_i != -1:
                first_line_indent_n = 0
                # Taking care of empty text whitout any character
                if len(text) == 1 and text[0] == "":
                    break
                for ch_ in text[tmp_i]:
                    if ch_ == " ":
                        first_line_indent_n = first_line_indent_n + 1
                    elif ch_ != "":
                        tmp_i = -2
                        break
                tmp_i = tmp_i + 1
            # Taking care of doc like bellow:
            # <doc>Text liness
            # text continues</doc>
            # So no indentaion at the staring or doc. So doc group will come along general
            # alignment
            if first_line_indent_n == 0:
                first_line_indent_n = yaml_indent_n

            # for indent_diff -ve all lines will move left by the same ammout
            # for indect_diff +ve all lines will move right the same amount
            indent_diff = yaml_indent_n - first_line_indent_n
            # CHeck for first line empty if not keep first line empty

            for _, line in enumerate(text):
                line_indent_n = 0
                # Collect first empty space without alphabate
                for ch_ in line:
                    if ch_ == " ":
                        line_indent_n = line_indent_n + 1
                    else:
                        break
                line_indent_n = line_indent_n + indent_diff
                if line_indent_n < yaml_indent_n:
                    # if line still under yaml identation
                    text_tmp.append(yaml_indent_n * " " + line.strip())
                else:
                    text_tmp.append(line_indent_n * " " + line.strip())

            text = "\n" + "\n".join(text_tmp)
            if "}" in tag:
                tag = remove_namespace_from_tag(tag)
            indent = depth * DEPTH_SIZE
        elif text:
            text = "\n" + (depth + 1) * DEPTH_SIZE + text.strip()
            if "}" in tag:
                tag = remove_namespace_from_tag(tag)
            indent = depth * DEPTH_SIZE
        else:
            text = ""
            if "}" in tag:
                tag = remove_namespace_from_tag(tag)
            indent = depth * DEPTH_SIZE

        doc_str = f"{indent}{tag}: |{text}\n"
        if file_out:
            file_out.write(doc_str)
            return None
        return doc_str

    def write_out(self, indent, text, file_out):
        """
        Write text line in output file.
        """
        line_string = f"{indent}{text.rstrip()}\n"
        file_out.write(line_string)

    def print_root_level_doc(self, file_out):
        """
        Print at the root level of YML file \
        the general documentation field found in XML file
        """
        indent = 0 * DEPTH_SIZE

        if (
            "root_doc" in self.root_level_comment
            and self.root_level_comment["root_doc"] != ""
        ):
            text = self.root_level_comment["root_doc"]
            self.write_out(indent, text, file_out)

        text = self.root_level_doc
        self.write_out(indent, text, file_out)
        self.root_level_doc = ""

    def comvert_to_ymal_comment(self, indent, text):
        """
        Convert into yaml comment by adding exta '#' char in front of comment lines
        """
        lines = text.split("\n")
        mod_lines = []
        for line in lines:
            line = line.strip()
            if line and line[0] != "#":
                line = indent + "# " + line
                mod_lines.append(line)
            elif line:
                line = indent + line
                mod_lines.append(line)
        # The starting '\n' to keep multiple comments separate
        return "\n" + "\n".join(mod_lines)

    def print_root_level_info(self, depth, file_out):
        """
        Print at the root level of YML file \
        the information stored as definition attributes in the XML file
        """
        # pylint: disable=consider-using-f-string
        if depth < 0:
            raise ValueError("Somthing wrong with indentaion in root level.")

        has_categoty = False
        for def_line in self.root_level_definition:
            if def_line in ("category: application", "category: base"):
                self.write_out(indent=0 * DEPTH_SIZE, text=def_line, file_out=file_out)
                # file_out.write(f"{def_line}\n")
                has_categoty = True

        if not has_categoty:
            raise ValueError(
                "Definition dose not get any category from 'base or application'."
            )
        self.print_root_level_doc(file_out)
        if (
            "symbols" in self.root_level_comment
            and self.root_level_comment["symbols"] != ""
        ):
            indent = depth * DEPTH_SIZE
            text = self.root_level_comment["symbols"]
            self.write_out(indent, text, file_out)
        if self.root_level_symbols:
            self.write_out(
                indent=0 * DEPTH_SIZE, text=self.root_level_symbols, file_out=file_out
            )
            # symbol_list include 'symbols doc', and all 'symbol'
            for ind, symbol in enumerate(self.symbol_list):
                # Taking care of comments that come on to of 'symbols doc' and 'symbol'
                if (
                    "symbol_comments" in self.root_level_comment
                    and self.root_level_comment["symbol_comments"][ind] != ""
                ):
                    indent = depth * DEPTH_SIZE
                    self.write_out(
                        indent,
                        self.root_level_comment["symbol_comments"][ind],
                        file_out,
                    )
                if (
                    "symbol_doc_comments" in self.root_level_comment
                    and self.root_level_comment["symbol_doc_comments"][ind] != ""
                ):
                    indent = depth * DEPTH_SIZE
                    self.write_out(
                        indent,
                        self.root_level_comment["symbol_doc_comments"][ind],
                        file_out,
                    )

                self.write_out(indent=(0 * DEPTH_SIZE), text=symbol, file_out=file_out)
        if len(self.pi_comments) > 1:
            indent = DEPTH_SIZE * depth
            # The first comment is top level copy-right doc string
            for comment in self.pi_comments[1:]:
                self.write_out(
                    indent, self.comvert_to_ymal_comment(indent, comment), file_out
                )
        if self.root_level_definition:
            # Soring NXname for writting end of the definition attributes
            nx_name = ""
            for defs in self.root_level_definition:
                if "NX" in defs and defs[-1] == ":":
                    nx_name = defs
                    continue
                if defs in ("category: application", "category: base"):
                    continue
                self.write_out(indent=0 * DEPTH_SIZE, text=defs, file_out=file_out)
            self.write_out(indent=0 * DEPTH_SIZE, text=nx_name, file_out=file_out)
        self.found_definition = False

    def handle_exists(self, exists_dict, key, val):
        """
        Create exist component as folows:

        {'min' : value for min,
         'max' : value for max,
         'optional' : value for optional}

        This is created separately so that the keys stays in order.
        """
        if not val:
            val = ""
        else:
            val = str(val)
        if "minOccurs" == key:
            exists_dict["minOccurs"] = ["min", val]
        if "maxOccurs" == key:
            exists_dict["maxOccurs"] = ["max", val]
        if "optional" == key:
            exists_dict["optional"] = ["optional", val]
        if "recommended" == key:
            exists_dict["recommended"] = ["recommended", val]
        if "required" == key:
            exists_dict["required"] = ["required", val]

    # pylint: disable=too-many-branches, consider-using-f-string
    def handle_group_or_field(self, depth, node, file_out):
        """Handle all the possible attributes that come along a field or group"""

        allowed_attr = [
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
            "optional",
            "primary",
            "signal",
            "stride",
            "units",
            "required",
            "deprecated",
            "exists",
        ]

        name_type = ""
        node_attr = node.attrib
        rm_key_list = []
        # Maintain order: name and type in form name(type) or (type)name that come first
        for key, val in node_attr.items():
            if key == "name":
                name_type = name_type + val
                rm_key_list.append(key)
            if key == "type":
                name_type = name_type + "(%s)" % val
                rm_key_list.append(key)
        if not name_type:
            raise ValueError(
                f"No 'name' or 'type' hase been found. But, 'group' or 'field' "
                f"must have at list a nme.We got attributes:  {node_attr}"
            )
        file_out.write(
            "{indent}{name_type}:\n".format(
                indent=depth * DEPTH_SIZE, name_type=name_type
            )
        )

        for key in rm_key_list:
            del node_attr[key]

        # tmp_dict intended to persevere order of attribnutes
        tmp_dict = {}
        exists_dict = {}
        for key, val in node_attr.items():
            # As both 'minOccurs', 'maxOccurs' and optionality move to the 'exists'
            if key in ["minOccurs", "maxOccurs", "optional", "recommended", "required"]:
                if "exists" not in tmp_dict:
                    tmp_dict["exists"] = []
                self.handle_exists(exists_dict, key, val)
            elif key == "units":
                tmp_dict["unit"] = str(val)
            else:
                tmp_dict[key] = str(val)
            if key not in allowed_attr:
                raise ValueError(
                    f"An attribute ({key}) in 'field' or 'group' has been found "
                    f"that is not allowed. The allowed attr is {allowed_attr}."
                )

        if exists_dict:
            for key, val in exists_dict.items():
                if key in ["minOccurs", "maxOccurs"]:
                    tmp_dict["exists"] = tmp_dict["exists"] + val
                elif key in ["optional", "recommended", "required"]:
                    tmp_dict["exists"] = key

        depth_ = depth + 1
        for key, val in tmp_dict.items():
            # Increase depth size inside handle_map...() for writting text with one
            # more indentation.
            file_out.write(
                f"{depth_ * DEPTH_SIZE}{key}: "
                f"{handle_mapping_char(val, depth_ + 1, False)}\n"
            )

    # pylint: disable=too-many-branches, too-many-locals
    def handle_dimension(self, depth, node, file_out):
        """
        Handle the dimension field.
            NOTE: Usually we take care of any xml element in xmlparse(...) and
        recursion_in_xml_tree(...) functions. But Here it is a bit different. The doc dimension
          and attributes of dim has been handled inside this function here.
        """
        # pylint: disable=consider-using-f-string
        possible_dim_attrs = ["ref", "required", "incr", "refindex"]
        possible_dimemsion_attrs = ["rank"]

        # taking care of Dimension tag
        file_out.write(
            "{indent}{tag}:\n".format(
                indent=depth * DEPTH_SIZE, tag=node.tag.split("}", 1)[1]
            )
        )
        # Taking care of dimension attributes
        for attr, value in node.attrib.items():
            if attr in possible_dimemsion_attrs and not isinstance(value, dict):
                indent = (depth + 1) * DEPTH_SIZE
                file_out.write(f"{indent}{attr}: {value}\n")
            else:
                raise ValueError(
                    f"Dimension has got an attribute {attr} that is not valid."
                    f"Current the allowd atributes are {possible_dimemsion_attrs}."
                    f" Please have a look"
                )
        # taking carew of dimension doc
        for child in list(node):
            tag = remove_namespace_from_tag(child.tag)
            if tag == "doc":
                text = self.handle_not_root_level_doc(depth + 1, child.text)
                file_out.write(text)
                node.remove(child)

        dim_index_value = ""
        dim_other_parts = {}
        dim_cmnt_node = []
        # taking care of dim and doc childs of dimension
        for child in list(node):
            tag = remove_namespace_from_tag(child.tag)
            child_attrs = child.attrib
            # taking care of index and value attributes
            if tag == ("dim"):
                # taking care of index and value in format [[index, value]]
                dim_index_value = dim_index_value + "[{index}, {value}], ".format(
                    index=child_attrs["index"] if "index" in child_attrs else "",
                    value=child_attrs["value"] if "value" in child_attrs else "",
                )
                if "index" in child_attrs:
                    del child_attrs["index"]
                if "value" in child_attrs:
                    del child_attrs["value"]

                # Taking care of doc comes as child of dim
                for cchild in list(child):
                    ttag = cchild.tag.split("}", 1)[1]
                    if ttag == ("doc"):
                        if ttag not in dim_other_parts:
                            dim_other_parts[ttag] = []
                        text = cchild.text
                        dim_other_parts[ttag].append(text.strip())
                        child.remove(cchild)
                        continue
                # taking care of other attributes except index and value
                for attr, value in child_attrs.items():
                    if attr in possible_dim_attrs:
                        if attr not in dim_other_parts:
                            dim_other_parts[attr] = []
                        dim_other_parts[attr].append(value)
            if tag == CMNT_TAG and self.include_comment:
                # Store and remove node so that comment nodes from dim node so
                # that it does not call in xmlparser function
                dim_cmnt_node.append(child)
                node.remove(child)

        # All 'dim' element comments on top of 'dim' yaml key
        if dim_cmnt_node:
            for ch_nd in dim_cmnt_node:
                self.handel_comment(depth + 1, ch_nd, file_out)
        # index and value attributes of dim elements
        file_out.write(
            "{indent}dim: [{value}]\n".format(
                indent=(depth + 1) * DEPTH_SIZE, value=dim_index_value[:-2] or ""
            )
        )
        # Write the attributes, except index and value, and doc of dim as child of dim_parameter.
        # But tthe doc or attributes for each dim come inside list according to the order of dim.
        if dim_other_parts:
            file_out.write(
                "{indent}dim_parameters:\n".format(indent=(depth + 1) * DEPTH_SIZE)
            )
            # depth = depth + 2 dim_paramerter has child such as doc of dim
            indent = (depth + 2) * DEPTH_SIZE
            for key, value in dim_other_parts.items():
                if key == "doc":
                    value = self.handle_not_root_level_doc(
                        depth + 2, str(value), key, file_out
                    )
                else:
                    # Increase depth size inside handle_map...() for writting text with one
                    # more indentation.
                    file_out.write(
                        f"{indent}{key}: "
                        f"{handle_mapping_char(value, depth + 3, False)}\n"
                    )

    def handle_enumeration(self, depth, node, file_out):
        """
            Handle the enumeration field parsed from the xml file.

        If the enumeration items contain a doc field, the yaml file will contain items as child
        fields of the enumeration field.

        If no doc are inherited in the enumeration items, a list of the items is given for the
        enumeration list.

        """
        # pylint: disable=consider-using-f-string

        check_doc = []
        for child in list(node):
            if list(child):
                check_doc.append(list(child))
        # pylint: disable=too-many-nested-blocks
        if check_doc:
            file_out.write(
                "{indent}{tag}: \n".format(
                    indent=depth * DEPTH_SIZE, tag=node.tag.split("}", 1)[1]
                )
            )
            for child in list(node):
                tag = remove_namespace_from_tag(child.tag)
                itm_depth = depth + 1
                if tag == ("item"):
                    file_out.write(
                        "{indent}{value}: \n".format(
                            indent=(itm_depth) * DEPTH_SIZE, value=child.attrib["value"]
                        )
                    )

                    if list(child):
                        for item_doc in list(child):
                            if remove_namespace_from_tag(item_doc.tag) == "doc":
                                item_doc_depth = itm_depth + 1
                                self.handle_not_root_level_doc(
                                    item_doc_depth,
                                    item_doc.text,
                                    item_doc.tag,
                                    file_out,
                                )
                            if (
                                remove_namespace_from_tag(item_doc.tag) == CMNT_TAG
                                and self.include_comment
                            ):
                                self.handel_comment(itm_depth + 1, item_doc, file_out)
                if tag == CMNT_TAG and self.include_comment:
                    self.handel_comment(itm_depth + 1, child, file_out)
        else:
            enum_list = ""
            remove_nodes = []
            for item_child in list(node):
                tag = remove_namespace_from_tag(item_child.tag)
                if tag == ("item"):
                    enum_list = enum_list + "{value}, ".format(
                        value=item_child.attrib["value"]
                    )
                if tag == CMNT_TAG and self.include_comment:
                    self.handel_comment(depth, item_child, file_out)
                    remove_nodes.append(item_child)
            for ch_node in remove_nodes:
                node.remove(ch_node)

            file_out.write(
                "{indent}{tag}: [{enum_list}]\n".format(
                    indent=depth * DEPTH_SIZE,
                    tag=remove_namespace_from_tag(node.tag),
                    enum_list=enum_list[:-2] or "",
                )
            )

    def handle_attributes(self, depth, node, file_out):
        """Handle the attributes parsed from the xml file"""

        allowed_attr = [
            "name",
            "type",
            "units",
            "nameType",
            "recommended",
            "optional",
            "minOccurs",
            "maxOccurs",
            "deprecated",
        ]

        name = ""
        node_attr = node.attrib
        if "name" in node_attr:
            pass
        else:
            raise ValueError("Attribute must have an name key.")
        rm_key_list = []
        # Maintain order: name and type in form name(type) or (type)name that come first
        for key, val in node_attr.items():
            if key == "name":
                name = val
                rm_key_list.append(key)

        for key in rm_key_list:
            del node_attr[key]

        file_out.write(
            "{indent}{escapesymbol}{name}:\n".format(
                indent=depth * DEPTH_SIZE, escapesymbol=r"\@", name=name
            )
        )

        tmp_dict = {}
        exists_dict = {}
        for key, val in node_attr.items():
            # As both 'minOccurs', 'maxOccurs' and optionality move to the 'exists'
            if key in ["minOccurs", "maxOccurs", "optional", "recommended", "required"]:
                if "exists" not in tmp_dict:
                    tmp_dict["exists"] = []
                self.handle_exists(exists_dict, key, val)
            elif key == "units":
                tmp_dict["unit"] = val
            else:
                tmp_dict[key] = val
            if key not in allowed_attr:
                raise ValueError(
                    f"An attribute ({key}) has been found that is not allowed."
                    f"The allowed attr is {allowed_attr}."
                )

        has_min_max = False
        has_opt_reco_requ = False
        if exists_dict:
            for key, val in exists_dict.items():
                if key in ["minOccurs", "maxOccurs"]:
                    tmp_dict["exists"] = tmp_dict["exists"] + val
                    has_min_max = True
                elif key in ["optional", "recommended", "required"]:
                    tmp_dict["exists"] = key
                    has_opt_reco_requ = True
        if has_min_max and has_opt_reco_requ:
            raise ValueError(
                "Optionality 'exists' can take only either from ['minOccurs',"
                " 'maxOccurs'] or from ['optional', 'recommended', 'required']"
                ". But not from both of the groups together. Please check in"
                " attributes"
            )

        depth_ = depth + 1
        for key, val in tmp_dict.items():
            # Increase depth size inside handle_map...() for writting text with one
            # more indentation.
            file_out.write(
                f"{depth_ * DEPTH_SIZE}{key}: "
                f"{handle_mapping_char(val, depth_ + 1, False)}\n"
            )

    def handel_link(self, depth, node, file_out):
        """
        Handle link elements of nxdl
        """

        possible_link_attrs = ["name", "target", "napimount"]
        node_attr = node.attrib
        # Handle special cases
        if "name" in node_attr:
            file_out.write(
                "{indent}{name}(link):\n".format(
                    indent=depth * DEPTH_SIZE, name=node_attr["name"] or ""
                )
            )
            del node_attr["name"]

        depth_ = depth + 1
        # Handle general cases
        for attr_key, val in node_attr.items():
            if attr_key in possible_link_attrs:
                file_out.write(
                    "{indent}{attr}: {value}\n".format(
                        indent=depth_ * DEPTH_SIZE, attr=attr_key, value=val
                    )
                )
            else:
                raise ValueError(
                    f"An anexpected attribute '{attr_key}' of link has found."
                    f"At this moment the alloed keys are {possible_link_attrs}"
                )

    def handel_choice(self, depth, node, file_out):
        """
        Handle choice element which is a parent node of group.
        """

        possible_attr = []

        node_attr = node.attrib
        # Handle special casees
        if "name" in node_attr:
            file_out.write(
                "{indent}{attr}(choice): \n".format(
                    indent=depth * DEPTH_SIZE, attr=node_attr["name"]
                )
            )
            del node_attr["name"]

        depth_ = depth + 1
        # Taking care of general attrinutes. Though, still no attrinutes have found,
        # but could be used for future
        for attr in node_attr.items():
            if attr in possible_attr:
                file_out.write(
                    "{indent}{attr}: {value}\n".format(
                        indent=depth_ * DEPTH_SIZE, attr=attr, value=node_attr[attr]
                    )
                )
            else:
                raise ValueError(
                    f"An unexpected attribute '{attr}' of 'choice' has been found."
                    f"At this moment attributes for choice {possible_attr}"
                )

    def handel_comment(self, depth, node, file_out):
        """
        Collect comment element and pass to write_out function
        """
        indent = depth * DEPTH_SIZE
        if self.is_last_element_comment:
            text = self.comvert_to_ymal_comment(indent, node.text)
            self.write_out(indent, text, file_out)
        else:
            text = self.comvert_to_ymal_comment(indent, node.text)
            self.write_out(indent, text, file_out)
            self.is_last_element_comment = True

    def recursion_in_xml_tree(self, depth, xml_tree, output_yml, verbose):
        """
            Descend lower level in xml tree. If we are in the symbols branch, the recursive
        behaviour is not triggered as we already handled the symbols' childs.
        """

        tree = xml_tree["tree"]
        node = xml_tree["node"]
        for child in list(node):
            xml_tree_children = {"tree": tree, "node": child}
            self.xmlparse(output_yml, xml_tree_children, depth, verbose)

    # pylint: disable=too-many-branches, too-many-statements
    def xmlparse(self, output_yml, xml_tree, depth, verbose):
        """
        Main of the nxdl2yaml converter.
        It parses XML tree, then prints recursively each level of the tree
        """
        tree = xml_tree["tree"]
        node = xml_tree["node"]
        if verbose:
            sys.stdout.write(f"Node tag: {remove_namespace_from_tag(node.tag)}\n")
            sys.stdout.write(f"Attributes: {node.attrib}\n")
        with open(output_yml, "a", encoding="utf-8") as file_out:
            tag = remove_namespace_from_tag(node.tag)
            if tag == "definition":
                self.found_definition = True
                self.handle_definition(node)
                # Taking care of root level doc and symbols
                remove_cmnt_n = None
                last_comment = ""
                for child in list(node):
                    tag_tmp = remove_namespace_from_tag(child.tag)
                    if tag_tmp == CMNT_TAG and self.include_comment:
                        last_comment = self.comvert_to_ymal_comment(
                            depth * DEPTH_SIZE, child.text
                        )
                        remove_cmnt_n = child
                    if tag_tmp == "doc":
                        self.store_root_level_comments("root_doc", last_comment)
                        last_comment = ""
                        self.handle_root_level_doc(child)
                        node.remove(child)
                        if remove_cmnt_n is not None:
                            node.remove(remove_cmnt_n)
                            remove_cmnt_n = None
                    if tag_tmp == "symbols":
                        self.store_root_level_comments("symbols", last_comment)
                        last_comment = ""
                        self.handle_symbols(depth, child)
                        node.remove(child)
                        if remove_cmnt_n is not None:
                            node.remove(remove_cmnt_n)
                            remove_cmnt_n = None

            if tag == ("doc") and depth != 1:
                parent = get_node_parent_info(tree, node)[0]
                doc_parent = remove_namespace_from_tag(parent.tag)
                if doc_parent != "item":
                    self.handle_not_root_level_doc(
                        depth, text=node.text, tag=node.tag, file_out=file_out
                    )

            if self.found_definition is True and self.root_level_doc:
                self.print_root_level_info(depth, file_out)
            # End of print root-level definitions in file
            if tag in ("field", "group") and depth != 0:
                self.handle_group_or_field(depth, node, file_out)
            if tag == ("enumeration"):
                self.handle_enumeration(depth, node, file_out)
            if tag == ("attribute"):
                self.handle_attributes(depth, node, file_out)
            if tag == ("dimensions"):
                self.handle_dimension(depth, node, file_out)
            if tag == ("link"):
                self.handel_link(depth, node, file_out)
            if tag == ("choice"):
                self.handel_choice(depth, node, file_out)
            if tag == CMNT_TAG and self.include_comment:
                self.handel_comment(depth, node, file_out)
        depth += 1
        # Write nested nodes
        self.recursion_in_xml_tree(depth, xml_tree, output_yml, verbose)


def compare_niac_and_my(tree, tree2, verbose, node, root_no_duplicates):
    """This function creates two trees with Niac XML file and My XML file.
    The main aim is to compare the two trees and create a new one that is the
    union of the two initial trees.
    """
    root = tree.getroot()
    root2 = tree2.getroot()
    attrs_list_niac = []
    for nodo in root.iter(node):
        attrs_list_niac.append(nodo.attrib)
    if verbose:
        sys.stdout.write("Attributes found in Niac file: \n")
        sys.stdout.write(str(attrs_list_niac) + "\n")
        sys.stdout.write("  \n")
        sys.stdout.write("Started merging of Niac and My file... \n")
    for elem in root.iter(node):
        if verbose:
            sys.stdout.write("- Niac element inserted: \n")
            sys.stdout.write(str(elem.attrib) + "\n")
        index = get_node_parent_info(tree, elem)[1]
        root_no_duplicates.insert(index, elem)

    for elem2 in root2.iter(node):
        index = get_node_parent_info(tree2, elem2)[1]
        if elem2.attrib not in attrs_list_niac:
            if verbose:
                sys.stdout.write("- My element inserted: \n")
                sys.stdout.write(str(elem2.attrib) + "\n")
            root_no_duplicates.insert(index, elem2)

    if verbose:
        sys.stdout.write("     \n")
    return root_no_duplicates
