"""
Developer Automation Configuration

Shared constants for automation scripts.
"""

from __future__ import annotations

# ----------------------------------------------------------------------
# Markdown Headings
# ----------------------------------------------------------------------

CURRENT_STATUS_HEADING = "## Current Status"

NEXT_TASK_HEADING = "## Next Task"

CURRENT_SESSION_HEADING = "## Current Session"

CHANGELOG_HEADING = "## Changelog"

# ----------------------------------------------------------------------
# Default Values
# ----------------------------------------------------------------------

DEFAULT_BUILD_STATUS = "PASS"

DEFAULT_TEST_RESULT = "Unknown"

DEFAULT_VERSION = "v0.4.0-alpha"

# ----------------------------------------------------------------------
# Date Format
# ----------------------------------------------------------------------

DATE_FORMAT = "%Y-%m-%d"

DATETIME_FORMAT = "%Y-%m-%d %H:%M"

# ----------------------------------------------------------------------
# Markdown Templates
# ----------------------------------------------------------------------

CHANGELOG_TEMPLATE = "- {date} | {feature} | {description}"

SESSION_TEMPLATE = (
    "- Feature: {feature}\n"
    "- Sprint: {sprint}\n"
    "- Build: {build}\n"
    "- Tests: {tests}"
)

STATUS_TEMPLATE = (
    "- Version: {version}\n"
    "- Sprint: {sprint}\n"
    "- Current Feature: {feature}\n"
    "- Build: {build}\n"
    "- Unit Tests: {tests}"
)