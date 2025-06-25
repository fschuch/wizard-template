# pre-commit

[pre-commit](https://pre-commit.com/) automates code quality checks by running hooks before each commit.
It handles the installation of ruff, mypy, codespell, and others, on an isolated environments.
It is a good pick since many of the fixes can be done automatically at commit time just on the changed files.
These tools are not declared as development dependencies on the project to avoid duplication.
The action `update-pre-commits.yaml` scheduled to run weekly to ensure the hooks are up-to-date.

## Usage

Install hooks is you like to run them on every commit:

```zsh
hatch run pre-commit-install
```

Run all hooks manually when needed:

```zsh
hatch run check
```

You can select them individually by `hatch run check <hook-id>`, for instance `hatch run check nbstripout`.
Some of them are available as scripts as a syntax sugar, like `hatch run lint`,
`hatch run format`, or `hatch run type`. They check the whole codebase using ruff, ruff-format, and mypy, respectively.

## Customization

The file `project.toml` includes configuration for some of the tools, so they can be consumed by your IDE as well.
The file `.pre-commit-config.yaml` includes the configuration for the pre-commit hooks.
