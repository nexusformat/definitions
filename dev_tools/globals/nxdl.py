"""Namespace of the schema in which NXDL is defined
(the XSD namespace) and the namespace of the NeXus
class definitions (the NXDL namespace).

Namespaces are URL's solely to be globally unique.
Do not use these URL's for validation. That's what
"xsi:schemaLocation" is for. Currently this is the
relative URI "../nxdl.xsd" which means validation
can only be done for NXDL files in subdirectories.
"""
import os
from subprocess import CalledProcessError, run
from typing import Optional

from .directories import get_nxdl_version_file

XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
NXDL_NAMESPACE = "http://definition.nexusformat.org/nxdl/3.1"


def get_vcs_version(tag_match="*[0-9]*") -> Optional[str]:
    """
    The version of the Nexus standard and the NeXus Definition language
    based on git tags and commits
    """
    try:
        return (
            run(
                ["git", "describe", "--tags", "--long", "--match", tag_match],
                cwd=os.path.join(os.path.dirname(__file__)),
                check=True,
                capture_output=True,
            )
            .stdout.decode("utf-8")
            .strip()
        )
    except CalledProcessError:
        return None


def get_nxdl_version() -> str:
    """The version of the NeXus standard and the NeXus Definition language"""
    version = get_vcs_version()
    if version is not None:
        return version

    with open(get_nxdl_version_file(), "r", encoding="utf-8") as fh:
        return fh.read().strip()
