# Hatch

Hatch is a modern Python project manager that handles environments, dependencies, builds, and publishing. In this template, Hatch is configured via `pyproject.toml` to manage development and documentation environments, as well as scripts for testing, linting, and more.

## Key Features

- Isolated virtual environments per project
- Easy dependency management
- Build and publish workflows
- Script runner for common tasks (see `hatch run <script>`)

## Alternatives

Other popular Python project and environment managers include:

- [uv](https://docs.astral.sh/uv/): An extremely fast Python package and project manager, written in Rust.
- [Poetry](https://python-poetry.org/): Dependency management and packaging with a simple CLI.
- [Pixi](https://pixi.sh/latest/): Pixi is a fast, modern, and reproducible package management tool for developers of all backgrounds.

For alternatives task runners, consider:

- [Make](https://www.gnu.org/software/make/): A classic build automation tool.
- [Mise](https://mise.jdx.dev) The front-end to your dev env.
- [taskpy](https://github.com/taskipy/taskipy): The complementary task runner for python.

## Customization

Edit the `[tool.hatch]` and `[tool.hatch.envs]` sections in `pyproject.toml` to add or modify environments and scripts. See the [Hatch documentation](https://hatch.pypa.io/latest/) for advanced usage.
