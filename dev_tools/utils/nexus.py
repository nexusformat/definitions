# pylint: disable=too-many-lines
"""Read files from different format and print it in a standard NeXus format
"""

import logging
import os
import sys
import textwrap
import xml.etree.ElementTree as ET
from functools import lru_cache
from glob import glob

import click
import h5py


class NxdlAttributeError(Exception):
    """An exception for throwing an error when an Nxdl attribute is not found."""


def get_app_defs_names():
    """Returns all the AppDef names without their extension: .nxdl.xml"""
    app_def_path_glob = (
        f"{get_nexus_definitions_path()}{os.sep}applications{os.sep}*.nxdl*"
    )
    contrib_def_path_glob = (
        f"{get_nexus_definitions_path()}{os.sep}"
        f"contributed_definitions{os.sep}*.nxdl*"
    )
    files = sorted(glob(app_def_path_glob)) + sorted(glob(contrib_def_path_glob))
    return [os.path.basename(file).split(".")[0] for file in files] + ["NXroot"]


@lru_cache(maxsize=None)
def get_xml_root(file_path):
    """Reducing I/O time by caching technique"""

    return ET.parse(file_path).getroot()


def get_nexus_definitions_path():
    """Check NEXUS_DEF_PATH variable.
    If it is empty, this function is filling it"""
    try:  # either given by sys env
        return os.environ["NEXUS_DEF_PATH"]
    except KeyError:  # or it should be available locally under the dir 'definitions'
        local_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(local_dir, f"..{os.sep}definitions")


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
    return "/".join(hdf_name.split("/")[:-1])


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


def get_nx_class_path(hdf_info):
    """Get the full path of an HDF5 node using nexus classes
    in case of a field, end with the field name"""
    hdf_node = hdf_info["hdf_node"]
    if hdf_node.name == "/":
        return ""
    if isinstance(hdf_node, h5py.Group):
        return (
            get_nx_class_path(get_hdf_info_parent(hdf_info))
            + "/"
            + (
                hdf_node.attrs["NX_class"]
                if "NX_class" in hdf_node.attrs.keys()
                else hdf_node.name.split("/")[-1]
            )
        )
    if isinstance(hdf_node, h5py.Dataset):
        return (
            get_nx_class_path(get_hdf_info_parent(hdf_info))
            + "/"
            + hdf_node.name.split("/")[-1]
        )
    return ""


def get_nxdl_entry(hdf_info):
    """Get the nxdl application definition for an HDF5 node"""
    entry = hdf_info
    while (
        isinstance(entry["hdf_node"], h5py.Dataset)
        or "NX_class" not in entry["hdf_node"].attrs.keys()
        or entry["hdf_node"].attrs["NX_class"] != "NXentry"
    ):
        entry = get_hdf_info_parent(entry)
        if entry["hdf_node"].name == "/":
            return "NO NXentry found"
    try:
        nxdef = entry["hdf_node"]["definition"][()]
        return nxdef.decode()
    except KeyError:  # 'NO Definition referenced'
        return "NXentry"


def get_nx_class(nxdl_elem):
    """Get the nexus class for a NXDL node"""
    if "category" in nxdl_elem.attrib.keys():
        return None
    try:
        return nxdl_elem.attrib["type"]
    except KeyError:
        return "NX_CHAR"


def get_nx_namefit(hdf_name, name, name_any=False):
    """Checks if an HDF5 node name corresponds to a child of the NXDL element
    uppercase letters in front can be replaced by arbitraty name, but
    uppercase to lowercase match is preferred,
    so such match is counted as a measure of the fit"""
    if name == hdf_name:
        return len(name) * 2
    # count leading capitals
    counting = 0
    while counting < len(name) and name[counting].upper() == name[counting]:
        counting += 1
    if (
        name_any
        or counting == len(name)
        or (counting > 0 and hdf_name.endswith(name[counting:]))
    ):  # if potential fit
        # count the matching chars
        fit = 0
        for i in range(min(counting, len(hdf_name))):
            if hdf_name[i].upper() == name[i]:
                fit += 1
            else:
                break
        if fit == min(counting, len(hdf_name)):  # accept only full fits as better fits
            return fit
        return 0
    return -1  # no fit


def get_nx_classes():
    """Read base classes from the NeXus definition folder.
    Check each file in base_classes, applications, contributed_definitions.
    If its category attribute is 'base', then it is added to the list."""
    base_classes = sorted(
        glob(os.path.join(get_nexus_definitions_path(), "base_classes", "*.nxdl.xml"))
    )
    applications = sorted(
        glob(os.path.join(get_nexus_definitions_path(), "applications", "*.nxdl.xml"))
    )
    contributed = sorted(
        glob(
            os.path.join(
                get_nexus_definitions_path(), "contributed_definitions", "*.nxdl.xml"
            )
        )
    )
    nx_clss = []
    for nexus_file in base_classes + applications + contributed:
        root = get_xml_root(nexus_file)
        if root.attrib["category"] == "base":
            nx_clss.append(str(nexus_file[nexus_file.rindex(os.sep) + 1 :])[:-9])
    nx_clss = sorted(nx_clss)
    return nx_clss


