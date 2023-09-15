"""Helper script to rename the project content after cloning the template."""
import itertools
import re
from pathlib import Path

from git.repo import Repo

# Constants for your username and repo name
ORIGINAL_USERNAME = "fschuch"
ORIGINAL_PROJECT_NAME = "wizard-template"

# Target files
TARGET_FILES = {"*.py", "*.md", "*.yaml", "*.toml", "LICENSE"}

# Get the current working directory
CWD = Path.cwd()
THIS_FILE = Path(__file__)


def main():
    """Rename the project content."""
    print("The wizard will now prepare your project...")
    # Get info about the project if is running from
    repo = Repo(CWD)
    remote_url = repo.remotes.origin.url

    # Extract username and project name
    username, project_name = remote_url.removesuffix(".git").split("/")[-2:]

    # Prepare the project name variations
    project_name_dash = project_name.replace("_", "-")
    project_name_underscore = project_name.replace("-", "_")

    # Map new values to the patterns to be replaced
    patterns = {
        username: re.compile(ORIGINAL_USERNAME),
        project_name: re.compile(ORIGINAL_PROJECT_NAME),
        project_name_dash: re.compile(ORIGINAL_PROJECT_NAME.replace("_", "-")),
        project_name_underscore: re.compile(
            ORIGINAL_PROJECT_NAME.replace("-", "_")
        ),
        "": re.compile(r"(post_)?wizard\s?=\s?\".+\""),
    }

    # Replace hardcoded strings
    for filepath in itertools.chain(*map(CWD.rglob, TARGET_FILES)):
        if any(p.startswith(".") for p in filepath.parts):
            continue

        print(f"Replacing text on file {filepath.relative_to(CWD)}")
        filedata = filepath.read_text()

        # Replace the target string
        for new_value, pattern in patterns.items():
            filedata = pattern.sub(new_value, filedata)

        # Write the file out again
        filepath.write_text(filedata)

    # Remove the script itself
    print(f"Removing file {THIS_FILE.relative_to(CWD)}")
    THIS_FILE.unlink()

    # Rename the directory
    print(f"Renaming folder wizard_template to {project_name_underscore}")
    Path("wizard_template").rename(project_name_underscore)

    # Stage the changes
    print("Staging changes...")
    repo.git.add(A=True)

    print("Done!")


if __name__ == "__main__":
    main()
