from pathlib import Path


def pytest_path_param_id(path: Path) -> str:
    return f"{path.parent.name}/{path.name}"