def get_nx_units():
    """Read unit kinds from the NeXus definition/nxdlTypes.xsd file"""
    filepath = f"{get_nexus_definitions_path()}{os.sep}nxdlTypes.xsd"
    root = get_xml_root(filepath)
    units_and_type_list = []
    for child in root:
        for i in child.attrib.values():
            units_and_type_list.append(i)
    flag = False
    for line in units_and_type_list:
        if line == "anyUnitsAttr":
            flag = True
            nx_units = []
        elif "NX" in line and flag is True:
            nx_units.append(line)
        elif line == "primitiveType":
            flag = False
        else:
            pass
    return nx_units


def get_nx_attribute_type():
    """Read attribute types from the NeXus definition/nxdlTypes.xsd file"""
    filepath = get_nexus_definitions_path() + "/nxdlTypes.xsd"
    root = get_xml_root(filepath)
    units_and_type_list = []
    for child in root:
        for i in child.attrib.values():
            units_and_type_list.append(i)
    flag = False
    for line in units_and_type_list:
        if line == "primitiveType":
            flag = True
            nx_types = []
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
    if "name" in node.attrib.keys():
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
        (name_any or "A" <= act_htmlname[0] <= "Z")
        and name != "doc"
        and name != "enumeration"
    ):
        fit = get_nx_namefit(chk_name, act_htmlname, name_any)  # check if name fits
        if fit < 0:
            return False
        for child2 in nxdl_elem:
            if (
                get_local_name_from_xml(child) != get_local_name_from_xml(child2)
                or get_node_name(child2) == act_htmlname
            ):
                continue
            # check if the name of another sibling fits better
            name_any2 = (
                "nameType" in child2.attrib.keys()
                and child2.attrib["nameType"] == "any"
            )
            fit2 = get_nx_namefit(chk_name, get_node_name(child2), name_any2)
            if fit2 > fit:
                return False
        # accept this fit
        return True
    return False


def get_local_name_from_xml(element):
    """Helper function to extract the element tag without the namespace."""
    return element.tag[element.tag.rindex("}") + 1 :]


def get_own_nxdl_child_reserved_elements(child, name, nxdl_elem):
    """checking reserved elements, like doc, enumeration"""
    if get_local_name_from_xml(child) == "doc" and name == "doc":
        if nxdl_elem.get("nxdlbase"):
            child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
            child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
            child.set("nxdlpath", nxdl_elem.get("nxdlpath") + "/doc")
        return child
    if get_local_name_from_xml(child) == "enumeration" and name == "enumeration":
        if nxdl_elem.get("nxdlbase"):
            child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
            child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
            child.set("nxdlpath", nxdl_elem.get("nxdlpath") + "/enumeration")
        return child
    return False


def get_own_nxdl_child_base_types(child, class_type, nxdl_elem, name, hdf_name):
    """checking base types of group, field,m attribute"""
    if get_local_name_from_xml(child) == "group":
        if (
            class_type is None or (class_type and get_nx_class(child) == class_type)
        ) and belongs_to(nxdl_elem, child, name, class_type, hdf_name):
            if nxdl_elem.get("nxdlbase"):
                child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
                child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
                child.set(
                    "nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child)
                )
            return child
    if get_local_name_from_xml(child) == "field" and belongs_to(
        nxdl_elem, child, name, None, hdf_name
    ):
        if nxdl_elem.get("nxdlbase"):
            child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
            child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
            child.set(
                "nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child)
            )
        return child
    if get_local_name_from_xml(child) == "attribute" and belongs_to(
        nxdl_elem, child, name, None, hdf_name
    ):
        if nxdl_elem.get("nxdlbase"):
            child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
            child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
            child.set(
                "nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child)
            )
        return child
    return False


def get_own_nxdl_child(
    nxdl_elem, name, class_type=None, hdf_name=None, nexus_type=None
):
    """Checks if an NXDL child node fits to the specific name (either nxdl or hdf)
    name       - nxdl name
    class_type - nxdl type or hdf classname (for groups, it is obligatory)
    hdf_name   - hdf name"""
    for child in nxdl_elem:
        if "name" in child.attrib and child.attrib["name"] == name:
            if nxdl_elem.get("nxdlbase"):
                child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
                child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
                child.set(
                    "nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child)
                )
            return child
    for child in nxdl_elem:
        if "name" in child.attrib and child.attrib["name"] == name:
            child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
            return child

    for child in nxdl_elem:
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
        if os.path.exists(
            f"{get_nexus_definitions_path()}{os.sep}"
            f"{nxdl_folder}{os.sep}{bc_name}.nxdl.xml"
        ):
            bc_filename = (
                f"{get_nexus_definitions_path()}{os.sep}"
                f"{nxdl_folder}{os.sep}{bc_name}.nxdl.xml"
            )
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
    try:
        if nxdl_elem.get("nxdlbase_class") == "base":
            return "<<OPTIONAL>>"
    except TypeError:
        return "<<REQUIRED>>"
    return "<<REQUIRED>>"


