# pylint: disable=too-many-lines
"""Parse NeXus definition files"""

import os
import re
import textwrap
from functools import lru_cache
from glob import glob
from pathlib import Path
from typing import List
from typing import Optional

import lxml.etree as ET
from lxml.etree import ParseError as xmlER


def remove_namespace_from_tag(tag):
    """Helper function to remove the namespace from an XML tag."""

    return tag.split("}")[-1]


class NxdlAttributeNotFoundError(Exception):
    """An exception to throw when an Nxdl attribute is not found."""


def get_nexus_definitions_path():
    """Check NEXUS_DEF_PATH variable.
    If it is empty, this function is filling it"""
    try:  # either given by sys env
        return Path(os.environ["NEXUS_DEF_PATH"])
    except KeyError:  # or it should be available locally under the dir 'definitions'
        local_dir = Path(__file__).resolve().parent
        for _ in range(2):
            local_dir = local_dir.parent
        return local_dir


nexus_def_path = get_nexus_definitions_path()


def get_app_defs_names():
    """Returns all the AppDef names without their extension: .nxdl.xml"""
    app_def_path_glob = nexus_def_path / "applications" / "*.nxdl*"

    contrib_def_path_glob = Path(nexus_def_path) / "contributed_definitions" / "*.nxdl*"

    files = sorted(glob(str(app_def_path_glob)))
    for nexus_file in sorted(glob(str(contrib_def_path_glob))):
        root = get_xml_root(nexus_file)
        if root.attrib["category"] == "application":
            files.append(nexus_file)

    return [Path(file).name[:-9] for file in files] + ["NXroot"]


@lru_cache(maxsize=None)
def get_xml_root(file_path):
    """Reducing I/O time by caching technique"""

    return ET.parse(file_path).getroot()


def get_hdf_root(hdf_node):
    """Get the root HDF5 node"""
    node = hdf_node
    while node.name != "/":
        node = node.parent
    return node


def get_hdf_parent(hdf_info):
    """Get the parent of an hdf_node in an hdf_info"""
    if "hdf_path" not in hdf_info:
        return hdf_info["hdf_node"].parent
    node = (
        get_hdf_root(hdf_info["hdf_node"])
        if "hdf_root" not in hdf_info
        else hdf_info["hdf_root"]
    )
    for child_name in hdf_info["hdf_path"].split("/"):
        node = node[child_name]
    return node


def get_parent_path(hdf_name):
    """Get parent path"""
    return hdf_name.rsplit("/", 1)[0]


def get_hdf_info_parent(hdf_info):
    """Get the hdf_info for the parent of an hdf_node in an hdf_info"""
    if "hdf_path" not in hdf_info:
        return {"hdf_node": hdf_info["hdf_node"].parent}
    node = (
        get_hdf_root(hdf_info["hdf_node"])
        if "hdf_root" not in hdf_info
        else hdf_info["hdf_root"]
    )
    for child_name in hdf_info["hdf_path"].split("/")[1:-1]:
        node = node[child_name]
    return {"hdf_node": node, "hdf_path": get_parent_path(hdf_info["hdf_path"])}


def get_nx_class(nxdl_elem):
    """Get the nexus class for a NXDL node"""
    if "category" in nxdl_elem.attrib.keys():
        return ""
    return nxdl_elem.attrib.get("type", "NX_CHAR")


