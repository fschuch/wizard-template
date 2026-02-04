#!/usr/bin/env python3
"""
Generate Copier Template from Wizard Template

This script converts the wizard-template (a working Python project) into a
copier template format. This allows maintaining the template as a real project
with working dependencies, CI/CD, and automated updates (dependabot, pre-commit),
while still providing a copier-compatible template for users.

Usage:
    python tools/generate-copier-template.py [--output-dir OUTPUT_DIR]

The generated copier template can be:
1. Committed to a separate repository
2. Used with GitHub Actions to auto-sync changes
3. Published for users to create projects via `copier copy`
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import NamedTuple


class TemplateVariable(NamedTuple):
    """Template variable definition."""

    name: str
    pattern: str
    jinja_expr: str


# Variables to replace in the template
TEMPLATE_VARIABLES = [
    TemplateVariable(
        name="username",
        pattern=r"fschuch",
        jinja_expr="{{ project_slug }}",
    ),
    TemplateVariable(
        name="project_name",
        pattern=r"wizard-template",
        jinja_expr="{{ project_name }}",
    ),
    TemplateVariable(
        name="project_slug",
        pattern=r"wizard_template",
        jinja_expr="{{ project_slug }}",
    ),
    TemplateVariable(
        name="email",
        pattern=r"me@fschuch\.com",
        jinja_expr="{{ author_email }}",
    ),
    TemplateVariable(
        name="author_name",
        pattern=r"fschuch",
        jinja_expr="{{ author_name }}",
    ),
    TemplateVariable(
        name="description",
        pattern=r"A template for a python project containing a package, tests, docs, and CI/CD\.",
        jinja_expr="{{ project_description }}",
    ),
]

# Files/directories to exclude from the copier template
EXCLUDE_PATTERNS = {
    ".git",
    ".github/workflows/template-sync-check.yaml.example",
    ".github/workflows/sync-copier-template.yaml.example",
    "__pycache__",
    "*.pyc",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".coverage",
    "htmlcov",
    "dist",
    "build",
    "*.egg-info",
    ".templaterc",
    "SOLUTION-SUMMARY.md",
    "docs/template-sync.md",
    "docs/template-sync-quickstart.md",
    "docs/template-sync-examples.md",
    "docs/copier-template-automation.md",  # Copier automation docs
    "docs/copier-quickstart.md",  # Copier quickstart docs
    "tests/test_template_sync.py",
    "tools/template-sync.py",
    "tools/generate-copier-template.py",  # Don't include this script
}

# Special handling for certain file types
BINARY_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf"}
SKIP_TEMPLATING_PATTERNS = {
    "LICENSE",  # Usually don't template licenses
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".github/workflows",  # Skip GitHub Actions workflows to avoid ${{ }} conflicts
}


def should_exclude(path: Path, base_path: Path) -> bool:
    """Check if a path should be excluded from the template."""
    relative_path = path.relative_to(base_path)
    path_str = str(relative_path)

    for pattern in EXCLUDE_PATTERNS:
        if pattern.endswith("*"):
            # Wildcard pattern
            if path_str.startswith(pattern[:-1]):
                return True
        elif "*" in pattern:
            # Extension pattern like *.pyc
            ext = pattern.split("*", 1)[1]
            if path_str.endswith(ext):
                return True
        elif path_str == pattern or relative_path.name == pattern:
            return True
        # Check if any parent directory matches
        for part in relative_path.parts:
            if part == pattern:
                return True

    return False


def should_skip_templating(file_path: Path) -> bool:
    """Check if a file should skip variable replacement."""
    # Binary files
    if file_path.suffix in BINARY_EXTENSIONS:
        return True

    # Specific patterns
    for pattern in SKIP_TEMPLATING_PATTERNS:
        if file_path.name == pattern or file_path.suffix == pattern:
            return True
        # Check if in workflows directory
        if ".github/workflows" in str(file_path) and ".github/workflows" in pattern:
            return True

    return False


def apply_template_variables(content: str, file_path: Path) -> str:
    """
    Replace hardcoded values with Jinja2 template variables.

    Args:
        content: File content as string
        file_path: Path to the file (for context-aware replacements)

    Returns:
        Content with template variables
    """
    result = content

    # Special handling for specific files
    if file_path.name == "pyproject.toml":
        # Replace name field
        result = re.sub(
            r'name\s*=\s*"wizard-template"',
            'name = "{{ project_name }}"',
            result,
        )
        # Replace description
        result = re.sub(
            r'description\s*=\s*"[^"]*"',
            'description = "{{ project_description }}"',
            result,
            count=1,
        )
        # Replace author name
        result = re.sub(
            r'\[\s*{\s*name\s*=\s*"fschuch"',
            '[{ name = "{{ author_name }}"',
            result,
        )
        # Replace email
        result = re.sub(
            r'email\s*=\s*"me@fschuch\.com"',
            'email = "{{ author_email }}"',
            result,
        )
        # Replace URLs
        result = re.sub(
            r"https://github\.com/fschuch/wizard-template",
            "https://github.com/{{ author_name }}/{{ project_name }}",
            result,
        )
        result = re.sub(
            r"https://fschuch\.github\.io/wizard-template",
            "https://{{ author_name }}.github.io/{{ project_name }}",
            result,
        )
        result = re.sub(
            r'source\s*=\s*"src/wizard_template"',
            'source = "src/{{ project_slug }}"',
            result,
        )
        result = re.sub(
            r'version-file\s*=\s*"src/wizard_template/_version\.py"',
            'version-file = "src/{{ project_slug }}/_version.py"',
            result,
        )

    elif file_path.name == "README.md":
        # Replace title
        result = re.sub(
            r"# The Wizard Template for Python Projects",
            "# {{ project_name }}",
            result,
        )
        # Replace badges and URLs
        result = re.sub(
            r"https://github\.com/fschuch/wizard-template",
            "https://github.com/{{ author_name }}/{{ project_name }}",
            result,
        )
        result = re.sub(
            r"https://docs\.fschuch\.com/wizard-template",
            "https://{{ author_name }}.github.io/{{ project_name }}",
            result,
        )
        result = re.sub(
            r"fschuch_wizard-template",
            "{{ author_name }}_{{ project_name }}",
            result,
        )

    elif file_path.suffix in {".yaml", ".yml"}:
        # YAML files (but not GitHub Actions, those are skipped)
        result = re.sub(
            r"https://github\.com/fschuch/wizard-template",
            "https://github.com/{{ author_name }}/{{ project_name }}",
            result,
        )

    # General replacements for all files
    # Replace wizard_template directory references
    result = re.sub(
        r"\bwizard_template\b",
        "{{ project_slug }}",
        result,
    )

    # Replace wizard-template (with dash)
    result = re.sub(
        r"\bwizard-template\b",
        "{{ project_name }}",
        result,
    )

    # Replace GitHub username in URLs
    result = re.sub(
        r"github\.com/fschuch/",
        "github.com/{{ author_name }}/",
        result,
    )

    # Replace author email
    result = re.sub(
        r"\bme@fschuch\.com\b",
        "{{ author_email }}",
        result,
    )

    return result


def generate_copier_yml() -> str:
    """Generate the copier.yml configuration file."""
    return """# Copier template configuration
