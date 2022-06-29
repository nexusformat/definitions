import os
from pathlib import Path

from ..utils.types import PathLike


def get_source_root() -> Path:
    """Root directory of the source code for the documentation
    (git repository root by default)"""
    if _SOURCE_ROOT is None:
        set_source_root(Path(__file__).absolute().parent.parent.parent)
    return _SOURCE_ROOT


def set_source_root(root: PathLike) -> None:
    if not isinstance(root, Path):
        root = Path(root)
    global _SOURCE_ROOT
    _SOURCE_ROOT = root.absolute()


def get_nxdl_root() -> Path:
    """Root directory of the XSD and NXDL files
    (same as the source root by default)"""
    if _NXDL_ROOT is None:
        set_nxdl_root(get_source_root())
    return _NXDL_ROOT


def set_nxdl_root(root: PathLike) -> None:
    if not isinstance(root, Path):
        root = Path(root)
    assert (root / _XSD_FILE_NAME).exists()
    global _NXDL_ROOT
    _NXDL_ROOT = root.absolute()


def get_xsd_file() -> Path:
    """The XSD file that defines the NXDL"""
    return get_nxdl_root() / _XSD_FILE_NAME


def get_xsd_units_file() -> Path:
    """The XSD file that defines the units in the NXDL"""
    return get_nxdl_root() / _XSD_UNITS_FILE_NAME


def get_nxdl_version_file() -> Path:
    """The version of the NeXus standard and the NeXus Definition language"""
    return get_source_root() / _VERSION_FILE_NAME


def get_build_root() -> Path:
    """Root directory in which the sources for documentation
    building are generated."""
    if _BUILD_ROOT is None:
        set_build_root(get_source_root() / "build")
    return _BUILD_ROOT


def set_build_root(root: PathLike) -> None:
    if not isinstance(root, Path):
        root = Path(root)
    global _BUILD_ROOT
    _BUILD_ROOT = root.absolute()


def manual_source_root() -> Path:
    """Source directory of the NeXus User Manual"""
    return get_source_root() / "manual"


def manual_build_root() -> Path:
    """Build directory of the NeXus User Manual"""
    return get_build_root() / "manual"


def impatient_source_root() -> Path:
    """Source directory of the NeXus Impatient Guide"""
    return get_source_root() / "impatient-guide"


def impatient_build_root() -> Path:
    """Build directory of the NeXus Impatient Guide"""
    return get_build_root() / "impatient-guide"


def manual_source_sphinxroot() -> Path:
    """Sphinx source directory of the NeXus User Manual"""
    return manual_source_root() / "source"


def manual_build_sphinxroot() -> Path:
    """Sphinx source directory for building of the NeXus User Manual"""
    return manual_build_root() / "source"


def manual_build_staticroot() -> Path:
    """Static source directory for building of the NeXus User Manual"""
    return manual_build_sphinxroot() / "_static"


def nxclass_build_root(nxdl_file: Path) -> Path:
    """NeXus class documentation directory for building of the NeXus User Manual"""
    root = manual_build_sphinxroot() / "classes"
    root /= os.path.relpath(nxdl_file.parent, get_nxdl_root())
    return root


def get_rst_filename(nxdl_file: Path) -> Path:
    rst_file_name = nxclass_build_root(nxdl_file)
    rst_file_name /= nxdl_file.with_suffix("").with_suffix(".rst").name
    return rst_file_name


_XSD_FILE_NAME = "nxdl.xsd"
_XSD_UNITS_FILE_NAME = "nxdlTypes.xsd"
_VERSION_FILE_NAME = "NXDL_VERSION"
_NXDL_ROOT = None
_BUILD_ROOT = None
_SOURCE_ROOT = None