def get_nx_namefit(hdf_name: str, name: str, name_any: bool = False) -> int:
    """
    Checks if an HDF5 node name corresponds to a child of the NXDL element.
    A group of uppercase letters anywhere in the name is treated as freely choosable
    part of this name.
    If a match is found this function returns twice the length for an exact match,
    otherwise the number of matching characters (case insensitive) or zero, if
    `name_any` is set to True, is returned.
    All uppercase groups are considered independently.
    Lowercase matches are independent of uppercase group lengths, e.g.,
    an hdf_name `get_nx_namefit("my_fancy_yet_long_name", "my_SOME_name")` would
    return a score of 8 for the lowercase matches `my_..._name`.
    All characters in `[a-zA-Z0-9_.]` are considered for matching to an uppercase letter.
    If you use any other letter in the name, it will not match and return -1.
    Periods at the beginning or end of the hdf_name are not allowed, only exact
    matches will be considered.

    Examples:

        * `get_nx_namefit("test_name", "TEST_name")` returns 9
        * `get_nx_namefit("te_name", "TEST_name")` returns 7
        * `get_nx_namefit("my_other_name", "TEST_name")` returns 5
        * `get_nx_namefit("test_name", "test_name")` returns 18
        * `get_nx_namefit("test_other", "test_name")` returns -1

    Args:
        hdf_name (str): The hdf_name, containing the name of the HDF5 node.
        name (str): The concept name to match against.
        name_any (bool, optional):
            Accept any name and return either 0 (match) or -1 (no match).
            Defaults to False.

    Returns:
        int: -1 if no match is found or the number of matching
             characters (case insensitive).
    """
    path_regex = r"([a-zA-Z0-9_.]+)"

    if name == hdf_name:
        return len(name) * 2
    if hdf_name.startswith(".") or hdf_name.endswith("."):
        # Don't match anything with a dot at the beginning or end
        return -1

    uppercase_parts = re.findall(r"[A-Z]+(?:_[A-Z]+)*", name)

    regex_name = name
    uppercase_count = 0
    for up in uppercase_parts:
        uppercase_count += len(up)
        regex_name = regex_name.replace(up, path_regex)

    name_match = re.search(rf"^{regex_name}$", hdf_name)
    if name_match is None:
        return 0 if name_any else -1

    match_count = 0
    for uppercase, match in zip(uppercase_parts, name_match.groups()):
        for s1, s2 in zip(uppercase.upper(), match.upper()):
            if s1 == s2:
                match_count += 1

    return len(name) + match_count - uppercase_count


def get_nx_classes():
    """Read base classes from the NeXus definition folder.
    Check each file in base_classes, applications, contributed_definitions.
    If its category attribute is 'base', then it is added to the list."""
    nexus_definition_path = nexus_def_path
    base_classes = sorted(nexus_definition_path.glob("base_classes/*.nxdl.xml"))
    applications = sorted(nexus_definition_path.glob("applications/*.nxdl.xml"))
    contributed = sorted(
        nexus_definition_path.glob("contributed_definitions/*.nxdl.xml")
    )
    nx_class = []
    for nexus_file in base_classes + applications + contributed:
        try:
            root = get_xml_root(nexus_file)
        except xmlER as e:
            raise ValueError(f"Getting an issue while parsing file {nexus_file}") from e
        if root.attrib["category"] == "base":
            nx_class.append(nexus_file.name[:-9])
    return sorted(nx_class)


def get_nx_units():
    """Read unit kinds from the NeXus definition/nxdlTypes.xsd file"""
    filepath = nexus_def_path / "nxdlTypes.xsd"
    root = get_xml_root(filepath)
    units_and_type_list = []
    for child in root:
        units_and_type_list.extend(child.attrib.values())
    flag = False
    nx_units = []
    for line in units_and_type_list:
        if line == "anyUnitsAttr":
            flag = True
        elif "NX" in line and flag:
            nx_units.append(line)
        elif line == "primitiveType":
            flag = False

    return nx_units


def get_nx_attribute_type():
    """Read attribute types from the NeXus definition/nxdlTypes.xsd file"""
    filepath = nexus_def_path / "nxdlTypes.xsd"

    root = get_xml_root(filepath)
    units_and_type_list = []
    for child in root:
        units_and_type_list.extend(child.attrib.values())
    flag = False
    nx_types = []
    for line in units_and_type_list:
        if line == "primitiveType":
            flag = True
        elif "NX" in line and flag is True:
            nx_types.append(line)
        elif line == "anyUnitsAttr":
            flag = False
        else:
            pass
    return nx_types


def get_node_name(node):
    """Node - xml node. Returns html documentation name.
    Either as specified by the 'name' or taken from the type (nx_class).
    Note that if only class name is available, the NX prefix is removed and
    the string is converted to UPPER case."""
    if "name" in node.attrib:
        name = node.attrib["name"]
    else:
        name = node.attrib["type"]
        if name.startswith("NX"):
            name = name[2:].upper()
    return name


def belongs_to(nxdl_elem, child, name, class_type=None, hdf_name=None):
    """Checks if an HDF5 node name corresponds to a child of the NXDL element
    uppercase letters in front can be replaced by arbitraty name, but
    uppercase to lowercase match is preferred"""
    if class_type and get_nx_class(child) != class_type:
        return False
    act_htmlname = get_node_name(child)
    chk_name = hdf_name or name
    if act_htmlname == chk_name:
        return True
    if not hdf_name:  # search for name fits is only allowed for hdf_nodes
        return False
    try:  # check if nameType allows different name
        name_any = bool(child.attrib["nameType"] == "any")
    except KeyError:
        name_any = False
    params = [act_htmlname, chk_name, name_any, nxdl_elem, child, name]
    return belongs_to_capital(params)


