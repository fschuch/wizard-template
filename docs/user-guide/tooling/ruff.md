# Ruff

[Ruff](https://docs.astral.sh/ruff/) is a fast Python linter and code formatter. It enforces code style, catches common errors, and can automatically fix many issues. In this template, Ruff is run via pre-commit hooks and as a script:

```zsh
hatch run lint
hatch run format
```

## Configuration

Ruff settings are in the `[tool.ruff]` section of `pyproject.toml`. Adjust rules, exclusions, and formatting options as needed.

## Further Reading

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- Hatch curates a handy baseline for ruff configuration, which you can find in the [ruff_defaults.toml](https://github.com/pypa/hatch/blob/master/ruff_defaults.toml) file.

## Alternatives

Other popular Python linters and formatters include:

- [Flake8](https://flake8.pycqa.org/): Classic linter with plugin support.
- [pylint](https://pylint.pycqa.org/): Highly configurable linter with code analysis.
- [Black](https://black.readthedocs.io/): Opinionated code formatter.
- [isort](https://pycqa.github.io/isort/): Sorts Python imports automatically.
