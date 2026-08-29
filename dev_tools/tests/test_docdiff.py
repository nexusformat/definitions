"""Diffing the generated documentation of two git references."""

import subprocess
from pathlib import Path

import pytest

from ..__main__ import main
from ..apps import docdiff_app
from ..globals import directories


def _has_git_repository() -> bool:
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=directories.get_source_root(),
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return False
    return True


@pytest.fixture
def build_root(tmp_path):
    original = directories.get_build_root()
    yield tmp_path
    directories.set_build_root(original)


@pytest.mark.skipif(not _has_git_repository(), reason="not a git repository")
def test_docdiff_same_reference(build_root, capsys):
    exit_code = main(
        [
            "dev_tools",
            "docdiff",
            "--nxclass",
            "NXentry",
            "--color",
            "never",
            "--exit-code",
            "--build-root",
            str(build_root),
            "HEAD",
            "HEAD",
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    assert not captured.out
    assert "0 file(s) differ" in captured.err
    assert not list(build_root.glob("docdiff/*"))


@pytest.mark.skipif(not _has_git_repository(), reason="not a git repository")
def test_docdiff_unknown_reference(build_root, capsys):
    exit_code = main(
        [
            "dev_tools",
            "docdiff",
            "--build-root",
            str(build_root),
            "no-such-reference",
            "HEAD",
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "invalid reference" in captured.err
    assert not (build_root / "docdiff").exists()


@pytest.mark.skipif(not _has_git_repository(), reason="not a git repository")
def test_docdiff_cleanup(build_root):
    """Left-overs of an interrupted run are removed."""
    repo = Path(directories.get_source_root())
    root = build_root / "docdiff"
    source_root = root / "old" / "source"
    subprocess.run(
        ["git", "worktree", "add", "--detach", str(source_root), "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    (root / "new").mkdir()

    docdiff_app._remove_generated(repo, root)

    assert not root.exists()
    worktrees = subprocess.run(
        ["git", "worktree", "list"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    assert str(source_root) not in worktrees
