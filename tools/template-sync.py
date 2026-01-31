#!/usr/bin/env python3
"""
Template Synchronization Tool

This tool helps keep projects derived from wizard-template up-to-date with
template changes, including dependabot updates to dependencies, GitHub Actions,
and pre-commit hooks.

Usage:
    python tools/template-sync.py [--dry-run] [--help]

Requirements:
    - Git repository with template remote configured
    - .templaterc configuration file in project root
"""

from __future__ import annotations

import argparse
import configparser
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


class TemplateConfig(NamedTuple):
    """Configuration loaded from .templaterc"""

    repository: str
    branch: str
    last_sync_commit: str
    username: str
    project_name: str
    exclude_paths: list[str]
    sync_paths: list[str]
    smart_merge_files: list[str]


class SyncResult(NamedTuple):
    """Result of a sync operation"""

    success: bool
    message: str
    new_files: list[str]
    modified_files: list[str]
    conflicts: list[str]


def run_command(
    cmd: list[str], check: bool = True, capture: bool = True
) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            check=check,
            capture_output=capture,
            text=True,
        )
        return result
    except subprocess.CalledProcessError as e:
        if capture:
            print(f"Command failed: {' '.join(cmd)}", file=sys.stderr)
            if e.stdout:
                print(f"STDOUT: {e.stdout}", file=sys.stderr)
            if e.stderr:
                print(f"STDERR: {e.stderr}", file=sys.stderr)
        raise


def load_config() -> TemplateConfig:
    """Load configuration from .templaterc file."""
    config_path = Path(".templaterc")
    if not config_path.exists():
        print("Error: .templaterc file not found in current directory", file=sys.stderr)
        print(
            "Please ensure you're in the project root and .templaterc exists",
            file=sys.stderr,
        )
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_path)

    def parse_list(value: str) -> list[str]:
        """Parse a list value from config."""
        return [
            line.strip().strip('"').strip("'")
            for line in value.strip().split("\n")
            if line.strip() and not line.strip().startswith("#")
        ]

    return TemplateConfig(
        repository=config.get("template", "repository"),
        branch=config.get("template", "branch", fallback="main"),
        last_sync_commit=config.get("template", "last_sync_commit", fallback=""),
        username=config.get("project", "username"),
        project_name=config.get("project", "project_name"),
        exclude_paths=parse_list(config.get("sync", "exclude_paths", fallback="")),
        sync_paths=parse_list(config.get("sync", "sync_paths", fallback="")),
        smart_merge_files=parse_list(
            config.get("sync", "smart_merge_files", fallback="")
        ),
    )


def setup_template_remote(config: TemplateConfig) -> None:
    """Ensure the template remote is configured."""
    print("🔧 Checking template remote configuration...")

    # Check if template remote exists
    result = run_command(
        ["git", "remote", "get-url", "template"], check=False, capture=True
    )

    if result.returncode != 0:
        print(f"   Adding template remote: {config.repository}")
        run_command(["git", "remote", "add", "template", config.repository])
    else:
        current_url = result.stdout.strip()
        if current_url != config.repository:
            print(
                f"   Updating template remote: {current_url} -> {config.repository}"
            )
            run_command(["git", "remote", "set-url", "template", config.repository])
        else:
            print("   ✓ Template remote already configured")


def fetch_template_updates(config: TemplateConfig) -> None:
    """Fetch latest changes from the template repository."""
    print(f"\n📡 Fetching updates from template ({config.branch})...")
    run_command(["git", "fetch", "template", config.branch], capture=False)
    print("   ✓ Fetch complete")


def get_template_changes(config: TemplateConfig) -> list[str]:
    """Get list of changed files in template since last sync."""
    if config.last_sync_commit:
        base = config.last_sync_commit
        print(f"\n📋 Checking changes since last sync ({base[:8]})...")
    else:
        base = "HEAD"
        print("\n📋 Checking all template changes (first sync)...")

    result = run_command(
        [
            "git",
            "diff",
            "--name-only",
            base,
            f"template/{config.branch}",
        ],
        check=False,
    )

    if result.returncode != 0:
        print("   Warning: Could not compare with last sync, showing all changes")
        result = run_command(
            ["git", "ls-tree", "-r", "--name-only", f"template/{config.branch}"]
        )

    files = [f.strip() for f in result.stdout.split("\n") if f.strip()]
    print(f"   Found {len(files)} changed files in template")
    return files


def should_sync_file(file_path: str, config: TemplateConfig) -> bool:
    """Determine if a file should be synced based on configuration."""
    from fnmatch import fnmatch

    # Check exclude patterns
    for pattern in config.exclude_paths:
        if fnmatch(file_path, pattern):
            return False

    # Check sync patterns (if specified, only sync matching files)
    if config.sync_paths:
        for pattern in config.sync_paths:
            if fnmatch(file_path, pattern):
                return True
        return False

    # Default: sync template infrastructure files
    template_files = [
        ".github/",
        ".pre-commit-config.yaml",
        "pyproject.toml",
        ".gitignore",
        ".vscode/",
        "docs/",
    ]

    for prefix in template_files:
        if file_path.startswith(prefix):
            return True

    return False


