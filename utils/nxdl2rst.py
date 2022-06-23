#!/usr/bin/env python

"""
Read the NeXus NXDL class specification and describe it.
Write a restructured text (.rst) document for use in the NeXus manual in
the NeXus NXDL Classes chapter.
"""

# testing:  see file dev_nxdl2rst.py

from collections import OrderedDict
from html import parser as HTMLParser
import datetime
import json
import lxml.etree
import os
import pathlib
import re
import sys
import yaml
from local_utilities import replicate


INDENTATION_UNIT = "  "
listing_category = None
repo_root_path = pathlib.Path(__file__).parent.parent
WRITE_ANCHOR_REGISTRY = False
HTML_ROOT = "https://github.com/nexusformat/definitions/blob/main"
MANUAL_ROOT = "https://manual.nexusformat.org/"
SUBDIR_MAP = {
    "base": "base_classes",
    "application": "applications",
    "contributed": "contributed_definitions",
}


class AnchorRegistry:
    """Document the NXDL vocabulary."""

    def __init__(self) -> None:
        path = repo_root_path / "manual" / "source" / "_static"
        base = "nxdl_vocabulary"
        self.html_file = path / f"{base}.html"
        self.txt_file = path / f"{base}.txt"
        self.json_file = path / f"{base}.json"
        self.yaml_file = path / f"{base}.yml"
        self.registry = self._read()
        self.local_anchors = []  # anchors from current NXDL file
        self.nxdl_file = None
        self.category = None

    @property
    def all_anchors(self):
        result = []
        for v in self.registry.values():
            result += list(v.keys())
        return result

    def add(self, anchor):
        if anchor not in self.local_anchors:
            self.local_anchors.append(anchor)

        key = self.key_from_anchor(anchor)

        if key not in self.registry:
            self.registry[key] = {}

        reg = self.registry[key]
        if anchor not in reg:
            hanchor = self._html_anchor(anchor)
            fnxdl = "/".join(pathlib.Path(self.nxdl_file).parts[-2:]).split(".")[0]
            url = f"{MANUAL_ROOT}classes/{self.category}/{fnxdl}.html{hanchor}"
            reg[anchor] = dict(term=anchor, html=hanchor, url=url,)

    def key_from_anchor(self, anchor):
        key = anchor.lower().split("/")[-1].split("@")[-1].split("-")[0]
        if "@" in anchor:
            # restore preceding "@" symbol
            key = "@" + key
        return key

    def write(self):
        contents = dict(
            _metadata=dict(
                datetime=datetime.datetime.utcnow().isoformat(),
                title="NeXus NXDL vocabulary.",
                subtitle="Anchors for all NeXus fields, groups, attributes, and links.",
            ),
            terms=self.registry,
        )

        self._write_yaml(contents)
        self._write_json(contents)
        self._write_txt()
        self._write_html(contents)

    def _html_anchor(self, anchor):
        """
        Create (internal hyperlink target for) HTML anchor from reST anchor.

        Example:

        * reST anchor: /NXcanSAS/ENTRY/TRANSMISSION_SPECTRUM@timestamp-attribute
        * HTML anchor: #nxcansas-entry-transmission-spectrum-timestamp-attribute
        """
        html_anchor = (
            anchor.lower()
            .lstrip("/")
            .replace("_", "-")
            .replace("@", "-")
            .replace("/", "-")
        )
        return f"#{html_anchor}"

    def _read(self):
        """The YAML file will record anchors (terms) from all NXDL files."""
        registry = None
        if self.yaml_file.exists():
            contents = yaml.load(open(self.yaml_file, "r").read(), Loader=yaml.Loader)
            if contents is not None:
                registry = contents.get("terms")
        return registry or {}

    def _write_html(self, contents):
        """Write the anchors to an HTML file."""
        root = lxml.etree.Element("html")
        body = lxml.etree.SubElement(root, "body")
        title = lxml.etree.SubElement(body, "h1")
        subtitle = lxml.etree.SubElement(body, "em")

        title.text = contents["_metadata"]["title"].strip(".")
        subtitle.text = contents["_metadata"]["subtitle"].strip(".")
        vocab_list = lxml.etree.SubElement(body, "h2")
        vocab_list.text = "NXDL Vocabulary"

        p = lxml.etree.SubElement(body, "p")
        p.text = "This content is also available in these formats: "
        for ext in "json txt yml".split():
            a = lxml.etree.SubElement(p, "a")
            a.attrib["href"] = f"{MANUAL_ROOT}_static/{self.txt_file.stem}.{ext}"
            a.text = f" {ext}"

        dl = lxml.etree.SubElement(body, "dl")
        for term, termlist in sorted(contents["terms"].items()):
            dterm = lxml.etree.SubElement(dl, "dt")
            dterm.text = term
            for _, itemdict in sorted(termlist.items()):
                ddef = lxml.etree.SubElement(dterm, "dd")
                a = lxml.etree.SubElement(ddef, "a")
                a.attrib["href"] = itemdict["url"]
                a.text = itemdict["term"]

        lxml.etree.SubElement(body, "hr")

        foot = lxml.etree.SubElement(body, "p")
        foot_em = lxml.etree.SubElement(foot, "em")
        foot_em.text = f"written: {contents['_metadata']['datetime']}"

        html = lxml.etree.tostring(root, pretty_print=True).decode()
        with open(self.html_file, "w") as f:
            f.write(html)
            f.write("\n")

    def _write_json(self, contents):
        with open(self.json_file, "w") as f:
            json.dump(contents, f, indent=4)
            f.write("\n")

    def _write_txt(self):
        """Compendium (dump the list of all known anchors in raw form)."""
        terms = self.all_anchors
        with open(self.txt_file, "w") as f:
            f.write("\n".join(sorted(terms)))
            f.write("\n")

    def _write_yaml(self, contents):
        with open(self.yaml_file, "w") as f:
            yaml.dump(contents, f)


