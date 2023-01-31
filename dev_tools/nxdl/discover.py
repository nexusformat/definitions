from pathlib import Path
from typing import Iterator
from typing import Optional
from typing import Tuple

from ..globals.directories import get_build_root
from ..globals.directories import get_nxdl_root


def iter_definitions(*subdirs: Tuple[str]) -> Iterator[Path]:
    """Yield all NeXus class definitions"""
    root = get_nxdl_root()
    build_root = get_build_root()
    for subdir in subdirs:
        root /= subdir
    for path in sorted(root.rglob("*.nxdl.xml")):
        try:
            path.relative_to(build_root)
            # Skip file in the build root
            continue
        except ValueError:
            yield path


def find_definition(nxclass: str, *subdirs: Tuple[str]) -> Optional[Path]:
    """Find the definition of a NeXus class"""
    s = nxclass.lower() + ".nxdl"
    for path in iter_definitions(*subdirs):
        if path.stem.lower() == s:
            return path
