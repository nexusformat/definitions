import difflib
import tempfile
from pathlib import Path
from typing import List


def diff_ascii(src_file: Path, new_content: List[str], dest_file: Path) -> None:
    """`new_content` is the parsed content of `src_file` to be compared
    with the content of `dest_file`.
    """
    if dest_file.exists():
        with open(dest_file, "r") as fh:
            original_content = list(fh)
    else:
        original_content = list()

    with tempfile.TemporaryFile("w+") as fh:
        fh.writelines(new_content)
        fh.seek(0)
        new_content = list(fh)

    for line in difflib.unified_diff(
        original_content,
        new_content,
        fromfile=str(dest_file),
        tofile=str(src_file),
    ):
        print(line)