anchor_registry = AnchorRegistry()


def printAnchorList():
    """Print the list of hypertext anchors."""

    def sorter(key):
        return key.lower()

    if len(anchor_registry.local_anchors) > 0:
        if WRITE_ANCHOR_REGISTRY:
            # ONLY in the build directory
            anchor_registry.write()

        print("")
        print("Hypertext Anchors")
        print("-----------------\n")
        print(
            "List of hypertext anchors for all groups, fields,\n"
            "attributes, and links defined in this class.\n\n"
        )
        # fmt: off
        rst = [
            f"* :ref:`{ref} <{ref}>`"
            for ref in sorted(anchor_registry.local_anchors, key=sorter)
        ]
        # fmt: on
        print("\n".join(rst))


def fmtTyp(node):
    typ = node.get("type", ":ref:`NX_CHAR <NX_CHAR>`")  # per default
    if typ.startswith("NX_"):
        typ = ":ref:`%s <%s>`" % (typ, typ)
    return typ


def fmtUnits(node):
    units = node.get("units", "")
    if not units:
        return ""
    if units.startswith("NX_"):
        units = "\ :ref:`%s <%s>`" % (units, units)
    return " {units=%s}" % units


def getDocBlocks(ns, node):
    docnodes = node.xpath("nx:doc", namespaces=ns)
    if docnodes is None or len(docnodes) == 0:
        return ""
    if len(docnodes) > 1:
        raise Exception(
            "Too many doc elements: line %d, %s"
            % (node.sourceline, os.path.split(node.base)[1])
        )
    docnode = docnodes[0]

    # be sure to grab _all_ content in the documentation
    # it might look like XML
    s = lxml.etree.tostring(
        docnode, pretty_print=True, method="c14n", with_comments=False
    ).decode("utf-8")
    m = re.search(r"^<doc[^>]*>\n?(.*)\n?</doc>$", s, re.DOTALL)
    if not m:
        raise Exception("unexpected docstring [%s] " % s)
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
    blocks = re.split("\n\s*\n", text)
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


def getDocLine(ns, node):
    blocks = getDocBlocks(ns, node)
    if len(blocks) == 0:
        return ""
    if len(blocks) > 1:
        raise Exception("Unexpected multi-paragraph doc [%s]" % "|".join(blocks))
    return re.sub(r"\n", " ", blocks[0])


def get_minOccurs(node, use_application_defaults):
    """
    get the value for the ``minOccurs`` attribute

    :param obj node: instance of lxml.etree._Element
    :param bool use_application_defaults: use special case value
    :returns str: value of the attribute (or its default)
    """
    # TODO: can we improve on the default by examining nxdl.xsd?
    minOccurs_default = {True: "1", False: "0"}[use_application_defaults]
    minOccurs = node.get("minOccurs", minOccurs_default)
    return minOccurs


