"""Compare the generated documentation of two git references."""

import contextlib
import difflib
import fnmatch
import os
import shutil
import signal
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Iterator
from typing import List
from typing import Optional
from typing import Sequence

from ..globals import directories

# reference name for the working tree, which includes uncommitted changes
WORKING_TREE = "."

# generated files that are compared (globs relative to the sphinx source directory)
GENERATED_PATTERNS = (
    "classes/*/*.rst",
    "nxdl_desc.rst",
    "units.table",
    "types.table",
    "_static/nxdl_vocabulary.txt",
)

_ANSI = {
    "+": "\033[32m",
    "-": "\033[31m",
    "@": "\033[36m",
}
_ANSI_RESET = "\033[0m"


def docdiff_args(parser):
    parser.add_argument(
        "refs",
        nargs="*",
        metavar="REF",
        help="Git references to compare, for example 'HEAD~2 HEAD' or a branch "
        f"name. Use '{WORKING_TREE}' for the working tree, which includes "
        f"uncommitted changes. Default: 'HEAD~1 HEAD'",
    )
    parser.add_argument(
        "-c",
        "--nxclass",
        action="append",
        metavar="NAME",
        help="Only compare this NeXus class (for example 'NXstress'). Repeatable. "
        "Default: all classes",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=3,
        metavar="N",
        help="Number of context lines in the diff. Default: 3",
    )
    parser.add_argument(
        "--color",
        choices=["auto", "always", "never"],
        default="auto",
        help="Colorize the diff. Default: auto",
    )
    parser.add_argument(
        "--output",
        type=str,
        metavar="FILE",
        help="Write the diff to this file instead of stdout",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Keep the generated documentation of both references",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print the output of the documentation generation",
    )
    parser.add_argument(
        "--exit-code",
        action="store_true",
        help="Exit with 1 when the documentation differs",
    )


def docdiff_exec(args) -> int:
    refs = args.refs or ["HEAD~1", "HEAD"]
    if len(refs) != 2:
        print(f"Expected two git references, got {len(refs)}", file=sys.stderr)
        return 1
    repo = Path(directories.get_source_root())
    root = Path(directories.get_build_root()) / "docdiff"

    generated = list()
    try:
        for name, ref in zip(("old", "new"), refs):
            print(f"generate the documentation of '{ref}' ...", file=sys.stderr)
            generated.append(
                _generate_docs(
                    repo, ref, root / name, args.nxclass, verbose=args.verbose
                )
            )
        diff_lines = list(
            _diff_directories(
                *generated, *refs, GENERATED_PATTERNS, context=args.context
            )
        )
    except KeyboardInterrupt:
        # nothing is left behind when interrupted, also not with --keep
        with contextlib.suppress(KeyboardInterrupt):
            _remove_generated(repo, root)
        print("\ndocdiff: interrupted", file=sys.stderr)
        return 1
    except Exception as e:
        with contextlib.suppress(KeyboardInterrupt):
            _remove_generated(repo, root)
        if args.verbose:
            traceback.print_exc()
        print(f"docdiff: {e}", file=sys.stderr)
        return 1
    if not args.keep:
        _remove_generated(repo, root)

    nfiles = sum(line.startswith("--- ") for line in diff_lines)
    if args.output:
        with open(args.output, "w") as fh:
            fh.writelines(diff_lines)
        print(f"{nfiles} file(s) differ, diff written to {args.output}")
    else:
        color = args.color == "always" or (args.color == "auto" and sys.stdout.isatty())
        sys.stdout.writelines(_colorize(diff_lines) if color else diff_lines)
        print(f"\n{nfiles} file(s) differ", file=sys.stderr)
    if args.keep:
        print(
            f"generated documentation in {root}\n"
            "remove the git worktrees with 'git worktree prune' after deleting it",
            file=sys.stderr,
        )

    return 1 if diff_lines and args.exit_code else 0


def _generate_docs(
    repo: Path,
    ref: str,
    dest: Path,
    nxclasses: Optional[Sequence[str]],
    verbose: bool = False,
) -> Path:
    """Generate the NeXus class documentation of a git reference. Returns the
    directory with the generated files.
    """
    _remove_generated(repo, dest)
    if ref == WORKING_TREE:
        source_root = repo
    else:
        source_root = dest / "source"
        _git(repo, "worktree", "add", "--detach", str(source_root), ref)
    build_root = dest / "build"

    if nxclasses:
        commands = [["nxclass", name, "--prepare"] for name in nxclasses]
    else:
        commands = [["manual", "--prepare"]]
    # the documentation is generated by the dev_tools of the reference itself
    env = dict(os.environ)
    pythonpath = [str(source_root)]
    if env.get("PYTHONPATH"):
        pythonpath.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(pythonpath)
    env.pop("NEXUS_DEF_PATH", None)
    for command in commands:
        _run_generator(
            [sys.executable, "-m", "dev_tools"]
            + command
            + ["--build-root", str(build_root)],
            ref,
            source_root,
            env,
            verbose,
        )
    return build_root / "manual" / "source"