def belongs_to_capital(params):
    """Checking continues for Upper case"""
    (act_htmlname, chk_name, name_any, nxdl_elem, child, name) = params
    # or starts with capital and no reserved words used
    if (
        (name_any or (act_htmlname[0].isalpha() and act_htmlname[0].isupper()))
        and name != "doc"
        and name != "enumeration"
    ):
        fit = get_nx_namefit(chk_name, act_htmlname, name_any)  # check if name fits
        if fit < 0:
            return False
        for child2 in nxdl_elem:
            if not isinstance(child2.tag, str):
                continue
            if (
                get_local_name_from_xml(child) != get_local_name_from_xml(child2)
                or get_node_name(child2) == act_htmlname
            ):
                continue
            # check if the name of another sibling fits better
            name_any2 = child2.attrib.get("nameType") == "any"
            fit2 = get_nx_namefit(chk_name, get_node_name(child2), name_any2)
            if fit2 > fit:
                return False
        # accept this fit
        return True
    return False


def get_local_name_from_xml(element):
    """Helper function to extract the element tag without the namespace."""
    return remove_namespace_from_tag(element.tag)


def get_own_nxdl_child_reserved_elements(child, name, nxdl_elem):
    """checking reserved elements, like doc, enumeration"""
    local_name = get_local_name_from_xml(child)
    if local_name == "doc" and name == "doc":
        return set_nxdlpath(child, nxdl_elem, tag_name=name)

    if local_name == "enumeration" and name == "enumeration":
        return set_nxdlpath(child, nxdl_elem, tag_name=name)
    return False


def get_own_nxdl_child_base_types(child, class_type, nxdl_elem, name, hdf_name):
    """checking base types of group, field, attribute"""
    if get_local_name_from_xml(child) == "group":
        if (
            class_type is None or (class_type and get_nx_class(child) == class_type)
        ) and belongs_to(nxdl_elem, child, name, class_type, hdf_name):
            return set_nxdlpath(child, nxdl_elem)
    if get_local_name_from_xml(child) == "field" and belongs_to(
        nxdl_elem, child, name, None, hdf_name
    ):
        return set_nxdlpath(child, nxdl_elem)
    if get_local_name_from_xml(child) == "attribute" and belongs_to(
        nxdl_elem, child, name, None, hdf_name
    ):
        return set_nxdlpath(child, nxdl_elem)
    return False


def get_own_nxdl_child(
    nxdl_elem, name, class_type=None, hdf_name=None, nexus_type=None
):
    """Checks if an NXDL child node fits to the specific name (either nxdl or hdf)
    name       - nxdl name
    class_type - nxdl type or hdf classname (for groups, it is obligatory)
    hdf_name   - hdf name"""
    for child in nxdl_elem:
        if not isinstance(child.tag, str):
            continue
        result = get_own_nxdl_child_reserved_elements(child, name, nxdl_elem)
        if result is not False:
            return result
        if nexus_type and get_local_name_from_xml(child) != nexus_type:
            continue
        result = get_own_nxdl_child_base_types(
            child, class_type, nxdl_elem, name, hdf_name
        )
        if result is not False:
            return result
    return None


def find_definition_file(bc_name):
    """find the nxdl file corresponding to the name.
    Note that it first checks in contributed and goes beyond only if no contributed found
    """
    bc_filename = None
    for nxdl_folder in ["contributed_definitions", "base_classes", "applications"]:
        nxdl_file = nexus_def_path / nxdl_folder / f"{bc_name}.nxdl.xml"
        if nxdl_file.exists():
            bc_filename = nexus_def_path / nxdl_folder / f"{bc_name}.nxdl.xml"
            break
    return bc_filename


