# Template Sync Usage Examples

Real-world scenarios demonstrating how to use the template sync tool.

## Scenario 1: Initial Setup in Existing Project

You have an existing project created from wizard-template and want to enable sync for the first time.

```bash
# 1. Ensure you have the required files
curl -o .templaterc https://raw.githubusercontent.com/fschuch/wizard-template/main/.templaterc
curl -o tools/template-sync.py https://raw.githubusercontent.com/fschuch/wizard-template/main/tools/template-sync.py
chmod +x tools/template-sync.py

# 2. Customize .templaterc for your project
vim .templaterc
# Update [project] section:
#   username = your-github-username
#   project_name = your-project-name

# 3. Run initial sync (dry-run first!)
python tools/template-sync.py --dry-run

# 4. If everything looks good, apply
python tools/template-sync.py
```

## Scenario 2: Syncing Dependabot Updates

The template repo got a dependabot PR that updated pytest from 8.2.2 to 8.3.0. You want to get this update.

```bash
# 1. Check what's new
python tools/template-sync.py --dry-run

# Output will show:
# Files to sync:
#   ✓ pyproject.toml (smart merge)

# 2. Apply the sync
python tools/template-sync.py

# 3. Review the changes
git log -1 --stat
git diff HEAD~1 pyproject.toml

# 4. Test with new pytest version
hatch run test

# 5. If tests pass, push
git push
```

## Scenario 3: Syncing GitHub Actions Update

Template updated `actions/checkout` from v6.0.1 to v6.0.2 via dependabot.

```bash
# 1. Preview
python tools/template-sync.py --dry-run

# Output shows:
# Files to sync:
#   ✓ .github/workflows/ci.yaml
#   ✓ .github/workflows/docs.yaml

# 2. Apply
python tools/template-sync.py

# 3. Check what changed
git diff HEAD~1 .github/workflows/

# 4. Test locally (if possible) or rely on CI
git push

# 5. Watch CI run with updated actions
```

## Scenario 4: Handling Merge Conflicts

You customized `pyproject.toml` and there's a conflict with template changes.

```bash
# 1. Try to sync
python tools/template-sync.py

# Output:
# ⚠️  Merge conflicts detected:
#     ⚠️  pyproject.toml
#
# Please resolve conflicts manually:
#   1. Edit conflicted files
#   2. git add <resolved-files>
#   3. git commit

# 2. Open the file and resolve conflicts
vim pyproject.toml

# Look for conflict markers:
# <<<<<<< HEAD
# your-dependency = "^1.0.0"
# =======
# template-dependency = "^2.0.0"
# >>>>>>> template/main

# Keep both if needed, or choose one

# 3. Mark as resolved
git add pyproject.toml

# 4. Complete the merge
git commit -m "chore: sync with template, resolve pyproject.toml conflicts"

# 5. Update tracking
python tools/template-sync.py --dry-run  # Will update .templaterc

# 6. Test and push
hatch run test
git push
```

## Scenario 5: Syncing Pre-commit Hook Updates

Template's `.pre-commit-config.yaml` got updated hooks via `pre-commit autoupdate`.

```bash
# 1. Check for updates
python tools/template-sync.py --dry-run

# Shows:
# Files to sync:
#   ✓ .pre-commit-config.yaml (smart merge)

# 2. Apply sync
python tools/template-sync.py

# 3. Review what hooks changed
git diff HEAD~1 .pre-commit-config.yaml

# Example diff:
# - rev: v0.14.0
# + rev: v0.15.0

# 4. Update pre-commit environments
pre-commit autoupdate  # Optional, to get latest
pre-commit run --all-files  # Test new versions

# 5. Commit and push
git push
```

## Scenario 6: Monthly Maintenance Sync

Regular maintenance to stay current with template improvements.

