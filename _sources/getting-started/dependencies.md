# Dependencies

## Python

This template is designed to work with Python 3.10 or later. Ensure you have the correct version installed on your system.

```{important} Keep an eye on the [Python Developer's Guide: Supported Versions](https://devguide.python.org/versions/#status-of-python-versions) to know which versions are actively supported, adapt your project accordingly, and plan for future upgrades.
```

## Hatch

The template is powered by [Hatch](https://hatch.pypa.io), a modern Python project manager that handles Python installations, virtual environments and dependencies, maintenance tasks, besides building,
and deploying the project to [PyPI](https://pypi.org). See [Why Hatch?](https://hatch.pypa.io/latest/why/) for more details and [Hatch Installation](https://hatch.pypa.io/latest/install/) for installation instructions on your system.

Edit the `[tool.hatch]` and `[tool.hatch.envs]` sections in `pyproject.toml` to add or modify environments and scripts. See the [Hatch documentation](https://hatch.pypa.io/latest/) for advanced usage.

At you project, you can run `hatch env show` at anytime to verify the environments, their features and scripts.

## Alternatives

Other popular Python project and environment managers include:

- [uv](https://docs.astral.sh/uv/): An extremely fast Python package and project manager, written in Rust.
- [Poetry](https://python-poetry.org/): Dependency management and packaging with a simple CLI.
- [Pixi](https://pixi.sh/latest/): Pixi is a fast, modern, and reproducible package management tool for developers of all backgrounds.

For alternatives task runners, consider:

- [Make](https://www.gnu.org/software/make/): A classic build automation tool.
- [Mise](https://mise.jdx.dev) The front-end to your dev env.
- [taskpy](https://github.com/taskipy/taskipy): The complementary task runner for python.
