# CHANGELOG

---

## v0.4.0-alpha

### Sprint 18

#### FEATURE-026 Target Portfolio Pipeline

Added

- TargetPortfolioBuilder
- PortfolioDashboardRenderer
- PortfolioMorningBriefAppender
- RebalancePlan to RebalancingRecommendation conversion
- Portfolio Pipeline unit and integration tests

Updated

- PortfolioOptimizer current-weight contract restored
- RecommendationEngine RiskReport evaluation restored
- CIOEngine Portfolio Workflow completed
- Dashboard Portfolio output connected
- MorningBrief Portfolio output connected

Architecture

- Current Portfolio and Target Portfolio responsibilities separated
- Business logic remains in services
- Workflow orchestration remains in core
- Existing interfaces preserved

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
