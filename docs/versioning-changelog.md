# Versioning & Changelog

This template enables conflict-free versioning and changelog management with git tags, pull request labels and GitHub releases.
To do so, it uses [hatch-vcs](https://github.com/ofek/hatch-vcs) to manage version numbers dynamically from Git tags. Release notes are generated automatically by GitHub when you create a new release. Configure the pull request labels on the file `.github/release.yml`.

For custom versioning, edit the `[tool.hatch.version]` section in `pyproject.toml`. For changelog best practices, see [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). You can also refer to conventions like [Semantic Versioning](https://semver.org/), [CalVer](https://calver.org/), or [EffVer Versioning](https://jacobtomlinson.dev/effver) for guidance on versioning strategies.
