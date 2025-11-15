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
**meuclaude** (Portuguese for "my Claude") - [Add project description here]

### Technology Stack
- **Language:** [To be determined]
- **Framework:** [To be determined]
- **Build Tool:** [To be determined]
- **Package Manager:** [To be determined]

### Project Goals
[Document the main objectives and goals of this project]

---

## Repository Structure

```
meuclaude/
├── .git/                  # Git version control
├── CLAUDE.md             # This file - AI assistant guide
└── [Other directories to be added as project grows]
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
# List required software and versions
# Example:
# - Node.js >= 18.x
# - Python >= 3.9
# - etc.
```

### Installation Steps
```bash
# Clone the repository
git clone http://local_proxy@127.0.0.1:34416/git/vitrine-show/meuclaude
cd meuclaude

# Install dependencies
# [Add commands here]

# Setup environment
# [Add commands here]
```

### Environment Variables
Document required environment variables:
```bash
# Example:
# DATABASE_URL=
# API_KEY=
# NODE_ENV=development
```

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
- Use lowercase with hyphens for file names: `user-service.js`
- Use PascalCase for class/component files: `UserService.js`
- Test files: `*.test.js` or `*.spec.js`

#### Code Organization
- Group related functionality together
- Keep imports organized (external → internal → relative)
- Export at the bottom of the file (or use named exports inline)

### Testing Conventions

- Write tests for all new features
- Maintain test coverage above [X]%
- Test file location: [Co-located / Separate test directory]
- Test naming: `describe('Component/Function', () => { it('should...', ...) })`

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
# Development mode
# [Add command]

# Production mode
# [Add command]
```

### Running Tests
```bash
# Run all tests
# [Add command]

# Run specific test file
# [Add command]

# Run with coverage
# [Add command]
```

### Building
```bash
# Development build
# [Add command]

# Production build
# [Add command]
```

### Linting and Formatting
```bash
# Run linter
# [Add command]

# Fix linting issues
# [Add command]

# Format code
# [Add command]
```

### Database Operations
```bash
# Run migrations
# [Add command]

# Seed database
# [Add command]

# Reset database
# [Add command]
```

---

## Troubleshooting

### Common Issues

#### Issue: [Common problem]
**Solution:** [How to fix it]

#### Issue: [Another common problem]
**Solution:** [How to fix it]

### Debug Mode
```bash
# Enable debug logging
# [Add command or environment variable]
```

### Getting Help

- Check existing issues in the repository
- Review documentation in `/docs`
- Contact: [Add contact information or links]

---

## Changelog

### Version 1.0.0 - 2025-11-15
- Initial CLAUDE.md creation
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

[Document common patterns used in this codebase as they emerge]

### Known Gotchas

[Document any quirks, workarounds, or non-obvious behaviors]

---

**Remember:** This is a living document. Update it as the project evolves, patterns emerge, and conventions are established.
