# pre-commit

[pre-commit](https://pre-commit.com/) automates code quality checks by running hooks before each commit. This ensures that code style, linting, and other checks are enforced consistently. The template includes a `.pre-commit-config.yaml` file with hooks for ruff, mypy, codespell, and more.

## Alternatives

Other tools for managing Git hooks and code quality automation include:

- [lefthook](https://evilmartians.com/chronicles/lefthook-fast-and-flexible-git-hooks-manager): Fast and flexible Git hooks manager.
- [husky](https://typicode.github.io/husky/): Popular in JavaScript/TypeScript, but can be used for Python projects too.
- Custom shell scripts in `.git/hooks/`.

## Usage

Install hooks with:

```zsh
hatch run pre-commit-install
```

Run all hooks manually:

```zsh
hatch run qa
```

## Customization

Edit `.pre-commit-config.yaml` to add, remove, or configure hooks. See the [pre-commit documentation](https://pre-commit.com/) for more details.
