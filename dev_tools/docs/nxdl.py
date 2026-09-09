import os
import re
from collections import OrderedDict
from html import parser as HTMLParser
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

import lxml

from ..globals.directories import get_nxdl_root
from ..globals.errors import NXDLParseError
from ..globals.nxdl import NXDL_NAMESPACE
from ..globals.urls import REPO_URL
from ..utils import nxdl_utils
from ..utils import xml_utils
from ..utils.github import get_file_contributors_via_api
from ..utils.types import PathLike
from .anchor_list import AnchorRegistry

# controlling the length of progressively more indented sub-node
MIN_COLLAPSE_HINT_LINE_LENGTH = 20
MAX_COLLAPSE_HINT_LINE_LENGTH = 80

# how a concept that is shown in the documentation of a class that does not
# define it is marked
REUSED_MARKER = "*(reused)*"

# which children are shown along with a reused concept
REUSE_CHILDREN_MODES = ("none", "direct", "all")

# maximal number of levels below a reused concept with `children="all"`
MAX_REUSE_DEPTH = 5

# maximal number of reused concepts in one class
MAX_REUSED_CONCEPTS = 200

# symbol names in a dimension size, which can be an expression like "nP+1"
SYMBOL_PATTERN = re.compile(r"[A-Za-z_][A-Za-z_0-9]*")

# characters that may precede or follow inline markup in reStructuredText
RST_INLINE_PREFIX = " \t-:/'\"<([{"
RST_INLINE_SUFFIX = " \t-.,:;!?\\/'\")]}>"

_BACKTICK_RUN = re.compile(r"`+")
_ASTERISK_RUN = re.compile(r"\*+")


class ReusedConcept:
    """A group, field or attribute that a class does not define itself but that is
    shown in its documentation.

    A class takes over everything defined by the class it ``extends`` and by the base
    classes of the groups it uses, without repeating any of it. Only what a class
    defines itself is shown in its documentation. The ``reused_concepts`` element of
    NXDL points at concepts that a class takes over unchanged, so that they are shown
    as well. Reusing a concept changes nothing about the class itself.
    """

    def __init__(
        self,
        name: str,
        is_attribute: bool,
        parent: Optional["ReusedConcept"],
        node: lxml.etree._Element,
        defined_here: bool,
    ) -> None:
        self.name = name
        self.is_attribute = is_attribute
        self.parent = parent
        self.node = node
        self.defined_here = defined_here
        parent_path = parent.path if parent is not None else ""
        self.path = f"{parent_path}{'@' if is_attribute else '/'}{name}"
        self.nxdl_path = f"{parent.nxdl_path if parent is not None else ''}/{name}"
        self.listed = False
        self.children_mode = "none"
        self.children: Dict[str, "ReusedConcept"] = OrderedDict()

    @property
    def element_type(self) -> str:
        return xml_utils.get_local_name(self.node)


