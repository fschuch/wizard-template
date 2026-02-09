# Migration to Jupyter Book 2.x

This document describes the migration from Jupyter Book 1.x (Sphinx-based) to Jupyter Book 2.x (MyST-based).

## What Changed

### Architecture
- **Jupyter Book 1.x**: Built on Sphinx (Python-based document engine)
- **Jupyter Book 2.x**: Built on MyST Document Engine (JavaScript/TypeScript-based)

### Configuration Files
- `_config.yml` and `_toc.yml` → consolidated into `myst.yml`
- Old configuration files backed up as `._config.yml.bak` and `._toc.yml.bak`

### Build Commands
- **Before**: `jupyter-book config sphinx docs && jupyter-book build docs`
- **After**: `jupyter-book build docs`

### Removed Features

The following Sphinx-specific features are no longer available in Jupyter Book 2.x:

1. **sphinx-github-changelog extension**: The automated changelog generation from GitHub releases is not supported. Users should refer to [GitHub Releases](https://github.com/fschuch/wizard-template/releases/) directly.

2. **Sphinx autodoc**: Automatic API documentation generation from Python docstrings is not available. The API reference has been simplified to point users to the source code.

3. **Bibliography support (.bib files)**: The `references.bib` file is no longer processed by the build system.

4. **Custom Sphinx directives**: Some directives like `:link-type:`, `:class-header:`, `:class-container:`, and `:gutter:` options in grids have been removed as they're not supported in MyST.

5. **RST files**: All reStructuredText (.rst) files have been converted to Markdown (.md) format.

### What Still Works

- MyST Markdown syntax (CommonMark + extensions)
- Jupyter notebooks
- Cross-references
- Grid layouts (with simplified options)
- All other MyST-supported directives and roles

## Benefits of the Migration

1. **Modern Architecture**: Built on modern JavaScript/TypeScript tooling
2. **Better Performance**: Faster builds with incremental compilation
3. **Improved Web Experience**: Better interactive features and responsive design
4. **Unified Configuration**: Single `myst.yml` file instead of multiple config files
5. **Active Development**: Jupyter Book 2.x is the actively maintained version

## Known Limitations

- No Sphinx extension support (including custom plugins)
- Bibliography/citations require different approach
- API documentation needs manual maintenance or alternative tools
- Some advanced Sphinx features not yet available in MyST

## Further Reading

- [Jupyter Book 2.x Documentation](https://jupyterbook.org/stable/)
- [MyST Markdown Guide](https://mystmd.org/guide)
- [Upgrade Guide](https://jupyterbook.org/stable/resources/upgrade/)