def get_nxdl_child(
    nxdl_elem, name, class_type=None, hdf_name=None, nexus_type=None, go_base=True
):  # pylint: disable=too-many-arguments
    """Get the NXDL child node corresponding to a specific name
    (e.g. of an HDF5 node,or of a documentation) note that if child is not found in application
    definition, it also checks for the base classes"""
    # search for possible fits for hdf_nodes : skipped
    # only exact hits are returned when searching an nxdl child
    own_child = get_own_nxdl_child(nxdl_elem, name, class_type, hdf_name, nexus_type)
    if own_child is not None:
        return own_child
    if not go_base:
        return None
    bc_name = get_nx_class(nxdl_elem)  # check in the base class, app def or contributed
    if bc_name[2] == "_":  # filter primitive types
        return None
    if (
        bc_name == "group"
    ):  # Check if it is the root element. Then send to NXroot.nxdl.xml
        bc_name = "NXroot"
    bc_filename = find_definition_file(bc_name)
    if not bc_filename:
        raise ValueError("nxdl file not found in definitions folder!")
    bc_obj = ET.parse(bc_filename).getroot()
    bc_obj.set("nxdlbase", bc_filename)
    if "category" in bc_obj.attrib:
        bc_obj.set("nxdlbase_class", bc_obj.attrib["category"])
    bc_obj.set("nxdlpath", "")
    return get_own_nxdl_child(bc_obj, name, class_type, hdf_name, nexus_type)


def get_required_string(nxdl_elem):
    """Check for being REQUIRED, RECOMMENDED, OPTIONAL, NOT IN SCHEMA"""
    if nxdl_elem is None:
        return "<<NOT IN SCHEMA>>"
    is_optional = (
        "optional" in nxdl_elem.attrib.keys() and nxdl_elem.attrib["optional"] == "true"
    )
    is_minoccurs = (
        "minOccurs" in nxdl_elem.attrib.keys() and nxdl_elem.attrib["minOccurs"] == "0"
    )
    is_recommended = (
        "recommended" in nxdl_elem.attrib.keys()
        and nxdl_elem.attrib["recommended"] == "true"
    )

    if is_recommended:
        return "<<RECOMMENDED>>"
    if is_optional or is_minoccurs:
        return "<<OPTIONAL>>"
    # default optionality: in BASE CLASSES is true; in APPLICATIONS is false
    if nxdl_elem.get("nxdlbase_class") == "base":
        return "<<OPTIONAL>>"
    return "<<REQUIRED>>"


# below there are some functions used in get_nxdl_doc function:
def write_doc_string(logger, doc, attr):
    """Simple function that prints a line in the logger if doc exists"""
    if doc:
        logger.debug(f"@{attr} [NX_CHAR]")
    return logger, doc, attr


def try_find_units(logger, elem, nxdl_path, doc, attr):
    """Try to find if units is defined inside the field in the NXDL element,
    otherwise try to find if units is defined as a child of the NXDL element."""
    try:  # try to find if units is defined inside the field in the NXDL element
        unit = elem.attrib[attr]
        if doc:
            logger.debug(get_node_concept_path(elem) + "@" + attr + " [" + unit + "]")
        elem = None
        nxdl_path.append(attr)
    except (
        KeyError
    ):  # otherwise try to find if units is defined as a child of the NXDL element
        orig_elem = elem
        elem = get_nxdl_child(elem, attr, nexus_type="attribute")
        if elem is not None:
            if doc:
                logger.debug(
                    get_node_concept_path(orig_elem)
                    + "@"
                    + attr
                    + " - ["
                    + get_nx_class(elem)
                    + "]"
                )
            nxdl_path.append(elem)
        else:  # if no units category were defined in NXDL:
            if doc:
                logger.debug(
                    get_node_concept_path(orig_elem)
                    + "@"
                    + attr
                    + " - REQUIRED, but undefined unit category"
                )
            nxdl_path.append(attr)
    return logger, elem, nxdl_path, doc, attr


