# CI/CD & Automation

This template includes robust continuous integration and deployment (CI/CD) workflows using GitHub Actions. Automated workflows run on every push and pull request, ensuring code quality and reliability before deployment.

- **check-links.yaml**: Validates links in documentation and code comments.
- **ci.yaml**: Runs tests, linting, type checks, and deploys to PyPI on valid tags.
- **docs.yaml**: Builds and deploys documentation to GitHub Pages.
- **update-pre-commits.yaml**: Weekly job to update pre-commit hooks.
- **dependabot.yml**: Keeps dependencies up-to-date.

You can customize workflows in the `.github/workflows/` directory. For more, see the [GitHub Actions documentation](https://docs.github.com/en/actions).
