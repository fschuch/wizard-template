# Versioning & Changelog

This template enables commitless releases since versioning and changelog are managed with git tags, pull request labels and GitHub releases.
To do so, it uses [hatch-vcs](https://github.com/ofek/hatch-vcs) to manage version numbers dynamically from Git tags.
Release notes are generated automatically by GitHub when you create a new release, configure the pull request labels on the file `.github/release.yml`.
They are ported to a documentation page thanks to [sphinx-github-changelog](https://github.com/ewjoachim/sphinx-github-changelog).

For custom versioning, edit the `[tool.hatch.version]` section in `pyproject.toml`. For changelog best practices, see [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). You can also refer to conventions like [Semantic Versioning](https://semver.org/), [CalVer](https://calver.org/), or [EffVer Versioning](https://jacobtomlinson.dev/effver) for guidance on versioning strategies.
