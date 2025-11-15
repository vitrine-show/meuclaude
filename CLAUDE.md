# CLAUDE.md - AI Assistant Guide

> **Version:** 1.0.0
> **Last Updated:** 2025-11-15
> **Repository:** meuclaude

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Development Setup](#development-setup)
4. [Development Workflows](#development-workflows)
5. [Key Conventions](#key-conventions)
6. [AI Assistant Guidelines](#ai-assistant-guidelines)
7. [Common Tasks](#common-tasks)
8. [Troubleshooting](#troubleshooting)

---

## Overview

### Project Description
**meuclaude** (Portuguese for "my Claude") - Um gerenciador de tarefas CLI inteligente, escrito em Python. Perfeito para desenvolvedores que vivem no terminal!

### Technology Stack
- **Language:** Python >= 3.8
- **CLI Framework:** Click >= 8.1.0
- **Testing:** pytest >= 7.4.0
- **Package Manager:** pip
- **Build Tool:** setuptools

### Project Goals
- Fornecer uma ferramenta CLI rápida e eficiente para gerenciamento de tarefas
- Demonstrar boas práticas de desenvolvimento Python
- Servir como exemplo de projeto bem documentado e testado
- Integração amigável com assistentes de IA

---

## Repository Structure

```
meuclaude/
├── .git/                  # Git version control
├── src/                   # Source code
│   ├── __init__.py
│   ├── todo_manager.py    # Core task management logic
│   └── cli.py             # Command-line interface
├── tests/                 # Unit tests
│   ├── __init__.py
│   └── test_todo_manager.py
├── docs/                  # Additional documentation
├── .gitignore
├── CLAUDE.md             # This file - AI assistant guide
├── README.md             # User documentation
├── requirements.txt      # Python dependencies
└── pyproject.toml        # Project configuration
```

### Directory Conventions

As the project grows, document the purpose of each major directory:

- **`src/`** - Source code
- **`tests/`** - Test files
- **`docs/`** - Documentation
- **`config/`** - Configuration files
- **`scripts/`** - Build and utility scripts
- **`assets/`** - Static assets (images, fonts, etc.)

---

## Development Setup

### Prerequisites
```bash
# Required software and versions:
# - Python >= 3.8
# - pip (package installer for Python)
# - virtualenv (recommended)
```

### Installation Steps
```bash
# Clone the repository
git clone http://local_proxy@127.0.0.1:34416/git/vitrine-show/meuclaude
cd meuclaude

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Environment Variables
This project does not require environment variables.

Tasks are stored in `~/.meuclaude/todos.json` by default.

---

## Development Workflows

### Branch Strategy

- **Main Branch:** `main` (or `master`)
- **Feature Branches:** `claude/claude-md-<session-id>`
- **Branch Naming Convention:**
  - Features: `feature/<feature-name>`
  - Bugfixes: `fix/<bug-name>`
  - Hotfixes: `hotfix/<fix-name>`
  - AI-assisted: `claude/claude-md-<session-id>`

### Git Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Make changes and commit:**
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

3. **Push changes:**
   ```bash
   git push -u origin feature/my-feature
   ```

4. **Create Pull Request:**
   - Review changes
   - Request reviews from team members
   - Merge when approved

### Commit Message Conventions

Follow conventional commits format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat(auth): add user authentication

Implement JWT-based authentication with refresh tokens.
Includes login, logout, and token refresh endpoints.

Closes #123
```

---

## Key Conventions

### Code Style

#### General Principles
- Write clear, self-documenting code
- Use meaningful variable and function names
- Keep functions small and focused (Single Responsibility Principle)
- Comment complex logic, not obvious code
- Follow DRY (Don't Repeat Yourself) principle

#### File Naming
- Use lowercase with underscores for Python files: `todo_manager.py`
- Use PascalCase for class names: `TodoManager`, `TaskStatus`
- Test files: `test_*.py`
- Follow PEP 8 style guide

#### Code Organization
- Group related functionality together
- Keep imports organized (standard library → third-party → local)
- Use type hints for function parameters and return values
- Write docstrings for all public methods and classes

### Testing Conventions

- Write tests for all new features
- Maintain test coverage above 80%
- Test file location: Separate `tests/` directory
- Test naming: `test_<function_name>()` or `test_<description>()`
- Use pytest fixtures for setup/teardown
- Run tests with: `pytest`
- Check coverage with: `pytest --cov=src --cov-report=html`

### Documentation Standards

- Document all public APIs
- Include usage examples in documentation
- Keep README.md up to date
- Document breaking changes in CHANGELOG.md

---

## AI Assistant Guidelines

### When Working on This Codebase

#### DO:
✅ Read existing code before making changes
✅ Follow established patterns and conventions
✅ Write tests for new functionality
✅ Update documentation when changing behavior
✅ Use descriptive commit messages
✅ Ask for clarification when requirements are unclear
✅ Consider backwards compatibility
✅ Look for existing utilities before creating new ones
✅ Use the TodoWrite tool for multi-step tasks
✅ Check security implications (OWASP Top 10)

#### DON'T:
❌ Make breaking changes without discussion
❌ Commit commented-out code
❌ Skip writing tests
❌ Ignore linting/formatting errors
❌ Push directly to main/master
❌ Use hard-coded secrets or credentials
❌ Introduce unnecessary dependencies
❌ Ignore error handling

### Code Review Checklist

Before committing changes, verify:
- [ ] Code follows project conventions
- [ ] Tests are passing
- [ ] No console.log or debug statements
- [ ] Error handling is implemented
- [ ] Documentation is updated
- [ ] No security vulnerabilities introduced
- [ ] Performance implications considered
- [ ] Backwards compatibility maintained

### Security Considerations

- Never commit secrets, API keys, or credentials
- Validate and sanitize all user inputs
- Use parameterized queries to prevent SQL injection
- Implement proper authentication and authorization
- Keep dependencies up to date
- Follow principle of least privilege
- Be aware of common vulnerabilities:
  - XSS (Cross-Site Scripting)
  - CSRF (Cross-Site Request Forgery)
  - SQL Injection
  - Command Injection
  - Insecure Deserialization

---

## Common Tasks

### Running the Project
```bash
# After installation, use the CLI:
meuclaude --help

# Add a task
meuclaude add "My task"

# List tasks
meuclaude list

# See all available commands
meuclaude --help
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_todo_manager.py

# Run with coverage
pytest --cov=src --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Installing the Package
```bash
# Development installation (editable)
pip install -e .

# Production installation
pip install .
```

### Code Quality
```bash
# Python has many linting/formatting tools (not yet configured)
# Future additions could include:
# - black (code formatter)
# - flake8 (linter)
# - mypy (type checker)
# - isort (import sorter)
```

### Data Storage
```bash
# Tasks are stored in JSON format
# Default location: ~/.meuclaude/todos.json

# To reset all data, simply delete the file:
rm ~/.meuclaude/todos.json
```

---

## Troubleshooting

### Common Issues

#### Issue: Command 'meuclaude' not found
**Solution:** Make sure you've installed the package with `pip install -e .` and that your virtual environment is activated.

#### Issue: Import errors when running tests
**Solution:** Install the package in development mode: `pip install -e .`

#### Issue: Permission denied when writing to todos.json
**Solution:** Check permissions on `~/.meuclaude/` directory. Create it manually if needed: `mkdir -p ~/.meuclaude`

### Debug Mode
```bash
# For debugging, you can check the stored data directly:
cat ~/.meuclaude/todos.json

# Run Python in interactive mode to test functions:
python -i -m src.todo_manager
```

### Getting Help

- Check existing issues in the repository
- Review documentation in `/docs`
- Contact: [Add contact information or links]

---

## Changelog

### Version 0.1.0 - 2025-11-15
- Initial project creation
- Implemented core task management functionality
- Added CLI interface with Click
- Created comprehensive test suite
- Established documentation structure
- Defined AI assistant guidelines

---

## Additional Resources

- [Project Wiki](#)
- [API Documentation](#)
- [Contributing Guidelines](#)
- [Code of Conduct](#)

---

## Notes for AI Assistants

### Context Gathering Strategy

When asked to work on this project:

1. **First Time:**
   - Read this CLAUDE.md file completely
   - Explore the repository structure
   - Check package.json / requirements.txt / etc.
   - Review README.md if it exists
   - Look at recent commits to understand recent changes

2. **Before Making Changes:**
   - Use Grep/Glob to find relevant files
   - Read the files you'll be modifying
   - Check for existing tests
   - Look for similar implementations

3. **During Implementation:**
   - Use TodoWrite for task tracking
   - Follow existing code patterns
   - Write tests alongside code
   - Update documentation

4. **After Implementation:**
   - Run tests
   - Check for linting errors
   - Review security implications
   - Update CHANGELOG if needed
   - Commit with descriptive message

### Project-Specific Patterns

1. **Task Status Management**: All task status changes go through `Task.update_status()` which automatically updates the `updated_at` timestamp.

2. **Data Persistence**: The `TodoManager` automatically saves to disk after every modification (add, update, delete). This ensures data is never lost.

3. **ID Assignment**: Task IDs are auto-incremented and never reused, even after deletion.

4. **CLI Design**: Each CLI command is self-contained and creates its own `TodoManager` instance. This ensures commands are stateless.

5. **Emoji Usage**: Status icons are consistently used throughout the application:
   - ⏳ Pending
   - 🔄 In Progress
   - ✅ Completed
   - ❌ Cancelled

### Known Gotchas

1. **Storage Location**: Tasks are stored in the user's home directory (`~/.meuclaude/`), not in the project directory. This allows the CLI to work from anywhere.

2. **JSON Encoding**: The storage file uses UTF-8 encoding with `ensure_ascii=False` to support Portuguese and other non-ASCII characters properly.

3. **Enum Serialization**: `TaskStatus` is an Enum that must be converted to/from its `.value` when serializing to JSON.

4. **Click Confirmation**: The `delete` and `clear` commands use Click's confirmation prompts for safety.

---

**Remember:** This is a living document. Update it as the project evolves, patterns emerge, and conventions are established.
