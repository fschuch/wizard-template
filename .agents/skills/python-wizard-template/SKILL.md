---
name: python-wizard-template
description: Expert guidance for working with Python projects using the wizard-template, including new projects, migrations, updates, and best practices for Hatch workflows and quality standards.
license: MIT
---

# Python Wizard Template Skill

This skill provides comprehensive guidance for AI assistants working with Python projects that use or want to use the [wizard-template](https://github.com/fschuch/wizard-template). It covers three main scenarios: new projects from template, applying template to existing projects, and updating projects with template changes.

## When to Use This Skill

### Automatic Detection

This skill applies when ANY of these conditions are met:

- Repository has a "Wizard Template" badge in README.md
- File `src/wizard_template/` directory exists (pre-renamed template)
- File `pyproject.toml` references `wizard-template` in URLs or comments
- File `.github/copilot-instructions.md` references wizard-template
- User explicitly mentions using wizard-template

### User Requests

This skill also applies when users ask to:

- Start a new Python project with quality tools
- Apply wizard-template structure to an existing project
- Update their project with latest template changes
- Set up Hatch, testing, documentation, or CI/CD from wizard-template

## Scenario 1: New Project from Template (Fresh Clone)

### CRITICAL First Step

**When `src/wizard_template/` exists, you MUST run the renaming wizard FIRST:**

```bash
hatch run _wizard
```

This script:
- Detects the git repository URL automatically
- Replaces all `wizard-template` references with the actual project name
- Replaces all `fschuch` references with the actual username
- Renames `src/wizard_template/` to `src/{project_name}/`
- Removes itself after completion (cleanup)

**DO NOT** make any other changes before running this script!

### After Renaming

1. Install pre-commit hooks:
   ```bash
   hatch run pre-commit-install
   ```

2. Verify the setup:
   ```bash
   hatch run qa
   ```

3. Update documentation in `docs/intro.md` with project-specific content

## Scenario 2: Applying Template to Existing Project

When a user wants to apply wizard-template structure to an existing Python project that has a different structure, follow this **gradual migration approach**:

### Assessment Phase

1. **Analyze current structure:**
   - Identify package layout (flat vs src layout)
   - Check existing tools (pytest, linting, docs)
   - Review current dependencies and build system
   - Note any custom CI/CD configurations

2. **Determine migration strategy:**
   - Full migration (recommended for small/new projects)
   - Gradual migration (recommended for large/established projects)

### Full Migration Steps

Use when project is small, young, or highly compatible:

1. **Backup current state:**
   ```bash
   git checkout -b backup-before-wizard-template
   git checkout -b migrate-to-wizard-template
   ```

2. **Clone template reference:**
   ```bash
   cd /tmp
   git clone https://github.com/fschuch/wizard-template.git wizard-ref
   ```

3. **Copy core configuration files:**
   - `pyproject.toml` (merge dependencies, keep project metadata)
   - `.pre-commit-config.yaml`
   - `.github/workflows/` (CI/CD workflows)
   - `docs/` structure (merge with existing docs)

4. **Migrate to src/ layout:**
   ```bash
   # If package is currently at project root
   mkdir -p src
   mv {package_name} src/
   ```

5. **Update import paths** in tests and code if needed

6. **Run quality checks:**
   ```bash
   hatch run qa
   ```

### Gradual Migration Steps

Use when project is large, established, or has significant customizations:

1. **Phase 1 - Build System:**
   - Add Hatch configuration to `pyproject.toml`
   - Keep existing build system temporarily
   - Test with: `hatch run test-no-cov`

2. **Phase 2 - Code Quality:**
   - Add Ruff configuration
   - Add MyPy configuration
   - Run and fix issues: `hatch run lint`, `hatch run type`

3. **Phase 3 - Testing:**
   - Add pytest configuration
   - Add coverage configuration
   - Migrate existing tests to pytest if needed

4. **Phase 4 - Documentation:**
   - Add Jupyter Book structure
   - Migrate existing docs to MyST markdown
   - Set up docs build: `hatch run docs:build`

5. **Phase 5 - CI/CD:**
   - Copy GitHub Actions workflows
   - Adapt to project-specific needs
   - Test in feature branch

6. **Phase 6 - Pre-commit Hooks:**
   - Add pre-commit configuration
   - Install: `hatch run pre-commit-install`

### Key Files to Customize

When migrating, **DO NOT** blindly copy these - customize them:

- `pyproject.toml` - Keep your project name, description, dependencies
- `README.md` - Keep your project content, add wizard badge
- `docs/intro.md` - Replace with your project documentation
- `LICENSE` - Keep your license (unless changing)

### Files Safe to Copy

These can typically be copied directly:

- `.pre-commit-config.yaml`
- `.github/workflows/ci.yaml`
- `.github/workflows/docs.yaml`
- `.github/workflows/check-links.yaml`
- `.github/copilot-instructions.md`
- `.agents/` (this skill!)

## Scenario 3: Updating Project with Template Changes

When wizard-template releases updates and you want to incorporate them:

### Tracking Template Updates

1. **Add template as remote (one-time setup):**
   ```bash
   git remote add template https://github.com/fschuch/wizard-template.git
   git fetch template
   ```

2. **Check for template changes:**
   ```bash
   git fetch template
   git log HEAD..template/main --oneline
   ```

3. **Review template changes:**
   ```bash
   git diff HEAD...template/main
   ```

### Selective Update Strategy

**IMPORTANT:** Never merge template directly! It will break your project.

Instead, **selectively apply changes:**

1. **Identify what changed:**
   ```bash
   # See changed files
   git diff --name-only HEAD...template/main
   
   # See specific file changes
   git diff HEAD...template/main -- pyproject.toml
   ```

2. **Common update patterns:**

   **Update tool configurations:**
   ```bash
   # Compare configurations
   git show template/main:pyproject.toml > /tmp/template-pyproject.toml
   # Manually merge relevant sections
   ```

   **Update workflows:**
   ```bash
   # Copy specific workflow
   git show template/main:.github/workflows/ci.yaml > .github/workflows/ci.yaml
   # Review and adjust for your project
   ```

   **Update dependencies:**
   ```bash
   # Check template dependency versions
   git show template/main:pyproject.toml | grep -A 20 "dependencies"
   # Update your versions as needed
   ```

3. **Test after each update:**
   ```bash
   hatch run qa
   ```

### Automated Update Helper

Create a script to compare configurations:

```bash
#!/bin/bash
# tools/check-template-updates.sh

echo "Fetching template updates..."
git fetch template

echo -e "\n=== Changed files in template ==="
git diff --name-only HEAD...template/main

echo -e "\n=== Tool configuration changes ==="
git diff HEAD...template/main -- pyproject.toml .pre-commit-config.yaml

echo -e "\n=== Workflow changes ==="
git diff HEAD...template/main -- .github/workflows/
```

## Project Management Tool: Hatch

All projects using wizard-template use [Hatch](https://hatch.pypa.io/) as the primary project management tool.

### Essential Hatch Commands

```bash
# Development workflow
hatch run test              # Run tests with coverage
hatch run test-no-cov       # Run tests without coverage (faster)
hatch run lint              # Run ruff linter
hatch run format            # Check code formatting
hatch run type              # Run mypy type checking
hatch run check             # Run pre-commit checks
hatch run qa                # Run ALL quality checks + tests

# Documentation
hatch run docs:build        # Build documentation
hatch run docs:serve        # Serve docs with live reload

# Pre-commit
hatch run pre-commit-install  # Install pre-commit hooks
```

### Hatch Environment Configuration

Configure Hatch to keep virtual environments in project folder:

```bash
hatch config set dirs.env.virtual .venv
```

## Code Quality Standards

### Required Conventions

1. **Google-style docstrings** for all public functions/classes
2. **Type hints** on all function signatures
3. **90% test coverage** minimum (configured in pyproject.toml)
4. **Ruff** for linting and formatting
5. **MyPy** for static type checking

### Example: Adding a New Module

```python
# src/{project_name}/my_module.py
"""Module for doing something useful.

This module provides functionality for...
"""

def calculate_something(value: int, multiplier: float = 1.5) -> float:
    """Calculate something useful.

    Args:
        value: The input value to process.
        multiplier: The multiplication factor.

    Returns:
        The calculated result.

    Raises:
        ValueError: If value is negative.

    Examples:
        >>> calculate_something(10)
        15.0
        >>> calculate_something(10, multiplier=2.0)
        20.0
    """
    if value < 0:
        raise ValueError("Value must be non-negative")
    return value * multiplier
```

### Example: Corresponding Test

```python
# tests/test_my_module.py
"""Tests for my_module."""

import pytest

from my_project.my_module import calculate_something


def test_calculate_something_basic():
    """Test basic calculation."""
    result = calculate_something(10)
    assert result == 15.0


def test_calculate_something_with_multiplier():
    """Test calculation with custom multiplier."""
    result = calculate_something(10, multiplier=2.0)
    assert result == 20.0


def test_calculate_something_negative_value():
    """Test that negative values raise ValueError."""
    with pytest.raises(ValueError, match="non-negative"):
        calculate_something(-1)
```

## Project Structure

Standard wizard-template structure:

```
.
├── src/{project_name}/      # Main package (after renaming)
│   ├── __init__.py
│   └── core.py
├── tests/                   # Test files
│   ├── __init__.py
│   └── test_core.py
├── docs/                    # Documentation (Jupyter Book)
│   ├── intro.md
│   ├── getting-started/
│   ├── user-guide/
│   └── references/
├── tools/                   # Helper scripts
│   └── rename_project_content.py
├── .github/                 # GitHub-specific files
│   ├── workflows/           # CI/CD workflows
│   ├── copilot-instructions.md
│   └── dependabot.yml
├── .agents/                 # Agent skills (you are here!)
│   └── skills/
├── pyproject.toml          # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md               # Project README
```

## CI/CD Workflows

Template includes these GitHub Actions workflows:

- **ci.yaml**: Runs tests on Python 3.10-3.14
- **docs.yaml**: Builds and deploys docs to GitHub Pages
- **check-links.yaml**: Validates documentation links
- **update-pre-commits.yaml**: Auto-updates pre-commit hooks

## Development Workflow Checklist

For any change to code:

- [ ] Create feature branch
- [ ] Make code changes with type hints
- [ ] Add Google-style docstrings
- [ ] Add/update tests (maintain 90% coverage)
- [ ] Run `hatch run qa` (all quality checks pass)
- [ ] Commit changes
- [ ] Push and create pull request

## Common Pitfalls to Avoid

1. **DON'T** skip the renaming wizard on new projects
2. **DON'T** use pip/pytest directly - use `hatch run` commands
3. **DON'T** commit `__pycache__`, `.venv`, `build/`, or other artifacts
4. **DON'T** merge template directly when updating - selectively apply changes
5. **DON'T** remove the Wizard Template badge from README
6. **DON'T** forget to run `hatch run qa` before committing
7. **DON'T** add dependencies without checking pyproject.toml structure

## Troubleshooting

### "hatch: command not found"

```bash
pip install hatch
# or
pipx install hatch
```

### "Module not found" errors in tests

Ensure you're using src layout correctly:

```bash
# Install in development mode
hatch run test
```

### Pre-commit hooks fail

```bash
# Update hooks
hatch run check

# Fix auto-fixable issues
hatch run format
```

### Coverage below 90%

```bash
# See coverage report
hatch run test

# Add missing tests for uncovered lines
```

## Cross-Repository Usage

### Using This Skill in Other Repositories

This skill is designed to be portable. You can use it in any repository:

#### Option 1: Project-Level (Recommended for Teams)

Copy this skill directory to your project:

```bash
# In your project repository
mkdir -p .agents/skills
cp -r /path/to/wizard-template/.agents/skills/python-wizard-template .agents/skills/
git add .agents
git commit -m "Add wizard-template agent skill"
```

All team members working on the repository will automatically benefit.

#### Option 2: User-Level (Personal Use Across All Projects)

Install for your user account to use across all repositories:

```bash
# Copy to user-level skills directory
mkdir -p ~/.agents/skills
cp -r /path/to/wizard-template/.agents/skills/python-wizard-template ~/.agents/skills/

# Or clone template and symlink
git clone https://github.com/fschuch/wizard-template.git ~/wizard-template
ln -s ~/wizard-template/.agents/skills/python-wizard-template ~/.agents/skills/python-wizard-template
```

This makes the skill available in ALL repositories you work on.

#### Option 3: Organization-Level (Future)

GitHub is developing organization-wide skills support. When available, organizations will be able to deploy skills centrally for all members and repositories.

### When to Use Each Option

- **Project-level**: Working on a specific project that uses wizard-template patterns
- **User-level**: You want wizard-template guidance available everywhere you work
- **Organization-level**: Your organization has standardized on wizard-template

## References and Resources

- Full documentation: <https://docs.fschuch.com/wizard-template>
- Template repository: <https://github.com/fschuch/wizard-template>
- Report issues: <https://github.com/fschuch/wizard-template/issues>
- Hatch documentation: <https://hatch.pypa.io/>
- Ruff documentation: <https://docs.astral.sh/ruff/>
- Jupyter Book documentation: <https://jupyterbook.org/>

## Relationship with copilot-instructions.md

This skill **complements** `.github/copilot-instructions.md`:

- **copilot-instructions.md**: Always loaded, provides quick reference
- **This skill**: Loaded on-demand, provides comprehensive guidance including migration and updates

Both files are maintained and serve different purposes:
- Use copilot-instructions.md for quick lookup and context
- Use this skill for detailed workflows, migration, and troubleshooting
