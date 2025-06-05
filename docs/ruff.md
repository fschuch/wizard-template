# Ruff

[Ruff](https://docs.astral.sh/ruff/) is a fast Python linter and code formatter. It enforces code style, catches common errors, and can automatically fix many issues. In this template, Ruff is run via pre-commit hooks and as a script:

```zsh
hatch run lint
hatch run format
```

## Configuration

Ruff settings are in the `[tool.ruff]` section of [pyproject.toml](../pyproject.toml). Adjust rules, exclusions, and formatting options as needed.

## Further Reading

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
