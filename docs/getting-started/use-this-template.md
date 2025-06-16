# How to use this Template

1. Create your project by clicking on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch) to generate a new repository from this template. Choose a name for your project, and optionally, a description. Ensure to mark the repository as public or private according to your needs.

   ````{note}
   If you are using GitHub, you can also use the [GitHub CLI](https://cli.github.com/) to create a new repository from this template:
   ```bash
   gh repo create <your-repo-name> --template fschuch/wizard-template
   ```
   ````

1. Ensure you have all [Dependencies](../dependencies.md) installed.

1. Clone your repository:

   ```zsh
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

1. Set up Python virtual environments, install dependencies, and run all quality checks and tests to verify you have green lights on your project. All it takes is running:

   ````{tip}
   Optionally, configure Hatch to keep virtual environments within the project folder:
   ```bash
   hatch config set dirs.env.virtual .venv
   ```
   ````

   ```zsh
   hatch run qa
   ```

1. To rename your project, a helper script is included to update the project name and author in all files:

   ```zsh
   hatch run _wizard
   ```

1. Review the previous changes, and ensure everything is correct before proceeding. You can now start developing your project!
