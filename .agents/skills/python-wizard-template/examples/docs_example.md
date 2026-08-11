# Example Documentation Page

This is an example of how documentation should be structured in projects
using the wizard-template.

## Overview

Use MyST Markdown for documentation. It supports both standard Markdown
and reStructuredText directives.

## Code Examples

Include code blocks with syntax highlighting:

```python
from my_package import DataProcessor

# Create a processor
processor = DataProcessor(multiplier=2.0)

# Process a value
result = processor.process(10)
print(result)  # Output: 20.0
```

## Admonitions

Use admonitions for important information:

```{note}
This is a note admonition. Use it for helpful tips.
```

```{warning}
This is a warning admonition. Use it for important caveats.
```

```{tip}
This is a tip admonition. Use it for best practices.
```

## Cross-References

Link to other documentation pages:

- [Getting Started](../getting-started/index.md)
- [API Reference](../references/api.md)

## API Documentation

Include docstrings in your API docs:

```{eval-rst}
.. automodule:: my_package.module_example
   :members:
   :undoc-members:
   :show-inheritance:
```

## Tables

Use Markdown tables:

| Command | Description |
|---------|-------------|
| `hatch run test` | Run tests with coverage |
| `hatch run lint` | Run linter |
| `hatch run qa` | Run all quality checks |

## Lists

Ordered lists:

1. First step
2. Second step
3. Third step

Unordered lists:

- Item one
- Item two
- Item three

## Images

Include images with captions:

```{figure} ../logo.png
:alt: Project logo
:width: 300px

The project logo.
```

## Math

Include mathematical expressions using LaTeX:

```{math}
E = mc^2
```

Inline math: $a^2 + b^2 = c^2$

## Links

- External link: [Hatch documentation](https://hatch.pypa.io/)
- Internal link: [Introduction](intro.md)
- Reference link: [About the Project][project-link]

[project-link]: https://github.com/your-user/your-project
