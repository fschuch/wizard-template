# Zizmor

[zizmor](https://github.com/woodruffw/zizmor) is a static analysis tool for GitHub Actions workflows. It helps catch misconfigurations and potential issues in your CI/CD pipelines. This template runs zizmor as part of the QA process and via pre-commit hooks:

```bash
hatch run check zizmor
```

## Configuration

Zizmor is configured in `.pre-commit-config.yaml`. You can add custom rules or adjust its behavior as needed.

## Further Reading

- [zizmor documentation](https://github.com/woodruffw/zizmor)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
