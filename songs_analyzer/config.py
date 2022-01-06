import os
import toml
from pathlib import Path

def read_toml(filename: str):
    with open(filename, "r") as f:
        toml_data = toml.load(f)
    return toml_data

def get_root_path():
    current_path = Path.cwd()
    while current_path.parent != current_path:
        if "pyproject.toml" in os.listdir(current_path):
            project_info = read_toml(Path(current_path) / "pyproject.toml")["tool"]["poetry"]
            if project_info.get("name") == "songs_analyzer":
                return current_path
        else:
            current_path = current_path.parent
    return None