def check_attr_name_nxdl(param):
    """Check for ATTRIBUTENAME_units in NXDL (normal).
    If not defined, check for ATTRIBUTENAME to see if the ATTRIBUTE
    is in the SCHEMA, but no units category were defined."""
    (logger, elem, nxdl_path, doc, attr, req_str) = param
    orig_elem = elem
    elem2 = get_nxdl_child(elem, attr, nexus_type="attribute")
    if elem2 is not None:  # check for ATTRIBUTENAME_units in NXDL (normal)
        elem = elem2
        if doc:
            logger.debug(
                get_node_concept_path(orig_elem)
                + "@"
                + attr
                + " - ["
                + get_nx_class(elem)
                + "]"
            )
        nxdl_path.append(elem)
    else:
        # if not defined, check for ATTRIBUTENAME to see if the ATTRIBUTE
        # is in the SCHEMA, but no units category were defined
        elem2 = get_nxdl_child(elem, attr[:-6], nexus_type="attribute")
        if elem2 is not None:
            req_str = "<<RECOMMENDED>>"
            if doc:
                logger.debug(
                    get_node_concept_path(orig_elem)
                    + "@"
                    + attr
                    + " - RECOMMENDED, but undefined unit category"
                )
            nxdl_path.append(attr)
        else:  # otherwise: NOT IN SCHEMA
            elem = elem2
            if doc:
                logger.debug(
                    get_node_concept_path(orig_elem)
                    + "@"
                    + attr
                    + " - IS NOT IN SCHEMA"
                )
    return logger, elem, nxdl_path, doc, attr, req_str


def try_find_default(
    logger, orig_elem, elem, nxdl_path, doc, attr
):  # pylint: disable=too-many-arguments
    """Try to find if default is defined as a child of the NXDL element"""
    if elem is not None:
        if doc:
            logger.debug(
                get_node_concept_path(orig_elem)
                + "@"
                + attr
                + " - ["
                + get_nx_class(elem)
                + "]"
            )
        nxdl_path.append(elem)
    else:  # if no default category were defined in NXDL:
        if doc:
            logger.debug(get_node_concept_path(orig_elem) + "@" + attr + " - [NX_CHAR]")
        nxdl_path.append(attr)
    return logger, elem, nxdl_path, doc, attr


def other_attrs(
    logger, orig_elem, elem, nxdl_path, doc, attr
):  # pylint: disable=too-many-arguments
    """Handle remaining attributes"""
    if elem is not None:
        if doc:
            logger.debug(
                get_node_concept_path(orig_elem)
                + "@"
                + attr
                + " - ["
                + get_nx_class(elem)
                + "]"
            )
        nxdl_path.append(elem)
    else:
        if doc:
            logger.debug(
                get_node_concept_path(orig_elem) + "@" + attr + " - IS NOT IN SCHEMA"
            )
    return logger, elem, nxdl_path, doc, attr


def get_node_concept_path(elem):
    """get the short version of nxdlbase:nxdlpath"""
    return f'{elem.get("nxdlbase").split("/")[-1]}:{elem.get("nxdlpath")}'


def get_doc(node, ntype, nxhtml, nxpath):
    """Get documentation"""
    # URL for html documentation
    anchor = ""
    for n_item in nxpath:
        anchor += n_item.lower() + "-"
    anchor = (
        "https://manual.nexusformat.org/classes/",
        nxhtml + "#" + anchor.replace("_", "-") + ntype,
    )
    if not ntype:
        anchor = anchor[:-1]
    doc = ""  # RST documentation from the field 'doc'
    doc_field = node.find("doc")
    if doc_field is not None:
        doc = doc_field.text
    enums = get_enums(node)  # enums
    if enums is not None:
        enum_str = (
            "\n "
            + ("Possible values:" if len(enums) > 1 else "Obligatory value:")
            + "\n   "
            + "["
            + ",".join(enums)
            + "]"
            + "\n"
        )
    else:
        enum_str = ""
    return anchor, doc + enum_str


def print_doc(node, ntype, level, nxhtml, nxpath):
    """Print documentation"""
    anchor, doc = get_doc(node, ntype, nxhtml, nxpath)
    print("  " * (level + 1) + anchor)
    preferred_width = 80 + level * 2
    wrapper = textwrap.TextWrapper(
        initial_indent="  " * (level + 1),
        width=preferred_width,
        subsequent_indent="  " * (level + 1),
        expand_tabs=False,
        tabsize=0,
    )
    if doc is not None:
        for par in doc.split("\n"):
            print(wrapper.fill(par))


def get_namespace(element):
    """Extracts the namespace for elements in the NXDL"""
    return element.tag[element.tag.index("{") : element.tag.rindex("}") + 1]


def get_enums(node: ET._Element) -> Optional[List[str]]:
    """
    Makes list of enumerations, if node contains any.

    Args:
        node (ET._Element): The node to check for enumerations.

    Returns:
        Optional[List[str]]:
            Returns a list of the enumeration values if an enumeration was found.
            If no enumeration was found it returns None.
    """
    namespace = get_namespace(node)
    enums = []
    for enumeration in node.findall(f"{namespace}enumeration"):
        for item in enumeration.findall(f"{namespace}item"):
            enums.append(item.attrib["value"])
        if enums:
            return enums
    return None


