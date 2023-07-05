#!usr/bin/env python3
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

"""
Collect comments in a list by CommentCollector class. Comment is a instance of Comment,
where each comment includes comment text and line info or neighbour info where the
comment must be assinged.

The class Comment is an abstract class for general functions or method to be implemented
XMLComment and YAMLComment class.

NOTE: Here comment block mainly stands for (comment text + line or element for what comment is
intended.)
"""


from typing import List, Type, Any, Tuple, Union, Dict
from pynxtools.nyaml2nxdl.nyaml2nxdl_helper import LineLoader

__all__ = ['Comment', 'CommentCollector', 'XMLComment', 'YAMLComment']


# pylint: disable=inconsistent-return-statements
class CommentCollector:
    """CommentCollector will store a full comment ('Comment') object in
    _comment_chain.
    """

    def __init__(self, input_file: str = None,
                 loaded_obj: Union[object, Dict] = None):
        """
        Initialise CommentCollector
        parameters:
            input_file: raw input file (xml, yml)
            loaded_obj: file loaded by third party library
        """
        self._comment_chain: List = []
        self.file = input_file
        self._comment_tracker = 0
        self._comment_hash: Dict[Tuple, Type[Comment]] = {}
        self.comment: Type[Comment]
        if self.file and not loaded_obj:
            if self.file.split('.')[-1] == 'xml':
                self.comment = XMLComment
            if self.file.split('.')[-1] == 'yaml':
                self.comment = YAMLComment
                with open(self.file, "r", encoding="utf-8") as plain_text_yaml:
                    loader = LineLoader(plain_text_yaml)
                    self.comment.__yaml_dict__ = loader.get_single_data()
        elif self.file and loaded_obj:
            if self.file.split('.')[-1] == 'yaml' and isinstance(loaded_obj, dict):
                self.comment = YAMLComment
                self.comment.__yaml_dict__ = loaded_obj
            else:
                raise ValueError("Incorrect inputs for CommentCollector e.g. Wrong file extension.")

        else:
            raise ValueError("Incorrect inputs for CommentCollector")

    def extract_all_comment_blocks(self):
        """
        Collect all comments. Note that here comment means (comment text + element or line info
        intended for comment.
        """
        id_ = 0
        single_comment = self.comment(comment_id=id_)
        with open(self.file, mode='r', encoding='UTF-8') as enc_f:
            lines = enc_f.readlines()
            # Make an empty line for last comment if no empty lines in original file
            if lines[-1] != '':
                lines.append('')
            for line_num, line in enumerate(lines):
                if single_comment.is_storing_single_comment():
                    # If the last comment comes without post nxdl fields, groups and attributes
                    if '++ SHA HASH ++' in line:
                        # Handle with stored nxdl.xml file that is not part of yaml
                        line = ''
                        single_comment.process_each_line(line + 'post_comment', (line_num + 1))
                        self._comment_chain.append(single_comment)
                        break
                    if line_num < (len(lines) - 1):
                        # Processing file from Line number 1
                        single_comment.process_each_line(line, (line_num + 1))
                    else:
                        # For processing last line of file
                        single_comment.process_each_line(line + 'post_comment', (line_num + 1))
                        self._comment_chain.append(single_comment)
                else:
                    self._comment_chain.append(single_comment)
                    single_comment = self.comment(last_comment=single_comment)
                    single_comment.process_each_line(line, (line_num + 1))

    def get_comment(self):
        """
            Return comment from comment_chain that must come earlier in order.
        """
        return self._comment_chain[self._comment_tracker]

    def get_coment_by_line_info(self, comment_locs: Tuple[str, Union[int, str]]):
        """
            Get comment using line information.
        """
        if comment_locs in self._comment_hash:
            return self._comment_hash[comment_locs]

        line_annot, line_loc = comment_locs
        for cmnt in self._comment_chain:
            if line_annot in cmnt:
                line_loc_ = cmnt.get_line_number(line_annot)
                if line_loc == line_loc_:
                    self._comment_hash[comment_locs] = cmnt
                    return cmnt

    def remove_comment(self, ind):
        """Remove a comment from comment list.
        """
        if ind < len(self._comment_chain):
            del self._comment_chain[ind]
        else:
            raise ValueError("Oops! Index is out of range.")

    def reload_comment(self):
        """
        Update self._comment_tracker after done with last comment.
        """
        self._comment_tracker += 1

    def __contains__(self, comment_locs: tuple):
        """
        Confirm wether the comment corresponds to key_line and line_loc
            is exist or not.
            comment_locs is equvalant to (line_annotation, line_loc) e.g.
            (__line__doc and 35)
        """
        if not isinstance(comment_locs, tuple):
            raise TypeError("Comment_locs should be 'tuple' containing line annotation "
                            "(e.g.__line__doc) and line_loc (e.g. 35).")
        line_annot, line_loc = comment_locs
        for cmnt in self._comment_chain:
            if line_annot in cmnt:
                line_loc_ = cmnt.get_line_number(line_annot)
                if line_loc == line_loc_:
                    self._comment_hash[comment_locs] = cmnt
                    return True
        return False

    def __getitem__(self, ind):
        """Get comment from  self.obj._comment_chain by index.
        """
        if isinstance(ind, int):
            if ind >= len(self._comment_chain):
                raise IndexError(f'Oops! Comment index {ind} in {__class__} is out of range!')
            return self._comment_chain[ind]

        if isinstance(ind, slice):
            start_n = ind.start or 0
            end_n = ind.stop or len(self._comment_chain)
            return self._comment_chain[start_n:end_n]

    def __iter__(self):
        """get comment ieratively
        """
        return iter(self._comment_chain)


