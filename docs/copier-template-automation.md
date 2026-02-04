# Copier Template Automation Guide

This guide explains how to maintain the wizard-template as a working Python project while providing a copier template for users.

## The Problem

Using copier directly has challenges:
1. **Template isn't a real project**: Copier templates are Jinja2 files, not working code
2. **Hard to maintain**: Can't run tests, linters, or CI on template files
3. **Automated updates don't work**: Dependabot, pre-commit autoupdate don't work on Jinja templates
4. **No validation**: Can't verify template changes actually work

## The Solution

**Keep wizard-template as a working Python project** and **generate** the copier template from it:

```
wizard-template (this repo)          wizard-template-copier (separate repo)
├── Working Python project    ──→    ├── Copier template with Jinja2
├── Real dependencies                ├── Generated from wizard-template
├── CI/CD tests                      ├── {{ project_name }} variables
├── Dependabot updates               └── Used by: copier copy ...
└── Pre-commit autoupdate
```

## Architecture

### 1. Source Repository (This One)

`https://github.com/fschuch/wizard-template`

- Maintained as a **working Python project**
- Has real dependencies that dependabot can update
- Has working CI/CD that can be tested
- Receives pre-commit autoupdates
- Source of truth for all template content

### 2. Copier Template Repository

`https://github.com/fschuch/wizard-template-copier` (to be created)

- **Generated automatically** from wizard-template
- Contains Jinja2-templated files
- Has `copier.yml` configuration
- Used by users with `copier copy`
- **Never edited manually**

### 3. Conversion Tool

`tools/generate-copier-template.py`

- Converts wizard-template → copier format
- Replaces hardcoded values with Jinja2 variables
- Creates `copier.yml` configuration
- Can be run manually or via GitHub Actions

## Setup Instructions

### Step 1: Create Copier Template Repository

```bash
# Create a new repository on GitHub
# Name: wizard-template-copier
# Description: Copier template (auto-generated from wizard-template)
# Visibility: Public

# Clone it locally
git clone https://github.com/fschuch/wizard-template-copier.git
cd wizard-template-copier

# Initial setup
echo "# Wizard Template - Copier Version" > README.md
git add README.md
git commit -m "Initial commit"
git push
```

### Step 2: Generate Copier Template

From the wizard-template repository:

```bash
# Generate the copier template
python tools/generate-copier-template.py --output-dir ../wizard-template-copier

# Review the generated files
cd ../wizard-template-copier
ls -la

# Test the template locally
copier copy . /tmp/test-project
cd /tmp/test-project
hatch run test  # Verify it works
```

### Step 3: Push to Copier Template Repository

```bash
cd ../wizard-template-copier

# Add all generated files
git add .
git commit -m "Generate copier template from wizard-template"
git push
```

### Step 4: Set Up GitHub Actions Automation

Add this workflow to wizard-template (`.github/workflows/sync-copier-template.yaml`):

```yaml
name: Sync Copier Template

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout wizard-template
        uses: actions/checkout@v6
        with:
          path: wizard-template

      - name: Checkout copier template
        uses: actions/checkout@v6
        with:
          repository: fschuch/wizard-template-copier
          token: ${{ secrets.COPIER_TEMPLATE_TOKEN }}
          path: wizard-template-copier

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Generate copier template
        run: |
          cd wizard-template
          python tools/generate-copier-template.py --output-dir ../wizard-template-copier-new

      - name: Update copier repository
        run: |
          # Remove old content (except .git)
          cd wizard-template-copier
          find . -mindepth 1 -maxdepth 1 -not -name .git -exec rm -rf {} +
          
          # Copy new content
          cd ../wizard-template-copier-new
          find . -mindepth 1 -maxdepth 1 -not -name .git -exec cp -r {} ../wizard-template-copier/ \;

      - name: Commit and push changes
        run: |
          cd wizard-template-copier
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add .
          if git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "Auto-sync from wizard-template @ ${{ github.sha }}"
            git push
          fi
```

**Important**: Create a Personal Access Token with `repo` scope and add it as a secret named `COPIER_TEMPLATE_TOKEN` in the wizard-template repository settings.

## Workflow

### Making Changes to the Template

1. **Edit wizard-template** (this repository)
   ```bash
   # Make changes to any file
   vim pyproject.toml  # Update dependencies
   vim .pre-commit-config.yaml  # Update hooks
   # etc.
   ```

2. **Test changes locally**
   ```bash
   hatch run test
   hatch run check
   ```

3. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: update pytest to 8.3.0"
   git push
   ```

4. **GitHub Actions automatically**:
   - Generates copier template
   - Pushes to wizard-template-copier repository

5. **Users get updates**:
   ```bash
   cd my-project
   copier update
   ```

### Handling Dependabot Updates

When dependabot creates a PR in wizard-template:

1. **Review PR** in wizard-template
2. **Merge if tests pass**
3. **GitHub Actions automatically**:
   - Regenerates copier template with new dependencies
   - Pushes to wizard-template-copier
4. **Users can update**:
   ```bash
   copier update  # Gets new dependencies
   ```

### Handling Pre-commit Autoupdates

Same workflow as dependabot:

1. Pre-commit bot updates `.pre-commit-config.yaml`
2. Merge PR
3. Copier template auto-syncs
4. Users get updated hooks via `copier update`

## Manual Sync

You can manually sync at any time:

```bash
# In wizard-template directory
python tools/generate-copier-template.py --output-dir ../wizard-template-copier

# In copier template directory
cd ../wizard-template-copier
git add .
git commit -m "Manual sync from wizard-template"
git push
```

## User Experience

### Creating a New Project

```bash
# Install copier
pip install copier

# Create project from copier template
copier copy https://github.com/fschuch/wizard-template-copier my-awesome-project

# Answer prompts:
# - project_name: my-awesome-project
# - project_slug: my_awesome_project
# - author_name: myusername
# - author_email: me@example.com
# - project_description: My awesome Python project

cd my-awesome-project
hatch run test  # Everything works!
```

### Updating Existing Project

```bash
cd my-awesome-project

# Get latest template updates
copier update

# Review changes, resolve conflicts if any
git diff

# Test
hatch run qa

# Commit
git add .
git commit -m "chore: update from template"
git push
```

## Benefits

### For Template Maintainers (You)

✅ **Maintain real project**: wizard-template is a working Python project  
✅ **Automated updates work**: Dependabot, pre-commit autoupdate function normally  
✅ **Can test changes**: CI/CD validates template works  
✅ **Single source of truth**: wizard-template is authoritative  
✅ **Automated sync**: GitHub Actions keeps copier template up-to-date  

### For Template Users

✅ **Easy project creation**: `copier copy` creates new projects  
✅ **Easy updates**: `copier update` pulls template improvements  
✅ **Conflict resolution**: Copier handles merge conflicts  
✅ **Selective updates**: Can choose which updates to apply  
✅ **Always current**: Template reflects latest wizard-template state  

## Comparison: Copier vs Manual Template Use

| Aspect | Copier Template | Manual Clone |
|--------|----------------|--------------|
| Project Creation | `copier copy` with prompts | Clone + manual rename |
| Updates | `copier update` | Manual sync or git remote |
| Variables | Prompted, validated | Manual find/replace |
| Conflict Resolution | Built-in | Manual git merge |
| User Experience | Streamlined | Technical |

## Troubleshooting

### Template Generation Fails

```bash
# Run with verbose output
python tools/generate-copier-template.py --output-dir /tmp/test-copier

# Check for errors in output
```

### GitHub Actions Sync Fails

1. Check `COPIER_TEMPLATE_TOKEN` secret is set
2. Verify token has `repo` permissions
3. Check GitHub Actions logs

### Copier Update Conflicts

```bash
# Users can resolve conflicts manually
copier update
# Edit conflicted files
git add .
git commit -m "chore: resolve template update conflicts"
```

### Testing Copier Template Locally

```bash
# Generate template
python tools/generate-copier-template.py --output-dir /tmp/copier-template

# Test creating a project
copier copy /tmp/copier-template /tmp/test-project

# Verify it works
cd /tmp/test-project
hatch run test
```

## Best Practices

1. **Always test in wizard-template first**: Make sure changes work before syncing
2. **Use semantic commits**: Clear commit messages help users understand updates
3. **Document breaking changes**: Note in README if template updates require user action
4. **Version copier template**: Consider tagging releases
5. **Test copier template**: Periodically create test projects to verify

## Advanced: Versioned Releases

You can tag copier template releases:

```bash
cd wizard-template-copier
git tag -a v1.0.0 -m "Release version 1.0.0"
git push --tags

# Users can target specific versions
copier copy https://github.com/fschuch/wizard-template-copier --vcs-ref v1.0.0 my-project
```

## FAQ

**Q: Can I edit the copier template directly?**  
A: No! All changes should be made in wizard-template. The copier template is auto-generated.

**Q: How often does sync happen?**  
A: On every push to wizard-template's main branch (if GitHub Actions is set up).

**Q: Can users still use the old git remote method?**  
A: Yes! The template-sync.py tool still works. Copier is an additional option.

**Q: What if I want different content in the copier template?**  
A: Modify the `generate-copier-template.py` script to customize what gets included.

**Q: How do I handle template-specific documentation?**  
A: Use the `EXCLUDE_PATTERNS` in `generate-copier-template.py` to exclude docs meant only for wizard-template.

## Next Steps

1. ✅ Read this guide
2. Create wizard-template-copier repository
3. Generate initial copier template
4. Set up GitHub Actions automation
5. Update wizard-template README to mention copier option
6. Test creating a project with copier
7. Share with users!

## Resources

- [Copier Documentation](https://copier.readthedocs.io/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [wizard-template](https://github.com/fschuch/wizard-template)
