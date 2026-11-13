# How to use this Template

## Option 1: Using Dev Container (Recommended)

The easiest way to get started is using the VS Code dev container:

1. Create your project by clicking on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch) to generate a new repository from this template.

1. Clone your repository:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

1. Open the project in VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.

1. Click "Reopen in Container" when prompted (or use Command Palette: "Dev Containers: Reopen in Container").

1. Wait for the container to build and the post-create script to complete. This will:
   - Install Hatch
   - Install Python versions 3.10, 3.11, 3.12, 3.13, and 3.14
   - Install pre-commit hooks
   - Configure the development environment

1. Run the renaming script to customize your project:

   ```bash
   hatch run _wizard
   ```

1. Verify everything is working:

   ```bash
   hatch run qa
   ```

See [`.devcontainer/README.md`](https://github.com/fschuch/wizard-template/blob/main/.devcontainer/README.md) for more details about the dev container configuration.

## Option 2: Manual Setup

1. Create your project by clicking on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch) to generate a new repository from this template. Choose a name for your project, and optionally, a description. Ensure to mark the repository as public or private according to your needs.

   ````{note}
   If you are using GitHub, you can also use the [GitHub CLI](https://cli.github.com/) to create a new repository from this template:
   ```bash
   gh repo create <your-repo-name> --template fschuch/wizard-template
   ```
   ````

1. Ensure you have all [Dependencies](dependencies.md) installed.

1. Clone your repository:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

   ````{tip}
   Optionally, configure Hatch to keep virtual environments within the project folder:
   ```bash
   hatch config set dirs.env.virtual .venv
   ```
   ````

1. Set up Python virtual environments, install dependencies, and run all quality checks and tests to verify you have green lights on your project. All it takes is running:

   ```bash
   $ hatch run qa
   cmd [1] | pre-commit run  --all-files
   check for added large files..............................................Passed
   check for case conflicts.................................................Passed
   check docstring is first.................................................Passed
   check json...............................................................Passed
   check for merge conflicts................................................Passed
   check toml...............................................................Passed
   check yaml...............................................................Passed
   debug statements (python)................................................Passed
   detect private key.......................................................Passed
   fix end of files.........................................................Passed
   mixed line ending........................................................Passed
   trim trailing whitespace.................................................Passed
   ruff (legacy alias)......................................................Passed
   ruff format..............................................................Passed
   mypy.....................................................................Passed
   codespell................................................................Passed
   mdformat.................................................................Passed
   nbstripout...........................................(no files to check)Skipped
   zizmor...................................................................Passed
   cmd [2] | pytest --cov --cov-report=term
   ============================= test session starts =============================
   platform darwin -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0
   configfile: pyproject.toml
   plugins: cov-6.2.1
   collected 8 items

   src/wizard_template/core.py .                                           [ 12%]
   tests/test_core.py ......                                               [ 87%]
   tools/rename_project_content.py s                                       [100%]

   =============================== tests coverage ================================

   Name                              Stmts   Miss Branch BrPart    Cover   Missing
   -------------------------------------------------------------------------------
   src/wizard_template/__init__.py       2      0      0      0  100.00%
   src/wizard_template/core.py           8      0      2      0  100.00%
   tests/__init__.py                     0      0      0      0  100.00%
   tests/test_core.py                   10      0      0      0  100.00%
   -------------------------------------------------------------------------------
   TOTAL                                20      0      2      0  100.00%
   Required test coverage of 90.0% reached. Total coverage: 100.00%
   ======================== 7 passed, 1 skipped in 0.05s =========================
   cmd [3] | echo '✅ QA passed'
   ✅ QA passed
   ```

1. To rename your project, a helper script is included to update the project name and author in all files:

   ```bash
   hatch run _wizard
   ```

1. Review the previous changes, and ensure everything is correct before proceeding. You can now start developing your project!
