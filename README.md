# The Wizard Template for Python Projects

<p align="center">
<a href="https://github.com/fschuch/wizard-template"><img src="docs/logo.png" alt="Wizard template logo" width="320"></a>
</p>
<p align="center">
    <em>Let the wizard do the heavy lifting so you can focus on your craft</em>
</p>

<p align="center">

|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CI/CD | [![CI](https://github.com/fschuch/wizard-template/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/fschuch/wizard-template/actions/workflows/ci.yaml) [![Docs](https://github.com/fschuch/wizard-template/actions/workflows/docs.yaml/badge.svg?branch=main)](https://docs.fschuch.com/wizard-template) [![CodeQL](https://github.com/fschuch/wizard-template/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/fschuch/wizard-template/actions/workflows/github-code-scanning/codeql)                                                                                                                                                                                |
| Meta  | [![Wizard Template](https://img.shields.io/badge/Wizard-Template-%23447CAA)](https://github.com/fschuch/wizard-template) [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/) [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) ![GitHub License](https://img.shields.io/github/license/fschuch/wizard-template?color=blue) [![EffVer Versioning](https://img.shields.io/badge/version_scheme-EffVer-0097a7)](https://jacobtomlinson.dev/effver) |

</p>

## Overview

This is a general-purpose template that aims to provide a magical start to any Python project. It includes the initial configuration of quality assurance tools, documentation, and automated actions to deploy a Python package.

The template is powered by [Hatch](https://hatch.pypa.io), which manages Python installations, virtual environments, dependencies, besides builds,
and deploys the project to [PyPI](https://pypi.org). See [Why Hatch?](https://hatch.pypa.io/latest/why/) for more details.
To ensure code quality, several tools are suggested and pre-configured:

- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
- [ruff](https://github.com/astral-sh/ruff) as the linter and code formatter
- [codespell](https://github.com/codespell-project/codespell) to check spelling
- [pytest](https://docs.pytest.org/en/7.4.x/) as the test engine

In addition, [Git hooks](https://pre-commit.com/) can be used to guarantee consistency and leverage the aforementioned tools. The workflow [ci.yaml](.github/workflows/ci.yaml) runs them automatically for you.

The documentation is initialized with [Jupyter Books](https://jupyterbook.org/en/stable/intro.html), providing a promising approach for interactive tutorials.

You can check at any time the environments and scripts that are prepared to support your development workflow:

```plain
$ hatch env show --ascii
                                          Standalone
+---------+---------+------------------+----------------------+------------------------------+
| Name    | Type    | Dependencies     | Scripts              | Description                  |
+=========+=========+==================+======================+==============================+
| default | virtual | coverage[toml]   | check                | Base development environment |
|         |         | pre-commit       | format               |                              |
|         |         | pytest           | lint                 |                              |
|         |         | pytest-cov       | pre-commit-install   |                              |
|         |         |                  | pre-commit-uninstall |                              |
|         |         |                  | qa                   |                              |
|         |         |                  | test                 |                              |
|         |         |                  | test-no-cov          |                              |
|         |         |                  | type                 |                              |
+---------+---------+------------------+----------------------+------------------------------+
| docs    | virtual | docutils         | build                | Documentation environment    |
|         |         | jupyter-book     | config               |                              |
|         |         | sphinx-autobuild | serve                |                              |
+---------+---------+------------------+----------------------+------------------------------+
                                                 Matrices
+------+---------+-------------+----------------------+----------------------+---------------------------+
| Name | Type    | Envs        | Dependencies         | Scripts              | Description               |
+======+=========+=============+======================+======================+===========================+
| test | virtual | test.py3.8  | coverage[toml]       | check                | Extended test environment |
|      |         | test.py3.9  | pre-commit           | extended             |                           |
|      |         | test.py3.10 | pytest               | format               |                           |
|      |         | test.py3.11 | pytest-cov           | lint                 |                           |
|      |         | test.py3.12 | pytest-randomly      | pre-commit-install   |                           |
|      |         |             | pytest-rerunfailures | pre-commit-uninstall |                           |
|      |         |             | pytest-xdist         | qa                   |                           |
|      |         |             |                      | test                 |                           |
|      |         |             |                      | test-no-cov          |                           |
|      |         |             |                      | type                 |                           |
+------+---------+-------------+----------------------+----------------------+---------------------------+
```

## Quick Start

### Use the template as a start point for your own project

1. Click on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch), creating a new project for you from it.

1. If you don't have Hatch, [download and install it](https://hatch.pypa.io/latest/install/) following the instructions for your OS.

   - I like to keep the Python environments within the project I'm working on, Hatch can be set to do so:

     ```bash
     hatch config set dirs.env.virtual .venv
     ```

1. Clone your repository and make it your working directory.

1. Assert that everything is up and running:

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
   ruff.....................................................................Passed
   ruff-format..............................................................Passed
   mypy.....................................................................Passed
   codespell................................................................Passed
   mdformat.................................................................Passed
   nbstripout...............................................................Passed
   cmd [2] | pytest --cov
   ================================ test session starts ================================
   platform darwin -- Python 3.12.2, pytest-8.0.2, pluggy-1.4.0
   rootdir: /Users/fschuch/Documents/GitHub/wizard-template
   configfile: pyproject.toml
   plugins: cov-4.1.0
   collected 7 items

   tests/test_core.py ......                                                     [ 85%]
   wizard_template/core.py .                                                     [100%]

   ---------- coverage: platform darwin, python 3.12.2-final-0 -------------
   Name                          Stmts   Miss Branch BrPart  Cover   Missing
   -------------------------------------------------------------------------

   tests/__init__.py                 0      0      0      0   100%
   tests/test_core.py               10      0      6      0   100%
   wizard_template/__init__.py       2      0      0      0   100%
   wizard_template/core.py           8      0      2      0   100%
   -------------------------------------------------------------------------

   TOTAL                            20      0      8      0   100%

   Required test coverage of 90.0% reached. Total coverage: 100.00%

   ================================= 7 passed in 0.11s =================================
   cmd [3] | echo '✅ QA passed'
   ✅ QA passed
   ```

   - On first invocation on the project folder, Hatch creates the virtual environments, install the dependencies, and gets ready to go.

1. A helper script is included to rename the git username and project name from the template files to your own new project, try it with:

   ```bash
   hatch run _wizard
   ```

1. Run `hatch run qa` another time to assert everything is still all right. You can now review the changes, stage, and commit them on your repo.

### Dependencies

1. The template is designed to work with Python 3.8 and later versions. It is recommended to use the latest stable version of Python.

1. Project dependencies are managed on the file [pyproject.toml](pyproject.toml), refer to
   [Dependency configuration](https://hatch.pypa.io/latest/config/dependency/) for more details on the topic.

1. Hatch specific configuration covering the development dependencies, environments, and maintenance scripts are defined also on the file [pyproject.toml](pyproject.toml). You can refer to [Environment configuration](https://hatch.pypa.io/latest/config/environment/) for more details.

1. To ensure quality standards on the codebase, [pre-commit](https://pre-commit.com) manages and runs the hooks configured on [.pre-commit-config.yaml](.pre-commit-config.yaml).

   - `pre-commit` handles the installation of ruff, mypy, codespell, and others, on an isolated environments.
   - It is a good pick since many of the fixes can be done automatically at commit time just on the changed files.
   - These tools are not declared as development dependencies on the project to avoid duplication.
   - The action [update-pre-commits.yaml](.github/workflows/update-pre-commits.yaml) scheduled to run weekly to ensure
     the hooks are up-to-date.

### Enforcing Code Quality

1. As mentioned above, the [pre-commit](https://pre-commit.com) tool is used to enforce code quality standards.
   Even though it performs checks on the changes for every commit when installed (`hatch run pre-commit-install`),
   it is a good practice to run the checks on the whole codebase occasionally (when a new hook is added or on Pull
   Requests). You can do so by running `hatch run check <hook-id>`, for instance `hatch run check nbstripout`.
   Some of them are available as scripts as a syntax sugar, like `hatch run lint`,
   `hatch run format`, or `hatch run type`. They check the whole codebase using ruff, ruff-format, and mypy, respectively.

   - The file [project.toml](pyproject.toml) includes configuration for some of the tools, so they can be consumed from your IDE as well.
   - The file [.pre-commit-config.yaml](.pre-commit-config.yaml) includes the configuration for the pre-commit hooks.

1. The [pytest](https://docs.pytest.org/en/7.4.x/) test suite can be run from the default environment with `hatch run test`
   or `hatch run test-no-cov` (the latter without coverage check).

   Code examples on docstrings and documentation are tested by the `doctest` module (configured on the file [pyproject.toml](pyproject.toml)).
   It is integrated with pytest, so the previous test commands will also run the doctests.

1. To run all the quality checks, you can use the command `hatch run qa`.

1. To step up in the game, an extended test environment and the command `hatch run test:extended` are available to
   verify the package on different Python versions and under different conditions thanks to the pytest plugins:

   - `pytest-randomly` that randomizes the test order;
   - `pytest-rerunfailures` that re-runs tests to eliminate intermittent failures;
   - `pytest-xdist` that parallelizes the test suite and reduce runtime, to help the previous points that increase the workload;
   - The file [pyproject.toml](pyproject.toml) includes configuration for them.

#### Continuous Integration

- The workflow [ci.yaml](.github/workflows/ci.yaml) performs the verifications on every push and pull request, and deploys the package if running from a valid tag.
- The workflow [update-pre-commits.yaml](.github/workflows/update-pre-commits.yaml) is scheduled to run weekly to ensure the pre-commit hooks are up-to-date.
- Dependabot is enabled to keep the dependencies up-to-date ([dependabot.yml](.github/dependabot.yml)).

### Managing the Changelog

The template relies on [Automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) from GitHub to handle the changelog.
Refer to [Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) and add the labels from [release.yml](.github/release.yml) to automatically organize your entries. This is a nice fit for [Managing releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

Some may argue about the importance of [Keeping a Changelog](https://keepachangelog.com/en/1.0.0/) on a dedicated file, but that results in frequent conflicts and merge issues to be solved when working with feature branches in parallel. The GitHub release notes are a good compromise, as they are automatically generated and can be edited before the release. Notice good Pull Request titles and small incremental changes are key to a good changelog.

### Managing the Version Number

The version in the project is set dynamically by [hatch-vcs](https://github.com/ofek/hatch-vcs).
At installation and build time, the version is recovered from the version control system and exported to the file `wizard_template/_version.py`.
In this way, there is no need to keep the version hard-coded on the codebase. You can use the command `hatch version` to check the current version.
On the deployment workflow, the version is recovered from the tag and used to build the package.

The downside is that the new version number must be manually entered for each release, rather than using the command `hatch version` to bump it up.
However, this is a reasonable trade-off, since it does not impose any restrictions on the project's versioning scheme nor branching model.

### Documentation

The template includes a documentation environment that uses [Jupyter Books](https://jupyterbook.org/en/stable/intro.html)
to provide a promising approach for interactive tutorials. The documentation source is on the `docs` folder and can be
served locally with `hatch run docs:serve`, it will be available on <http://127.0.0.1:8000>.
The documentation is also built automatically on the deployment workflow [docs.yaml](.github/workflows/docs.yaml).

- Modules and functions docstrings are used to generate the documentation thanks to the [sphinx-autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [sphinx-napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) packages.

- Follow the instructions in [Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to set up a publishing source for your GitHub Pages site. When using the automated workflow, the files will be located at the root (`/`) on the `gh-pages` branch. You will need the secret `TOKEN` with your [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to make it work.

### Publishing

The package can be published to PyPI in a general-purpose workflow that can be used for any branch model and versioning strategy.

The action [ci.yaml](.github/workflows/ci.yaml) is triggered to publish the package to PyPi when any valid tag is pushed to the repository. The tag matching pattern is set to `v*.*.*`, for instance, `1.2.3`, `0.0.1rc2`, `2023.2.0`, etc. Notice all previous steps on CI are executed before the deployment, including static analysis and tests.

- Refer to [Adding a trusted publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) to integrate the package with the PyPI project.

The process can also be triggered when a Release creates a new tag on your repo, so it sinergizes with the GitHub release notes cited above on the Changelog management.

### Miscellaneous

#### VSCode Configuration

The template includes a `.vscode` folder with a `extensions.json` file that suggests the extensions to be installed on VSCode, in line with the quality assurance tools included in the template. It allows test, debug, auto-format, lint, and a few other functionalities to work directly on your IDE. It also includes a `settings.json` file that configures the Python extension to use the virtual environment created by Hatch. Remember to set hatch to use the virtual environment within the project folder `hatch config set dirs.env.virtual .venv`.

#### Communicate Type Annotations

[PEP 561](https://www.python.org/dev/peps/pep-0561/) is a guideline that explains how a Python package can show that it has inline type annotations.
These annotations are useful for static type checkers, which are tools that help ensure your code has been error-free. [Mypy](https://mypy.readthedocs.io/en/stable/installed_packages.html) checks for a file named `py.typed` in the root of the installed package.

## Next steps

- You can now customize the codebase to best suit your project.
- Take a look on the classifiers to set on the [pyproject.toml](pyproject.toml) file:
  - <https://pypi.org/classifiers/>
  - <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml>
- Don't forget to review the [LICENSE](./LICENSE) file on your repository to let others know how they can legally use your project.
- It is highly recommended that you set up [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).
- Refer to [Configuring issue templates for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#configuring-the-template-chooser) to configure issue templates for your repository.
- Keep an eye on [Status of Python versions](https://devguide.python.org/versions/#status-of-python-versions) to know when
  it is time to drop support for some of them. [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) is
  also a good reference for the topic.
- You can use CodeQL to identify vulnerabilities and errors in your code. Refer to [About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/) to learn more about it.

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/wizard-template/blob/main/LICENSE).