def chk_nxdataaxis_v2(hdf_node, name, logger):
    """Check if dataset is an axis"""
    own_signal = hdf_node.attrs.get("signal")  # check for being a Signal
    if own_signal is str and own_signal == "1":
        logger.debug("Dataset referenced (v2) as NXdata SIGNAL")
    own_axes = hdf_node.attrs.get("axes")  # check for being an axis
    if own_axes is str:
        axes = own_axes.split(":")
        for i in len(axes):
            if axes[i] and name == axes[i]:
                logger.debug("Dataset referenced (v2) as NXdata AXIS #%d", i)
                return None
    ownpaxis = hdf_node.attrs.get("primary")
    own_axis = hdf_node.attrs.get("axis")
    if own_axis is int:
        # also convention v1
        if ownpaxis is int and ownpaxis == 1:
            logger.debug("Dataset referenced (v2) as NXdata AXIS #%d", own_axis - 1)
        else:
            logger.debug(
                "Dataset referenced (v2) as NXdata (primary/alternative) AXIS #%d",
                own_axis - 1,
            )
    return None


def chk_nxdataaxis(hdf_node, name, logger):
    """NEXUS Data Plotting Standard v3: new version from 2014"""
    if not isinstance(
        hdf_node, h5py.Dataset
    ):  # check if it is a field in an NXdata node
        return None
    parent = hdf_node.parent
    if not parent or (parent and not parent.attrs.get("NX_class") == "NXdata"):
        return None
    signal = parent.attrs.get("signal")  # chk for Signal
    if signal and name == signal:
        logger.debug("Dataset referenced as NXdata SIGNAL")
        return None
    axes = parent.attrs.get("axes")  # check for default Axes
    if axes is str:
        if name == axes:
            logger.debug("Dataset referenced as NXdata AXIS")
            return None
    elif axes is not None:
        for i, j in enumerate(axes):
            if name == j:
                indices = parent.attrs.get(j + "_indices")
                if indices is int:
                    logger.debug(f"Dataset referenced as NXdata AXIS #{indices}")
                else:
                    logger.debug(f"Dataset referenced as NXdata AXIS #{i}")
                return None
    indices = parent.attrs.get(name + "_indices")  # check for alternative Axes
    if indices is int:
        logger.debug(f"Dataset referenced as NXdata alternative AXIS #{indices}")
    return chk_nxdataaxis_v2(hdf_node, name, logger)  # check for older conventions


# below there are some functions used in get_nxdl_doc function:
def write_doc_string(logger, doc, attr):
    """Simple function that prints a line in the logger if doc exists"""
    if doc:
        logger.debug("@" + attr + " [NX_CHAR]")
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


def check_deprecation_enum_axis(variables, doc, elist, attr, hdf_node):
    """Check for several attributes. - deprecation - enums - nxdataaxis"""
    logger, elem, path = variables
    dep_str = elem.attrib.get("deprecated")  # check for deprecation
    if dep_str:
        if doc:
            logger.debug("DEPRECATED - " + dep_str)
    for base_elem in elist if not attr else [elem]:  # check for enums
        sdoc = get_nxdl_child(base_elem, "enumeration", go_base=False)
        if sdoc is not None:
            if doc:
                logger.debug("enumeration (" + get_node_concept_path(base_elem) + "):")
            for item in sdoc:
                if get_local_name_from_xml(item) == "item":
                    if doc:
                        logger.debug("-> " + item.attrib["value"])
    chk_nxdataaxis(
        hdf_node, path.split("/")[-1], logger
    )  # look for NXdata reference (axes/signal)
    for base_elem in elist if not attr else [elem]:  # check for doc
        sdoc = get_nxdl_child(base_elem, "doc", go_base=False)
        if doc:
            logger.debug("documentation (" + get_node_concept_path(base_elem) + "):")
            logger.debug(sdoc.text if sdoc is not None else "")
    return logger, elem, path, doc, elist, attr, hdf_node


def get_node_concept_path(elem):
    """get the short version of nxdlbase:nxdlpath"""
    return str(elem.get("nxdlbase").split("/")[-1] + ":" + elem.get("nxdlpath"))


