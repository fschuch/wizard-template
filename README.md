# The Wizard Template for Python Projects

<p align="center">
<a href="https://github.com/fschuch/wizard-template"><img src="docs/logo.png" alt=Wizard template logo" width="320"></a>
</p>
<p align="center">
    <em>Let the wizard do the heavy lifting so you can focus on your craft</em>
</p>

----

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/fschuch/wizard-template/actions/workflows/test-package.yaml/badge.svg)](https://github.com/fschuch/wizard-template/actions/workflows/test-package.yaml)

This is a general-purpose template that aims to provide a magical start to any Python project.
It includes the initial configuration of quality assurance tools, documentation, and automated actions.

The template is powered by [Poetry](https://python-poetry.org/), which manages dependencies, builds, and publishes the package every time a new [release is created on GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), thanks to the [publish-package](https://github.com/fschuch/wizard-template/blob/main/.github/workflows/publish-package.yaml) workflow. The release process is simplified since the current version is recovered automatically at building time by using [poetry-version-plugin](https://github.com/tiangolo/poetry-version-plugin/blob/main/pyproject.toml) and GitHub can generate the release notes automatically based on labels on each Pull Request ([release.yml](.github/release.yml)).

This approach ensures that releases do not modify the main branch, eliminating the need to resolve merge conflicts on feature branches constantly. The downside is that the new version number must be manually entered for each release, rather than using the command `poetry version`. However, this is a reasonable trade-off, since it does not impose any restrictions on the project's versioning scheme or branching model.

To ensure code quality, several tools are suggested and pre-configured:

- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
- [ruff](https://github.com/astral-sh/ruff) as the linter and code formatter
- [codespell](https://github.com/codespell-project/codespell) to check spelling
- [pytest](https://docs.pytest.org/en/7.4.x/) as the test engine

In addition, [Git hooks](https://pre-commit.com/) can be used to guarantee consistency and leverage the aforementioned tools. The workflow [test-package.yaml](.github/workflows/test-package.yaml) runs them automatically for you.

The documentation is initialized with [Jupyter Books](https://jupyterbook.org/en/stable/intro.html), providing a promising approach for interactive tutorials.

## Quick Start

1. Click on [Use this template](https://github.com/new?template_name=wizard-template&template_owner=fschuch), creating a new project for you from it.
2. If you don't have poetry, [download and install Poetry](https://python-poetry.org/docs/#installation) following the instructions for your OS.
3. Clone your repository and make it your working directory.
4. To install the project, its development dependencies, and the pre-commit hooks, just run:

    ```bash
    poetry install
    poetry shell
    ```

5. The regular maintenance tasks are handled by [taskipy](https://github.com/taskipy/taskipy/tree/master).
You can see the available tasks by running:

    ```plain
    $ task --list
    pre_commit_install pre-commit install
    test               pytest
    pre_lint           task pre_commit_install
    lint               pre-commit run --all-files
    qa                 task lint && task test
    pre_docs           poetry install --with docs
    docs               jupyter-book build docs --path-output build
    pre_docs_serve     task pre_docs
    docs_serve         sphinx-autobuild docs build/_build/html
    wizard             python ./scripts/rename_project_content.py
    ```

    Type `task <task_name>` to run a task. For example, to run the tests, try `task test`.

6. Assert that everything is up and running:

    ```bash
    task qa
    ```

7. A helper script is included to rename the git username and project name from the template to your new project, try it with:

    ```bash
    task wizard
    ```

8. You can now review the changes, stage, and commit them on your repo. Run `task qa` another time to assert everything is still all right.

## Next steps

- You can now customize the codebase to best suit your project.
- Don't forget to review the [LICENSE](./LICENSE) file on your repository to let others know how they can legally use your project.
- Obtain a [Test PyPI token](https://test.pypi.org) and/or [PyPI token](https://pypi.org) (note that they are not the same) and add them as secrets to your repository (`TEST_PYPI_TOKEN` and `PYPI_TOKEN`, respectively) so that the deployment workflow will function.
- Refer to [Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) and add the labels from [release.yml](.github/release.yml) to automatically organize your change logs.
- It is highly recommended that you set up [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).
- Follow the instructions in [Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to set up a publishing source for your GitHub Pages site. When using the automated workflow, the files will be located at the root (`/`) on the `gh-pages` branch. You will need the secret `TOKEN` with your [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to make it work.
- Refer to [Configuring issue templates for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#configuring-the-template-chooser) to configure issue templates for your repository.
- You can use CodeQL to identify vulnerabilities and errors in your code. Refer to [About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/) to learn more about it.

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/wizard-template/blob/main/LICENSE).
