# AI Agent Context for Wizard Template

This file provides context for AI coding assistants (like GitHub Copilot) working with projects created from this template.

## Template Overview

This is a Python project template that includes:

- Modern Python package structure using `src` layout
- Automated testing with pytest
- Code quality tools (ruff, mypy, pre-commit)
- Documentation with Jupyter Book
- CI/CD workflows with GitHub Actions
- Project management with Hatch
- VS Code dev container with multi-version Python support

## First-Time Setup (CRITICAL)

**When creating a new project from this template, the FIRST step is to run the renaming script:**

```bash
hatch run _wizard
```

This script:

- Replaces all references to `wizard-template` with your project name
- Replaces all references to `fschuch` with your username
- Renames the `src/wizard_template` directory to your project name
- Removes itself after completion

**Do not skip this step** - it must be run immediately after cloning a new project from this template.

## Development Environment

### Dev Container (Recommended)

This project includes a VS Code dev container configuration (`.devcontainer/`) that provides:

- **Hatch**: Pre-installed via pipx
- **Multiple Python versions**: Python 3.10, 3.11, 3.12, 3.13, and 3.14 (managed via pyenv)
- **Pre-configured VS Code**: Extensions and settings for Python development
- **Automatic setup**: Post-create script installs all Python versions and pre-commit hooks

To use the dev container:
1. Open the project in VS Code
2. Click "Reopen in Container" when prompted
3. Wait for the container to build and setup to complete

See `.devcontainer/README.md` for detailed information about the dev container configuration.

## Project Management Tool: Hatch

This project uses [Hatch](https://hatch.pypa.io/) as the primary project management tool.

### Key Hatch Commands

```bash
# Run the renaming wizard (first-time setup only)
hatch run _wizard

# Install pre-commit hooks
hatch run pre-commit-install

# Run all quality checks (linting, type checking, formatting)
hatch run check

# Run type checking only
hatch run type

# Run linting only
hatch run lint

# Run formatting check only
hatch run format

# Run tests with coverage
hatch run test

# Run tests without coverage (faster)
hatch run test-no-cov

# Run all quality assurance checks + tests (recommended before commits)
hatch run qa

# Build documentation
hatch run docs:build

# Serve documentation with live reload
hatch run docs:serve
```

### Hatch Virtual Environments

Hatch automatically manages virtual environments. To configure Hatch to keep environments within the project folder:

```bash
hatch config set dirs.env.virtual .venv
```

## Quality Assurance Tools

### Linting & Formatting

- **Ruff**: Fast Python linter and formatter (replaces flake8, black, isort)
  - Configured in `pyproject.toml` under `[tool.ruff]`
  - Convention: Google-style docstrings

### Type Checking

- **MyPy**: Static type checker for Python
  - Configured in `pyproject.toml` under `[tool.mypy]`
  - Type hints are expected in all new code

### Testing

- **Pytest**: Testing framework
  - Tests located in `tests/` directory
  - Run with `hatch run test`
  - Coverage requirement: 90% (configured in `pyproject.toml`)
  - Doctests are enabled for all Python files

### Pre-commit Hooks

- Configured in `.pre-commit-config.yaml`
- Includes: ruff, mypy, codespell, file checks, mdformat, nbstripout, zizmor
- Install with `hatch run pre-commit-install`
- Run manually with `hatch run check`

## Project Structure

```
.
├── src/wizard_template/     # Main package source code (rename after setup)
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
│   └── dependabot.yml
├── pyproject.toml          # Project configuration and dependencies
├── .pre-commit-config.yaml # Pre-commit hooks configuration
└── README.md               # Project README
```

## Development Workflow

### Making Changes

1. Create a new branch for your changes
1. Make your code changes
1. Add/update tests as needed
1. Run QA checks: `hatch run qa`
1. Commit your changes
1. Push and create a pull request

### Adding Dependencies

Add dependencies to `pyproject.toml` under:

- `dependencies` for runtime dependencies
- `project.optional-dependencies.tests` for test dependencies
- `project.optional-dependencies.docs` for documentation dependencies

Hatch will automatically install them in the virtual environment.

## CI/CD Workflows

This template includes several GitHub Actions workflows:

- **ci.yaml**: Runs tests on multiple Python versions (3.10-3.14)
- **docs.yaml**: Builds and deploys documentation to GitHub Pages
- **check-links.yaml**: Validates links in documentation
- **update-pre-commits.yaml**: Automatically updates pre-commit hook versions

## Common Patterns

### Adding a New Module

1. Create new file in `src/wizard_template/` (or your renamed package)
1. Add type hints to all functions
1. Add Google-style docstrings
1. Create corresponding test file in `tests/`
1. Ensure coverage stays above 90%

### Adding Tests

- Use pytest conventions (test files start with `test_`, test functions start with `test_`)
- Use fixtures for common setup
- Include doctests in docstrings for simple examples
- Run with `hatch run test` to see coverage report

### Documentation

- Documentation is built with Jupyter Book
- Located in `docs/` directory
- Uses MyST Markdown (supports both Markdown and reStructuredText)
- Build locally with `hatch run docs:build`
- Preview with `hatch run docs:serve`

## Versioning

This project uses:

- **EffVer** (Effort-based Versioning) for version scheme
- **hatch-vcs** for automatic version management from git tags
- Version is automatically generated from git tags

## Important Notes for AI Assistants

1. **Always run the renaming script first** when working with a new project from this template
1. **Use `hatch run` prefix** for all project commands, not direct pip/pytest/etc.
1. **Maintain 90% test coverage** - add tests for new code
1. **Follow Google docstring convention** for all docstrings
1. **Add type hints** to all new functions and methods
1. **Run `hatch run qa`** before committing to ensure all checks pass
1. **Keep the wizard badge** in README.md - it shows the project was created from this template
1. **Do not commit** `__pycache__`, `.venv`, `build/`, or other build artifacts

## Getting Help

- Full documentation: <https://docs.fschuch.com/wizard-template>
- Template repository: <https://github.com/fschuch/wizard-template>
- Report issues: <https://github.com/fschuch/wizard-template/issues>