def get_required_or_optional_text(node, use_application_defaults):
    """
    make clear if a reported item is required or optional

    :param obj node: instance of lxml.etree._Element
    :param bool use_application_defaults: use special case value
    :returns: formatted text
    """
    tag = node.tag.split("}")[-1]
    nm = node.get("name")
    if tag in ("field", "group"):
        optional_default = not use_application_defaults
        optional = node.get("optional", optional_default) in (True, "true", "1", 1)
        recommended = node.get("recommended", None) in (True, "true", "1", 1)
        minOccurs = get_minOccurs(node, use_application_defaults)
        if recommended:
            optional_text = "(recommended) "
        elif minOccurs in ("0", 0) or optional:
            optional_text = "(optional) "
        elif minOccurs in ("1", 1):
            optional_text = "(required) "
        else:
            # this is unexpected and remarkable
            # TODO: add a remark to the log
            optional_text = "(``minOccurs=%s``) " % str(minOccurs)
    elif tag in ("attribute",):
        optional_default = not use_application_defaults
        optional = node.get("optional", optional_default) in (True, "true", "1", 1)
        recommended = node.get("recommended", None) in (True, "true", "1", 1)
        optional_text = {True: "(optional) ", False: "(required) "}[optional]
        if recommended:
            optional_text = "(recommended) "
    else:
        optional_text = "(unknown tag: " + str(tag) + ") "
    return optional_text


