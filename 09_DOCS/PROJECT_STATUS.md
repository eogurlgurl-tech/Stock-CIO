# PROJECT STATUS

Version

v1.0.0-rc

Sprint

20

Status

V1 Stabilization - Verified

Build

Completed

Regression Baseline

172 Passed

Expected Test Collection

172 Tests

---

## V1 Required Improvements

Completed in code

- Repeated maximum-weight redistribution
- 1.0%p rebalancing tolerance
- Unified market and portfolio decision
- Current and target allocation output
- Final decision reason output
- Market and news data collection status
- Korean desktop output
- Yahoo Finance market news collection

Completed

- Full pytest verification
- Windows EXE rebuild
- Packaged application verification
- Version release confirmation

---

## Architecture Contract

- PortfolioOptimizer calculates Current Portfolio weights.
- TargetPortfolioBuilder creates a separate Target Portfolio.
- RebalancingEngine applies tolerance without changing inputs.
- UnifiedDecisionEngine combines market and portfolio actions.
- CIOEngine owns workflow orchestration.
