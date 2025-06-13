# How to use this Template

The Wizard Template for Python Projects provides a robust foundation for building production-ready Python packages. This template comes pre-configured with essential tools for code quality, testing, documentation, and automation, allowing you to focus on your core logic.

## How to Use the Template

1. **Create your project**: Click on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch) on GitHub to generate a new repository from this template.

1. **Clone your repository**:

   ```zsh
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

1. **Install Hatch**: Hatch manages environments and dependencies. Follow the [Hatch installation guide](https://hatch.pypa.io/latest/install/) for your OS. On macOS with Homebrew:

   ```zsh
   brew install hatch
   ```

1. **Configure local environments** (optional):

   ```zsh
   hatch config set dirs.env.virtual .venv
   ```

1. **Install dependencies and run checks**:

   ```zsh
   hatch run qa
   ```

   This will set up virtual environments, install dependencies, and run all quality checks and tests.

## Renaming Your Project

A helper script is included to update the project name and author in all files:

```zsh
hatch run _wizard
```

For more details, see the [README.md](../README.md) and the [Hatch documentation](https://hatch.pypa.io/).