# pylint: disable=too-many-instance-attributes
class Comment:
    """
    This class is building yaml comment and the intended line for what comment is written.
    """

    def __init__(self,
                 comment_id: int = -1,
                 last_comment: 'Comment' = None) -> None:
        """Comment object can be considered as a block element that includes
            document element (an entity for what the comment is written).
        """
        self._elemt: Any = None
        self._elemt_text: str = None
        self._is_elemt_found: bool = None
        self._is_elemt_stored: bool = None

        self._comnt: str = ''
        # If Multiple comments for one element or entity
        self._comnt_list: List[str] = []
        self.last_comment: 'Comment' = last_comment if last_comment else None
        if comment_id >= 0 and last_comment:
            self.cid = comment_id
            self.last_comment = last_comment
        elif comment_id == 0 and not last_comment:
            self.cid = comment_id
            self.last_comment = None
        elif last_comment:
            self.cid = self.last_comment.cid + 1
            self.last_comment = last_comment
        else:
            raise ValueError("Neither last comment nor comment id dound")
        self._comnt_start_found: bool = False
        self._comnt_end_found: bool = False
        self.is_storing_single_comment = lambda: not (self._comnt_end_found
                                                      and self._is_elemt_stored)

    def get_comment_text(self) -> Union[List, str]:
        """
        Extract comment text from entrire comment (comment text + elment or
        line for what comment is intended)
        """

    def append_comment(self, text: str) -> None:
        """
        Append lines of the same comment.
        """

    def store_element(self, args) -> None:
        """
        Strore comment text and line or element that is intended for comment.
        """


