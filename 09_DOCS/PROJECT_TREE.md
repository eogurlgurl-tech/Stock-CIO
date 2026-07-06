
# STOCK-CIO Project Tree

> Source of Truth
>
> 본 문서는 실제 프로젝트 구조를 관리한다.
> 신규 Feature 작업 전 반드시 본 문서를 기준으로 한다.
> tree /f 갱신 시 함께 업데이트한다.

D:.
│  main.py
│  README.md
│  requirements.txt
│
├─.github
├─.gitignore
├─.pytest_cache
│  │  .gitignore
│  │  CACHEDIR.TAG
│  │  README.md
│  │
│  └─v
│      └─cache
│              lastfailed
│              nodeids
│
├─01_PROJECT
│      CHANGELOG.md
│      CHECKLIST.md
│      INVESTMENT_PLAYBOOK.md
│      metadata.md
│      PROJECT_STATUS.md
│      README.md
│
├─02_ANALYSIS
│      AI.md
│      Foreign.md
│      Macro.md
│      Market.md
│      MARKET_RULEBOOK.md
│      Sector.md
│      Semiconductor.md
│
├─03_PORTFOLIO
│      PORTFOLIO.md
│      TRADING_JOURNAL.md
│      WATCHLIST.md
│
├─04_REPORT
│  │  Evening_Report.md
│  │  Monthly_Report.md
│  │  Morning_Brief.md
│  │  Weekly_Report.md
│  │
│  ├─DAILY
│  │      2026-06-24.md
│  │      2026-06-25.md
│  │      2026-06-30.md
│  │      2026-07-02.md
│  │      Daily_Report.md
│  │
│  ├─MONTHLY
│  └─WEEKLY
├─05_DATA
├─06_TEMPLATE
├─07_AUTOMATION
├─08_BACKTEST
├─09_DOCS
│      AI_START.md
│      API.md
│      Architecture.md
│      CHANGELOG.md
│      DataFlow.md
│      NEXT_TASK.md
│      PROJECT_CONTEXT.md
│      project_state.json
│      PROJECT_STATUS.md
│      Roadmap.md
│      SESSION.md
│      Version.md
│
├─10_CONFIG
│      .env
│      app.yaml
│      market.yaml
│      news.yaml
│      portfolio.yaml
│      report.yaml
│      score.yaml
│      strategy.yaml
│      weight.yaml
│
├─src
│  │  __init__.py
│  │
│  ├─analyzers
│  │  │  macro_analyzer.py
│  │  │  market_analyzer.py
│  │  │  news_analyzer.py
│  │  │  performance_analyzer.py
│  │  │  portfolio_analyzer.py
│  │  │  score_engine.py
│  │  │  stock_screener.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          macro_analyzer.cpython-314.pyc
│  │          market_analyzer.cpython-314.pyc
│  │          news_analyzer.cpython-314.pyc
│  │          performance_analyzer.cpython-314.pyc
│  │          score_engine.cpython-314.pyc
│  │          stock_screener.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─collectors
│  │  │  base_collector.py
│  │  │  base_loader.py
│  │  │  historical_data_loader.py
│  │  │  krx_loader.py
│  │  │  market_data_loader.py
│  │  │  news_collector.py
│  │  │  news_loader.py
│  │  │  portfolio_loader.py
│  │  │  us_loader.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          base_collector.cpython-314.pyc
│  │          base_loader.cpython-314.pyc
│  │          historical_data_loader.cpython-314.pyc
│  │          krx_loader.cpython-314.pyc
│  │          market_data_loader.cpython-314.pyc
│  │          news_collector.cpython-314.pyc
│  │          us_loader.cpython-314.pyc
│  │          yahoo_loader.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─config
│  │  │  config_manager.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          config_manager.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─constants
│  │  │  actions.py
│  │  │  decision_type.py
│  │  │  rebalance_action.py
│  │  │  rebalancing_action.py
│  │  │  risk_level.py
│  │  │  sectors.py
│  │  │
│  │  └─__pycache__
│  │          decision_type.cpython-314.pyc
│  │          rebalance_action.cpython-314.pyc
│  │          rebalancing_action.cpython-314.pyc
│  │          risk_level.cpython-314.pyc
│  │
│  ├─core
│  │  │  backtest_engine.py
│  │  │  cio_engine.py
│  │  │  decision_engine.py
│  │  │  portfolio_optimizer.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          backtest_engine.cpython-314.pyc
│  │          cio_engine.cpython-314.pyc
│  │          decision_engine.cpython-314.pyc
│  │          portfolio_optimizer.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─dashboard
│  │  │  dashboard_renderer.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          dashboard_renderer.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─models
│  │  │  backtest_result.py
│  │  │  cio_decision.py
│  │  │  cio_report.py
│  │  │  decision.py
│  │  │  historical_price.py
│  │  │  market_snapshot.py
│  │  │  news.py
│  │  │  performance_metrics.py
│  │  │  portfolio.py
│  │  │  position.py
│  │  │  rebalance_item.py
│  │  │  rebalance_plan.py
│  │  │  rebalancing_recommendation.py
│  │  │  recommendation.py
│  │  │  recommendation_item.py
│  │  │  risk_report.py
│  │  │  score.py
│  │  │  sector_candidate.py
│  │  │  signal.py
│  │  │  stock_candidate.py
│  │  │  trade.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          backtest_result.cpython-314.pyc
│  │          cio_decision.cpython-314.pyc
│  │          cio_report.cpython-314.pyc
│  │          decision.cpython-314.pyc
│  │          historical_price.cpython-314.pyc
│  │          market_snapshot.cpython-314.pyc
│  │          news.cpython-314.pyc
│  │          performance_metrics.cpython-314.pyc
│  │          portfolio.cpython-314.pyc
│  │          position.cpython-314.pyc
│  │          rebalance_item.cpython-314.pyc
│  │          rebalance_plan.cpython-314.pyc
│  │          rebalancing_recommendation.cpython-314.pyc
│  │          recommendation.cpython-314.pyc
│  │          risk_report.cpython-314.pyc
│  │          score.cpython-314.pyc
│  │          signal.cpython-314.pyc
│  │          trade.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─reports
│  │  │  morning_brief.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          morning_brief.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─repositories
│  │  │  historical_repository.py
│  │  │
│  │  └─__pycache__
│  │          historical_repository.cpython-314.pyc
│  │
│  ├─scripts
│  │  │  base.py
│  │  │  config.py
│  │  │  finish_feature.py
│  │  │  update_changelog.py
│  │  │  update_next_task.py
│  │  │  update_session.py
│  │  │  update_status.py
│  │  │  __init__.py
│  │  │
│  │  └─utils
│  │          base_generator.py
│  │          document.py
│  │          git_helper.py
│  │          markdown.py
│  │          project_info.py
│  │          state.py
│  │          __init__.py
│  │
│  ├─services
│  │  │  cio_engine.py
│  │  │  decision_engine.py
│  │  │  rebalancing_engine.py
│  │  │  rebalancing_recommendation_engine.py
│  │  │  recommendation_engine.py
│  │  │  risk_analyzer.py
│  │  │
│  │  └─__pycache__
│  │          cio_engine.cpython-314.pyc
│  │          decision_engine.cpython-314.pyc
│  │          rebalancing_engine.cpython-314.pyc
│  │          rebalancing_recommendation_engine.cpython-314.pyc
│  │          recommendation_engine.cpython-314.pyc
│  │          risk_analyzer.cpython-314.pyc
│  │
│  ├─storage
│  │  │  csv_storage.py
│  │  │
│  │  └─__pycache__
│  │          csv_storage.cpython-314.pyc
│  │
│  ├─strategies
│  │  │  allocation_strategy.py
│  │  │  buy_and_hold_strategy.py
│  │  │  equal_weight_strategy.py
│  │  │  market_value_weight_strategy.py
│  │  │  strategy.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          allocation_strategy.cpython-314.pyc
│  │          buy_and_hold_strategy.cpython-314.pyc
│  │          equal_weight_strategy.cpython-314.pyc
│  │          market_value_weight_strategy.cpython-314.pyc
│  │          strategy.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  ├─utils
│  │  │  logger.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          logger.cpython-314.pyc
│  │          __init__.cpython-314.pyc
│  │
│  └─__pycache__
│          __init__.cpython-314.pyc
│
└─tests
    │  project_scripts.py
    │  test_allocation_strategy.py
    │  test_backtest_engine.py
    │  test_backtest_integration.py
    │  test_buy_and_hold_strategy.py
    │  test_cio_engine.py
    │  test_cio_report.py
    │  test_csv_storage.py
    │  test_dashboard_renderer.py
    │  test_decision.py
    │  test_decision_engine.py
    │  test_equal_weight_strategy.py
    │  test_historical_data_loader.py
    │  test_historical_repository.py
    │  test_macro_analyzer.py
    │  test_market_analyzer.py
    │  test_morning_brief.py
    │  test_news_analyzer.py
    │  test_performance_analyzer.py
    │  test_portfolio.py
    │  test_portfolio_optimizer.py
    │  test_position.py
    │  test_rebalancing_engine.py
    │  test_rebalancing_recommendation_engine.py
    │  test_recommendation_engine.py
    │  test_risk_analyzer.py
    │  test_score_engine.py
    │  test_stock_screener.py
    │
    └─__pycache__
            test_allocation_strategy.cpython-314-pytest-9.1.1.pyc
            test_backtest_engine.cpython-314-pytest-9.1.1.pyc
            test_backtest_integration.cpython-314-pytest-9.1.1.pyc
            test_buy_and_hold_strategy.cpython-314-pytest-9.1.1.pyc
            test_cio_engine.cpython-314-pytest-9.1.1.pyc
            test_cio_report.cpython-314-pytest-9.1.1.pyc
            test_csv_storage.cpython-314-pytest-9.1.1.pyc
            test_dashboard_renderer.cpython-314-pytest-9.1.1.pyc
            test_decision.cpython-314-pytest-9.1.1.pyc
            test_decision_engine.cpython-314-pytest-9.1.1.pyc
            test_equal_weight_strategy.cpython-314-pytest-9.1.1.pyc
            test_historical_data_loader.cpython-314-pytest-9.1.1.pyc
            test_historical_repository.cpython-314-pytest-9.1.1.pyc
            test_macro_analyzer.cpython-314-pytest-9.1.1.pyc
            test_market_analyzer.cpython-314-pytest-9.1.1.pyc
            test_morning_brief.cpython-314-pytest-9.1.1.pyc
            test_news_analyzer.cpython-314-pytest-9.1.1.pyc
            test_performance_analyzer.cpython-314-pytest-9.1.1.pyc
            test_portfolio.cpython-314-pytest-9.1.1.pyc
            test_portfolio_optimizer.cpython-314-pytest-9.1.1.pyc
            test_position.cpython-314-pytest-9.1.1.pyc
            test_project_scripts.cpython-314-pytest-9.1.1.pyc
            test_rebalancing_engine.cpython-314-pytest-9.1.1.pyc
            test_rebalancing_recommendation_engine.cpython-314-pytest-9.1.1.pyc
            test_recommendation_engine.cpython-314-pytest-9.1.1.pyc
            test_risk_analyzer.cpython-314-pytest-9.1.1.pyc
            test_score_engine.cpython-314-pytest-9.1.1.pyc
            test_stock_screener.cpython-314-pytest-9.1.1.pyc
