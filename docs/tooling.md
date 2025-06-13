# Tooling & Quality Assurance

This template is designed with production-readiness in mind, integrating a suite of tools to enforce code quality, consistency, and reliability. Each tool is pre-configured in the project and can be customized as needed.

## Why Quality Assurance?

Automated quality assurance (QA) ensures that your codebase remains clean, maintainable, and free of common errors. By leveraging static analysis, linting, type checking, and automated testing, you reduce the risk of bugs and technical debt.

## Included Tools

- **Hatch**: Environment and dependency management ([pyproject.toml](../pyproject.toml))
- **mypy**: Static type checking
- **ruff**: Linting and formatting
- **codespell**: Spell checking
- **pytest**: Testing framework
- **pre-commit**: Git hooks for automated checks
- **zizmor**: Static analysis for GitHub Actions workflows
- **coverage**: Test coverage reporting
- **dependabot**: Automated dependency updates

For more details, see each tool's dedicated page and the [pyproject.toml](../pyproject.toml) configuration. For further reading, see the [Python Packaging Guide](https://packaging.python.org/) and [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/).