class XMLComment(Comment):
    """
    XMLComment to store xml comment element.
    """

    def __init__(self, comment_id: int = -1, last_comment: 'Comment' = None) -> None:
        super().__init__(comment_id, last_comment)

    def process_each_line(self, text, line_num):
        """Take care of each line of text. Through which function the text
        must be passed should be decide here.
        """
        text = text.strip()
        if text and line_num:
            self.append_comment(text)
            if self._comnt_end_found and not self._is_elemt_found:
                # for multiple comment if exist
                if self._comnt:
                    self._comnt_list.append(self._comnt)
                    self._comnt = ''

            if self._comnt_end_found:
                self.store_element(text)

    def append_comment(self, text: str) -> None:
        # Comment in single line
        if '<!--' == text[0:4]:
            self._comnt_start_found = True
            self._comnt_end_found = False
            self._comnt = self._comnt + text.replace('<!--', '')
            if '-->' == text[-4:]:
                self._comnt_end_found = True
                self._comnt_start_found = False
                self._comnt = self._comnt.replace('-->', '')

        elif '-->' == text[0:4] and self._comnt_start_found:
            self._comnt_end_found = True
            self._comnt_start_found = False
            self._comnt = self._comnt + '\n' + text.replace('-->', '')
        elif self._comnt_start_found:
            self._comnt = self._comnt + '\n' + text

    # pylint: disable=arguments-differ, arguments-renamed
    def store_element(self, text) -> None:
        def collect_xml_attributes(text_part):
            for part in text_part:
                part = part.strip()
                if part and '">' == ''.join(part[-2:]):
                    self._is_elemt_stored = True
                    self._is_elemt_found = False
                    part = ''.join(part[0:-2])
                elif part and '"/>' == ''.join(part[-3:]):
                    self._is_elemt_stored = True
                    self._is_elemt_found = False
                    part = ''.join(part[0:-3])
                elif part and '/>' == ''.join(part[-2:]):
                    self._is_elemt_stored = True
                    self._is_elemt_found = False
                    part = ''.join(part[0:-2])
                elif part and '>' == part[-1]:
                    self._is_elemt_stored = True
                    self._is_elemt_found = False
                    part = ''.join(part[0:-1])
                elif part and '"' == part[-1]:
                    part = ''.join(part[0:-1])

                if '="' in part:
                    lf_prt, rt_prt = part.split('="')
                else:
                    continue
                if ':' in lf_prt:
                    continue
                self._elemt[lf_prt] = str(rt_prt)
        if not self._elemt:
            self._elemt = {}
        # First check for comment part has been collected prefectly
        if '</' == text[0:2]:
            pass
        elif '<' == text[0] and not '<!--' == text[0:4]:
            self._is_elemt_found = True
            text = text.replace('<', '', 1)
            text_part = text.split(' ')
            # collect tag
            self._elemt['tag'] = text_part[0]
            self._elemt['attrib'] = {}
            collect_xml_attributes(text_part[1:])

        elif self._is_elemt_found:
            text_part = text.split(' ')
            collect_xml_attributes(text_part)

    def get_element_info(self):
        """
            The method returns info dict that includes:
        'tag' and 'attrib' keys.
        """
        return self._elemt

    def get_comment_text(self) -> Union[List, str]:
        """
            This method returns list of commnent text. As some xml element might have
            multiple separated comment intended for a single element.
        """
        return self._comnt_list


