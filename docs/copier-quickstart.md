# Quick Start: Copier Template Setup

Fast-track guide to set up automated copier template generation.

## Prerequisites

- GitHub account
- Python 3.10+
- Git installed locally

## 5-Minute Setup

### 1. Create Copier Template Repository (GitHub)

```bash
# On GitHub.com
# Click "New Repository"
# Name: wizard-template-copier
# Description: Copier template (auto-generated from wizard-template)
# Public
# Don't initialize with README
# Create repository
```

### 2. Generate Initial Template (Local)

```bash
# Clone both repositories
git clone https://github.com/fschuch/wizard-template.git
git clone https://github.com/fschuch/wizard-template-copier.git

# Generate copier template
cd wizard-template
python tools/generate-copier-template.py --output-dir ../wizard-template-copier

# Push to copier repository
cd ../wizard-template-copier
git add .
git commit -m "Initial copier template generation"
git push
```

### 3. Set Up GitHub Actions (Optional)

```bash
# Create Personal Access Token
# GitHub.com → Settings → Developer Settings → Personal Access Tokens
# Generate new token (classic)
# Scopes: repo (all)
# Copy token

# Add secret to wizard-template repository
# GitHub.com → wizard-template → Settings → Secrets → Actions
# New repository secret
# Name: COPIER_TEMPLATE_TOKEN
# Value: <paste token>

# Enable workflow
cd wizard-template
cp .github/workflows/sync-copier-template.yaml.example \
   .github/workflows/sync-copier-template.yaml
git add .github/workflows/sync-copier-template.yaml
git commit -m "ci: enable copier template auto-sync"
git push
```

## Test It

### Create a Test Project

```bash
# Install copier
pip install copier

# Create project from your copier template
copier copy https://github.com/fschuch/wizard-template-copier test-project

# Answer prompts
# project_name: test-project
# project_slug: test_project
# author_name: yourusername
# author_email: you@example.com
# project_description: Test project

# Verify it works
cd test-project
python -m pip install hatch
hatch run test
```

### Test Auto-Sync (if GitHub Actions enabled)

```bash
# Make a change to wizard-template
cd wizard-template
echo "# Test change" >> README.md
git add README.md
git commit -m "test: verify copier sync works"
git push

# Wait ~1 minute, then check wizard-template-copier
# Should have a new commit: "chore: auto-sync from wizard-template"
```

## Usage

### Make Template Changes

```bash
# Edit wizard-template (normal workflow)
cd wizard-template
vim pyproject.toml  # Make changes
git add pyproject.toml
git commit -m "feat: update dependencies"
git push

# If GitHub Actions enabled:
#   ✅ Copier template auto-syncs
# 
# If manual:
python tools/generate-copier-template.py --output-dir ../wizard-template-copier
cd ../wizard-template-copier
git add . && git commit -m "Sync from wizard-template" && git push
```

### Users Create Projects

```bash
copier copy https://github.com/fschuch/wizard-template-copier my-project
cd my-project
hatch run test
```

### Users Update Projects

```bash
cd my-project
copier update
# Review changes, test, commit
```

## Troubleshooting

### "COPIER_TEMPLATE_TOKEN not found"

GitHub Actions needs a token to push to copier repository:
1. Create Personal Access Token with `repo` scope
2. Add as secret `COPIER_TEMPLATE_TOKEN` in wizard-template repo

### "Generation fails"

```bash
# Test locally
python tools/generate-copier-template.py --output-dir /tmp/test-copier
# Check output for errors
```

### "Copier template doesn't work"

```bash
# Test the generated template
copier copy /path/to/wizard-template-copier /tmp/test-project
cd /tmp/test-project
python -m pip install hatch
hatch run test
# Check for errors
```

## Next Steps

1. ✅ Read full guide: [docs/copier-template-automation.md](copier-template-automation.md)
2. Update wizard-template README to mention copier option
3. Create template releases/tags for versioning
4. Share with users

## Resources

- [Full Documentation](copier-template-automation.md)
- [Copier Docs](https://copier.readthedocs.io/)
- [wizard-template](https://github.com/fschuch/wizard-template)
