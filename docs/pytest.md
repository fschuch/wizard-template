# pytest

[pytest](https://docs.pytest.org/en/stable/) is a powerful testing framework for Python. It supports unit tests, doctests, and advanced features like fixtures and plugins. In this template, pytest is run with:

```zsh
hatch run test
hatch run test-no-cov
```

## Configuration

Pytest settings are in the `[tool.pytest.ini_options]` section of [pyproject.toml](../pyproject.toml). Doctest integration and coverage are enabled by default.

## Further Reading

- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Doctest module](https://docs.python.org/3/library/doctest.html)
