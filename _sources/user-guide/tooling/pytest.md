# pytest

[pytest](https://docs.pytest.org/en/stable/) is a powerful testing framework for Python. It supports unit tests, doctests, and advanced features like fixtures and plugins. In this template, pytest is run with:

```zsh
hatch run test
hatch run test-no-cov
```

## Configuration

Pytest settings are in the `[tool.pytest.ini_options]` section of `pyproject.toml`\].
Doctest integration and coverage are enabled by default.

## Extended Testing

To step up in the game, an extended test environment and the command `hatch run test:extended` are available to
verify the package on different Python versions and under different conditions thanks to the pytest plugins:

- `pytest-randomly` that randomizes the test order;
- `pytest-rerunfailures` that re-runs tests to eliminate intermittent failures;
- `pytest-xdist` that parallelizes the test suite and reduce runtime, to help the previous points that increase the workload;
- The file `pyproject.toml`includes configuration for them.

## Further Reading

- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Doctest module](https://docs.python.org/3/library/doctest.html)

## Alternatives

Other Python testing frameworks include:

- [unittest](https://docs.python.org/3/library/unittest.html): Built-in Python testing framework.
- [nose2](https://docs.nose2.io/): Successor to nose, compatible with unittest.
- [doctest](https://docs.python.org/3/library/doctest.html): Test code examples in docstrings.