```bash
# 1. Create a branch for the sync
git checkout -b chore/template-sync-$(date +%Y-%m)

# 2. Preview what's changed
python tools/template-sync.py --dry-run

# 3. If changes look good, apply
python tools/template-sync.py

# 4. Run full QA suite
hatch run qa

# 5. Check all workflows still work
git push -u origin chore/template-sync-$(date +%Y-%m)
# Wait for CI to pass

# 6. Create PR and merge
gh pr create --title "chore: sync with template" \
             --body "Monthly template sync to stay current"
```

## Scenario 7: Selective Sync After Custom Changes

You heavily customized your CI workflows and want to sync only some files.

```bash
# 1. Edit .templaterc to be more selective
vim .templaterc

# Update sync_paths to exclude custom workflows:
# sync_paths = 
#     .github/workflows/ci.yaml
#     # .github/workflows/custom-workflow.yaml  # Comment out
#     .pre-commit-config.yaml
#     pyproject.toml

# 2. Preview (will skip custom files)
python tools/template-sync.py --dry-run

# 3. Apply selective sync
python tools/template-sync.py

# 4. Your custom workflows are preserved!
```

## Scenario 8: Catching Up After Long Time

Haven't synced in 6 months, many template updates accumulated.

```bash
# 1. See all changes since last sync
git fetch template main
git log .templaterc  # Find last sync commit

# 2. Preview (may show many files)
python tools/template-sync.py --dry-run

# 3. Consider incremental approach
# Option A: Sync everything at once (brave!)
python tools/template-sync.py

# Option B: Cherry-pick specific commits
git fetch template main
git log HEAD..template/main --oneline
git cherry-pick <specific-commit-hash>

# 4. Test thoroughly
hatch run qa
hatch run test

# 5. May need multiple rounds to resolve conflicts
```

## Scenario 9: Using Automated Checks

Set up GitHub Actions to notify you of template updates.

```bash
# 1. Copy the example workflow
cp .github/workflows/template-sync-check.yaml.example \
   .github/workflows/template-sync-check.yaml

# 2. Customize the schedule if needed
vim .github/workflows/template-sync-check.yaml

# 3. Commit and push
git add .github/workflows/template-sync-check.yaml
git commit -m "ci: add template sync check workflow"
git push

# 4. Workflow will create issues when updates are available
# Check your repo issues for "🧙 Template updates available"
```

## Scenario 10: Emergency Security Update

Template got a critical security fix that you need immediately.

```bash
# 1. Quick check (skip dry-run in emergency)
python tools/template-sync.py

# 2. Review security-related changes
git log -1 --stat
git diff HEAD~1

# 3. Fast-track testing
hatch run test  # Just run tests, skip linting

# 4. Deploy immediately
git push

# 5. Follow up with full QA when time permits
hatch run qa
```

## Tips and Tricks

### See What Changed in Template

```bash
# View all template changes since last sync
git fetch template main
git log HEAD..template/main --oneline

# View specific file changes
git diff HEAD template/main -- pyproject.toml
```

### Sync Only Specific Files

Temporarily modify `.templaterc`:

```toml
sync_paths = 
    .github/workflows/ci.yaml  # Only sync this one file
```

### Undo a Sync

```bash
# If you just synced and want to undo
git reset --hard HEAD~1

# If you already pushed
git revert HEAD
```

### Test Before Sync

```bash
# Fetch but don't merge
git fetch template main

# Create a test branch
git checkout -b test-template-sync
git merge template/main

# Test thoroughly
hatch run qa

# If good, apply to main branch
git checkout main
python tools/template-sync.py
```

### Keep Your Own Template Modifications

If you want to maintain template files with your own modifications:

1. Create a `local-template` branch with your changes
2. Sync template to a temporary branch
3. Rebase your changes on top

```bash
# Sync to temp branch
git checkout -b temp-sync main
python tools/template-sync.py

# Rebase your modifications
git checkout local-template
git rebase temp-sync

# Merge to main
git checkout main
git merge local-template
```
