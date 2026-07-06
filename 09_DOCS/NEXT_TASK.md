# NEXT_TASK.md

# STOCK-CIO

## Next Development Task

### Sprint

**Sprint 17**

---

## Feature

**FEATURE-025**

Portfolio Pipeline

---

## Goal

Implement the Portfolio Pipeline currently defined as a stub in the Application Orchestrator.

---

## Background

FEATURE-024 completed the Application Orchestrator and established the end-to-end workflow.

The Portfolio Pipeline currently exists only as a placeholder and should become the bridge between market analysis and portfolio recommendation.

---

## Scope

### Core

- Implement Portfolio Pipeline
- Replace Stub implementation
- Preserve existing workflow
- Maintain shared context

### Services

- Connect Portfolio Analyzer
- Connect Recommendation Engine
- Connect Rebalancing Engine
- Connect Decision Engine

### Output

Generate portfolio-related context for downstream components.

Example:

- Portfolio Analysis
- Portfolio Recommendation
- Rebalancing Recommendation

---

## Workflow

```text
initialize
    ↓
load_market_data
    ↓
analyze_market
    ↓
calculate_score
    ↓
make_market_decision
    ↓
portfolio_pipeline
        ├── Portfolio Analysis
        ├── Recommendation
        ├── Rebalancing
        └── Portfolio Decision
    ↓
render_dashboard
    ↓
generate_morning_brief
    ↓
ready
```

---

## Constraints

- Python 3.14
- Clean Architecture
- One Class = One File
- Full-file Replacement Only
- Business Logic in services
- Workflow in core
- Immutable Model
- Regression Zero

---

## Expected Result

- Portfolio Pipeline implemented
- Existing workflow preserved
- Existing tests continue to pass
- No regression introduced
- Ready for future CIO integrati

# STOCK-CIO Next Task

Version : v0.4.0-alpha

---

## Current Status

Sprint 15 Completed

Build PASS

118 Passed

Regression Zero

Sprint 16 Architecture Completed

---

## Next Sprint

Sprint 16

FEATURE-024

Application Orchestrator

Priority

Highest

---

## Goal

Connect all existing engines through src/core/cio_engine.py and execute the complete investment workflow using:

```bash
python main.py
```

---

## Development Order

1. Review Risk Analyzer
2. Review Recommendation Engine
3. Review Decision Engine
4. Review AI CIO Engine
5. Full-file Replacement of src/core/cio_engine.py
6. pytest
7. Document Update
8. Git Commit

---

## Success Criteria

* Build PASS
* 118 Unit Tests Passed
* Regression Zero
* Existing Architecture Preserved
* Full-file Replacement Only
* Production Quality
