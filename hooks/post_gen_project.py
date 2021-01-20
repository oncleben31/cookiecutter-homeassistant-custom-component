#!/usr/bin/env python
import json
import os
import shutil
from pathlib import Path

REMOVE_PATHS = [
    '{% if cookiecutter.test_suite != "yes" %} tests/ {% endif %}',
]

def remove_path():
    """Remove some path according to cookiecutter parameters."""
    for path in REMOVE_PATHS:
        path = path.strip()
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)



def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


if __name__ == "__main__":
    reindent_cookiecutter_json()
    remove_path()
