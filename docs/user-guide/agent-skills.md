# AI Agent Skills

The wizard-template includes a comprehensive [Agent Skill](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) for GitHub Copilot and other AI assistants. This skill teaches AI how to work effectively with projects that use wizard-template patterns and conventions.

## What Are Agent Skills?

Agent Skills are special instruction sets that teach AI assistants about specific workflows, patterns, and best practices. They provide:

- **Context-aware guidance**: AI understands your project structure and conventions
- **Task-specific help**: Detailed instructions for common scenarios
- **Code examples**: Patterns and templates that follow best practices
- **Troubleshooting**: Solutions to common problems

## Wizard-Template Agent Skill

The wizard-template agent skill is located in `.agents/skills/python-wizard-template/` and provides comprehensive guidance for:

### Scenario 1: New Projects from Template

When starting a new project from wizard-template, the skill helps AI assistants:

- Recognize the need to run `hatch run _wizard` first
- Guide through initial setup and configuration
- Explain project structure and conventions
- Help with first module and test creation

### Scenario 2: Applying Template to Existing Projects

When you want to migrate an existing Python project to use wizard-template structure, the skill provides:

- **Assessment guidance**: How to analyze your current project structure
- **Migration strategies**: Full migration vs. gradual adoption
- **Step-by-step instructions**: Detailed migration phases
- **Safety practices**: Backing up and testing changes

Example migration workflow:

```bash
# 1. Backup current state
git checkout -b backup-before-wizard-template
git checkout -b migrate-to-wizard-template

# 2. Clone template for reference
cd /tmp
git clone https://github.com/fschuch/wizard-template.git wizard-ref

# 3. Copy and adapt configurations
# (AI assistant helps identify what to copy/adapt)

# 4. Test incrementally
hatch run qa
```

### Scenario 3: Updating Projects with Template Changes

When wizard-template releases updates, the skill helps:

- Track template changes over time
- Selectively apply relevant updates
- Avoid breaking changes
- Test after each update

Example update workflow:

```bash
# Add template as remote (one-time)
git remote add template https://github.com/fschuch/wizard-template.git
git fetch template

# Check for updates
git log HEAD..template/main --oneline

# Review specific changes
git diff HEAD...template/main -- pyproject.toml

# Apply selectively (never merge directly!)
# AI assistant helps identify what to update
```

A helper script is provided in the skill's templates directory.

## Installation Options

### Option 1: Project-Level (Default)

If you created your project from wizard-template, the skill is already included in `.agents/skills/`. All team members working on the repository automatically benefit.

**Pros:**
- Automatic for all contributors
- Version controlled with project
- Team-wide consistency

**Cons:**
- Only available in this repository

### Option 2: User-Level (Personal)

Install the skill globally for your user account to use across **all** repositories:

```bash
# Copy to user skills directory
mkdir -p ~/.agents/skills
cp -r .agents/skills/python-wizard-template ~/.agents/skills/

# Or symlink if you have wizard-template cloned locally
ln -s /path/to/wizard-template/.agents/skills/python-wizard-template ~/.agents/skills/python-wizard-template
```

**Pros:**
- Available in all repositories you work on
- Personal productivity boost
- Works even in non-template projects

**Cons:**
- Not shared with team members
- Requires manual installation/updates

### Option 3: Organization-Level (Future)

GitHub is developing organization-wide agent skills. When available, organizations will be able to deploy skills centrally for all members and repositories.

## How AI Assistants Use the Skill

When you work with Copilot or other AI assistants in a wizard-template project:

1. **Automatic detection**: The AI recognizes you're using wizard-template
2. **Skill loading**: Relevant sections of the skill are loaded based on context
3. **Enhanced suggestions**: AI provides wizard-template-specific guidance
4. **Pattern following**: Suggestions follow template conventions

For example:

- When adding a new module, AI suggests Google-style docstrings and type hints
- When writing tests, AI uses pytest patterns with proper fixtures
- When updating configs, AI checks template best practices
- When you ask about Hatch commands, AI provides correct usage

