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

### For AI Assistants

This template includes an [Agent Skill](.agents/skills/python-wizard-template/) that teaches AI assistants (like GitHub Copilot) how to work effectively with wizard-template projects. The skill provides comprehensive guidance for:

- **New projects**: Starting fresh from the template
- **Migration**: Applying template structure to existing projects
- **Updates**: Incorporating template changes into your project
- **Best practices**: Following wizard-template conventions

AI assistants will automatically use this skill when working in repositories created from this template. You can also [install it at user-level](.agents/skills/python-wizard-template/README.md#installation-options) to use across all your projects.

Additionally, [`.github/copilot-instructions.md`](.github/copilot-instructions.md) provides quick reference context for everyday development tasks.

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/wizard-template/blob/main/LICENSE).