class NXClassDocGenerator:
    """Generate documentation in reStructuredText markup
    for a NeXus class definition."""

    _INDENTATION_UNIT = " " * 2

    _CATEGORY_TO_LISTING = {
        "base": "base class",
        "application": "application definition",
    }

    def __init__(self) -> None:
        self._rst_lines = None
        self._reset()

    def _reset(self):
        self._anchor_registry = None
        self._listing_category = None
        self._use_application_defaults = None
        self._nxclass_name = None
        self._nxdl_file = None
        self._root_element = None
        self._reused_concepts = OrderedDict()
        self._reused_index = dict()
        self._reused_count = 0
        self._declared_symbols = set()
        self._used_symbols = dict()

    def __call__(
        self, nxdl_file: PathLike, anchor_registry: Optional[AnchorRegistry] = None
    ) -> List[str]:
        self._rst_lines = list()
        self._anchor_registry = anchor_registry
        nxdl_file = Path(nxdl_file)
        if anchor_registry:
            self._anchor_registry.nxdl_file = nxdl_file
        try:
            try:
                self._parse_nxdl_file(nxdl_file)
            except Exception as e:
                raise NXDLParseError(f"{nxdl_file}: {e}") from e
        finally:
            self._reset()
        return self._rst_lines

    def _parse_nxdl_file(self, nxdl_file: Path):
        assert nxdl_file.is_file()
        tree = lxml.etree.parse(str(nxdl_file))
        root = tree.getroot()

        # NXDL_NAMESPACE needs to be a globally unique identifier of
        # the NXDL schema. It needs to match the xmlns attribute
        # in the NXDL definition of the NeXus class.
        ns = {"nx": NXDL_NAMESPACE}

        nxclass_name = root.get("name")
        category = root.attrib["category"]
        title = nxclass_name
        parent_path = "/" + nxclass_name  # absolute path of parent nodes, no trailing /
        if len(nxclass_name) < 2 or nxclass_name[0:2] != "NX":
            raise Exception(
                f'Unexpected class name "{nxclass_name}"; does not start with NX'
            )
        lexical_name = nxclass_name[2:]  # without padding 'NX', for indexing

        self._listing_category = self._CATEGORY_TO_LISTING[category]
        self._use_application_defaults = category == "application"
        self._contribution = nxdl_file.parent.name == "contributed_definitions"
        self._nxclass_name = nxclass_name
        self._nxdl_file = nxdl_file
        self._root_element = root

        # print ReST comments and section header
        source = os.path.relpath(nxdl_file, get_nxdl_root())
        self._print(
            f".. auto-generated by {__name__} from the NXDL source {source} -- DO NOT EDIT"
        )

        self._print("")
        self._print(".. index::")
        self._print(f"    ! {nxclass_name} ({self._listing_category})")
        self._print(f"    ! {lexical_name} ({self._listing_category})")
        self._print(
            f"    see: {lexical_name} ({self._listing_category}); {nxclass_name}"
        )
        self._print("")
        self._print(f".. _{nxclass_name}:\n")
        self._print("=" * len(title))
        self._print(title)
        self._print("=" * len(title))

        # print category & parent class
        extends = root.get("extends")
        if extends is None:
            extends = "none"
        else:
            extends = f":ref:`{extends}`"

        # add the contributors as variables to the rst file that will
        nxdl_root = get_nxdl_root()
        rel_path = str(nxdl_file.relative_to(nxdl_root))
        rel_html = str(rel_path).replace(os.sep, "/")
        contribs_dct = get_file_contributors_via_api("definitions", rel_html)
        if contribs_dct is not None:
            self._print("")
            self._print("..")
            self._print("    Contributors List")
            for date_str, contrib_dct in contribs_dct.items():
                date_str = date_str.split("T")[0]
                name = contrib_dct["name"]
                gh_login_nm = contrib_dct["commit_dct"]["committer"]["login"]
                gh_avatar_url = contrib_dct["commit_dct"]["committer"]["avatar_url"]
                self._print("")
                s = "|".join([name, gh_login_nm, gh_avatar_url, date_str])
                self._print(f"    .. |contrib_name| replace:: {s}")

        self._print("")
        self._print("**Status**:\n")
        if self._contribution:
            self._print(
                f"  *{self._listing_category}* (contribution), extends {extends}"
            )
        else:
            self._print(f"  {self._listing_category}, extends {extends}")

        self._print_if_deprecated(ns, root, "")

        # print official description of this class
        self._print("")
        self._print("**Description**:\n")
        self._print_doc_enum("", ns, root, required=True)

        # print symbol list
        node_list = root.xpath("nx:symbols", namespaces=ns)
        self._print("**Symbols**:\n")
        if len(node_list) == 0:
            self._print("  No symbol table\n")
        elif len(node_list) > 1:
            raise Exception(f"Invalid symbol table in {nxclass_name}")
        else:
            self._print_doc_enum("", ns, node_list[0])
            for node in node_list[0].xpath("nx:symbol", namespaces=ns):
                name = node.get("name")
                reused_from = node.get("reused_from")
                self._declared_symbols.add(name)
                if reused_from:
                    doc = self._reused_symbol_doc(ns, node, name, reused_from)
                    suffix = f" :ref:`⤆ </{reused_from}/{name}-symbol>` {REUSED_MARKER}"
                else:
                    doc = self._get_doc_line(ns, node)
                    suffix = ""
                self._print(
                    f"  {self._hyperlink_target(f'/{nxclass_name}', name, 'symbol')}"
                )
                self._print(f"  **{name}**", end="")
                if doc:
                    self._print(f": {doc}", end="")
                self._print(f"{suffix}\n")

        # concepts of other classes that are shown in the documentation of this one
        self._parse_reused_concepts(ns, root)

        # print group references
        self._print("**Groups cited**:")
        node_list = root.xpath("//nx:group", namespaces=ns)
        groups = []
        for node in node_list:
            g = node.get("type")
            if g.startswith("NX") and g not in groups:
                groups.append(g)
        for concept in self._iter_reused_concepts():
            if concept.element_type != "group":
                continue
            g = concept.node.get("type")
            if g.startswith("NX") and g not in groups:
                groups.append(g)
        if len(groups) == 0:
            self._print("  none\n")
        else:
            out = [(f":ref:`{g}`") for g in groups]
            txt = ", ".join(sorted(out))
            self._print(f"  {txt}\n")
            out = [
                ("%s (base class); used in %s" % (g, self._listing_category))
                for g in groups
            ]
            txt = ", ".join(out)
            self._print(f".. index:: {txt}\n")

        # print full tree
        self._print("**Structure**:\n")
        self._print_reuse_legend()
        for subnode in root.xpath("nx:attribute", namespaces=ns):
            optional = self._get_required_or_optional_text(subnode)
            self._print_attribute(
                ns, "file", subnode, optional, self._INDENTATION_UNIT, parent_path
            )  # FIXME: +"/"+name )
        self._print_full_tree(
            ns, root, nxclass_name, self._INDENTATION_UNIT, parent_path
        )

        self._check_symbols()

        self._print_anchor_list()

        # print NXDL source location
        self._print("")
        self._print("**NXDL Source**:")
        nxdl_root = get_nxdl_root()
        rel_path = str(nxdl_file.relative_to(nxdl_root))
        rel_html = str(rel_path).replace(os.sep, "/")
        self._print(f"  {REPO_URL}/{rel_html}")

        return self._rst_lines

    def _print_anchor_list(self):
        """Print the list of hypertext anchors."""
        if not self._anchor_registry:
            return
        anchors = self._anchor_registry.flush_anchor_buffer()
        if not anchors:
            return

        self._print("")
        self._print("Hypertext Anchors")
        self._print("-----------------\n")
        self._print(
            "List of hypertext anchors for all groups, fields,\n"
            "attributes, links, and symbols defined in this class.\n\n"
        )

        def sorter(key):
            return key.lower()

        rst = [f"* :ref:`{ref} <{ref}>`" for ref in sorted(anchors, key=sorter)]

        self._print("\n".join(rst))

    @staticmethod
    def _format_type(node):
        typ = node.get("type", ":ref:`NX_CHAR <NX_CHAR>`")  # per default
        if typ.startswith("NX_"):
            typ = f":ref:`{typ} <{typ}>`"
        return typ

    @staticmethod
    def _format_units(node):
        units = node.get("units", "")
        if not units:
            return ""
        if units.startswith("NX_"):
            units = rf"\ :ref:`{units} <{units}>`"
        return f" {{units={units}}}"

    @staticmethod
    def _get_doc_blocks(ns, node):
        docnodes = node.xpath("nx:doc", namespaces=ns)
        if docnodes is None or len(docnodes) == 0:
            return ""
        if len(docnodes) > 1:
            raise Exception(
                f"Too many doc elements: line {node.sourceline}, {Path(node.base).name}"
            )
        docnode = docnodes[0]

        # be sure to grab _all_ content in the documentation
        # it might look like XML
        s = lxml.etree.tostring(
            docnode, pretty_print=True, method="c14n", with_comments=False
        ).decode("utf-8")
        m = re.search(r"^<doc[^>]*>\n?(.*)\n?</doc>$", s, re.DOTALL)
        if not m:
            raise Exception(f"unexpected docstring [{s}] ")
        text = m.group(1)

        # substitute HTML entities in markup: "<" for "&lt;"
        # thanks: http://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
        htmlparser = HTMLParser.HTMLParser()
        try:  # see #661
            import html

            text = html.unescape(text)
        except (ImportError, AttributeError):
            text = htmlparser.unescape(text)

        # Blocks are separated by whitelines
        blocks = re.split("\n\\s*\n", text)
        if len(blocks) == 1 and len(blocks[0].splitlines()) == 1:
            return [blocks[0].rstrip().lstrip()]

        # Indentation must be given by first line
        m = re.match(r"(\s*)(\S+)", blocks[0])
        if not m:
            return [""]
        indent = m.group(1)

        # Remove common indentation as determined from first line
        if indent == "":
            raise Exception(
                "Missing initial indentation in <doc> of %s [%s]"
                % (node.get("name"), blocks[0])
            )

        out_blocks = []
        for block in blocks:
            lines = block.rstrip().splitlines()
            out_lines = []
            for line in lines:
                if line[: len(indent)] != indent:
                    raise Exception(
                        'Bad indentation in <doc> of %s [%s]: expected "%s" found "%s".'
                        % (
                            node.get("name"),
                            block,
                            re.sub(r"\t", "\\\\t", indent),
                            re.sub(r"\t", "\\\\t", line),
                        )
                    )
                out_lines.append(line[len(indent) :])
            out_blocks.append("\n".join(out_lines))
        return out_blocks

    def _handle_multiline_docstring(self, blocks):
        link_pattern = re.compile(r"\.\. _([^:]+):(.*)")

        links = []
        docstring = ""
        expanded_blocks = []

        for block in blocks:
            expanded_blocks += block.split("\n")

        for block in expanded_blocks:
            if not block:
                continue

            link_match = link_pattern.search(block)
            if link_match is not None:
                links.append((link_match.group(1), link_match.group(2).strip()))
            else:
                docstring += " " + block.strip().replace("\n", " ")

        for name, target in links:
            docstring = docstring.replace(f"`{name}`_", f"`{name} <{target}>`_")

        return docstring

    def _get_doc_line(self, ns, node):
        blocks = self._get_doc_blocks(ns, node)
        if len(blocks) == 0:
            return ""
        if len(blocks) > 1:
            return self._handle_multiline_docstring(blocks)
        return blocks[0].replace("\n", " ")

    def _get_minOccurs(self, node, use_application_defaults=None):
        """
        get the value for the ``minOccurs`` attribute

        :param obj node: instance of lxml.etree._Element
        :param use_application_defaults: defaults of the class defining the node
        :returns str: value of the attribute (or its default)
        """
        # TODO: can we improve on the default by examining nxdl.xsd?
        if use_application_defaults is None:
            use_application_defaults = self._use_application_defaults
        minOccurs_default = str(int(use_application_defaults))
        minOccurs = node.get("minOccurs", minOccurs_default)
        return minOccurs

    def _get_required_or_optional_text(self, node, use_application_defaults=None):
        """
        make clear if a reported item is required or optional

        :param obj node: instance of lxml.etree._Element
        :param use_application_defaults: defaults of the class defining the node
        :returns: formatted text
        """
        if use_application_defaults is None:
            use_application_defaults = self._use_application_defaults
        nxdl_element_type = nxdl_utils.get_nxdl_element_type(node)
        if nxdl_element_type in ("field", "group", "choice"):
            optional_default = not use_application_defaults
            optional = node.get("optional", optional_default) in (True, "true", "1", 1)
            recommended = node.get("recommended", None) in (True, "true", "1", 1)
            minOccurs = self._get_minOccurs(node, use_application_defaults)
            if recommended:
                optional_text = "(recommended) "
            elif minOccurs in ("0", 0) or optional:
                optional_text = "(optional) "
            elif minOccurs in ("1", 1):
                optional_text = "(required) "
            else:
                # this is unexpected and remarkable
                # TODO: add a remark to the log
                optional_text = f"(``minOccurs={str(minOccurs)}``) "
        elif nxdl_element_type in ("attribute",):
            optional_default = not use_application_defaults
            optional = node.get("optional", optional_default) in (True, "true", "1", 1)
            recommended = node.get("recommended", None) in (True, "true", "1", 1)
            optional_text = {True: "(optional) ", False: "(required) "}[optional]
            if recommended:
                optional_text = "(recommended) "
        else:
            optional_text = "(unknown tag: " + str(nxdl_element_type) + ") "
        return optional_text

    def _analyze_dimensions(self, ns, parent) -> str:
        """These are the different dimensions that can occur:

        1. Fixed rank

            <dimensions rank="dataRank">
            <dim index="1" value="a" />
            <dim index="2" value="b" />
            <dim index="3" value="c" />
            </dimensions>

        2. Variable rank because of optional dimensions

            <dimensions rank="dataRank">
            <dim index="1" value="a" />
            <dim index="2" value="b" />
            <dim index="3" value="c" />
            <dim index="4" value="d" required="false"/>
            </dimensions>

        3. Variable rank because no dimensions specified

            <dimensions rank="dataRank">
            </dimensions>

        4. Rank and dimensions equal to that of another field called `field_name`

            <dimensions rank="dataRank">
            <dim index="1" ref="field_name" />
            </dimensions>
        """
        node_list = parent.xpath("nx:dimensions", namespaces=ns)
        if len(node_list) != 1:
            return ""
        node = node_list[0]
        node_list = node.xpath("nx:dim", namespaces=ns)

        dims = []
        optional = False
        for subnode in node_list:
            # Dimension index (starts from index 1)
            index = subnode.get("index", "")
            if not index.isdigit():
                raise RuntimeError("A dimension must have an index")
            index = int(index)
            if index <= 0:
                # No longer permitted
                raise RuntimeError(
                    "A dimension's index must be a positive integer (>=1)"
                )

            # Expand dimensions when needed
            index -= 1
            nadd = max(index - len(dims) + 1, 0)
            if nadd:
                dims += ["."] * nadd

            # Dimension symbol
            dim = subnode.get("value")  # integer or symbol from the table
            if dim:
                self._register_dimension_symbols(dim, parent)
                dim = self._link_dimension_symbols(dim)
            if not dim:
                ref = subnode.get("ref")
                if ref:
                    return (
                        f" (Rank: same as field {ref}, Dimensions: same as field {ref})"
                    )
                dim = "."  # dimension has no symbol

            # Dimension might be optional
            if subnode.get("required", "true").lower() == "false":
                optional = True
            elif optional:
                raise RuntimeError(
                    "A required dimension cannot come after an optional dimension"
                )
            if optional:
                dim = f"[{dim}]"

            dims[index] = dim

        # When the rank is missing, set to the number of dimensions when
        # there are dimensions specified and none of them are optional.
        ndims = len(dims)
        rank = node.get("rank", None)
        if rank is None and not optional and ndims:
            rank = str(ndims)

        # Validate rank and dimensions
        rank_is_fixed = rank and rank.isdigit()
        if optional and rank_is_fixed:
            raise RuntimeError("A fixed rank cannot have optional dimensions")
        if rank_is_fixed and ndims and int(rank) != ndims:
            raise RuntimeError(
                "The rank and the number of dimensions do not correspond"
            )

        # Omit rank and/or dimensions when not specified
        if rank and dims:
            dims = ", ".join(dims)
            return f" (Rank: {rank}, Dimensions: [{dims}])"
        elif rank:
            return f" (Rank: {rank})"
        elif dims:
            dims = ", ".join(dims)
            return f" (Dimensions: [{dims}])"
        return ""

    def _hyperlink_target(self, parent_path, name, nxtype):
        """Return internal hyperlink target for HTML anchor."""
        if nxtype == "attribute":
            sep = "@"
        else:
            sep = "/"
        target = f"{parent_path}{sep}{name}-{nxtype}"
        if self._anchor_registry:
            self._anchor_registry.add(target)
        return f".. _{target}:\n"

    def _print_enumeration(self, indent, ns, parent):
        node_list = parent.xpath("nx:item", namespaces=ns)
        if len(node_list) == 0:
            return ""

        if parent.attrib.get("open", "false") == "true":
            self._print(
                f"{indent}Any of these values or a custom value (if you use a custom value, also set @custom=True):",
                end="",
            )
        else:
            if len(node_list) == 1:
                self._print(f"{indent}Obligatory value:", end="")
            else:
                self._print(f"{indent}Any of these values:", end="")

        docs = OrderedDict()
        for item in node_list:
            name = item.get("value")
            docs[name] = self._get_doc_line(ns, item)

        ENUMERATION_INLINE_LENGTH = 60

        def show_as_typed_text(msg):
            return f"``{msg}``"

        oneliner = " | ".join(map(show_as_typed_text, docs.keys()))
        if (
            any(doc for doc in docs.values())
            or len(oneliner) > ENUMERATION_INLINE_LENGTH
        ):
            # print one item per line
            self._print("\n")
            for name, doc in docs.items():
                self._print(f"{indent}  * {show_as_typed_text(name)}", end="")
                if doc:
                    self._print(f": {doc}", end="")
                self._print("\n")
        else:
            # print all items in one line
            self._print(f" {oneliner}")
        self._print("")

    def _print_doc(self, indent, ns, node, required=False):
        blocks = self._get_doc_blocks(ns, node)
        if len(blocks) == 0:
            if required:
                raise Exception("No documentation for: " + node.get("name"))
            self._print("")
        else:
            for block in blocks:
                for line in block.splitlines():
                    self._print(f"{indent}{line}")
                self._print()

    def long_doc(self, ns, node, left_margin):
        length = 0
        line = "documentation"
        fnd = False
        blocks = self._get_doc_blocks(ns, node)
        max_characters = max(
            MIN_COLLAPSE_HINT_LINE_LENGTH, (MAX_COLLAPSE_HINT_LINE_LENGTH - left_margin)
        )
        for block in blocks:
            lines = block.splitlines()
            length += len(lines)
            for single_line in lines:
                if len(single_line) > 2 and single_line[0] != "." and not fnd:
                    fnd = True
                    line = self._truncate_rst_line(single_line, max_characters)
        return (length, line, blocks)

    @staticmethod
    def _has_unbalanced_runs(text: str, pattern: "re.Pattern[str]") -> bool:
        """Whether text has an odd number of matching delimiter runs, e.g. a `role` or ``literal``
        cut off before its closing delimiters."""
        stack: List[str] = []
        for run in pattern.findall(text):
            if stack and stack[-1] == run:
                stack.pop()
            else:
                stack.append(run)
        return bool(stack)

    @staticmethod
    def _truncate_rst_line(text: str, max_length: int) -> str:
        """Truncate text to at most max_length characters without leaving unterminated RST inline
        markup (a role/link cut mid-``target``) or a dangling implicit hyperlink reference (word_).
        """
        candidate = text[:max_length]
        while candidate:
            stripped = candidate.rstrip()
            if (
                not stripped.endswith("_")
                and not NXClassDocGenerator._has_unbalanced_runs(
                    stripped, _BACKTICK_RUN
                )
                and not NXClassDocGenerator._has_unbalanced_runs(
                    stripped, _ASTERISK_RUN
                )
            ):
                return candidate
            candidate = candidate.rsplit(" ", 1)[0] if " " in candidate else ""
        return candidate

    def _print_doc_enum(self, indent, ns, node, required=False):
        collapse_indent = indent
        node_list = node.xpath("nx:enumeration", namespaces=ns)
        doclen, line, blocks = self.long_doc(ns, node, len(indent))
        if len(node_list) + doclen > 1:
            collapse_indent = f"{indent}    "
            self._print(f"{indent}{self._INDENTATION_UNIT}.. collapse:: {line} ...\n")
        self._print_doc(
            collapse_indent + self._INDENTATION_UNIT, ns, node, required=required
        )
        if len(node_list) == 1:
            self._print_enumeration(
                collapse_indent + self._INDENTATION_UNIT, ns, node_list[0]
            )

    def _print_attribute(
        self, ns, kind, node, optional, indent, parent_path, reused=False
    ):
        name = node.get("name")
        formatted_name = nxdl_utils.get_rst_formatted_name(node)
        index_name = name
        self._print(
            f"{indent}" f"{self._hyperlink_target(parent_path, name, 'attribute')}"
        )
        self._print(f"{indent}.. index:: {index_name} ({kind} attribute)\n")
        if reused:
            reference = f"{self._reused_ref(node, 'attribute')} {REUSED_MARKER}"
        else:
            reference = self.get_first_parent_ref(f"{parent_path}/{name}", "attribute")
        self._print(
            f"{indent}{formatted_name}: {optional}{self._format_type(node)}{self._format_units(node)} {reference}\n"
        )
        self._print_if_deprecated(ns, node, indent + self._INDENTATION_UNIT)
        self._print_doc_enum(indent, ns, node)

    def _print_if_deprecated(self, ns, node, indent):
        deprecated = node.get("deprecated", None)
        if deprecated is not None:
            self._print(f"\n{indent}.. index:: deprecated\n")
            self._print(f"\n{indent}**DEPRECATED**: {deprecated}\n")

    def _print_full_tree(self, ns, parent, name, indent, parent_path):
        """
        recursively print the full tree structure

        :param dict ns: dictionary of namespaces for use in XPath expressions
        :param lxml_element_node parent: parent node to be documented
        :param str name: name of elements, such as NXentry/NXuser
        :param indent: to keep track of indentation level
        :param parent_path: NX class path of parent nodes
        """
        # Reused concepts are shown where the class would define them: attributes
        # right after the ones of the class itself, fields before the first group
        # and groups last.
        reused = self._reused_index.get(parent_path, ())
        reused_attributes = [c for c in reused if c.element_type == "attribute"]
        reused_fields = [c for c in reused if c.element_type in ("field", "link")]
        reused_groups = [c for c in reused if c.element_type == "group"]
        for concept in reused_attributes:
            self._print_reused_concept(ns, concept, indent)
        fields_printed = False

        # Process children in document order to preserve XML ordering.
        for node in parent.xpath("nx:field|nx:group|nx:choice|nx:link", namespaces=ns):
            nxdl_element_type = nxdl_utils.get_nxdl_element_type(node)
            if not fields_printed and xml_utils.get_local_name(node) in (
                "group",
                "choice",
            ):
                fields_printed = True
                for concept in reused_fields:
                    self._print_reused_concept(ns, concept, indent)

            if nxdl_element_type == "field":
                name = node.get("name")
                formatted_name = nxdl_utils.get_rst_formatted_name(node)
                index_name = name
                dims = self._analyze_dimensions(ns, node)

                optional_text = self._get_required_or_optional_text(node)
                self._print(
                    f"{indent}{self._hyperlink_target(parent_path, name, 'field')}"
                )
                self._print(f"{indent}.. index:: {index_name} (field)\n")
                self._print(
                    f"{indent}{formatted_name}: "
                    f"{optional_text}"
                    f"{self._format_type(node)}"
                    f"{dims}"
                    f"{self._format_units(node)}"
                    f" {self.get_first_parent_ref(f'{parent_path}/{name}', 'field')}"
                    "\n"
                )

                self._print_if_deprecated(ns, node, indent + self._INDENTATION_UNIT)
                self._print_doc_enum(indent, ns, node)

                for subnode in node.xpath("nx:attribute", namespaces=ns):
                    optional = self._get_required_or_optional_text(subnode)
                    self._print_attribute(
                        ns,
                        "field",
                        subnode,
                        optional,
                        indent + self._INDENTATION_UNIT,
                        parent_path + "/" + name,
                    )

                self._print_reused_concepts(
                    ns, indent + self._INDENTATION_UNIT, parent_path + "/" + name
                )

            elif nxdl_element_type == "group":
                name = node.get("name", "")
                formatted_name = nxdl_utils.get_rst_formatted_name(node)
                typ = node.get("type", "untyped (this is an error; please report)")

                optional_text = self._get_required_or_optional_text(node)
                if typ.startswith("NX"):
                    if name == "":
                        name = typ.lstrip("NX").upper()
                    typ = f":ref:`{typ}`"
                hTarget = self._hyperlink_target(parent_path, name, "group")
                # target = hTarget.replace(".. _", "").replace(":\n", "")
                # TODO: https://github.com/nexusformat/definitions/issues/1057
                self._print(f"{indent}{hTarget}")
                self._print(
                    f"{indent}{formatted_name}: {optional_text}{typ} "
                    f"{self.get_first_parent_ref(f'{parent_path}/{name}', 'group')}\n"
                )

                self._print_if_deprecated(ns, node, indent + self._INDENTATION_UNIT)
                self._print_doc_enum(indent, ns, node)

                for subnode in node.xpath("nx:attribute", namespaces=ns):
                    optional = self._get_required_or_optional_text(subnode)
                    self._print_attribute(
                        ns,
                        "group",
                        subnode,
                        optional,
                        indent + self._INDENTATION_UNIT,
                        parent_path + "/" + name,
                    )

                nodename = "%s/%s" % (name, node.get("type"))
                self._print_full_tree(
                    ns,
                    node,
                    nodename,
                    indent + self._INDENTATION_UNIT,
                    parent_path + "/" + name,
                )

            elif nxdl_element_type == "choice":
                name = node.get("name", "")
                hTarget = self._hyperlink_target(parent_path, name, "choice")
                self._print(f"{indent}{hTarget}")
                optional_text = self._get_required_or_optional_text(node).strip("() ")
                self._print(
                    f"{indent}**{name}**: ({optional_text}) "
                    "Only one of the following groups may be present:\n"
                )
                self._print_doc_enum(indent, ns, node)

                # Print each group option within the choice.
                for subnode in node.xpath("nx:group", namespaces=ns):
                    subname = subnode.get("name", "")
                    typ = subnode.get(
                        "type", "untyped (this is an error; please report)"
                    )
                    if typ.startswith("NX"):
                        if subname == "":
                            subname = typ.lstrip("NX").upper()
                        typ_ref = f":ref:`{typ}`"
                    else:
                        typ_ref = typ
                    sub_indent = indent + self._INDENTATION_UNIT
                    subTarget = self._hyperlink_target(
                        parent_path + "/" + name, subname, "group"
                    )
                    self._print(f"{sub_indent}{subTarget}")
                    self._print(f"{sub_indent}**{subname}**: {typ_ref}\n")
                    self._print_doc_enum(sub_indent, ns, subnode)

                    # Recursively print any content within this group option.
                    nodename = "%s/%s" % (subname, subnode.get("type"))
                    self._print_full_tree(
                        ns,
                        subnode,
                        nodename,
                        sub_indent + self._INDENTATION_UNIT,
                        parent_path + "/" + name + "/" + subname,
                    )

            elif nxdl_element_type == "link":
                name = node.get("name")
                formatted_name = nxdl_utils.get_rst_formatted_name(node)
                self._print(
                    f"{indent}{self._hyperlink_target(parent_path, name, 'link')}"
                )
                self._print(
                    f"{indent}{formatted_name}: "
                    ":ref:`link<Design-Links>` "
                    f"(suggested target: ``{node.get('target')}``)"
                    "\n"
                )
                self._print_doc_enum(indent, ns, node)

            else:
                raise ValueError(f"Unknown node type: {nxdl_element_type}")

        if not fields_printed:
            for concept in reused_fields:
                self._print_reused_concept(ns, concept, indent)
        for concept in reused_groups:
            self._print_reused_concept(ns, concept, indent)

    def _parse_reused_concepts(self, ns, root) -> None:
        """Parse the ``reused_concepts`` element: concepts of other classes that are
        shown in the documentation of this class.
        """
        node_list = root.xpath("nx:reused_concepts", namespaces=ns)
        if not node_list:
            return
        if len(node_list) > 1:
            raise ValueError(f"Invalid reused_concepts list in {self._nxclass_name}")

        listed = list()
        for node in node_list[0].xpath("nx:reuse", namespaces=ns):
            path = node.get("path")
            children_mode = node.get("children", "none")
            if children_mode not in REUSE_CHILDREN_MODES:
                raise ValueError(
                    f"'{path}': children='{children_mode}' is not one of "
                    f"{', '.join(REUSE_CHILDREN_MODES)}"
                )
            concept = None
            concepts = self._reused_concepts
            for name, is_attribute in self._split_reuse_path(path):
                key = f"@{name}" if is_attribute else name
                child = concepts.get(key)
                if child is None:
                    child = self._create_reused_concept(concept, name, is_attribute)
                    concepts[key] = child
                concept = child
                concepts = concept.children
            if concept.listed:
                raise ValueError(f"'{path}' is reused more than once")
            if concept.defined_here:
                raise ValueError(
                    f"'{path}' is defined by {self._nxclass_name} itself: remove the "
                    "definition or remove it from the 'reused_concepts' list"
                )
            concept.listed = True
            concept.children_mode = children_mode
            listed.append(concept)

        for concept in listed:
            self._expand_reused_concept(ns, concept, concept.children_mode, 1)
        self._index_reused_concepts(self._reused_concepts, f"/{self._nxclass_name}")

    @staticmethod
    def _split_reuse_path(path: str) -> List[Tuple[str, bool]]:
        """Split a ``reuse`` path into ``(name, is_attribute)`` per level."""
        if not path or not path.startswith("/"):
            raise ValueError(f"reuse path '{path}' must start with '/'")
        segments = list()
        for part in path[1:].split("/"):
            names = part.split("@")
            if len(names) > 2 or not all(names):
                raise ValueError(f"'{path}' is not a valid reuse path")
            segments.append((names[0], False))
            if len(names) == 2:
                segments.append((names[1], True))
        return segments

    def _create_reused_concept(
        self, parent: Optional[ReusedConcept], name: str, is_attribute: bool
    ) -> ReusedConcept:
        nxdl_path = f"{parent.nxdl_path if parent is not None else ''}/{name}"
        elist = nxdl_utils.get_inherited_nodes(nxdl_path, None, self._root_element)[2]
        if not elist:
            raise ValueError(f"'{nxdl_path}' does not exist in {self._nxclass_name}")
        node = elist[0]
        element_type = xml_utils.get_local_name(node)
        if element_type == "choice":
            raise ValueError(
                f"'{nxdl_path}' is a choice, which cannot be highlighted in the "
                "documentation"
            )
        if is_attribute != (element_type == "attribute"):
            raise ValueError(
                f"'{nxdl_path}' is a {element_type}: an attribute is separated from "
                "its parent with '@', anything else with '/'"
            )
        defined_name = nxdl_utils.get_node_name(node)
        if defined_name != name:
            raise ValueError(
                f"'{nxdl_path}' must be spelled '{defined_name}' as in the class that defines it"
            )
        # nodes of the class being documented have an empty 'nxdlbase'
        defined_here = not node.get("nxdlbase")
        if not defined_here:
            self._check_not_renamed(parent, node, name, nxdl_path)
        return ReusedConcept(name, is_attribute, parent, node, defined_here)

    def _check_not_renamed(
        self, parent: Optional[ReusedConcept], node, name: str, nxdl_path: str
    ) -> None:
        """A concept that this class redefines under another name, such as a group
        with a flexible name that the class names itself, is not the same concept."""
        if parent is None:
            parent_node = self._root_element
        elif parent.defined_here:
            parent_node = parent.node
        else:
            # this class does not define the parent, so it cannot redefine its children
            return
        own_node, _ = nxdl_utils.get_best_child(
            parent_node,
            None,
            name,
            nxdl_utils.get_nx_class(node),
            nxdl_utils.get_nxdl_element_type(node),
        )
        if own_node is None:
            return
        own_name = nxdl_utils.get_node_name(own_node)
        if own_name != name:
            raise ValueError(
                f"'{nxdl_path}' is redefined by {self._nxclass_name} as "
                f"'{own_name}': reuse that concept instead"
            )

    def _expand_reused_concept(
        self, ns, concept: ReusedConcept, children_mode: str, level: int
    ) -> None:
        """Add the children of a reused concept that are shown as well."""
        if children_mode == "none" or concept.element_type not in ("group", "field"):
            return
        if level > MAX_REUSE_DEPTH:
            raise ValueError(
                f"'{concept.nxdl_path}' shows more than {MAX_REUSE_DEPTH} levels of "
                "children: list the concepts to be shown instead of using "
                "children='all'"
            )
        child_mode = "all" if children_mode == "all" else "none"
        for name, node in self._reused_children_nodes(ns, concept).items():
            if name in concept.children:
                continue
            child = ReusedConcept(name, False, concept, node, not node.get("nxdlbase"))
            if child.defined_here or self._reused_cycle(child):
                # documented where it is defined or already documented above
                continue
            child.listed = True
            child.children_mode = child_mode
            concept.children[name] = child
            self._reused_count += 1
            if self._reused_count > MAX_REUSED_CONCEPTS:
                raise ValueError(
                    f"more than {MAX_REUSED_CONCEPTS} concepts are reused: list the "
                    "concepts to be shown instead of using children='all'"
                )
            self._expand_reused_concept(ns, child, child_mode, level + 1)

    def _reused_children_nodes(self, ns, concept: ReusedConcept) -> Dict:
        """The groups, fields and links of a reused concept, including those of the
        class it is typed as but excluding those that every group takes over from
        NXobject."""
        elist = nxdl_utils.get_inherited_nodes(
            concept.nxdl_path, None, self._root_element
        )[2]
        nodes = OrderedDict()
        for elem in elist:
            if elem.get("name") == "NXobject":
                # every group has these, showing them everywhere is noise
                continue
            for child in elem.xpath("nx:field|nx:group|nx:link", namespaces=ns):
                name = nxdl_utils.get_node_name(child)
                if name not in nodes:
                    nodes[name] = nxdl_utils.set_nxdlpath(child, elem)
        return nodes

    @staticmethod
    def _reused_cycle(concept: ReusedConcept) -> bool:
        """A concept or its group type is already reused by one of its own ancestors
        (like NXsample in NXsample)."""

        def source(concept):
            return concept.node.get("nxdlbase"), concept.node.get("nxdlpath")

        key = source(concept)
        nxclass_name = (
            concept.node.get("type") if concept.element_type == "group" else None
        )
        parent = concept.parent
        while parent is not None:
            if source(parent) == key:
                return True
            if nxclass_name is not None and parent.node.get("type") == nxclass_name:
                return True
            parent = parent.parent
        return False

    def _index_reused_concepts(self, concepts, doc_parent_path: str) -> None:
        """Index the concepts by the path at which they are documented. The children
        of a concept that this class defines are documented below that definition."""
        for concept in concepts.values():
            if concept.defined_here:
                self._index_reused_concepts(
                    concept.children, f"{doc_parent_path}/{concept.name}"
                )
            else:
                self._reused_index.setdefault(doc_parent_path, list()).append(concept)

    def _iter_reused_concepts(self, concepts=None) -> Iterator[ReusedConcept]:
        if concepts is None:
            concepts = self._reused_concepts
        for concept in concepts.values():
            if not concept.defined_here:
                yield concept
            yield from self._iter_reused_concepts(concept.children)

    def _print_reuse_legend(self) -> None:
        if not self._reused_concepts:
            return
        # the same indentation as the structure tree, else the tree ends up
        # inside the note
        indent = self._INDENTATION_UNIT
        self._print(
            f"{indent}.. note:: The ⤆ link points at the class a concept comes from. "
            f"Items marked {REUSED_MARKER} are not defined by this class at all: they "
            "are used exactly as that class defines them. Items with a ⤆ link but no "
            "marker are defined by this class, which may change what they mean.\n"
        )

    def _print_reused_concepts(self, ns, indent: str, parent_path: str) -> None:
        for concept in self._reused_index.get(parent_path, ()):
            self._print_reused_concept(ns, concept, indent)

    def _print_reused_concept(self, ns, concept: ReusedConcept, indent: str) -> None:
        node = concept.node
        element_type = concept.element_type
        name = concept.name
        tag = "field" if element_type == "link" else element_type
        doc_parent_path = f"/{self._nxclass_name}" + (
            concept.parent.path if concept.parent is not None else ""
        )
        # occurrences follow the defaults of the class that defines the concept
        use_application_defaults = node.get("nxdlbase_class") == "application"
        optional_text = self._get_required_or_optional_text(
            node, use_application_defaults
        )

        if element_type == "attribute":
            self._print_attribute(
                ns,
                concept.parent.element_type if concept.parent is not None else "file",
                node,
                optional_text,
                indent,
                doc_parent_path,
                reused=True,
            )
            return

        marker = f"{self._reused_ref(node, tag)} {REUSED_MARKER}"
        formatted_name = nxdl_utils.get_rst_formatted_name(node)
        self._print(f"{indent}{self._hyperlink_target(doc_parent_path, name, tag)}")
        if element_type == "group":
            typ = node.get("type", "untyped (this is an error; please report)")
            if typ.startswith("NX"):
                typ = f":ref:`{typ}`"
            self._print(f"{indent}{formatted_name}: {optional_text}{typ} {marker}\n")
        elif element_type == "link":
            self._print(
                f"{indent}{formatted_name}: "
                ":ref:`link<Design-Links>` "
                f"(suggested target: ``{node.get('target')}``)"
                f" {marker}\n"
            )
        else:
            self._print(f"{indent}.. index:: {name} (field)\n")
            self._print(
                f"{indent}{formatted_name}: "
                f"{optional_text}"
                f"{self._format_type(node)}"
                f"{self._analyze_dimensions(ns, node)}"
                f"{self._format_units(node)}"
                f" {marker}"
                "\n"
            )

        self._print_if_deprecated(ns, node, indent + self._INDENTATION_UNIT)

        if concept.listed:
            self._print_doc_enum(indent, ns, node)
            for subnode in node.xpath("nx:attribute", namespaces=ns):
                if f"@{subnode.get('name')}" in concept.children:
                    continue
                nxdl_utils.set_nxdlpath(subnode, node)
                optional = self._get_required_or_optional_text(
                    subnode, use_application_defaults
                )
                self._print_attribute(
                    ns,
                    element_type,
                    subnode,
                    optional,
                    indent + self._INDENTATION_UNIT,
                    f"/{self._nxclass_name}{concept.path}",
                    reused=True,
                )

        for child in concept.children.values():
            self._print_reused_concept(ns, child, indent + self._INDENTATION_UNIT)

    @staticmethod
    def _reused_ref(node, tag: str) -> str:
        """Reference to the concept in the class that defines it."""
        nxdlbase = node.get("nxdlbase")
        nxdlpath = node.get("nxdlpath")
        if not nxdlbase or not nxdlpath:
            return ""
        nxclass_name = Path(nxdlbase).name.split(".")[0]
        if tag == "attribute":
            pos = nxdlpath.rfind("/")
            nxdlpath = f"{nxdlpath[:pos]}@{nxdlpath[pos + 1:]}"
        return f":ref:`⤆ </{nxclass_name}{nxdlpath}-{tag}>`"

    def _reused_symbol_doc(self, ns, node, name: str, nxclass_name: str) -> str:
        """Documentation of a symbol that is taken from another class."""
        if node.xpath("nx:doc", namespaces=ns):
            raise ValueError(
                f"symbol '{name}' has a 'doc' element as well as "
                f"reused_from='{nxclass_name}'"
            )
        nxdl_file = nxdl_utils.find_definition_file(nxclass_name)
        if nxdl_file is None:
            raise ValueError(
                f"symbol '{name}' is reused from unknown class '{nxclass_name}'"
            )
        root = xml_utils.read_xml_file(nxdl_file)
        for symbol in root.xpath("nx:symbols/nx:symbol", namespaces=ns):
            if symbol.get("name") == name:
                return self._get_doc_line(ns, symbol)
        raise ValueError(f"'{nxclass_name}' does not define the symbol '{name}'")

    def _link_dimension_symbols(self, size: str) -> str:
        """Turn the symbols in the size of a dimension into links to the symbol
        table of this class.
        """
        parts = []
        end = 0
        for match in SYMBOL_PATTERN.finditer(size):
            name = match.group()
            if name not in self._declared_symbols:
                continue
            before = size[end : match.start()]
            parts.append(before)
            if before and before[-1] not in RST_INLINE_PREFIX:
                parts.append("\\ ")
            parts.append(f":ref:`{name} </{self._nxclass_name}/{name}-symbol>`")
            end = match.end()
            if end < len(size) and size[end] not in RST_INLINE_SUFFIX:
                parts.append("\\ ")
        parts.append(size[end:])
        return "".join(parts)

    def _register_dimension_symbols(self, size: str, node) -> None:
        """Register the symbols used in the size of a dimension."""
        for symbol in SYMBOL_PATTERN.findall(size):
            self._used_symbols.setdefault(symbol, nxdl_utils.get_node_name(node))

    def _check_symbols(self) -> None:
        """All symbols that appear in the documentation must be in the symbol table."""
        missing = {
            symbol: used_by
            for symbol, used_by in self._used_symbols.items()
            if symbol not in self._declared_symbols
        }
        if not missing:
            return
        details = ", ".join(
            f"'{symbol}' (dimension of '{used_by}')"
            for symbol, used_by in sorted(missing.items())
        )
        raise ValueError(
            f"{self._nxclass_name} documents symbols that are missing from its symbol "
            f"table: {details}. Add them to the 'symbols' element, with a 'doc' element "
            "or with a 'reused_from' attribute naming the class that documents the "
            "symbol."
        )

    def _print(self, *args, end="\n"):
        # TODO: change instances of \t to proper indentation
        self._rst_lines.append(" ".join(args) + end)

    def get_first_parent_ref(self, path, tag):
        nx_name = path[1 : path.find("/", 1)]
        path = path[path.find("/", 1) :]

        try:
            parents = nxdl_utils.get_inherited_nodes(path, nx_name)[2]
        except FileNotFoundError:
            return ""
        if len(parents) > 1:
            for parent in parents:
                # iterate back and check tag matches
                if xml_utils.get_local_name(parent) not in (tag, "definition"):
                    print(
                        f"Warning: {path} has a mismatching inherited node - {parent.tag} cf {tag}"
                    )
                    return ""

            parent = parents[1]
            parent_path = parent_display_name = parent.attrib["nxdlpath"]
            parent_path_segments = parent_path[1:].split("/")
            parent_def_name = parent.attrib["nxdlbase"][
                parent.attrib["nxdlbase"]
                .rfind("/") : parent.attrib["nxdlbase"]
                .rfind(".nxdl")
            ]

            # Case where the first parent is a base_class
            if parent_path_segments[0] == "":
                return ""

            # special treatment for NXnote@type
            if (
                tag == "attribute"
                and parent_def_name == "/NXnote"
                and parent_path == "/type"
            ):
                return ""

            if tag == "attribute":
                pos_of_right_slash = parent_path.rfind("/")
                parent_path = (
                    parent_path[:pos_of_right_slash]
                    + "@"
                    + parent_path[pos_of_right_slash + 1 :]
                )
            parent_display_name = f"{parent_def_name[1:]}{parent_path}"
            return f":ref:`⤆ </{parent_display_name}-{tag}>`"
        return ""
