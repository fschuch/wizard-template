"""Version information for the wizard_template package.

References
----------
- https://packaging.python.org/guides/single-sourcing-package-version
- https://github.com/python-poetry/poetry/pull/2366#issuecomment-652418094
"""

import importlib.metadata as importlib_metadata

__version__ = importlib_metadata.version(__package__ or __name__)