# https://copier.readthedocs.io/

# Questions to ask the user
project_name:
  type: str
  help: What is your project name (with dashes)?
  default: my-awesome-project
  validator: "{% if not project_name %}Required{% endif %}"

project_slug:
  type: str
  help: What is your project slug (with underscores, for Python package)?
  default: "{{ project_name|replace('-', '_') }}"

author_name:
  type: str
  help: What is your GitHub username or organization?
  default: myusername
  validator: "{% if not author_name %}Required{% endif %}"

author_email:
  type: str
  help: What is your email?
  default: me@example.com
  validator: "{% if not author_email %}Required{% endif %}"

project_description:
  type: str
  help: Brief description of your project
  default: A Python project based on the wizard template

# Template options
_subdirectory: ""

# Only process .jinja files with Jinja templating
# Other files are copied as-is
_templates_suffix: ".jinja"

# Tasks to run after generation (optional, users can skip with --skip-tasks)
_tasks:
  - "git init"
  - "git add ."
  - "git commit -m 'Initial commit from wizard-template'"

# Files to exclude from the template
_exclude:
  - "copier.yml"
  - "*.pyc"
  - "__pycache__"
  - ".git"
  - ".pytest_cache"
  - ".mypy_cache"
  - ".ruff_cache"
  - ".coverage"
  - "htmlcov"
  - "*.egg-info"
  - "dist"
  - "build"

# Minimum copier version
_min_copier_version: "9.0.0"
"""


def generate_readme_for_copier() -> str:
    """Generate README for the copier template repository."""
    return """# Wizard Template - Copier Version

