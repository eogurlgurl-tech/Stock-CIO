# AI_START.md

> STOCK-CIO Developer Context
> Read this file before implementing any code.

---

# Project

**Name**

STOCK-CIO

**Current Version**

v0.4.0-alpha

---

# Mission

Maintain and extend STOCK-CIO using Production Quality standards.

The objective is long-term maintainability, zero regression, and clean architecture.

---

# Source of Truth

Never assume project structure.

Always use the actual project tree.

Before implementation:

1. Read project structure.
2. Read existing files.
3. Read related tests.
4. Design first.
5. Implement after approval.

---

# Development Rules

* Full-file replacement only.
* Never output partial code.
* Production quality only.
* One class per file.
* Keep existing architecture.
* Regression Zero.
* Backward compatible whenever possible.
* Pytest compatibility is mandatory.
* Prefer pathlib over os.path.
* Use type hints.
* Follow PEP 8.
* Avoid duplicated logic.
* Keep responsibilities separated.

---

# Import Convention

Always follow project imports.

Examples:

```python
from src.models...
from src.core...
from src.repositories...
from src.services...
from src.scripts...
```

Never introduce inconsistent import styles.

---

# Workflow

Every feature follows this sequence:

1. Analyze
2. Design
3. Implement
4. Test
5. Refactor (if necessary)
6. Update documentation

Do not skip steps.

---

# Developer Automation Rules

Automation must never overwrite project documents blindly.

Instead:

* Read existing markdown.
* Update only required sections.
* Preserve manual content.
* Preserve formatting whenever possible.

Automation scripts must use shared utilities.

---

# Documentation

Keep the following documents synchronized.

* STATUS.md
* SESSION.md
* NEXT_TASK.md
* CHANGELOG.md

Automation should update only the relevant sections.

---

# Testing

Run pytest after each completed phase.

Never continue if regression exists.

Goal:

* 100% passing tests
* Zero regression

---

# Coding Style

Prefer:

* Small classes
* Small methods
* Explicit naming
* Dependency injection
* Single responsibility

Avoid:

* Hidden side effects
* Hard-coded paths
* Magic strings
* Global mutable state

---

# Project Structure

Treat the current repository tree as the single source of truth.

Never assume folders or files that do not exist.

---

# Implementation Policy

Before writing code:

* Understand existing implementation.
* Reuse existing architecture.
* Extend rather than replace.
* Keep compatibility.

If required information is missing, request the relevant project files before implementation.

---

# Session Policy

At the beginning of every new development session:

1. Review current project structure.
2. Review current Sprint status.
3. Review related source files.
4. Review related tests.
5. Confirm implementation plan.
6. Start coding.

---

# Completion Checklist

Before considering a feature complete:

* Architecture unchanged
* Tests passing
* No regression
* Documentation updated
* Imports verified
* Formatting verified
* Ready for Git commit

---

# Principle

Read first.

Design second.

Implement third.

Test continuously.

Deliver production-quality code.
