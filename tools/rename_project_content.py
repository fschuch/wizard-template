"""Helper script to rename the project content after cloning the template."""

from __future__ import annotations

import itertools
import re
import subprocess
from pathlib import Path
from typing import NamedTuple

# Constants for your username and repo name
ORIGINAL_USERNAME = "fschuch"
ORIGINAL_PROJECT_NAME = "wizard-template"

# Target files
TARGET_FILES = {"*.py", "*.md", "*.yaml", "*.toml", "LICENSE"}

# Get the current working directory
CWD = Path.cwd()
THIS_FILE = Path(__file__)

COMMUNITY_BADGE_TEMPLATE = (
    "[![Wizard Template]"
    "(https://img.shields.io/badge/Wizard-Template-%23447CAA)]"
    "(https://github.com/{}/{})"
)

ORIGINAL_BADGE = COMMUNITY_BADGE_TEMPLATE.format(
    ORIGINAL_USERNAME, ORIGINAL_PROJECT_NAME
)


class GitInfo(NamedTuple):
    """Named tuple to store the git info."""

    username: str
    repo: str


def get_git_url() -> str:
    """Get the git URL from the repository."""
    git_command = ["git", "config", "--get", "remote.origin.url"]
    return subprocess.check_output(git_command).decode("utf-8").strip()


def match_git_url(git_url: str) -> GitInfo:
    """
    Match a git URL to extract the username and repository name.

    >>> match_git_url("https://github.com/fschuch/wizard-template.git")
    GitInfo(username='fschuch', repo='wizard-template')
    >>> match_git_url("git@github.com:fschuch/wizard-template.git")
    GitInfo(username='fschuch', repo='wizard-template')
    >>> match_git_url("not-a-repo")
    Traceback (most recent call last):
        ...
    ValueError: Could not parse git URL
    """
    match = re.fullmatch(
        r"(?:https://|git@)[\w.-]+[:/](?P<username>[^/]+)/(?P<repo>[^/]+)\.git", git_url
    )
    if match:
        return GitInfo(**match.groupdict())
    raise ValueError("Could not parse git URL")


def from_repo_info_with_fallback() -> GitInfo:
    """Get the repository information."""
    try:
        return match_git_url(get_git_url())
    except (ValueError, subprocess.CalledProcessError):
        print("Could not parse git URL, please enter the information manually.")
        username = input("Enter your username: ")
        repo = input("Enter your repo: ")
        return GitInfo(username, repo)


def main() -> None:
    """Rename the project content."""
    print("The wizard will now prepare your project...")

    # Get username and project name
    username, project_name = from_repo_info_with_fallback()

    # Prepare the project name variations
    project_name_dash = project_name.replace("_", "-")
    project_name_underscore = project_name.replace("-", "_")

    tmp_badge = COMMUNITY_BADGE_TEMPLATE.format(username, project_name)

    # Pair new values and the patterns to be replaced
    patterns = [
        (username, re.compile(ORIGINAL_USERNAME)),
        (project_name, re.compile(ORIGINAL_PROJECT_NAME)),
        (project_name_dash, re.compile(ORIGINAL_PROJECT_NAME.replace("_", "-"))),
        (project_name_underscore, re.compile(ORIGINAL_PROJECT_NAME.replace("-", "_"))),
        ("", re.compile(r"_wizard\s?=\s?\[\".+\"\]\n")),
    ]

    # Replace hardcoded strings
    for filepath in itertools.chain(*map(CWD.rglob, TARGET_FILES)):
        if any(p.startswith(".") for p in filepath.parts):
            continue

        print(f"Replacing text on file {filepath.relative_to(CWD)}")
        filedata = filepath.read_text()

        # Replace the target string
        for new_value, pattern in patterns:
            filedata = pattern.sub(new_value, filedata)

        # Revert back the badge to support the original project
        filedata = filedata.replace(tmp_badge, ORIGINAL_BADGE)

        # Write the file out again
        filepath.write_text(filedata)

    # Remove the script itself
    print(f"Removing file {THIS_FILE.relative_to(CWD)}")
    THIS_FILE.unlink()

    # Rename the directory
    print(f"Renaming folder wizard_template to {project_name_underscore}")
    Path("src/wizard_template").rename(f"src/{project_name_underscore}")

    print("Done!")


if __name__ == "__main__":
    main()
