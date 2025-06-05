# Versioning & Changelog

This template uses [hatch-vcs](https://github.com/ofek/hatch-vcs) to manage version numbers dynamically from Git tags. Release notes are generated automatically by GitHub when you create a new release.

- Version is set from the latest tag (e.g., `v1.2.3`)
- No hard-coded version in the codebase
- Changelog is managed via GitHub Releases

For custom versioning, edit the `[tool.hatch.version]` section in [pyproject.toml](../pyproject.toml). For changelog best practices, see [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
