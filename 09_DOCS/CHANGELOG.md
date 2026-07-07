# CHANGELOG

---

## v1.0.0-rc

### Sprint 20 - V1 Stabilization

Added

- UnifiedDecision model and engine
- Rebalancing tolerance
- Current and target allocation output
- Data collection status output
- Korean desktop decision output
- Live market news collection

Fixed

- Maximum position weight could be exceeded after redistribution
- Missing score categories incorrectly reduced total score
- pykrx index collection failure through Yahoo fallback
- Internal Context keys exposed to desktop users
- Conflicting market and portfolio actions lacked a final decision

Status

- Verification Complete
- Current baseline: 172 Passed
- Package verified: dist\STOCK-CIO\STOCK-CIO.exe

---

## v0.4.0-alpha

### Sprint 19

#### FEATURE-027 Portfolio Data Integration

Added

- YAML Portfolio configuration schema
- PortfolioLoader validation
- Configured Portfolio end-to-end test

Validated

- Configuration to Portfolio mapping
- Portfolio Pipeline decision flow
- Dashboard Portfolio output
- MorningBrief Portfolio output

Result

- v0.4 MVP Completed
- Build PASS
- 149 Passed
- Regression Zero

---

### Sprint 18

#### FEATURE-026 Target Portfolio Pipeline

Added

- TargetPortfolioBuilder
- PortfolioDashboardRenderer
- PortfolioMorningBriefAppender
- RebalancePlan recommendation conversion
- Portfolio Pipeline unit and integration tests

Updated

- PortfolioOptimizer current-weight contract restored
- RecommendationEngine RiskReport evaluation restored
- CIOEngine Portfolio Workflow completed

Result

- Build PASS
- 135 Passed
- Regression Zero

---

### Sprint 17

#### FEATURE-025 Portfolio Pipeline

Added

- PortfolioLoader
- Portfolio Context
- Portfolio dependency injection

Result

- Build PASS
- 118 Passed
- Regression Zero
