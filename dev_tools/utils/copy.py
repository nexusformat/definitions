import shutil
from pathlib import Path
from typing import List
from typing import Tuple

from ..globals import directories


def copyfile(from_path: Path, to_path: Path) -> None:
    print("copy", from_path)
    print("  ->", to_path)
    shutil.copyfile(from_path, to_path)


def copydir(from_path: Path, to_path: Path) -> None:
    print("copy", from_path)
    print("  ->", to_path)
    shutil.copytree(from_path, to_path, dirs_exist_ok=True)


def copy_files(files: List[Tuple[str, str, bool]]) -> None:
    source_root = directories.get_source_root()
    build_root = directories.get_build_root()
    for from_subname, to_subname, overwrite in files:
        to_path = build_root / to_subname
        if overwrite or not to_path.exists():
            from_path = source_root / from_subname
            copyfile(from_path, to_path)
        else:
            print("already exists", to_path)
