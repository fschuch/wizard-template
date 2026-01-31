# Template Synchronization Guide

This guide explains how to keep your project up-to-date with the wizard-template, including automated updates from dependabot for dependencies, GitHub Actions, and pre-commit hooks.

## Overview

The wizard-template provides a synchronization tool that allows you to:

- 🔄 Pull template updates into your project
- 📦 Keep dependencies up-to-date (via dependabot updates in the template)
- 🔧 Sync GitHub Actions workflow improvements
- 🎯 Maintain pre-commit hook updates
- 🛡️ Preserve your project-specific customizations

## How It Works

The template sync system uses Git remotes to track the template repository and merge updates selectively:

1. **Template Remote**: Your project adds the template as a Git remote
2. **Configuration**: `.templaterc` file defines what to sync and what to keep project-specific
3. **Smart Merging**: The sync tool intelligently merges template changes while preserving your modifications
4. **Dependabot Flow**: When dependabot updates dependencies in the template, you can pull those updates to your project

## Initial Setup (One-Time)

### 1. Ensure Your Project Has .templaterc

If you created your project from the template, you should have a `.templaterc` file. If not, copy it from the template and customize it:

```bash
# Copy from template (if needed)
curl -o .templaterc https://raw.githubusercontent.com/fschuch/wizard-template/main/.templaterc

# Edit to match your project
vim .templaterc
```

Update these values in `.templaterc`:

```toml
[project]
username = "your-github-username"
project_name = "your-project-name"
```

### 2. Copy the Sync Tool

Ensure you have the sync tool in your project:

```bash
# Copy from template (if needed)
curl -o tools/template-sync.py https://raw.githubusercontent.com/fschuch/wizard-template/main/tools/template-sync.py
chmod +x tools/template-sync.py
```

### 3. Verify Setup

```bash
python tools/template-sync.py --dry-run
```

This will check your configuration and show you what would be synced without making any changes.

## Regular Sync Workflow

### Step 1: Preview Changes

Before syncing, see what updates are available:

```bash
python tools/template-sync.py --dry-run
```

This shows:
- Which files will be updated
- Which files will be skipped (project-specific)
- Any potential conflicts

### Step 2: Sync Template Updates

When you're ready to sync:

```bash
python tools/template-sync.py
```

The tool will:
1. Fetch latest template changes
2. Show you a preview
3. Ask for confirmation
4. Merge changes from the template
5. Update `.templaterc` with the sync timestamp

### Step 3: Handle Conflicts (If Any)

If there are merge conflicts:

1. The tool will stop and list conflicted files
2. Manually resolve conflicts:
   ```bash
   # Edit conflicted files
   vim path/to/conflicted/file
   
   # Mark as resolved
   git add path/to/conflicted/file
   
   # Complete the merge
   git commit
   ```
3. Run the sync tool again to update `.templaterc`

### Step 4: Test and Push

After syncing:

```bash
# Review changes
git log -1 --stat
git diff HEAD~1

# Test your project
hatch run qa

# Push to your repository
git push
```

## What Gets Synced?

By default, these files are synced from the template:

### ✅ Always Synced (Template Infrastructure)

- `.github/workflows/*.yaml` - CI/CD workflows
- `.github/dependabot.yml` - Dependabot configuration
- `.pre-commit-config.yaml` - Pre-commit hooks
- `.gitignore` - Git ignore patterns
- `.vscode/` - VS Code settings
- `docs/` - Documentation structure
- `pyproject.toml` - Build configuration (smart merge)

### ⊘ Never Synced (Project-Specific)

- `src/*/` - Your source code
- `tests/test_*.py` - Your project tests
- `.templaterc` - Your sync configuration
- `tools/rename_project_content.py` - One-time setup script

### 🔀 Smart Merge

Some files use intelligent merging:
- `pyproject.toml` - Merges dependencies while preserving your additions
- `.pre-commit-config.yaml` - Updates hook versions

## Handling Dependabot Updates

One of the key benefits of template sync is receiving dependabot updates:

### How Dependabot Updates Flow

1. **In Template Repo**: Dependabot creates PR to update dependencies
2. **Template Maintainer**: Reviews and merges the PR
3. **Your Project**: Run `template-sync.py` to pull the updates
4. **Your Review**: Test that updates work with your code
5. **Commit**: Push the synced changes

### Example: GitHub Actions Update

When the template receives a dependabot PR like:

```yaml
# .github/workflows/ci.yaml
- uses: actions/checkout@v6.0.1  # Was v6.0.0
```

Running `template-sync.py` will:
1. Fetch this change
2. Apply it to your project
3. Create a merge commit
4. You test and push