## Skill Contents

The agent skill includes:

```
.agents/skills/python-wizard-template/
├── SKILL.md                      # Main skill definition
│   ├── Scenario 1: New projects
│   ├── Scenario 2: Migration
│   ├── Scenario 3: Updates
│   ├── Hatch commands
│   ├── Code quality standards
│   └── Troubleshooting
├── examples/
│   ├── module_example.py        # Example module with best practices
│   ├── test_example.py          # Example tests with patterns
│   └── docs_example.md          # Example documentation
├── templates/
│   ├── module_template.py       # Template for new modules
│   ├── test_template.py         # Template for new tests
│   └── check-template-updates.sh  # Helper script
└── README.md                     # Installation and usage guide
```

## Relationship with Copilot Instructions

The agent skill **complements** `.github/copilot-instructions.md`:

| File | Purpose | When Loaded | Best For |
|------|---------|-------------|----------|
| `.github/copilot-instructions.md` | Quick reference | Always | Everyday development |
| `.agents/skills/python-wizard-template/` | Comprehensive guide | On-demand | Complex scenarios |

Both are maintained and serve different purposes:

- **copilot-instructions.md**: Provides context that's always available for quick lookups
- **Agent skill**: Provides detailed workflows for migration, updates, and troubleshooting

## Using the Skill Effectively

### For New Projects

When you start a new project from the template, simply work naturally with your AI assistant. It will:

- Remind you to run `hatch run _wizard` if needed
- Suggest proper project structure
- Help with initial module creation
- Guide testing and documentation

### For Migration

When migrating an existing project, tell your AI assistant explicitly:

> "I want to apply wizard-template structure to this project. Help me assess and migrate."

The AI will:

- Analyze your current structure
- Suggest a migration strategy
- Guide you through each phase
- Help test changes

### For Updates

When updating from template changes, ask:

> "Check if there are updates in wizard-template and help me apply them."

The AI will:

- Help you compare with template
- Identify relevant changes
- Suggest what to update
- Warn about potential breaking changes

## Example Interactions

### Getting Started

**You:** "How do I add a new module to this project?"

**AI (with skill):** "In wizard-template projects, create your module in `src/{project_name}/` with Google-style docstrings and type hints. Here's the pattern..."

### Migration Help

**You:** "I have an existing Python project. How can I adopt wizard-template structure?"

**AI (with skill):** "Let's assess your project first. I can help you either with a full migration or gradual adoption. First, let me check your current structure..."

### Update Assistance

**You:** "How do I update my project with the latest template changes?"

**AI (with skill):** "Let's add the template as a remote and check for updates. Run: `git remote add template https://github.com/fschuch/wizard-template.git && git fetch template`..."

## Troubleshooting

### AI Not Using the Skill

If your AI assistant doesn't seem to be using the skill:

1. **Verify the skill exists**: Check `.agents/skills/python-wizard-template/SKILL.md` exists
2. **Update your AI tool**: Ensure you're using a version that supports agent skills
3. **Be explicit**: Mention "wizard-template" in your questions
4. **Check configuration**: Some tools require enabling agent skills in settings

### Skill Not Found in Other Repos

If you want to use the skill in repositories that don't include it:

- Install at user-level (see Installation Options section above, Option 2)
- Or copy the skill directory to your project

### Skill Conflicts

If you have multiple skills with similar guidance:

- Project-level skills take precedence over user-level
- More specific skills override general ones
- You can disable specific skills in your AI tool settings

## Learn More

- [GitHub Copilot Agent Skills Documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- Wizard-Template Agent Skill README (in `.agents/skills/python-wizard-template/README.md`)
- Copilot Instructions (in `.github/copilot-instructions.md`)

## Contributing to the Skill

Found an issue or have suggestions for the agent skill?

1. [Open an issue](https://github.com/fschuch/wizard-template/issues)
2. Describe what guidance could be improved
3. Provide examples of AI mistakes or missing information

The skill is continuously improved based on real-world usage and feedback.
