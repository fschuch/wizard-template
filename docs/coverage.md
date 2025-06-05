# Coverage

Test coverage tools measure how much of your code is exercised by tests. This template uses `coverage.py` (integrated via pytest-cov) to ensure your code is well-tested. Run with:

```zsh
hatch run test
```

Coverage settings are in the `[tool.coverage]` section of [pyproject.toml](../pyproject.toml). Adjust thresholds and reporting as needed.

## Further Reading

- [coverage.py documentation](https://coverage.readthedocs.io/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
