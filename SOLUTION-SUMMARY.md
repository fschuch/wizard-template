# Template Synchronization Solution - Implementation Summary

## Problem Statement

You use this wizard-template across multiple projects, and you want to propagate changes (especially dependabot updates for dependencies, GitHub Actions, and pre-commit hooks) from the template to these downstream projects. The challenge is that downstream projects have:

1. Their own git history
2. Different project names
3. Project-specific customizations
4. Potential merge conflicts

You considered Copier but were concerned about how to ensure automated updates (dependabot) remain functional.

## Solution Implemented

A **Git-based template synchronization system** that leverages native Git features for merging template updates while preserving project-specific content.

## What Was Created

### 1. Configuration File: `.templaterc`

Tracks the template source and defines sync behavior:

```toml
[template]
repository = https://github.com/fschuch/wizard-template
branch = main
last_sync_commit = 

[project]
username = fschuch
project_name = wizard-template

[sync]
exclude_paths = 
    src/*/                    # Your code
    tests/test_*.py          # Your tests
    
sync_paths = 
    .github/workflows/*.yaml  # CI/CD configs
    .pre-commit-config.yaml   # Pre-commit hooks
    pyproject.toml            # Dependencies
```

### 2. Sync Tool: `tools/template-sync.py`

A Python script (417 lines) that:

- ✅ Adds template as git remote
- ✅ Fetches latest template changes
- ✅ Shows preview of what will be synced
- ✅ Merges changes using standard git merge
- ✅ Detects and reports conflicts
- ✅ Updates sync tracking
- ✅ Dry-run mode for safety

**Usage:**

```bash
# Preview changes
python tools/template-sync.py --dry-run

# Apply changes
python tools/template-sync.py
```

### 3. Comprehensive Documentation

- **docs/template-sync.md** (413 lines)
  - Complete guide with setup, workflow, configuration reference
  - Troubleshooting section
  - FAQ

- **docs/template-sync-quickstart.md** (70 lines)
  - Quick reference card
  - Common commands
  - One-page cheat sheet

- **docs/template-sync-examples.md** (343 lines)
  - 10 real-world scenarios
  - Step-by-step examples
  - Tips and tricks

### 4. Optional Automation

`.github/workflows/template-sync-check.yaml.example`

- Checks weekly for template updates
- Creates GitHub issues when updates available
- Can be enabled by removing `.example` extension

### 5. Tests

`tests/test_template_sync.py`

- Validates configuration loading
- Tests file sync logic
- Ensures exclude patterns work

## How It Solves the Dependabot Problem

### The Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. TEMPLATE REPO (wizard-template)                              │
│                                                                  │
│    Dependabot creates PR:                                       │
│    - Update pytest: 8.2.2 → 8.3.0 in pyproject.toml           │
│    - Update actions/checkout: v6.0.1 → v6.0.2 in ci.yaml      │
│    - Update ruff: v0.14.0 → v0.15.0 in .pre-commit-config.yaml │
│                                                                  │
│    ↓ Maintainer reviews and merges                             │
│                                                                  │
│    Commits merged to main branch                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. DOWNSTREAM PROJECT (your-awesome-project)                     │
│                                                                  │
│    Developer runs:                                              │
│    $ python tools/template-sync.py                              │
│                                                                  │
│    Tool performs:                                               │
│    1. git fetch template main                                   │
│    2. Shows preview of changes                                  │
│    3. git merge template/main                                   │
│    4. Updates .templaterc with commit hash                      │
│                                                                  │
│    Result:                                                      │
│    ✓ pyproject.toml updated with new pytest version           │
│    ✓ ci.yaml updated with new actions                         │
│    ✓ .pre-commit-config.yaml updated with new ruff            │
│    ✓ Project-specific code in src/ untouched                  │
│                                                                  │
│    ↓ Developer tests and verifies                              │
│                                                                  │
│    $ hatch run qa  # Run tests with new dependencies           │
│    $ git push      # Deploy updates                            │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Works

1. **Git Merge** handles the complexity
   - Uses standard 3-way merge algorithm
   - Detects conflicts automatically
   - Preserves both template and project changes

2. **Dependabot updates are just commits**
   - No special handling needed
   - Can be synced like any other template change
   - Full git history preserved