def preview_changes(changed_files: list[str], config: TemplateConfig) -> None:
    """Preview which files will be synced and which will be skipped."""
    print("\n📝 Preview of sync operation:")

    to_sync = []
    to_skip = []

    for file_path in changed_files:
        if should_sync_file(file_path, config):
            to_sync.append(file_path)
        else:
            to_skip.append(file_path)

    if to_sync:
        print("\n   Files to sync:")
        for f in sorted(to_sync):
            marker = " (smart merge)" if f in config.smart_merge_files else ""
            print(f"      ✓ {f}{marker}")

    if to_skip:
        print("\n   Files to skip (project-specific):")
        for f in sorted(to_skip)[:10]:  # Show first 10
            print(f"      ⊘ {f}")
        if len(to_skip) > 10:
            print(f"      ... and {len(to_skip) - 10} more")


def perform_sync(
    changed_files: list[str], config: TemplateConfig, dry_run: bool = False
) -> SyncResult:
    """Perform the actual sync operation."""
    if dry_run:
        print("\n🔍 DRY RUN MODE - No changes will be made")
        return SyncResult(
            success=True,
            message="Dry run completed successfully",
            new_files=[],
            modified_files=[],
            conflicts=[],
        )

    print("\n🔄 Starting sync operation...")

    # Get current branch
    result = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    current_branch = result.stdout.strip()

    # Check for uncommitted changes
    result = run_command(["git", "status", "--porcelain"])
    if result.stdout.strip():
        print("\n⚠️  Warning: You have uncommitted changes.")
        response = input("Continue with sync? (y/N): ")
        if response.lower() != "y":
            return SyncResult(
                success=False,
                message="Sync cancelled by user",
                new_files=[],
                modified_files=[],
                conflicts=[],
            )

    # Create a merge commit with template changes
    print(f"\n   Merging template/{config.branch} into {current_branch}...")
    merge_result = run_command(
        ["git", "merge", "--no-ff", f"template/{config.branch}", "-m", 
         f"chore: sync with template ({config.branch})"],
        check=False,
        capture=True,
    )

    if merge_result.returncode != 0:
        # Check if there are conflicts
        conflict_result = run_command(
            ["git", "diff", "--name-only", "--diff-filter=U"]
        )
        conflicts = [f.strip() for f in conflict_result.stdout.split("\n") if f.strip()]

        if conflicts:
            print("\n⚠️  Merge conflicts detected:")
            for f in conflicts:
                print(f"      ⚠️  {f}")
            print("\n   Please resolve conflicts manually:")
            print("      1. Edit conflicted files")
            print("      2. git add <resolved-files>")
            print("      3. git commit")
            print("      4. Run this script again to update .templaterc")

            return SyncResult(
                success=False,
                message="Merge conflicts require manual resolution",
                new_files=[],
                modified_files=[],
                conflicts=conflicts,
            )
        else:
            return SyncResult(
                success=False,
                message=f"Merge failed: {merge_result.stderr}",
                new_files=[],
                modified_files=[],
                conflicts=[],
            )

    # Get the new commit hash
    result = run_command(["git", "rev-parse", f"template/{config.branch}"])
    new_commit = result.stdout.strip()

    # Update .templaterc with new commit
    update_config_last_sync(new_commit)

    print("\n   ✓ Merge completed successfully")

    return SyncResult(
        success=True,
        message="Template sync completed successfully",
        new_files=[],
        modified_files=[],
        conflicts=[],
    )


def update_config_last_sync(commit_hash: str) -> None:
    """Update the last_sync_commit in .templaterc."""
    config_path = Path(".templaterc")
    content = config_path.read_text()

    # Update last_sync_commit line
    import re

    # Match either 'last_sync_commit = ' or 'last_sync_commit = <value>'
    pattern = r'(last_sync_commit\s*=\s*).*$'
    replacement = f'\\1{commit_hash}'
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    config_path.write_text(new_content)
    print(f"   ✓ Updated .templaterc with commit {commit_hash[:8]}")


def main() -> None:
    """Main entry point for the template sync tool."""
    parser = argparse.ArgumentParser(
        description="Sync template updates to downstream project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview changes without applying
  python tools/template-sync.py --dry-run

  # Perform actual sync
  python tools/template-sync.py

  # Get help
  python tools/template-sync.py --help
        """,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying them",
    )

    args = parser.parse_args()

    print("🧙 Wizard Template Sync Tool")
    print("=" * 50)

    # Load configuration
    config = load_config()
    print(f"\n📦 Project: {config.username}/{config.project_name}")
    print(f"📄 Template: {config.repository}")

    # Setup and fetch
    setup_template_remote(config)
    fetch_template_updates(config)

    # Get changes
    changed_files = get_template_changes(config)

    if not changed_files:
        print("\n✨ No template updates available. Your project is up-to-date!")
        return

    # Preview changes
    preview_changes(changed_files, config)

    if args.dry_run:
        print("\n✅ Dry run complete. Use without --dry-run to apply changes.")
        return

    # Confirm before proceeding
    print("\n" + "=" * 50)
    response = input("Proceed with sync? (y/N): ")
    if response.lower() != "y":
        print("\n❌ Sync cancelled")
        return

    # Perform sync
    result = perform_sync(changed_files, config, dry_run=False)

    # Report results
    print("\n" + "=" * 50)
    if result.success:
        print(f"✅ {result.message}")
        print("\n📝 Next steps:")
        print("   1. Review the changes: git log -1 --stat")
        print("   2. Test your project")
        print("   3. Push changes: git push")
    else:
        print(f"❌ {result.message}")
        if result.conflicts:
            print("\n⚠️  Conflicts need manual resolution")
        sys.exit(1)


if __name__ == "__main__":
    main()