This is the [Copier](https://copier.readthedocs.io/) template version of the
[wizard-template](https://github.com/fschuch/wizard-template) Python project template.

## About

This template is **automatically generated** from the wizard-template repository.
The wizard-template is maintained as a working Python project with real dependencies,
CI/CD, tests, and receives automated updates from dependabot and pre-commit.

Changes made to wizard-template are automatically converted to this copier template
format, ensuring that template improvements and dependency updates flow downstream
to users.

## Usage

### Create a new project

```bash
# Install copier
pip install copier

# Create a new project from this template
copier copy https://github.com/fschuch/wizard-template-copier my-project

# Or from a local clone
copier copy . /path/to/my-project
```

You'll be prompted for:
- Project name (with dashes, e.g., `my-awesome-project`)
- Project slug (with underscores, e.g., `my_awesome_project`)
- Author name (GitHub username)
- Author email
- Project description

### Update an existing project

```bash
# Update your project with the latest template
cd my-project
copier update
```

## Features

This template includes:

- 🚀 **Modern Python Setup**: Uses `hatchling` for building and `hatch` for development
- ✅ **Quality Assurance**: Pre-configured linting (ruff), type checking (mypy), and testing (pytest)
- 📚 **Documentation**: Automated documentation with Jupyter Book
- 🤖 **CI/CD**: GitHub Actions workflows for testing, building, and deployment
- 📦 **Dependency Management**: Dependabot configuration for automated updates
- 🎯 **Pre-commit Hooks**: Automated code quality checks
- 🔒 **Security**: CodeQL analysis and zizmor security scanning

## Source Repository

This copier template is generated from:
https://github.com/fschuch/wizard-template

To contribute or report issues, please use the main wizard-template repository.

## Maintenance

**Do not manually edit files in this repository!**

This repository is automatically synchronized from the wizard-template source.
All changes should be made to the wizard-template repository and will be
automatically converted to copier format.

## License

MIT License - See LICENSE file for details.

© 2023 Felipe N. Schuch
"""


def copy_template_files(source_dir: Path, output_dir: Path) -> None:
    """
    Copy files from source to output, applying template transformations.

    Args:
        source_dir: Source directory (wizard-template)
        output_dir: Output directory (copier template)
    """
    print(f"Copying template files from {source_dir} to {output_dir}")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Track statistics
    stats = {"copied": 0, "templated": 0, "skipped": 0}

    # Walk through source directory
    for item in source_dir.rglob("*"):
        if not item.is_file():
            continue

        # Check if should be excluded
        if should_exclude(item, source_dir):
            stats["skipped"] += 1
            continue

        # Calculate relative path and output path
        relative_path = item.relative_to(source_dir)
        output_path = output_dir / relative_path

        # Handle special case: rename src/wizard_template to src/{{ project_slug }}
        if "wizard_template" in str(relative_path):
            new_relative = Path(str(relative_path).replace("wizard_template", "{{ project_slug }}"))
            output_path = output_dir / new_relative

        # Create parent directories
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Copy file
        if should_skip_templating(item):
            # Binary file or should not be templated - copy as-is
            shutil.copy2(item, output_path)
            stats["copied"] += 1
            print(f"  Copied: {relative_path}")
        else:
            # Text file - apply template transformations and add .jinja extension
            try:
                content = item.read_text(encoding="utf-8")
                templated_content = apply_template_variables(content, item)
                # Add .jinja extension so copier knows to process it
                jinja_output_path = output_path.parent / (output_path.name + ".jinja")
                jinja_output_path.write_text(templated_content, encoding="utf-8")
                stats["templated"] += 1
                print(f"  Templated: {relative_path} → {relative_path}.jinja")
            except Exception as e:
                print(f"  Warning: Could not template {relative_path}: {e}")
                # Fall back to copying
                shutil.copy2(item, output_path)
                stats["copied"] += 1

    print(f"\nStatistics:")
    print(f"  Templated: {stats['templated']}")
    print(f"  Copied as-is: {stats['copied']}")
    print(f"  Skipped: {stats['skipped']}")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate copier template from wizard-template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate in default output directory
  python tools/generate-copier-template.py

  # Generate in custom directory
  python tools/generate-copier-template.py --output-dir /path/to/copier-template

  # The output can then be:
  # 1. Pushed to a separate git repository
  # 2. Used with copier: copier copy /path/to/copier-template my-project
        """,
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("../wizard-template-copier"),
        help="Output directory for the copier template (default: ../wizard-template-copier)",
    )

    args = parser.parse_args()

    source_dir = Path(__file__).parent.parent
    output_dir = args.output_dir.resolve()

    print("=" * 70)
    print("Wizard Template → Copier Template Generator")
    print("=" * 70)
    print(f"\nSource: {source_dir}")
    print(f"Output: {output_dir}")
    print()

    # Confirm if output directory exists
    if output_dir.exists():
        response = input(f"Output directory {output_dir} exists. Overwrite? (y/N): ")
        if response.lower() != "y":
            print("Aborted.")
            sys.exit(1)
        shutil.rmtree(output_dir)

    # Copy and transform files
    copy_template_files(source_dir, output_dir)

    # Generate copier.yml
    print("\nGenerating copier.yml...")
    copier_yml_path = output_dir / "copier.yml"
    copier_yml_path.write_text(generate_copier_yml(), encoding="utf-8")
    print(f"  Created: copier.yml")

    # Generate README for copier template
    print("\nGenerating README for copier template...")
    readme_path = output_dir / "README-COPIER.md"
    readme_path.write_text(generate_readme_for_copier(), encoding="utf-8")
    print(f"  Created: README-COPIER.md")

    print("\n" + "=" * 70)
    print("✅ Copier template generation complete!")
    print("=" * 70)
    print(f"\nNext steps:")
    print(f"1. Review the generated template in: {output_dir}")
    print(f"2. Test it: copier copy {output_dir} /tmp/test-project")
    print(f"3. Initialize git repo: cd {output_dir} && git init")
    print(f"4. Push to GitHub: create repo and push")
    print(f"\nSee docs/copier-template-automation.md for automation setup.")


if __name__ == "__main__":
    main()
