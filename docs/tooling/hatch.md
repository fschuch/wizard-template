# Hatch

Hatch is a modern Python project manager that handles environments, dependencies, builds, and publishing. In this template, Hatch is configured via [pyproject.toml](../pyproject.toml) to manage development and documentation environments, as well as scripts for testing, linting, and more.

## Key Features

- Isolated virtual environments per project
- Easy dependency management
- Build and publish workflows
- Script runner for common tasks (see `hatch run <script>`)

## Alternatives

Other popular Python project and environment managers include:

- [Poetry](https://python-poetry.org/): Dependency management and packaging with a simple CLI.
- [Pipenv](https://pipenv.pypa.io/): Combines pip and virtualenv for dependency management.
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/): Enhances virtualenv with additional commands.

## Customization

Edit the `[tool.hatch]` and `[tool.hatch.envs]` sections in `pyproject.toml` to add or modify environments and scripts. See the [Hatch documentation](https://hatch.pypa.io/latest/) for advanced usage.