def get_nxdl_attr_doc(  # pylint: disable=too-many-arguments,too-many-locals
    elem, elist, attr, hdf_node, logger, doc, nxdl_path, req_str, path, hdf_info
):
    """Get nxdl documentation for an attribute"""
    new_elem = []
    old_elem = elem
    for elem_index, act_elem1 in enumerate(elist):
        act_elem = act_elem1
        # NX_class is a compulsory attribute for groups in a nexus file
        # which should match the type of the corresponding NXDL element
        if (
            attr == "NX_class"
            and not isinstance(hdf_node, h5py.Dataset)
            and elem_index == 0
        ):
            elem = None
            logger, doc, attr = write_doc_string(logger, doc, attr)
            new_elem = elem
            break
        # units category is a compulsory attribute for any fields
        if attr == "units" and isinstance(hdf_node, h5py.Dataset):
            req_str = "<<REQUIRED>>"
            logger, act_elem, nxdl_path, doc, attr = try_find_units(
                logger, act_elem, nxdl_path, doc, attr
            )
        # units for attributes can be given as ATTRIBUTENAME_units
        elif attr.endswith("_units"):
            logger, act_elem, nxdl_path, doc, attr, req_str = check_attr_name_nxdl(
                (logger, act_elem, nxdl_path, doc, attr, req_str)
            )
        # default is allowed for groups
        elif attr == "default" and not isinstance(hdf_node, h5py.Dataset):
            req_str = "<<RECOMMENDED>>"
            # try to find if default is defined as a child of the NXDL element
            act_elem = get_nxdl_child(
                act_elem, attr, nexus_type="attribute", go_base=False
            )
            logger, act_elem, nxdl_path, doc, attr = try_find_default(
                logger, act_elem1, act_elem, nxdl_path, doc, attr
            )
        else:  # other attributes
            act_elem = get_nxdl_child(
                act_elem, attr, nexus_type="attribute", go_base=False
            )
            if act_elem is not None:
                logger, act_elem, nxdl_path, doc, attr = other_attrs(
                    logger, act_elem1, act_elem, nxdl_path, doc, attr
                )
        if act_elem is not None:
            new_elem.append(act_elem)
            if req_str is None:
                req_str = get_required_string(act_elem)  # check for being required
                if doc:
                    logger.debug(req_str)
            variables = [logger, act_elem, path]
            (
                logger,
                elem,
                path,
                doc,
                elist,
                attr,
                hdf_node,
            ) = check_deprecation_enum_axis(variables, doc, elist, attr, hdf_node)
    elem = old_elem
    if req_str is None and doc:
        if attr != "NX_class":
            logger.debug("@" + attr + " - IS NOT IN SCHEMA")
        logger.debug("")
    return (req_str, get_nxdl_entry(hdf_info), nxdl_path)


