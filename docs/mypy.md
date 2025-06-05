# mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is a static type checker for Python. It helps catch type errors before runtime, improving code safety and maintainability. This template configures mypy as part of the QA process, and you can run it with:

```zsh
hatch run type
```

## Configuration

Mypy settings are defined in the `[tool.mypy]` section of [pyproject.toml](../pyproject.toml). You can customize strictness, ignored files, and more.

## Further Reading

- [mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [PEP 484 – Type hints](https://peps.python.org/pep-0484/)