def add_base_classes(elist, nx_name=None, elem: ET.Element = None):
    """
    Add the base classes corresponding to the last element in elist to the list. Note that if
    elist is empty, a nxdl file with the name of nx_name or a placeholder elem is used if provided
    """
    if elist and nx_name is None:
        nx_name = get_nx_class(elist[-1])
    # to support recursive defintions, like NXsample in NXsample, the following test is removed
    # if elist and nx_name and f"{nx_name}.nxdl.xml" in (e.get('nxdlbase') for e in elist):
    #     return
    if elem is None:
        if not nx_name:
            return
        nxdl_file_path = find_definition_file(nx_name)
        if nxdl_file_path is None:
            nxdl_file_path = f"{nx_name}.nxdl.xml"

        try:
            elem = ET.parse(os.path.abspath(nxdl_file_path)).getroot()
            # elem = ET.parse(nxdl_file_path).getroot()
        except OSError:
            with open(nxdl_file_path, "r") as f:
                elem = ET.parse(f).getroot()

        if not isinstance(nxdl_file_path, str):
            nxdl_file_path = str(nxdl_file_path)
        elem.set("nxdlbase", nxdl_file_path)
    else:
        elem.set("nxdlbase", "")
    if "category" in elem.attrib:
        elem.set("nxdlbase_class", elem.attrib["category"])
    elem.set("nxdlpath", "")
    elist.append(elem)
    # add inherited base class
    if "extends" in elem.attrib and elem.attrib["extends"] != "NXobject":
        add_base_classes(elist, elem.attrib["extends"])
    else:
        add_base_classes(elist)


def set_nxdlpath(child, nxdl_elem, tag_name=None):
    """Setting up child nxdlbase, nxdlpath and nxdlbase_class from nxdl_element."""
    if nxdl_elem.get("nxdlbase") is not None:
        child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
        child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
        # Handle element that does not has 'name' attr e.g. doc, enumeration
        if tag_name:
            child.set("nxdlpath", nxdl_elem.get("nxdlpath") + "/" + tag_name)
        else:
            child.set(
                "nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child)
            )

    return child


def get_direct_child(nxdl_elem, html_name):
    """returns the child of nxdl_elem which has a name
    corresponding to the html documentation name html_name"""
    for child in nxdl_elem:
        if not isinstance(child.tag, str):
            continue
        if get_local_name_from_xml(child) in (
            "group",
            "field",
            "attribute",
        ) and html_name == get_node_name(child):
            decorated_child = set_nxdlpath(child, nxdl_elem)
            return decorated_child
    return None


def get_field_child(nxdl_elem, html_name):
    """returns the child of nxdl_elem which has a name
    corresponding to the html documentation name html_name"""
    data_child = None
    for child in nxdl_elem:
        if not isinstance(child.tag, str):
            continue
        if get_local_name_from_xml(child) != "field":
            continue
        if get_node_name(child) == html_name:
            data_child = set_nxdlpath(child, nxdl_elem)
            break
    return data_child


def get_best_nxdata_child(nxdl_elem, hdf_node, hdf_name):
    """returns the child of an NXdata nxdl_elem which has a name
    corresponding to the hdf_name"""
    nxdata = hdf_node.parent
    signals = []
    if "signal" in nxdata.attrs.keys():
        signals.append(nxdata.attrs.get("signal"))
    if "auxiliary_signals" in nxdata.attrs.keys():
        for aux_signal in nxdata.attrs.get("auxiliary_signals"):
            signals.append(aux_signal)
    data_child = get_field_child(nxdl_elem, "DATA")
    data_error_child = get_field_child(nxdl_elem, "FIELDNAME_errors")
    for signal in signals:
        if signal == hdf_name:
            return (data_child, 100)
        if hdf_name.endswith("_errors") and signal == hdf_name[:-7]:
            return (data_error_child, 100)
    axes = []
    if "axes" in nxdata.attrs.keys():
        for axis in nxdata.attrs.get("axes"):
            axes.append(axis)
    axis_child = get_field_child(nxdl_elem, "AXISNAME")
    for axis in axes:
        if axis == hdf_name:
            return (axis_child, 100)
    return (None, 0)


