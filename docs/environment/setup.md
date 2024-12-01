# Local Development Setup

This guide will help you set up the documentation environment locally and start contributing.

## Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- Git for version control

## Installation Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd cascade-env-docs
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install --no-root
   ```

   !!! note
       We use `--no-root` because this is a documentation-only project and doesn't need to be installed as a Python package.

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

## Running Documentation Locally

1. Start the development server:

   ```bash
   poetry run mkdocs serve
   ```

2. View the documentation:
   - Open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - The documentation will automatically reload when you make changes

## Making Contributions

1. Create a new branch for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes to the documentation
   - Documentation source files are in the `docs/` directory
   - Files are written in Markdown format
   - Images should be placed in `docs/assets/`

3. Preview your changes locally using `mkdocs serve`

4. Commit your changes:

   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. Push your changes and create a pull request:

   ```bash
   git push origin feature/your-feature-name
   ```

## Testing Changes

1. Verify your changes locally:
   - Check that all links work
   - Ensure images are displayed correctly
   - Verify navigation structure in mkdocs.yml
   - Test both light and dark mode

2. Run pre-commit checks:

   ```bash
   pre-commit run --all-files
   ```

3. Build the documentation locally to catch any build errors:

   ```bash
   poetry run mkdocs build
   ```

## Troubleshooting

### Common Issues

1. Poetry installation fails:
   - Ensure you have Python 3.12+ installed
   - Try updating pip: `pip install --upgrade pip`

2. MkDocs server won't start:
   - Check if port 8000 is already in use
   - Ensure all dependencies are installed
   - Try running `poetry install` again

3. Pre-commit hooks failing:
   - Run `poetry run black .` to format code
   - Run `poetry run isort .` to sort imports
   - Fix any flake8 issues manually

### Getting Help

If you encounter any issues not covered here:

1. Check the [MkDocs documentation](https://www.mkdocs.org/)
2. Check the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
3. Open an issue in the repository