### Example: Python Dependency Update

When template's `pyproject.toml` gets updated:

```toml
# Old
pytest = ">=8.2.2"

# New
pytest = ">=8.3.0"
```

The sync tool:
1. Detects the change
2. Smart-merges into your `pyproject.toml`
3. Preserves your additional dependencies
4. You run tests to verify compatibility

## Configuration Reference

### .templaterc Structure

```toml
[template]
repository = "https://github.com/fschuch/wizard-template"
branch = "main"
last_sync_commit = "abc123..."  # Auto-updated

[project]
username = "your-username"
project_name = "your-project"

[sync]
# Paths to exclude (never sync)
exclude_paths = [
    "src/*/",
    "tests/test_*.py",
]

# Paths to always sync
sync_paths = [
    ".github/workflows/*.yaml",
    ".pre-commit-config.yaml",
    "pyproject.toml",
]

# Files that need smart merging
smart_merge_files = [
    "pyproject.toml",
]
```

### Customizing Sync Behavior

You can modify `.templaterc` to:

**Exclude additional files:**
```toml
exclude_paths = [
    "src/*/",
    "tests/test_*.py",
    "docs/custom-section/",  # Your custom docs
]
```

**Include additional files:**
```toml
sync_paths = [
    ".github/workflows/*.yaml",
    ".github/custom-action.yaml",  # Your custom addition
]
```

## Best Practices

### 1. Sync Regularly

Check for template updates monthly or quarterly:

```bash
# Add to your calendar
python tools/template-sync.py --dry-run
```

### 2. Review Before Applying

Always use `--dry-run` first to understand what will change.

### 3. Test After Syncing

Run your full test suite after syncing:

```bash
hatch run qa
```

### 4. Keep .templaterc Updated

If you modify your project structure, update `.templaterc` to reflect your changes.

### 5. Commit Sync Changes Separately

Keep template syncs in their own commits for clarity:

```bash
git log --oneline
# abc123 chore: sync with template (main)
# def456 feat: add new feature
```

## Troubleshooting

### "Could not parse git URL"

The template remote might not be configured. Run:

```bash
git remote add template https://github.com/fschuch/wizard-template
```

### "Merge conflicts detected"

Some changes conflict with your modifications. This is normal! Resolve conflicts manually:

1. Edit conflicted files (look for `<<<<<<<` markers)
2. `git add <resolved-file>`
3. `git commit`
4. Run sync tool again

### "No template updates available"

Your project is already up-to-date! Check back later or verify the template has new commits:

```bash
git fetch template main
git log HEAD..template/main
```

### Sync Tool Not Found

Ensure the tool exists and is executable:

```bash
curl -o tools/template-sync.py https://raw.githubusercontent.com/fschuch/wizard-template/main/tools/template-sync.py
chmod +x tools/template-sync.py
```

## Advanced Usage

### Sync from a Specific Branch

Edit `.templaterc`:

```toml
[template]
branch = "develop"  # Instead of "main"
```

### Manual Sync Using Git

If you prefer manual control:

```bash
# Add template remote (once)
git remote add template https://github.com/fschuch/wizard-template

# Fetch updates
git fetch template main

# View changes
git log HEAD..template/main

# Cherry-pick specific commits
git cherry-pick abc123

# Or merge everything
git merge template/main
```

### Automated Sync Checks (Optional)

You can add a GitHub Action to check for template updates:

```yaml
# .github/workflows/template-sync-check.yaml
name: Check Template Updates

on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
      - name: Check for updates
        run: python tools/template-sync.py --dry-run
```

## FAQ

**Q: Will syncing overwrite my code?**  
A: No. The tool excludes `src/*/` and project-specific files by default.

**Q: What if I've customized a template file?**  
A: Git will detect conflicts and ask you to resolve them manually. Your changes won't be lost.

**Q: How often should I sync?**  
A: Depends on your needs. Monthly or quarterly is typical. Check when you see dependabot updates in the template repo.

**Q: Can I stop syncing after setup?**  
A: Yes, but you'll miss out on improvements and security updates.

**Q: What if template changes break my project?**  
A: You can revert the merge commit: `git revert HEAD`. Then investigate the breaking change.

## Contributing

Found an issue with the sync tool? Have suggestions? Please:

1. Open an issue in the template repository
2. Include error messages and your `.templaterc` configuration
3. Describe your sync scenario

## Support

- 📖 [Full Documentation](https://docs.fschuch.com/wizard-template)
- 🐛 [Report Issues](https://github.com/fschuch/wizard-template/issues)
- 💬 [Discussions](https://github.com/fschuch/wizard-template/discussions)
