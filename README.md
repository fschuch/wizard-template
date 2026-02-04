# The Wizard Template for Python Projects

<p align="center">
<a href="https://github.com/fschuch/wizard-template"><img src="https://raw.githubusercontent.com/fschuch/wizard-template/refs/heads/main/docs/logo.png" alt="Wizard template logo" width="320"></a>
</p>
<p align="center">
    <em>Let the wizard do the heavy lifting so you can focus on your craft</em>
</p>

______________________________________________________________________

- CI/CD:
  [![CI](https://github.com/fschuch/wizard-template/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/fschuch/wizard-template/actions/workflows/ci.yaml)
  [![Docs](https://github.com/fschuch/wizard-template/actions/workflows/docs.yaml/badge.svg?branch=main)](https://docs.fschuch.com/wizard-template)
  [![CodeQL](https://github.com/fschuch/wizard-template/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/fschuch/wizard-template/actions/workflows/github-code-scanning/codeql)
  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fschuch_wizard-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fschuch_wizard-template)

- Meta:
  [![Wizard Template](https://img.shields.io/badge/Wizard-Template-%23447CAA)](https://github.com/fschuch/wizard-template)
  [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
  [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
  [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  ![GitHub License](https://img.shields.io/github/license/fschuch/wizard-template?color=blue)
  [![EffVer Versioning](https://img.shields.io/badge/version_scheme-EffVer-0097a7)](https://jacobtomlinson.dev/effver)

______________________________________________________________________

## Overview

This is a general-purpose template that aims to provide a magical start to any Python project. It includes the initial configuration of quality assurance tools, documentation, and automated actions to deploy a Python package.

Check out the documentation for more details on how to use the template and its features: <https://docs.fschuch.com/wizard-template>.

## Using This Template

You can use this template in two ways:

### Option 1: Copier (Recommended for new projects)

Use [Copier](https://copier.readthedocs.io/) for interactive project creation with automatic variable substitution:

```bash
# Install copier
pip install copier

# Create a new project (will be available after setup)
copier copy https://github.com/fschuch/wizard-template-copier my-project
```

**Benefits**: Interactive prompts, easy updates, smart conflict resolution

See [Copier Quick Start](docs/copier-quickstart.md) for setup instructions.

### Option 2: GitHub Template

Use GitHub's "Use this template" button to create a new repository, then manually customize:

1. Click "Use this template" on GitHub
2. Create your new repository
3. Clone and run customization script:
   ```bash
   git clone https://github.com/yourusername/your-project
   cd your-project
   python tools/rename_project_content.py
   ```

**Benefits**: Simple GitHub integration, full control

## Features

- 🚀 **Quick Start**: Get a fully configured Python project in minutes
- 🔄 **Template Sync**: Keep your project up-to-date with template improvements
- 📦 **Automated Updates**: Receive dependabot updates for dependencies, GitHub Actions, and pre-commit hooks
- ✅ **Quality Assurance**: Pre-configured linting, type checking, and testing
- 📚 **Documentation**: Automated documentation generation with Jupyter Book
- 🤖 **CI/CD**: GitHub Actions workflows for testing, building, and deployment

## Keeping Your Project Updated

Projects created from this template can stay synchronized with template improvements using the built-in sync tool:

```bash
# Preview available updates
python tools/template-sync.py --dry-run

# Apply template updates
python tools/template-sync.py
```

This allows you to receive:

- 📦 Dependabot updates to dependencies
- 🔧 GitHub Actions workflow improvements  
- 🎯 Pre-commit hook updates
- 🛡️ Security patches

See the [Template Sync Guide](docs/template-sync.md) for detailed instructions.

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/wizard-template/blob/main/LICENSE).
