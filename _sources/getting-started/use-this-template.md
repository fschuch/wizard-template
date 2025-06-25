# How to use this Template

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