def get_best_child(nxdl_elem, hdf_node, hdf_name, hdf_class_name, nexus_type):
    """returns the child of nxdl_elem which has a name
    corresponding to the html documentation name html_name"""
    bestfit = -1
    bestchild = None
    if (
        "name" in nxdl_elem.attrib.keys()
        and nxdl_elem.attrib["name"] == "NXdata"
        and hdf_node is not None
        and hdf_node.parent is not None
        and hdf_node.parent.attrs.get("NX_class") == "NXdata"
    ):
        (fnd_child, fit) = get_best_nxdata_child(nxdl_elem, hdf_node, hdf_name)
        if fnd_child is not None:
            return (fnd_child, fit)
    for child in nxdl_elem:
        if not isinstance(child.tag, str):
            continue
        fit = -2
        if get_local_name_from_xml(child) == nexus_type and (
            nexus_type != "group" or get_nx_class(child) == hdf_class_name
        ):
            name_any = (
                "nameType" in nxdl_elem.attrib.keys()
                and nxdl_elem.attrib["nameType"] == "any"
            )
            fit = get_nx_namefit(hdf_name, get_node_name(child), name_any)
        if fit > bestfit:
            bestfit = fit
            bestchild = set_nxdlpath(child, nxdl_elem)
    return (bestchild, bestfit)


def walk_elist(elist, html_name):
    """Handle elist from low priority inheritance classes to higher"""
    for ind in range(len(elist) - 1, -1, -1):
        child = get_direct_child(elist[ind], html_name)
        if child is None:
            # check for names fitting to a superclas definition
            main_child = None
            for potential_direct_parent in elist:
                main_child = get_direct_child(potential_direct_parent, html_name)
                if main_child is not None:
                    (fitting_child, _) = get_best_child(
                        elist[ind],
                        None,
                        html_name,
                        get_nx_class(main_child),
                        get_local_name_from_xml(main_child),
                    )
                    if fitting_child is not None:
                        child = fitting_child
                    break
        elist[ind] = child
        if child is None:
            del elist[ind]
            continue
        # override: remove low priority inheritance classes if class_type is overriden
        if len(elist) > ind + 1 and get_nx_class(elist[ind]) != get_nx_class(
            elist[ind + 1]
        ):
            del elist[ind + 1 :]
        # add new base class(es) if new element brings such (and not a primitive type)
        if len(elist) == ind + 1 and not get_nx_class(elist[ind]).startswith("NX_"):
            add_base_classes(elist)
    return elist, html_name


@lru_cache(maxsize=None)
def get_inherited_nodes(
    nxdl_path: str = None,  # pylint: disable=too-many-arguments,too-many-locals
    nx_name: str = None,
    elem: ET.Element = None,
):
    """Returns a list of ET.Element for the given path."""
    # let us start with the given definition file
    elist = []  # type: ignore[var-annotated]
    add_base_classes(elist, nx_name, elem)
    nxdl_elem_path = [elist[0]]

    class_path = []  # type: ignore[var-annotated]
    html_paths = nxdl_path.split("/")[1:]
    for html_name in html_paths:
        elist, _ = walk_elist(elist, html_name)
        if elist:
            class_path.append(get_nx_class(elist[0]))
            nxdl_elem_path.append(elist[0])
    return (class_path, nxdl_elem_path, elist)


def get_node_at_nxdl_path(
    nxdl_path: str = None,
    nx_name: str = None,
    elem: ET.Element = None,
    exc: bool = True,
):
    """Returns an ET.Element for the given path.
    This function either takes the name for the NeXus Application Definition
    we are looking for or the root elem from a previously loaded NXDL file
    and finds the corresponding XML element with the needed attributes."""
    try:
        if nxdl_path.count("/") == 1 and not nxdl_path.upper().startswith("/ENTRY"):
            elem = None
            nx_name = "NXroot"
        (class_path, nxdlpath, elist) = get_inherited_nodes(nxdl_path, nx_name, elem)
    except ValueError as value_error:
        if exc:
            raise NxdlAttributeNotFoundError(
                f"Attributes were not found for {nxdl_path}. "
                "Please check this entry in the template dictionary."
            ) from value_error
        return None
    if class_path and nxdlpath and elist:
        elem = elist[0]
    else:
        elem = None
        if exc:
            raise NxdlAttributeNotFoundError(
                f"Attributes were not found for {nxdl_path}. "
                "Please check this entry in the template dictionary."
            )
    return elem
