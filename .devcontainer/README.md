# Development Container Configuration

This directory contains the configuration for a VS Code development container that provides a complete development environment for the wizard-template project.

## Features

- **Python Versions**: Includes Python 3.10, 3.11, 3.12, 3.13, and 3.14 (managed via pyenv)
- **Hatch**: Pre-installed project management tool
- **Pre-configured VS Code**: Extensions and settings optimized for Python development
- **Pre-commit Hooks**: Automatically installed on container creation

## What's Included

### Tools

- **Hatch**: Python project management tool (installed via pipx)
- **Pyenv**: Python version management (for managing multiple Python versions)
- **Git**: Version control
- **Build tools**: Essential build dependencies for Python packages

### VS Code Extensions

- Python extension with Pylance
- Ruff linter and formatter
- Better TOML support
- GitHub Copilot (if available)

### Configuration

- Python formatting and linting configured for Ruff
- Format on save enabled
- Pytest testing framework configured
- Virtual environments stored in `.venv` directory

## Usage

### Opening in VS Code

1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the project in VS Code
3. When prompted, click "Reopen in Container" (or use Command Palette: "Dev Containers: Reopen in Container")
4. Wait for the container to build and the post-create script to complete

### First-Time Setup

The post-create script automatically:
1. Installs pyenv for Python version management
2. Installs Python versions 3.10, 3.11, 3.12, 3.13, and 3.14
3. Configures hatch to use local virtual environments
4. Installs pre-commit hooks

### Working with Multiple Python Versions

All Python versions are available via pyenv:

```bash
# List all installed Python versions
pyenv versions

# Use a specific version for the current shell
pyenv shell 3.11

# Use a specific version for the current directory
pyenv local 3.11

# Run tests with a specific Python version using hatch
hatch run +py=3.11 test
```

### Running Common Tasks

```bash
# Install dependencies and run tests
hatch run test

# Run quality assurance checks
hatch run qa

# Build documentation
hatch run docs:build

# Run pre-commit hooks
hatch run check
```

## Customization

To customize the development container:

1. Edit `devcontainer.json` to add features, extensions, or change settings
2. Modify `post-create.sh` to change post-creation setup steps
3. Rebuild the container: Command Palette → "Dev Containers: Rebuild Container"

## Troubleshooting

### Python Version Not Found

If a Python version is not available:

```bash
# List available versions
pyenv install --list

# Install a specific version
pyenv install 3.12.1

# Set it as global
pyenv global 3.10.x 3.11.x 3.12.1 3.13.x 3.14.x
```

### Hatch Not Found

If hatch is not available:

```bash
# Install hatch via pipx
pipx install hatch

# Or install it via pip
pip install hatch
```

## Technical Details

- **Base Image**: `mcr.microsoft.com/devcontainers/python:1-3.12-bookworm`
- **Default Python**: 3.12 (from base image)
- **Additional Pythons**: Installed via pyenv
- **Package Manager**: Hatch with uv installer
- **User**: `vscode` (non-root)

## References

- [Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Hatch Documentation](https://hatch.pypa.io/)
- [Pyenv Documentation](https://github.com/pyenv/pyenv)
