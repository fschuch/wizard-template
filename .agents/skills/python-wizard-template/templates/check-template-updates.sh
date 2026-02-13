#!/bin/bash
# Script to check for template updates
# Usage: tools/check-template-updates.sh

set -e

echo "=== Wizard Template Update Checker ==="
echo ""

# Check if template remote exists
if ! git remote | grep -q "^template$"; then
    echo "Adding wizard-template as remote 'template'..."
    git remote add template https://github.com/fschuch/wizard-template.git
fi

echo "Fetching latest template changes..."
git fetch template

echo ""
echo "=== Changed files in template since your last sync ==="
git diff --name-only HEAD...template/main

echo ""
echo "=== Summary of changes ==="
git log HEAD..template/main --oneline --no-decorate | head -20

echo ""
echo "=== Tool configuration changes ==="
echo "Changes in pyproject.toml:"
git diff HEAD...template/main -- pyproject.toml | head -50

echo ""
echo "Changes in pre-commit config:"
git diff HEAD...template/main -- .pre-commit-config.yaml | head -30

echo ""
echo "=== Workflow changes ==="
git diff --name-only HEAD...template/main -- .github/workflows/

echo ""
echo "=== Next steps ==="
echo "1. Review changes above"
echo "2. Selectively apply relevant changes (DO NOT merge directly)"
echo "3. Test with: hatch run qa"
echo ""
echo "To see full diff of a file:"
echo "  git diff HEAD...template/main -- path/to/file"
echo ""
echo "To copy a specific file (BE CAREFUL):"
echo "  git show template/main:path/to/file > path/to/file"
