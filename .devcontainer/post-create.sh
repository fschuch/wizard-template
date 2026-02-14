#!/bin/bash
set -e

echo "🚀 Starting post-create setup..."

# Install pyenv for managing multiple Python versions
# Note: pyenv-installer is the official pyenv installation method
# See: https://github.com/pyenv/pyenv-installer
echo "📦 Installing pyenv..."
curl -fsSL https://pyenv.run | bash

# Add pyenv to PATH for this script
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Configure shell for pyenv
echo '' >> ~/.bashrc
echo '# Pyenv configuration' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Install required Python versions
echo "🐍 Installing Python versions..."
PYTHON_VERSIONS=("3.10" "3.11" "3.12" "3.13" "3.14")

for version in "${PYTHON_VERSIONS[@]}"; do
    echo "Installing Python $version..."
    # Get the latest patch version for each minor version
    latest_patch=$(pyenv install --list | grep -E "^\s*$version\.[0-9]+$" | tail -1 | tr -d ' ')
    if [ -n "$latest_patch" ]; then
        pyenv install -s "$latest_patch"
        echo "✅ Installed Python $latest_patch"
    else
        echo "⚠️  Could not find Python $version"
    fi
done

# Set all installed versions as global (available system-wide)
echo "🔧 Configuring global Python versions..."
INSTALLED_VERSIONS=$(pyenv versions --bare | tr '\n' ' ')
pyenv global $INSTALLED_VERSIONS

# Verify Python installations
echo "✅ Available Python versions:"
pyenv versions

# Verify hatch is available
echo "🔍 Verifying hatch installation..."
if command -v hatch &> /dev/null; then
    echo "✅ Hatch is installed: $(hatch --version)"
else
    echo "⚠️  Hatch not found, installing via pipx..."
    pipx install hatch
fi

# Configure hatch to use local virtual environments
echo "🔧 Configuring hatch..."
hatch config set dirs.env.virtual .venv

# Install pre-commit hooks
echo "📋 Installing pre-commit hooks..."
hatch run pre-commit-install

echo "✨ Post-create setup complete!"
echo ""
echo "Available Python versions:"
pyenv versions
echo ""
echo "To use a specific Python version, run:"
echo "  pyenv shell <version>  # For current shell"
echo "  pyenv local <version>  # For current directory"
echo ""
echo "Hatch will automatically use the appropriate Python version based on the matrix configuration."