class YAMLComment(Comment):
    """
    This class for stroing comment text as well as location of the comment e.g. line
    number of other in the file.
    NOTE:
     1. Do not delete any element form yaml dictionary (for loaded_obj. check: Comment_collector
     class. because this loaded file has been exploited in nyaml2nxdl forward tools.)
    """
    # Class level variable. The main reason behind that to follow structure of
    # abstract class 'Comment'
    __yaml_dict__: dict = {}
    __yaml_line_info: dict = {}
    __comment_escape_char = {'--': '-\\-'}

    def __init__(self, comment_id: int = -1, last_comment: 'Comment' = None) -> None:
        """Initialization of YAMLComment follow Comment class.
        """
        super().__init__(comment_id, last_comment)
        self.collect_yaml_line_info(YAMLComment.__yaml_dict__, YAMLComment.__yaml_line_info)

    def process_each_line(self, text, line_num):
        """Take care of each line of text. Through which function the text
        must be passed should be decide here.
        """
        text = text.strip()
        self.append_comment(text)
        if self._comnt_end_found and not self._is_elemt_found:
            if self._comnt:
                self._comnt_list.append(self._comnt)
                self._comnt = ''

        if self._comnt_end_found:
            line_key = ''
            if ':' in text:
                ind = text.index(':')
                line_key = '__line__' + ''.join(text[0:ind])

            for l_num, l_key in self.__yaml_line_info.items():
                if line_num == int(l_num) and line_key == l_key:
                    self.store_element(line_key, line_num)
                    break
                # Comment comes very end of the file
                if text == 'post_comment' and line_key == '':
                    line_key = '__line__post_comment'
                    self.store_element(line_key, line_num)

    def has_post_comment(self):
        """
        Ensure is this a post coment or not.
        Post comment means the comment that come at the very end without having any
        nxdl element(class, group, filed and attribute.)
        """
        for key, _ in self._elemt.items():
            if '__line__post_comment' == key:
                return True
        return False

    def append_comment(self, text: str) -> None:
        """
            Collects all the line of the same comment and
        append them with that single comment.
        """
        # check for escape char
        text = self.replace_scape_char(text)
        # Empty line after last line of comment
        if not text and self._comnt_start_found:
            self._comnt_end_found = True
            self._comnt_start_found = False
        # For empty line inside doc or yaml file.
        elif not text:
            return
        elif '# ' == ''.join(text[0:2]):
            self._comnt_start_found = True
            self._comnt_end_found = False
            self._comnt = '' if not self._comnt else self._comnt + '\n'
            self._comnt = self._comnt + ''.join(text[2:])
        elif '#' == text[0]:
            self._comnt_start_found = True
            self._comnt_end_found = False
            self._comnt = '' if not self._comnt else self._comnt + '\n'
            self._comnt = self._comnt + ''.join(text[1:])
        elif 'post_comment' == text:
            self._comnt_end_found = True
            self._comnt_start_found = False
        # for any line after 'comment block' found
        elif self._comnt_start_found:
            self._comnt_start_found = False
            self._comnt_end_found = True

    # pylint: disable=arguments-differ
    def store_element(self, line_key, line_number):
        """
            Store comment content and information of commen location (for what comment is
            created.).
        """
        self._elemt = {}
        self._elemt[line_key] = int(line_number)
        self._is_elemt_found = False
        self._is_elemt_stored = True

    def get_comment_text(self):
        """
        Return list of comments if there are multiple comment for same yaml line.
        """
        return self._comnt_list

    def get_line_number(self, line_key):
        """
        Retrun line number for what line the comment is created
        """
        return self._elemt[line_key]

    def get_line_info(self):
        """
            Return line annotation and line number from a comment.
        """
        for line_anno, line_loc in self._elemt.items():
            return line_anno, line_loc

    def replace_scape_char(self, text):
        """Replace escape char according to __comment_escape_char dict
        """
        for ecp_char, ecp_alt in YAMLComment.__comment_escape_char.items():
            if ecp_char in text:
                text = text.replace(ecp_char, ecp_alt)
        return text

    def get_element_location(self):
        """
        Retrun yaml line '__line__KEY' info and and line numner
        """
        if len(self._elemt) > 1:
            raise ValueError(f"Comment element should be one but got "
                             f"{self._elemt}")

        for key, val in self._elemt.items():
            yield key, val

    def collect_yaml_line_info(self, yaml_dict, line_info_dict):
        """Collect __line__key and corresponding value from
        a yaml file dictonary in another dictionary.
        """
        for line_key, line_n in yaml_dict.items():
            if '__line__' in line_key:
                line_info_dict[line_n] = line_key

        for _, val in yaml_dict.items():
            if isinstance(val, dict):
                self.collect_yaml_line_info(val, line_info_dict)

    def __contains__(self, line_key):
        """For Checking whether __line__NAME is in _elemt dict or not."""
        return line_key in self._elemt

    def __eq__(self, comment_obj):
        """Check the self has same value as right comment.
        """
        if len(self._comnt_list) != len(comment_obj._comnt_list):
            return False
        for left_cmnt, right_cmnt in zip(self._comnt_list, comment_obj._comnt_list):
            left_cmnt = left_cmnt.split('\n')
            right_cmnt = right_cmnt.split('\n')
            for left_line, right_line in zip(left_cmnt, right_cmnt):
                if left_line.strip() != right_line.strip():
                    return False
        return True
