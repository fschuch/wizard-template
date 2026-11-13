# Python Wizard Template Agent Skill

This directory contains an [Agent Skill](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) for GitHub Copilot and other AI assistants.

## What is This?

This skill teaches AI assistants how to work effectively with Python projects that use the wizard-template. It provides comprehensive guidance for:

1. **New projects** - Starting fresh from the template
2. **Migration** - Applying template structure to existing projects  
3. **Updates** - Incorporating template changes into your project
4. **Best practices** - Following wizard-template conventions

## How AI Assistants Use This

When you work with a project that uses wizard-template:

- AI assistants (like GitHub Copilot) automatically load this skill
- They learn about Hatch commands, code quality standards, and project structure
- They can help with common tasks like adding modules, writing tests, and updating configurations
- They provide better suggestions that follow wizard-template conventions

## Installation Options

### Option 1: Comes with Template (Default)

If you created your project from wizard-template, this skill is already included! AI assistants will automatically use it when working in your repository.

### Option 2: User-Level Installation

To use this skill across **all** your repositories (not just template-based ones):

```bash
# Copy to your user skills directory
mkdir -p ~/.agents/skills
cp -r .agents/skills/python-wizard-template ~/.agents/skills/

# Or symlink if you have wizard-template cloned locally
ln -s /path/to/wizard-template/.agents/skills/python-wizard-template ~/.agents/skills/python-wizard-template
```

### Option 3: Add to Existing Project

To add this skill to a project that didn't start from wizard-template:

```bash
# In your project directory
mkdir -p .agents/skills
cp -r /path/to/wizard-template/.agents/skills/python-wizard-template .agents/skills/
git add .agents
git commit -m "Add wizard-template agent skill"
```

## What's Inside

```
python-wizard-template/
├── SKILL.md                    # Main skill definition (comprehensive guide)
├── examples/                   # Example code following best practices
│   ├── module_example.py      # Example module with proper style
│   ├── test_example.py        # Example tests with various patterns
│   └── docs_example.md        # Example documentation page
└── templates/                  # Code templates
    ├── module_template.py     # Template for new modules
    ├── test_template.py       # Template for new tests
    └── check-template-updates.sh  # Helper script for checking updates
```

## Covered Scenarios

The skill provides guidance for:

### For New Projects
- Running the renaming wizard (`hatch run _wizard`)
- Setting up development environment
- Installing pre-commit hooks
- Understanding project structure

### For Existing Projects (Migration)
- Assessing current project structure
- Choosing migration strategy (full vs. gradual)
- Applying template configurations selectively
- Testing after migration

### For Updates
- Tracking template changes
- Selectively applying updates
- Avoiding common pitfalls
- Testing changes

### For Daily Development
- Using Hatch commands correctly
- Following code quality standards
- Writing proper docstrings
- Maintaining test coverage
- Building documentation

## Relationship with copilot-instructions.md

This skill **complements** `.github/copilot-instructions.md`:

- **copilot-instructions.md**: Quick reference, always loaded
- **This skill**: Comprehensive guide, loaded on-demand

Both files serve different purposes and are maintained separately. The skill provides deeper guidance for complex scenarios like migration and updates, while copilot-instructions.md provides quick context for everyday development.

## Learn More

- [Full wizard-template documentation](https://docs.fschuch.com/wizard-template)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Template repository](https://github.com/fschuch/wizard-template)

## Contributing

Found an issue or have a suggestion? Please [open an issue](https://github.com/fschuch/wizard-template/issues) in the wizard-template repository.
