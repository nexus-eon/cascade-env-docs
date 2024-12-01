# Tools Usage Guide

This guide provides detailed instructions on how to use the various tools in the Cascade Environment effectively.

## MkDocs

### Basic Commands

1. **Serve Documentation**

   ```bash
   mkdocs serve
   ```

   - Starts local server
   - Auto-reloads on changes
   - Available at <http://127.0.0.1:8000>

2. **Build Documentation**

   ```bash
   mkdocs build
   ```

   - Creates static site
   - Output in `site/` directory

3. **Create New Pages**

   ```bash
   touch docs/new-page.md
   ```

   - Add to mkdocs.yml navigation
   - Follow style guide

### Advanced Features

1. **Search**
   - Built-in search functionality
   - Indexes all documentation
   - Supports highlighting

2. **Navigation**
   - Tab-based navigation
   - Section collapsing
   - "Back to top" button

## Poetry

### Package Management

1. **Install Dependencies**

   ```bash
   poetry install --no-root
   ```

   - Creates virtual environment
   - Installs all dependencies

2. **Add Dependencies**

   ```bash
   poetry add package-name
   ```

   - Updates pyproject.toml
   - Maintains lock file

3. **Update Dependencies**

   ```bash
   poetry update
   ```

   - Updates to latest versions
   - Respects version constraints

### Environment Management

1. **Activate Environment**

   ```bash
   poetry shell
   ```

   - Activates virtual environment
   - Sets up PATH

2. **Run Commands**

   ```bash
   poetry run command
   ```

   - Runs in virtual environment
   - No activation needed

## Pre-commit Hooks

### Setup

1. **Install Hooks**

   ```bash
   pre-commit install
   ```

   - Enables git hooks
   - Runs automatically

2. **Manual Run**

   ```bash
   pre-commit run --all-files
   ```

   - Check all files
   - Fix formatting

### Available Hooks

1. **Black**
   - Code formatting
   - PEP 8 compliance
   - Consistent style

2. **isort**
   - Import sorting
   - Grouping imports
   - Maintaining order

3. **flake8**
   - Code linting
   - Style checking
   - Error detection

## Best Practices

### Documentation

1. **Writing**
   - Follow style guide
   - Use templates
   - Include examples

2. **Organization**
   - Logical structure
   - Clear navigation
   - Consistent naming

### Development

1. **Version Control**
   - Commit often
   - Clear messages
   - Follow branching strategy

2. **Code Quality**
   - Run hooks before commit
   - Address all warnings
   - Test changes

## Troubleshooting

### Common Issues

1. **MkDocs**
   - Port conflicts
   - Build errors
   - Navigation issues

2. **Poetry**
   - Dependency conflicts
   - Environment issues
   - Installation problems

### Solutions

1. **Port Conflicts**

   ```bash
   mkdocs serve -a localhost:8001
   ```

2. **Dependency Issues**

   ```bash
   poetry update --lock
   ```

## Related Resources

- [Environment Setup](../environment/setup.md)
- [Configuration Guide](../environment/configuration.md)
- [Style Guide](../development/style-guide.md)
