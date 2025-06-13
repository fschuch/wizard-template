# Zizmor

[zizmor](https://github.com/woodruffw/zizmor) is a static analysis tool for GitHub Actions workflows. It helps catch misconfigurations and potential issues in your CI/CD pipelines. This template runs zizmor as part of the QA process and via pre-commit hooks.

## Alternatives

Other tools for analyzing GitHub Actions workflows include:

- [actionlint](https://github.com/rhysd/actionlint): Linter for GitHub Actions workflow files.
- [Yamllint](https://yamllint.readthedocs.io/): General-purpose YAML linter, can be used for workflow files.

## Configuration

Zizmor is configured in `.pre-commit-config.yaml`. You can add custom rules or adjust its behavior as needed.

## Further Reading

- [zizmor documentation](https://github.com/woodruffw/zizmor)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