def _run_generator(
    command: Sequence[str], ref: str, cwd: Path, env: dict, verbose: bool
) -> None:
    """Run a documentation generator in its own process group, so that a CTRL-C
    in the terminal is handled here and the process is never left behind.
    """
    with subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        stdout=None if verbose else subprocess.DEVNULL,
        stderr=None if verbose else subprocess.PIPE,
        text=not verbose,
        start_new_session=True,
    ) as process:
        try:
            _, stderr = process.communicate()
        except BaseException:
            _kill(process)
            raise
    if process.returncode:
        raise RuntimeError(
            f"generating the documentation of '{ref}' failed "
            f"(exit code {process.returncode})\n{(stderr or '').strip()}"
        )


def _kill(process: subprocess.Popen) -> None:
    """Kill a process and everything it started."""
    with contextlib.suppress(BaseException):
        os.killpg(os.getpgid(process.pid), signal.SIGKILL)
    with contextlib.suppress(BaseException):
        process.kill()


def _remove_generated(repo: Path, root: Path) -> None:
    """Remove the generated documentation and unregister the git worktrees.
    Interrupting this leaves nothing behind, it cannot be interrupted.
    """
    with _delayed_interrupt():
        for source_root in [root / "source"] + [
            root / name / "source" for name in ("old", "new")
        ]:
            if not source_root.is_dir():
                continue
            with contextlib.suppress(BaseException):
                _git(
                    repo, "worktree", "remove", "--force", str(source_root), detach=True
                )
        shutil.rmtree(root, ignore_errors=True)
        with contextlib.suppress(BaseException):
            _git(repo, "worktree", "prune", detach=True)


@contextlib.contextmanager
def _delayed_interrupt():
    """Handle SIGINT (CTRL-C) when leaving the context instead of inside it."""
    interrupted = False

    def handler(*_):
        nonlocal interrupted
        interrupted = True

    try:
        original = signal.signal(signal.SIGINT, handler)
    except ValueError:
        yield  # not the main thread
        return
    try:
        yield
    finally:
        signal.signal(signal.SIGINT, original)
        if interrupted:
            raise KeyboardInterrupt


def _git(repo: Path, *args: str, detach: bool = False) -> str:
    """`detach` shields the git process from a CTRL-C in the terminal."""
    result = subprocess.run(
        ["git"] + list(args),
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=detach,
    )
    if result.returncode in (-signal.SIGINT, -signal.SIGTERM):
        raise KeyboardInterrupt
    if result.returncode:
        raise RuntimeError(f"'git {' '.join(args)}' failed: {result.stderr.strip()}")
    return result.stdout


def _diff_directories(
    old_root: Path,
    new_root: Path,
    old_ref: str,
    new_ref: str,
    patterns: Sequence[str],
    context: int = 3,
) -> Iterator[str]:
    """Unified diff of the generated files of two references."""
    for relpath in _iter_generated(old_root, new_root, patterns):
        old_lines = _read(old_root / relpath)
        new_lines = _read(new_root / relpath)
        if old_lines == new_lines:
            continue
        yield from difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=f"{old_ref}:{relpath}",
            tofile=f"{new_ref}:{relpath}",
            n=context,
        )


def _iter_generated(
    old_root: Path, new_root: Path, patterns: Sequence[str]
) -> Iterator[Path]:
    """Files generated for either reference, in a reproducible order."""
    relpaths = set()
    for root in (old_root, new_root):
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            relpath = path.relative_to(root)
            if any(fnmatch.fnmatch(str(relpath), pattern) for pattern in patterns):
                relpaths.add(relpath)
    yield from sorted(relpaths)


def _read(path: Path) -> List[str]:
    if not path.is_file():
        return list()
    with open(path, "r") as fh:
        return list(fh)


def _colorize(lines: Sequence[str]) -> Iterator[str]:
    for line in lines:
        color = _ANSI.get(line[:1]) if not line.startswith(("+++", "---")) else None
        yield f"{color}{line}{_ANSI_RESET}" if color else line
