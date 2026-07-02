
# STOCK-CIO Next Task

Version : v2.2.0-alpha

Last Update : 2026-06-30

---

# Sprint

Sprint 7

---

# Current Feature

FEATURE-014

Morning Brief Upgrade

---

# Current Status

STEP6 Complete

Build Green

31 Tests Passed

---

# Next Task

STEP7

Today's CIO Comment

---

# Goal

Complete the final section of Morning Brief.

Generate practical CIO comments based on:

- Score
- CIO Decision

Return natural Markdown bullet comments instead of a table.

---

# Expected Method

_generate_cio_comment(
    score,
    decision,
)

---

# Output Example

Today's CIO Comment

- Global macro environment remains favorable.
- Overall investment score remains weak.
- Maintain defensive allocation.
- Recommended cash ratio : 80%.

---

# Development Order

STEP7

↓

Unit Test

↓

Integration Test

↓

Morning Brief Final Review

↓

Commit

---

# Working Rules

Feature Development Only

One Feature At A Time

No Architecture Change

Build Must Stay Green

Review current file before every modification.

---

# Build Verification

python main.py

↓

PASS

python -m pytest

↓

31 Passed

↓

Commit

---

# After FEATURE-014

FEATURE-015

Dashboard

↓

FEATURE-016

Backtest

↓

FEATURE-017

Portfolio Optimizer

↓

FEATURE-018

AI CIO
