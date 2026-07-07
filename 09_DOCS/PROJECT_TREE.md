# STOCK-CIO Project Tree

> Source of Truth for the current project structure.
> Generated artifacts and cache directories are excluded.

```text
Stock-CIO/
|-- 01_PROJECT/
|-- 02_ANALYSIS/
|-- 03_PORTFOLIO/
|-- 04_REPORT/
|-- 05_DATA/
|-- 06_TEMPLATE/
|-- 07_AUTOMATION/
|-- 08_BACKTEST/
|-- 09_DOCS/
|-- 10_CONFIG/
|-- main.py
|-- README.md
|-- requirements.txt
|-- src/
|   |-- analyzers/
|   |-- collectors/
|   |   `-- portfolio_loader.py
|   |-- config/
|   |-- constants/
|   |-- core/
|   |   |-- backtest_engine.py
|   |   |-- cio_engine.py
|   |   |-- decision_engine.py
|   |   `-- portfolio_optimizer.py
|   |-- dashboard/
|   |   |-- dashboard_renderer.py
|   |   `-- portfolio_dashboard_renderer.py
|   |-- models/
|   |   |-- unified_decision.py
|   |   |-- portfolio.py
|   |   |-- position.py
|   |   |-- rebalance_item.py
|   |   |-- rebalance_plan.py
|   |   |-- rebalancing_recommendation.py
|   |   |-- recommendation.py
|   |   `-- risk_report.py
|   |-- reports/
|   |   |-- morning_brief.py
|   |   `-- portfolio_morning_brief_appender.py
|   |-- repositories/
|   |-- scripts/
|   |-- services/
|   |   |-- unified_decision_engine.py
|   |   |-- cio_engine.py
|   |   |-- decision_engine.py
|   |   |-- rebalancing_engine.py
|   |   |-- rebalancing_recommendation_engine.py
|   |   |-- recommendation_engine.py
|   |   |-- risk_analyzer.py
|   |   `-- target_portfolio_builder.py
|   |-- storage/
|   |-- strategies/
|   |   |-- allocation_strategy.py
|   |   |-- buy_and_hold_strategy.py
|   |   |-- equal_weight_strategy.py
|   |   |-- market_value_weight_strategy.py
|   |   |-- rule_based_strategy.py
|   |   `-- strategy.py
|   `-- utils/
`-- tests/
    |-- test_dashboard_data_status.py
    |-- test_portfolio_allocation_output.py
    |-- test_rebalancing_tolerance.py
    |-- test_rule_based_strategy_limits.py
    |-- test_unified_decision_engine.py
    |-- test_configured_portfolio_end_to_end.py
    |-- test_complete_portfolio_pipeline.py
    |-- test_portfolio_output_integration.py
    |-- test_portfolio_outputs.py
    |-- test_portfolio_pipeline.py
    |-- test_portfolio_loader.py
    |-- test_rebalancing_recommendation_from_plan.py
    |-- test_target_portfolio_builder.py
    `-- existing regression test modules
```