def analyzeDimensions(ns, parent):
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

    The legacy way of doing this (still supported)

        <dimensions rank="dataRank">
          <dim index="0" value="n" />
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
        if index == 0:
            # No longer needed: legacy way to specify that the
            # rank is variable
            continue

        # Expand dimensions when needed
        index -= 1
        nadd = max(index - len(dims) + 1, 0)
        if nadd:
            dims += ["."] * nadd

        # Dimension symbol
        dim = subnode.get("value")  # integer or symbol from the table
        if not dim:
            ref = subnode.get("ref")
            if ref:
                return " (Rank: same as field %s, Dimensions: same as field %s)" % (
                    ref,
                    ref,
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
            dim = "[%s]" % dim

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
        raise RuntimeError("The rank and the number of dimensions do not correspond")

    # Omit rank and/or dimensions when not specified
    if rank and dims:
        dims = ", ".join(dims)
        return " (Rank: %s, Dimensions: [%s])" % (rank, dims)
    elif rank:
        return " (Rank: %s)" % rank
    elif dims:
        dims = ", ".join(dims)
        return " (Dimensions: [%s])" % dims
    return ""


def hyperlinkTarget(parent_path, name, nxtype):
    """Return internal hyperlink target for HTML anchor."""
    if nxtype == "attribute":
        sep = "@"
    else:
        sep = "/"
    target = "%s%s%s-%s" % (parent_path, sep, name, nxtype)
    anchor_registry.add(target)
    return ".. _%s:\n" % target


def printEnumeration(indent, ns, parent):
    node_list = parent.xpath("nx:item", namespaces=ns)
    if len(node_list) == 0:
        return ""

    if len(node_list) == 1:
        print(f"{indent}Obligatory value:", end="")
    else:
        print(f"{indent}Any of these values:", end="")

    docs = OrderedDict()
    for item in node_list:
        name = item.get("value")
        docs[name] = getDocLine(ns, item)

    ENUMERATION_INLINE_LENGTH = 60

    def show_as_typed_text(msg):
        return "``%s``" % msg

    oneliner = " | ".join(map(show_as_typed_text, docs.keys()))
    if any(doc for doc in docs.values()) or len(oneliner) > ENUMERATION_INLINE_LENGTH:
        # print one item per line
        print("\n")
        for name, doc in docs.items():
            print(f"{indent}  * {show_as_typed_text(name)}", end="")
            if doc:
                print(f": {doc}", end="")
            print("\n")
    else:
        # print all items in one line
        print(f" {oneliner}")
    print("")


def printDoc(indent, ns, node, required=False):
    blocks = getDocBlocks(ns, node)
    if len(blocks) == 0:
        if required:
            raise Exception("No documentation for: " + node.get("name"))
        print("")
    else:
        for block in blocks:
            for line in block.splitlines():
                print(f"{indent}{line}")
            print()


def printAttribute(ns, kind, node, optional, indent, parent_path):
    name = node.get("name")
    index_name = name
    print(f"{indent}" f"{hyperlinkTarget(parent_path, name, 'attribute')}")
    print(f"{indent}.. index:: {index_name} ({kind} attribute)\n")
    print(f"{indent}**@{name}**: {optional}{fmtTyp(node)}{fmtUnits(node)}\n")
    printDoc(indent + INDENTATION_UNIT, ns, node)
    node_list = node.xpath("nx:enumeration", namespaces=ns)
    if len(node_list) == 1:
        printEnumeration(indent + INDENTATION_UNIT, ns, node_list[0])


def printIfDeprecated(ns, node, indent):
    deprecated = node.get("deprecated", None)
    if deprecated is not None:
        print(f"\n{indent}.. index:: deprecated\n")
        print(f"\n{indent}**DEPRECATED**: {deprecated}\n")


def printFullTree(ns, parent, name, indent, parent_path):
    """
    recursively print the full tree structure

    :param dict ns: dictionary of namespaces for use in XPath expressions
    :param lxml_element_node parent: parent node to be documented
    :param str name: name of elements, such as NXentry/NXuser
    :param indent: to keep track of indentation level
    :param parent_path: NX class path of parent nodes
    """
    global listing_category

    use_application_defaults = listing_category in (
        "application definition",
        "contributed definition",
    )

    for node in parent.xpath("nx:field", namespaces=ns):
        name = node.get("name")
        index_name = name
        dims = analyzeDimensions(ns, node)

        optional_text = get_required_or_optional_text(node, use_application_defaults)
        print(f"{indent}{hyperlinkTarget(parent_path, name, 'field')}")
        print(f"{indent}.. index:: {index_name} (field)\n")
        print(
            f"{indent}**{name}**: "
            f"{optional_text}"
            f"{fmtTyp(node)}"
            f"{dims}"
            f"{fmtUnits(node)}"
            "\n"
        )

        printIfDeprecated(ns, node, indent + INDENTATION_UNIT)
        printDoc(indent + INDENTATION_UNIT, ns, node)

        node_list = node.xpath("nx:enumeration", namespaces=ns)
        if len(node_list) == 1:
            printEnumeration(indent + INDENTATION_UNIT, ns, node_list[0])

        for subnode in node.xpath("nx:attribute", namespaces=ns):
            optional = get_required_or_optional_text(subnode, use_application_defaults)
            printAttribute(
                ns,
                "field",
                subnode,
                optional,
                indent + INDENTATION_UNIT,
                parent_path + "/" + name,
            )

    for node in parent.xpath("nx:group", namespaces=ns):
        name = node.get("name", "")
        typ = node.get("type", "untyped (this is an error; please report)")

        optional_text = get_required_or_optional_text(node, use_application_defaults)
        if typ.startswith("NX"):
            if name == "":
                name = typ.lstrip("NX").upper()
            typ = ":ref:`%s`" % typ
        hTarget = hyperlinkTarget(parent_path, name, "group")
        target = hTarget.replace(".. _", "").replace(":\n", "")
        # TODO: https://github.com/nexusformat/definitions/issues/1057
        print(f"{indent}{hTarget}")
        print(f"{indent}**{name}**: {optional_text}{typ}\n")

        printIfDeprecated(ns, node, indent + INDENTATION_UNIT)
        printDoc(indent + INDENTATION_UNIT, ns, node)

        for subnode in node.xpath("nx:attribute", namespaces=ns):
            optional = get_required_or_optional_text(subnode, use_application_defaults)
            printAttribute(
                ns,
                "group",
                subnode,
                optional,
                indent + INDENTATION_UNIT,
                parent_path + "/" + name,
            )

        nodename = "%s/%s" % (name, node.get("type"))
        printFullTree(
            ns, node, nodename, indent + INDENTATION_UNIT, parent_path + "/" + name
        )

    for node in parent.xpath("nx:link", namespaces=ns):
        name = node.get("name")
        print(f"{indent}{hyperlinkTarget(parent_path, name, 'link')}")
        print(
            f"{indent}**{name}**: "
            ":ref:`link<Design-Links>` "
            f"(suggested target: ``{node.get('target')}``"
            "\n"
        )
        printDoc(indent + INDENTATION_UNIT, ns, node)


def print_rst_from_nxdl(nxdl_file):
    """
    print restructured text from the named .nxdl.xml file
    """
    global listing_category

    # parse input file into tree
    tree = lxml.etree.parse(nxdl_file)

    # The following URL is outdated, but that doesn't matter;
    # it won't be accessed; it's just an arbitrary namespace name.
    # It only needs to match the xmlns attribute in the NXDL files.
    NAMESPACE = "http://definition.nexusformat.org/nxdl/3.1"
    ns = {"nx": NAMESPACE}

    root = tree.getroot()
    name = root.get("name")
    title = name
    parent_path = "/" + name  # absolute path of parent nodes, no trailing /
    if len(name) < 2 or name[0:2] != "NX":
        raise Exception('Unexpected class name "%s"; does not start with NX' % (name))
    lexical_name = name[2:]  # without padding 'NX', for indexing

    # retrieve category from directory
    # subdir = os.path.split(os.path.split(tree.docinfo.URL)[0])[1]
    subdir = root.attrib["category"]

    # Pass these terms to construct the full URL
    anchor_registry.nxdl_file = nxdl_file
    anchor_registry.category = SUBDIR_MAP[subdir]

    # TODO: check for consistency with root.get('category')
    listing_category = {
        "base": "base class",
        "application": "application definition",
        "contributed": "contributed definition",
    }[subdir]

    use_application_defaults = listing_category in (
        "application definition",
        "contributed definition",
    )

    # print ReST comments and section header
    print(
        f".. auto-generated by script {sys.argv[0]} "
        f"from the NXDL source {sys.argv[1]}"
    )
    print("")
    print(".. index::")
    print(f"    ! {name} ({listing_category})")
    print(f"    ! {lexical_name} ({listing_category})")
    print(f"    see: {lexical_name} ({listing_category}); {name}")
    print("")
    print(f".. _{name}:\n")
    print("=" * len(title))
    print(title)
    print("=" * len(title))

    # print category & parent class
    extends = root.get("extends")
    if extends is None:
        extends = "none"
    else:
        extends = ":ref:`%s`" % extends

    print("")
    print("**Status**:\n")
    print(f"  {listing_category.strip()}, extends {extends}")

    printIfDeprecated(ns, root, "")

    # print official description of this class
    print("")
    print("**Description**:\n")
    printDoc(INDENTATION_UNIT, ns, root, required=True)

    # print symbol list
    node_list = root.xpath("nx:symbols", namespaces=ns)
    print("**Symbols**:\n")
    if len(node_list) == 0:
        print("  No symbol table\n")
    elif len(node_list) > 1:
        raise Exception("Invalid symbol table in " % root.get("name"))
    else:
        printDoc(INDENTATION_UNIT, ns, node_list[0])
        for node in node_list[0].xpath("nx:symbol", namespaces=ns):
            doc = getDocLine(ns, node)
            print(f"  **{node.get('name')}**", end="")
            if doc:
                print(f": {doc}", end="")
            print("\n")

    # print group references
    print("**Groups cited**:")
    node_list = root.xpath("//nx:group", namespaces=ns)
    groups = []
    for node in node_list:
        g = node.get("type")
        if g.startswith("NX") and g not in groups:
            groups.append(g)
    if len(groups) == 0:
        print("  none\n")
    else:
        out = [(":ref:`%s`" % g) for g in groups]
        txt = ", ".join(sorted(out))
        print(f"  {txt}\n")
        out = [("%s (base class); used in %s" % (g, listing_category)) for g in groups]
        txt = ", ".join(out)
        print(f".. index:: {txt}\n")

    # TODO: change instances of \t to proper indentation

    # print full tree
    print("**Structure**:\n")
    for subnode in root.xpath("nx:attribute", namespaces=ns):
        optional = get_required_or_optional_text(subnode, use_application_defaults)
        printAttribute(
            ns, "file", subnode, optional, INDENTATION_UNIT, parent_path
        )  # FIXME: +"/"+name )
    printFullTree(ns, root, name, INDENTATION_UNIT, parent_path)

    printAnchorList()

    # print NXDL source location
    print("")
    print("**NXDL Source**:")
    print(f"  {HTML_ROOT}/{SUBDIR_MAP[subdir]}/{name}.nxdl.xml")


def main():
    """
    standard command-line processing
    """
    import argparse

    parser = argparse.ArgumentParser(description="test nxdl2rst code")
    parser.add_argument("nxdl_file", help="name of NXDL file")
    results = parser.parse_args()
    nxdl_file = results.nxdl_file

    if not os.path.exists(nxdl_file):
        print(f"Cannot find {nxdl_file}")
        exit()

    print_rst_from_nxdl(nxdl_file)

    # if the NXDL has a subdirectory,
    # copy that subdirectory (quietly) to the pwd, such as:
    #  contributed/NXcanSAS.nxdl.xml: cp -a contributed/canSAS ./
    category = os.path.basename(os.getcwd())
    path = os.path.join("../../../../", category)
    basename = os.path.basename(nxdl_file)
    corename = basename[2:].split(".")[0]
    source = os.path.join(path, corename)
    if os.path.exists(source):
        target = os.path.join(".", corename)
        replicate(source, target)


if __name__ == "__main__":
    WRITE_ANCHOR_REGISTRY = True
    main()


# NeXus - Neutron and X-ray Common Data Format
#
# Copyright (C) 2008-2022 NeXus International Advisory Committee (NIAC)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org