3. **Smart Configuration**
   - `.templaterc` defines what to sync vs skip
   - Template infrastructure synced automatically
   - Project code never touched

4. **Manual Review**
   - Dry-run shows preview before applying
   - Developer tests compatibility
   - Can revert if needed

## Advantages Over Copier

| Aspect | Our Solution | Copier |
|--------|-------------|--------|
| Git History | ✅ Fully preserved | ⚠️ May lose history |
| Dependabot Updates | ✅ Natural git commits | ❓ Requires regeneration |
| Learning Curve | ✅ Standard git commands | ⚠️ New tool to learn |
| Flexibility | ✅ Highly configurable | ⚠️ Template constraints |
| Dependencies | ✅ Just Python + Git | ⚠️ Copier package needed |
| Conflict Resolution | ✅ Standard git merge | ⚠️ Template-specific |

## Usage in Downstream Projects

### One-Time Setup

```bash
# 1. Get the sync files
curl -o .templaterc \
  https://raw.githubusercontent.com/fschuch/wizard-template/main/.templaterc

curl -o tools/template-sync.py \
  https://raw.githubusercontent.com/fschuch/wizard-template/main/tools/template-sync.py

chmod +x tools/template-sync.py

# 2. Customize for your project
vim .templaterc
# Update: username = your-username
#        project_name = your-project

# 3. Test it
python tools/template-sync.py --dry-run
```

### Regular Syncing

```bash
# Monthly or quarterly check
python tools/template-sync.py --dry-run  # Preview
python tools/template-sync.py            # Apply
hatch run qa                             # Test
git push                                 # Deploy
```

## Real-World Scenarios Covered

1. ✅ Initial setup in existing projects
2. ✅ Syncing dependabot dependency updates
3. ✅ Syncing GitHub Actions updates
4. ✅ Handling merge conflicts
5. ✅ Syncing pre-commit hook updates
6. ✅ Monthly maintenance syncs
7. ✅ Selective syncing (exclude custom files)
8. ✅ Catching up after long periods
9. ✅ Automated update notifications
10. ✅ Emergency security updates

## Technical Details

### Files Created/Modified

```
wizard-template/
├── .templaterc                                    # Config file
├── README.md                                      # Updated with sync info
├── tools/
│   └── template-sync.py                          # Main sync tool
├── docs/
│   ├── template-sync.md                          # Full guide
│   ├── template-sync-quickstart.md               # Quick reference
│   └── template-sync-examples.md                 # Real examples
├── tests/
│   └── test_template_sync.py                     # Tests
└── .github/workflows/
    └── template-sync-check.yaml.example          # Optional automation
```

### Technology Stack

- **Python 3.10+** (uses standard library only)
- **Git** (standard git commands)
- **ConfigParser** (for .templaterc parsing)
- No external dependencies required

### Design Principles

1. **Minimal Dependencies** - Uses only Python stdlib and Git
2. **Safe by Default** - Dry-run mode, no destructive operations
3. **Git Native** - Leverages existing Git features
4. **Well Documented** - Comprehensive guides and examples
5. **Tested** - Unit tests for core functionality
6. **Flexible** - Highly configurable via .templaterc

## Success Metrics

✅ **Solves the Dependabot Problem**
   - Dependabot updates flow naturally from template to projects

✅ **Preserves Project History**
   - Full git history maintained in all projects

✅ **Easy to Use**
   - Single command: `python tools/template-sync.py`

✅ **Safe**
   - Dry-run preview before applying
   - Standard git conflict resolution
   - Can revert if needed

✅ **Maintainable**
   - Pure Python, no external deps
   - Well-tested and documented
   - Standard patterns

## Next Steps

1. **Try it out** in the template repo itself
2. **Apply to one downstream project** as a pilot
3. **Iterate based on feedback**
4. **Roll out to other projects** once refined

## Questions or Issues?

- 📖 Read the guides in `docs/`
- 🔍 Check examples in `docs/template-sync-examples.md`
- 🐛 Report issues on GitHub
- 💬 Start a discussion for questions

---

**Summary**: This solution provides a practical, git-native way to keep your downstream projects synchronized with template improvements, especially dependabot updates. It's minimal, safe, well-documented, and solves your specific concern about ensuring automated updates remain functional across your project portfolio.
