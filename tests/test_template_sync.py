"""Tests for the template-sync tool."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_template_sync_module():
    """Dynamically load the template_sync module from tools directory."""
    tools_dir = Path(__file__).parent.parent / "tools"
    module_path = tools_dir / "template-sync.py"

    spec = importlib.util.spec_from_file_location("template_sync", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["template_sync"] = module
    spec.loader.exec_module(module)
    return module


# Load the module
template_sync = load_template_sync_module()
load_config = template_sync.load_config
should_sync_file = template_sync.should_sync_file


def test_load_config() -> None:
    """Test loading configuration from .templaterc."""
    # Save current directory
    import os

    original_dir = os.getcwd()

    try:
        # Change to repo root
        repo_root = Path(__file__).parent.parent
        os.chdir(repo_root)

        config = load_config()

        assert config.repository == "https://github.com/fschuch/wizard-template"
        assert config.branch == "main"
        assert config.username == "fschuch"
        assert config.project_name == "wizard-template"
        assert "src/*/" in config.exclude_paths
        assert ".github/workflows/*.yaml" in config.sync_paths

    finally:
        os.chdir(original_dir)


def test_should_sync_file() -> None:
    """Test file sync decision logic."""
    # Save current directory
    import os

    original_dir = os.getcwd()

    try:
        # Change to repo root
        repo_root = Path(__file__).parent.parent
        os.chdir(repo_root)

        config = load_config()

        # Should sync template infrastructure files
        assert should_sync_file(".github/workflows/ci.yaml", config)
        assert should_sync_file(".pre-commit-config.yaml", config)
        assert should_sync_file("pyproject.toml", config)

        # Should NOT sync project-specific files
        assert not should_sync_file("src/wizard_template/core.py", config)
        assert not should_sync_file("tests/test_core.py", config)
        assert not should_sync_file(".templaterc", config)

    finally:
        os.chdir(original_dir)


def test_config_exclude_patterns() -> None:
    """Test that exclude patterns work correctly."""
    import os

    original_dir = os.getcwd()

    try:
        repo_root = Path(__file__).parent.parent
        os.chdir(repo_root)

        config = load_config()

        # Test various source code paths
        assert not should_sync_file("src/myproject/main.py", config)
        assert not should_sync_file("src/another_project/utils.py", config)

        # Test various test files
        assert not should_sync_file("tests/test_main.py", config)
        assert not should_sync_file("tests/test_utils.py", config)

    finally:
        os.chdir(original_dir)