def get_nxdl_doc(hdf_info, logger, doc, attr=False):
    """Get nxdl documentation for an HDF5 node (or its attribute)"""
    hdf_node = hdf_info["hdf_node"]
    # new way: retrieve multiple inherited base classes
    (class_path, nxdl_path, elist) = get_inherited_nodes(
        None,
        nx_name=get_nxdl_entry(hdf_info),
        hdf_node=hdf_node,
        hdf_path=hdf_info["hdf_path"] if "hdf_path" in hdf_info else None,
        hdf_root=hdf_info["hdf_root"] if "hdf_root" in hdf_info else None,
    )
    elem = elist[0] if class_path and elist else None
    if doc:
        logger.debug("classpath: " + str(class_path))
        logger.debug(
            "NOT IN SCHEMA"
            if elem is None
            else "classes:\n" + "\n".join(get_node_concept_path(e) for e in elist)
        )
    # old solution with a single elem instead of using elist
    path = get_nx_class_path(hdf_info)
    req_str = None
    if elem is None:
        if doc:
            logger.debug("")
        return ("None", None, None)
    if attr:
        return get_nxdl_attr_doc(
            elem, elist, attr, hdf_node, logger, doc, nxdl_path, req_str, path, hdf_info
        )
    req_str = get_required_string(elem)  # check for being required
    if doc:
        logger.debug(req_str)
    variables = [logger, elem, path]
    logger, elem, path, doc, elist, attr, hdf_node = check_deprecation_enum_axis(
        variables, doc, elist, attr, hdf_node
    )
    return (req_str, get_nxdl_entry(hdf_info), nxdl_path)


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
    (index, enums) = get_enums(node)  # enums
    if index:
        enum_str = (
            "\n "
            + ("Possible values:" if len(enums.split(",")) > 1 else "Obligatory value:")
            + "\n   "
            + enums
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


def get_enums(node):
    """Makes list of enumerations, if node contains any.
    Returns comma separated STRING of enumeration values, if there are enum tag,
    otherwise empty string."""
    # collect item values from enumeration tag, if any
    namespace = get_namespace(node)
    enums = []
    for enumeration in node.findall(f"{namespace}enumeration"):
        for item in enumeration.findall(f"{namespace}item"):
            enums.append(item.attrib["value"])
        enums = ",".join(enums)
        if enums != "":
            return (True, "[" + enums + "]")
    return (False, "")  # if there is no enumeration tag, returns empty string


def add_base_classes(elist, nx_name=None, elem: ET.Element = None):
    """Add the base classes corresponding to the last eleme in elist to the list. Note that if
    elist is empty, a nxdl file with the name of nx_name or a rather room elem is used if provided
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
        elem = ET.parse(nxdl_file_path).getroot()
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


def set_nxdlpath(child, nxdl_elem):
    """
    Setting up child nxdlbase, nxdlpath and nxdlbase_class from nxdl_element.
    """
    if nxdl_elem.get("nxdlbase"):
        child.set("nxdlbase", nxdl_elem.get("nxdlbase"))
        child.set("nxdlbase_class", nxdl_elem.get("nxdlbase_class"))
        child.set("nxdlpath", nxdl_elem.get("nxdlpath") + "/" + get_node_name(child))
    return child


def get_direct_child(nxdl_elem, html_name):
    """returns the child of nxdl_elem which has a name
    corresponding to the the html documentation name html_name"""
    for child in nxdl_elem:
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
    corresponding to the the html documentation name html_name"""
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
        if elist[ind] is None:
            del elist[ind]
            continue
        # override: remove low priority inheritance classes if class_type is overriden
        if len(elist) > ind + 1 and get_nx_class(elist[ind]) != get_nx_class(
            elist[ind + 1]
        ):
            del elist[ind + 1 :]
        # add new base class(es) if new element brings such (and not a primitive type)
        if len(elist) == ind + 1 and get_nx_class(elist[ind])[0:3] != "NX_":
            add_base_classes(elist)
    return elist, html_name


def helper_get_inherited_nodes(hdf_info2, elist, pind, attr):
    """find the best fitting name in all children"""
    hdf_path, hdf_node, hdf_class_path = hdf_info2
    hdf_name = hdf_path[pind]
    hdf_class_name = hdf_class_path[pind]
    if pind < len(hdf_path) - (2 if attr else 1):
        act_nexus_type = "group"
    elif pind == len(hdf_path) - 1 and attr:
        act_nexus_type = "attribute"
    else:
        act_nexus_type = "field" if isinstance(hdf_node, h5py.Dataset) else "group"
    # find the best fitting name in all children
    bestfit = -1
    html_name = None
    for ind in range(len(elist) - 1, -1, -1):
        newelem, fit = get_best_child(
            elist[ind], hdf_node, hdf_name, hdf_class_name, act_nexus_type
        )
        if fit >= bestfit and newelem is not None:
            html_name = get_node_name(newelem)
    return hdf_path, hdf_node, hdf_class_path, elist, pind, attr, html_name


def get_hdf_path(hdf_info):
    """Get the hdf_path from an hdf_info"""
    if "hdf_path" in hdf_info:
        return hdf_info["hdf_path"].split("/")[1:]
    return hdf_info["hdf_node"].name.split("/")[1:]


@lru_cache(maxsize=None)
def get_inherited_nodes(
    nxdl_path: str = None,  # pylint: disable=too-many-arguments,too-many-locals
    nx_name: str = None,
    elem: ET.Element = None,
    hdf_node=None,
    hdf_path=None,
    hdf_root=None,
    attr=False,
):
    """Returns a list of ET.Element for the given path."""
    # let us start with the given definition file
    elist = []  # type: ignore[var-annotated]
    add_base_classes(elist, nx_name, elem)
    nxdl_elem_path = [elist[0]]

    class_path = []  # type: ignore[var-annotated]
    if hdf_node is not None:
        hdf_info = {"hdf_node": hdf_node}
        if hdf_path:
            hdf_info["hdf_path"] = hdf_path
        if hdf_root:
            hdf_root["hdf_root"] = hdf_root
        hdf_node = hdf_info["hdf_node"]
        hdf_path = get_hdf_path(hdf_info)
        hdf_class_path = get_nx_class_path(hdf_info).split("/")[1:]
        if attr:
            hdf_path.append(attr)
            hdf_class_path.append(attr)
        path = hdf_path
    else:
        html_path = nxdl_path.split("/")[1:]
        path = html_path
    for pind in range(len(path)):
        if hdf_node is not None:
            hdf_info2 = [hdf_path, hdf_node, hdf_class_path]
            [
                hdf_path,
                hdf_node,
                hdf_class_path,
                elist,
                pind,
                attr,
                html_name,
            ] = helper_get_inherited_nodes(hdf_info2, elist, pind, attr)
            if html_name is None:  # return if NOT IN SCHEMA
                return (class_path, nxdl_elem_path, None)
        else:
            html_name = html_path[pind]
        elist, html_name = walk_elist(elist, html_name)
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
        (class_path, nxdlpath, elist) = get_inherited_nodes(nxdl_path, nx_name, elem)
    except ValueError as value_error:
        if exc:
            raise NxdlAttributeError(
                f"Attributes were not found for {nxdl_path}. "
                "Please check this entry in the template dictionary."
            ) from value_error
        return None
    if class_path and nxdlpath and elist:
        elem = elist[0]
    else:
        elem = None
        if exc:
            raise NxdlAttributeError(
                f"Attributes were not found for {nxdl_path}. "
                "Please check this entry in the template dictionary."
            )
    return elem


def process_node(hdf_node, hdf_path, parser, logger, doc=True):
    """Processes an hdf5 node.
    - it logs the node found and also checks for its attributes
    - retrieves the corresponding nxdl documentation
    TODO:
    - follow variants
    - NOMAD parser: store in NOMAD"""
    hdf_info = {"hdf_path": hdf_path, "hdf_node": hdf_node}
    if isinstance(hdf_node, h5py.Dataset):
        logger.debug(f"===== FIELD (/{hdf_path}): {hdf_node}")
        val = (
            str(hdf_node[()]).split("\n")
            if len(hdf_node.shape) <= 1
            else str(hdf_node[0]).split("\n")
        )
        logger.debug(f'value: {val[0]} {"..." if len(val) > 1 else ""}')
    else:
        logger.debug(
            f"===== GROUP (/{hdf_path} "
            f"[{get_nxdl_entry(hdf_info)}"
            f"::{get_nx_class_path(hdf_info)}]): {hdf_node}"
        )
    (req_str, nxdef, nxdl_path) = get_nxdl_doc(hdf_info, logger, doc)
    if parser is not None and isinstance(hdf_node, h5py.Dataset):
        parser(
            {
                "hdf_info": hdf_info,
                "nxdef": nxdef,
                "nxdl_path": nxdl_path,
                "val": val,
                "logger": logger,
            }
        )
    for key, value in hdf_node.attrs.items():
        logger.debug(f"===== ATTRS (/{hdf_path}@{key})")
        val = str(value).split("\n")
        logger.debug(f'value: {val[0]} {"..." if len(val) > 1 else ""}')
        (req_str, nxdef, nxdl_path) = get_nxdl_doc(hdf_info, logger, doc, attr=key)
        if (
            parser is not None
            and req_str is not None
            and "NOT IN SCHEMA" not in req_str
            and "None" not in req_str
        ):
            parser(
                {
                    "hdf_info": hdf_info,
                    "nxdef": nxdef,
                    "nxdl_path": nxdl_path,
                    "val": val,
                    "logger": logger,
                },
                attr=key,
            )


def logger_auxiliary_signal(logger, nxdata):
    """Handle the presence of auxiliary signal"""
    aux = nxdata.attrs.get("auxiliary_signals")
    if aux is not None:
        if isinstance(aux, str):
            aux = [aux]
        for asig in aux:
            logger.debug(f"Further auxiliary signal has been identified: {asig}")
    return logger


def print_default_plotable_header(logger):
    """Print a three-lines header"""
    logger.debug("========================")
    logger.debug("=== Default Plotable ===")
    logger.debug("========================")


def get_default_plotable(root, logger):
    """Get default plotable"""
    print_default_plotable_header(logger)
    # v3 from 2014
    # nxentry
    nxentry = None
    default_nxentry_group_name = root.attrs.get("default")
    if default_nxentry_group_name:
        try:
            nxentry = root[default_nxentry_group_name]
        except KeyError:
            nxentry = None
    if not nxentry:
        nxentry = entry_helper(root)
    if not nxentry:
        logger.debug("No NXentry has been found")
        return
    logger.debug("")
    logger.debug("NXentry has been identified: " + nxentry.name)
    # nxdata
    nxdata = None
    nxgroup = nxentry
    default_group_name = nxgroup.attrs.get("default")
    while default_group_name:
        try:
            nxgroup = nxgroup[default_group_name]
            default_group_name = nxgroup.attrs.get("default")
        except KeyError:
            pass
    if nxgroup == nxentry:
        nxdata = nxdata_helper(nxentry)
    else:
        nxdata = nxgroup
    if not nxdata:
        logger.debug("No NXdata group has been found")
        return
    logger.debug("")
    logger.debug("NXdata group has been identified: " + nxdata.name)
    process_node(nxdata, nxdata.name, None, logger, False)
    # signal
    signal = None
    signal_dataset_name = nxdata.attrs.get("signal")
    try:
        signal = nxdata[signal_dataset_name]
    except (TypeError, KeyError):
        signal = None
    if not signal:
        signal = signal_helper(nxdata)
    if not signal:
        logger.debug("No Signal has been found")
        return
    logger.debug("")
    logger.debug("Signal has been identified: " + signal.name)
    process_node(signal, signal.name, None, logger, False)
    logger = logger_auxiliary_signal(logger, nxdata)  # check auxiliary_signals
    dim = len(signal.shape)
    axes = []  # axes
    axis_helper(dim, nxdata, signal, axes, logger)


def entry_helper(root):
    """Check entry related data"""
    nxentries = []
    for key in root.keys():
        if (
            isinstance(root[key], h5py.Group)
            and root[key].attrs.get("NX_class")
            and root[key].attrs["NX_class"] == "NXentry"
        ):
            nxentries.append(root[key])
    if len(nxentries) >= 1:
        return nxentries[0]
    return None


def nxdata_helper(nxentry):
    """Check if nxentry hdf5 object has a NX_class and, if it contains NXdata,
    return its value"""
    lnxdata = []
    for key in nxentry.keys():
        if (
            isinstance(nxentry[key], h5py.Group)
            and nxentry[key].attrs.get("NX_class")
            and nxentry[key].attrs["NX_class"] == "NXdata"
        ):
            lnxdata.append(nxentry[key])
    if len(lnxdata) >= 1:
        return lnxdata[0]
    return None


def signal_helper(nxdata):
    """Check signal related data"""
    signals = []
    for key in nxdata.keys():
        if isinstance(nxdata[key], h5py.Dataset):
            signals.append(nxdata[key])
    if (
        len(signals) == 1
    ):  # v3: as there was no selection given, only 1 data field shall exists
        return signals[0]
    if len(signals) > 1:  # v2: select the one with an attribute signal="1" attribute
        for sig in signals:
            if (
                sig.attrs.get("signal")
                and sig.attrs.get("signal") is str
                and sig.attrs.get("signal") == "1"
            ):
                return sig
    return None


def find_attrib_axis_actual_dim_num(nxdata, a_item, ax_list):
    """Finds axis that have defined dimensions"""
    # find those with attribute axis= actual dimension number
    lax = []
    for key in nxdata.keys():
        if isinstance(nxdata[key], h5py.Dataset):
            try:
                if nxdata[key].attrs["axis"] == a_item + 1:
                    lax.append(nxdata[key])
            except KeyError:
                pass
    if len(lax) == 1:
        ax_list.append(lax[0])
    # if there are more alternatives, prioritise the one with an attribute primary="1"
    elif len(lax) > 1:
        for sax in lax:
            if sax.attrs.get("primary") and sax.attrs.get("primary") == 1:
                ax_list.insert(0, sax)
            else:
                ax_list.append(sax)


def get_single_or_multiple_axes(nxdata, ax_datasets, a_item, ax_list):
    """Gets either single or multiple axes from the NXDL"""
    try:
        if isinstance(ax_datasets, str):  # single axis is defined
            # explicite definition of dimension number
            ind = nxdata.attrs.get(ax_datasets + "_indices")
            if ind and ind is int:
                if ind == a_item:
                    ax_list.append(nxdata[ax_datasets])
            elif a_item == 0:  # positional determination of the dimension number
                ax_list.append(nxdata[ax_datasets])
        else:  # multiple axes are listed
            # explicite definition of dimension number
            for aax in ax_datasets:
                ind = nxdata.attrs.get(aax + "_indices")
                if ind and isinstance(ind, int):
                    if ind == a_item:
                        ax_list.append(nxdata[aax])
            if not ax_list:  # positional determination of the dimension number
                ax_list.append(nxdata[ax_datasets[a_item]])
    except KeyError:
        pass
    return ax_list


def axis_helper(dim, nxdata, signal, axes, logger):
    """Check axis related data"""
    for a_item in range(dim):
        ax_list = []
        ax_datasets = nxdata.attrs.get("axes")  # primary axes listed in attribute axes
        ax_list = get_single_or_multiple_axes(nxdata, ax_datasets, a_item, ax_list)
        for attr in nxdata.attrs.keys():  # check for corresponding AXISNAME_indices
            if (
                attr.endswith("_indices")
                and nxdata.attrs[attr] == a_item
                and nxdata[attr.split("_indices")[0]] not in ax_list
            ):
                ax_list.append(nxdata[attr.split("_indices")[0]])
        # v2  # check for ':' separated axes defined in Signal
        if not ax_list:
            try:
                ax_datasets = signal.attrs.get("axes").split(":")
                ax_list.append(nxdata[ax_datasets[a_item]])
            except (KeyError, AttributeError):
                pass
        if not ax_list:  # check for axis/primary specifications
            find_attrib_axis_actual_dim_num(nxdata, a_item, ax_list)
        axes.append(ax_list)
        logger.debug("")
        logger.debug(
            f"For Axis #{a_item}, {len(ax_list)} axes have been identified: {str(ax_list)}"
        )


def get_all_is_a_rel_from_hdf_node(hdf_node, hdf_path):
    """Return list of nxdl concept paths for a nxdl element which corresponds to
    hdf node.
    """
    hdf_info = {"hdf_path": hdf_path, "hdf_node": hdf_node}
    (_, _, elist) = get_inherited_nodes(
        None,
        nx_name=get_nxdl_entry(hdf_info),
        hdf_node=hdf_node,
        hdf_path=hdf_info["hdf_path"] if "hdf_path" in hdf_info else None,
        hdf_root=hdf_info["hdf_root"] if "hdf_root" in hdf_info else None,
    )
    return elist


def hdf_node_to_self_concept_path(hdf_info, logger):
    """Get concept or nxdl path from given hdf_node."""
    # The bellow logger is for deactivatine unnecessary debug message above
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
    (_, _, nxdl_path) = get_nxdl_doc(hdf_info, logger, None)
    con_path = ""
    if nxdl_path:
        for nd_ in nxdl_path:
            con_path = con_path + "/" + get_node_name(nd_)
    return con_path


class HandleNexus:
    """documentation"""

    def __init__(self, logger, nexus_file, d_inq_nd=None, c_inq_nd=None):
        self.logger = logger
        local_dir = os.path.abspath(os.path.dirname(__file__))

        self.input_file_name = (
            nexus_file
            if nexus_file is not None
            else os.path.join(local_dir, "../../tests/data/nexus/201805_WSe2_arpes.nxs")
        )
        self.parser = None
        self.in_file = None
        self.d_inq_nd = d_inq_nd
        self.c_inq_nd = c_inq_nd
        # Aggregating hdf path corresponds to concept query node
        self.hdf_path_list_for_c_inq_nd = []

    def visit_node(self, hdf_name, hdf_node):
        """Function called by h5py that iterates on each node of hdf5file.
        It allows h5py visititems function to visit nodes."""
        if self.d_inq_nd is None and self.c_inq_nd is None:
            process_node(hdf_node, "/" + hdf_name, self.parser, self.logger)
        elif self.d_inq_nd is not None and hdf_name in (
            self.d_inq_nd,
            self.d_inq_nd[1:],
        ):
            process_node(hdf_node, "/" + hdf_name, self.parser, self.logger)
        elif self.c_inq_nd is not None:
            attributed_concept = self.c_inq_nd.split("@")
            attr = attributed_concept[1] if len(attributed_concept) > 1 else None
            elist = get_all_is_a_rel_from_hdf_node(hdf_node, "/" + hdf_name)
            if elist is None:
                return
            fnd_superclass = False
            fnd_superclass_attr = False
            for elem in reversed(elist):
                tmp_path = elem.get("nxdlbase").split(".nxdl")[0]
                con_path = "/NX" + tmp_path.split("NX")[-1] + elem.get("nxdlpath")
                if fnd_superclass or con_path == attributed_concept[0]:
                    fnd_superclass = True
                    if attr is None:
                        self.hdf_path_list_for_c_inq_nd.append(hdf_name)
                        break
                    for attribute in hdf_node.attrs.keys():
                        attr_concept = get_nxdl_child(
                            elem, attribute, nexus_type="attribute", go_base=False
                        )
                        if attr_concept is not None and attr_concept.get(
                            "nxdlpath"
                        ).endswith(attr):
                            fnd_superclass_attr = True
                            con_path = (
                                "/NX"
                                + tmp_path.split("NX")[-1]
                                + attr_concept.get("nxdlpath")
                            )
                            self.hdf_path_list_for_c_inq_nd.append(
                                hdf_name + "@" + attribute
                            )
                            break
                if fnd_superclass_attr:
                    break

    def not_yet_visited(self, root, name):
        """checking if a new node has already been visited in its path"""
        path = name.split("/")
        for i in range(1, len(path)):
            act_path = "/".join(path[:i])
            # print(act_path+' - '+name)
            if root["/" + act_path] == root["/" + name]:
                return False
        return True

    def full_visit(self, root, hdf_node, name, func):
        """visiting recursivly all children, but avoiding endless cycles"""
        # print(name)
        if len(name) > 0:
            func(name, hdf_node)
        if isinstance(hdf_node, h5py.Group):
            for ch_name, child in hdf_node.items():
                full_name = ch_name if len(name) == 0 else name + "/" + ch_name
                if self.not_yet_visited(root, full_name):
                    self.full_visit(root, child, full_name, func)

    def process_nexus_master_file(self, parser):
        """Process a nexus master file by processing all its nodes and their attributes"""
        self.parser = parser
        self.in_file = h5py.File(
            self.input_file_name[0]
            if isinstance(self.input_file_name, list)
            else self.input_file_name,
            "r",
        )
        self.full_visit(self.in_file, self.in_file, "", self.visit_node)
        if self.d_inq_nd is None and self.c_inq_nd is None:
            get_default_plotable(self.in_file, self.logger)
        # To log the provided concept and concepts founded
        if self.c_inq_nd is not None:
            for hdf_path in self.hdf_path_list_for_c_inq_nd:
                self.logger.info(hdf_path)
        self.in_file.close()


@click.command()
@click.option(
    "-f",
    "--nexus-file",
    required=False,
    default=None,
    help=(
        "NeXus file with extension .nxs to learn NeXus different concept"
        " documentation and concept."
    ),
)
@click.option(
    "-d",
    "--documentation",
    required=False,
    default=None,
    help=(
        "Definition path in nexus output (.nxs) file. Returns debug"
        "log relavent with that definition path. Example: /entry/data/delays"
    ),
)
@click.option(
    "-c",
    "--concept",
    required=False,
    default=None,
    help=(
        "Concept path from application definition file (.nxdl,xml). Finds out"
        "all the available concept definition (IS-A realation) for rendered"
        "concept path. Example: /NXarpes/ENTRY/INSTRUMENT/analyser"
    ),
)
def main(nexus_file, documentation, concept):
    """The main function to call when used as a script."""
    logging_format = "%(levelname)s: %(message)s"
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    logging.basicConfig(
        level=logging.INFO, format=logging_format, handlers=[stdout_handler]
    )
    logger = logging.getLogger(__name__)
    logger.addHandler(stdout_handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if documentation and concept:
        raise ValueError(
            "Only one option either documentation (-d) or is_a relation "
            "with a concept (-c) can be requested."
        )
    nexus_helper = HandleNexus(
        logger, nexus_file, d_inq_nd=documentation, c_inq_nd=concept
    )
    nexus_helper.process_nexus_master_file(None)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
