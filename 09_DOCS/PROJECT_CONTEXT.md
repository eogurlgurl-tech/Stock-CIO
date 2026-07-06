
# PROJECT CONTEXT

## Project

Stock-CIO

AI Chief Investment Officer

---

## Source of Truth

실제 프로젝트 코드가 Source of Truth이다.

설계 문서보다 현재 코드를 우선한다.

PROJECT_TREE.md의 구조를 기준으로 개발한다.

---

## Development Rules

- Python 3.14
- Clean Architecture
- One Class = One File
- Full-file Replacement Only
- Regression Zero
- Immutable Model
- Business Logic → services
- Workflow → core
- Existing Interface First
- Optional Parameter Only

---

## Layer Responsibilities

core/
Application Workflow

services/
Business Logic

analyzers/
Analysis

collectors/
External Data

models/
Immutable Models

repositories/
Repository

reports/
Report Generator

dashboard/
Dashboard

strategies/
Strategy Pattern

storage/
Persistence

utils/
Utilities

---

## Duplicate Class

core.CIOEngine
Application Orchestrator

services.CIOEngine
CIO Report Generator

core.DecisionEngine
Market Decision

services.DecisionEngine
Portfolio Decision

---

## Current Status

Version
v0.4.0-alpha

Sprint
17

Build
PASS

Unit Test
118 Passed

Regression
Zero

---

## Current Feature

FEATURE-025
Portfolio Pipeline

Current Scope

- PortfolioLoader
- Portfolio Context
- Dependency Injection
- Skip Processing
- Backward Compatibility

Target Portfolio Generation
Not Implemented

---

## Reference

PROJECT_TREE.md
Architecture.md
Roadmap.md
NEXT_TASK.md
