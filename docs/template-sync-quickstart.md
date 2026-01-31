# Template Sync Quick Reference

## One-Time Setup

```bash
# 1. Ensure you have .templaterc (copy from template if needed)
curl -o .templaterc https://raw.githubusercontent.com/fschuch/wizard-template/main/.templaterc

# 2. Customize .templaterc with your project details
vim .templaterc  # Update username and project_name

# 3. Get the sync tool (if not already present)
curl -o tools/template-sync.py https://raw.githubusercontent.com/fschuch/wizard-template/main/tools/template-sync.py
chmod +x tools/template-sync.py
```

## Regular Usage

```bash
# Preview what would be updated (safe, read-only)
python tools/template-sync.py --dry-run

# Apply updates
python tools/template-sync.py

# If conflicts occur, resolve them manually:
vim <conflicted-file>    # Fix conflicts
git add <conflicted-file>
git commit
python tools/template-sync.py  # Re-run to update tracking
```

## What Gets Updated

✅ **Synced from template:**

- GitHub Actions workflows
- Dependabot configuration
- Pre-commit hooks
- Build configuration (pyproject.toml)
- Documentation structure

⊘ **Never touched:**

- Your source code (src/)
- Your tests (tests/test_*.py)
- Project-specific files

## Common Commands

```bash
# Check if template has updates
git fetch template main
git log HEAD..template/main

# View what changed in last sync
git log -1 --stat

# Test after syncing
hatch run qa

# Push synced changes
git push
```

## Getting Help

- Full guide: [docs/template-sync.md](template-sync.md)
- Template repo: <https://github.com/fschuch/wizard-template>
- Issues: <https://github.com/fschuch/wizard-template/issues>
