# STOCK-CIO API Specification

Version : v1.0.0

Last Update : 2026-06-29

---

# 1. Purpose

본 문서는 STOCK-CIO 내부 모듈 간 인터페이스(API)를 정의한다.

외부 REST API가 아닌 Python Module Interface를 의미한다.

모든 모듈은 본 문서의 인터페이스를 따른다.

---

# 2. Architecture

```
Collectors

↓

Analyzers

↓

Decision Engine

↓

Portfolio

↓

Reports
```

---

# 3. Collector API

## Responsibility

시장 데이터를 수집한다.

분석하지 않는다.

---

### Input

없음

### Output

MarketSnapshot

---

### Example

```python
market = collector.load_market()
```

---

# 4. Analyzer API

## Responsibility

수집된 데이터를 분석한다.

---

### Input

MarketSnapshot

### Output

Score

---

### Example

```python
score = analyzer.analyze(market)
```

---

# 5. Score Model

## Input

각 Analyzer 결과

- Macro
- Sector
- Money Flow
- News
- Risk

---

## Output

```python
Score
```

---

# 6. Decision Engine API

## Responsibility

최종 투자 판단

---

### Input

Score

### Output

CIODecision

---

### Example

```python
decision = engine.decide(score)
```

---

# 7. Portfolio API

## Responsibility

포트폴리오 관리

---

### Input

CIODecision

### Output

Portfolio

---

### Example

```python
portfolio = manager.update(decision)
```

---

# 8. Report API

## Responsibility

보고서 생성

---

### Input

Portfolio

Score

Decision

---

### Output

Markdown Report

---

### Example

```python
report.generate()
```

---

# 9. Configuration API

모든 설정은 YAML에서 로드한다.

예시

```python
config.load("score.yaml")
```

지원 파일

- app.yaml
- market.yaml
- score.yaml
- report.yaml
- portfolio.yaml
- news.yaml

---

# 10. Logging API

모든 모듈은 Logger를 사용한다.

지원 레벨

- INFO
- WARNING
- ERROR

예시

```python
logger.info()

logger.warning()

logger.error()
```

---

# 11. Exception Policy

모든 예외는 처리한다.

예외를 무시하지 않는다.

필요 시 상위 모듈로 전달한다.

---

# 12. Naming Convention

## Class

PascalCase

예

- MarketCollector
- MacroAnalyzer
- DecisionEngine

---

## Function

snake_case

예

- load_market()
- analyze()
- generate_report()

---

## Variable

snake_case

예

- market_data
- macro_score
- decision_score

---

# 13. Return Type

모든 Public Function은 Return Type을 명시한다.

예

```python
def analyze(data: MarketSnapshot) -> Score:
```

---

# 14. Future API

추가 예정

- Dashboard API
- Backtest API
- AI Advisor API
- Notification API
- Web API

---

# Revision History

| Version | Date       | Description          |
| ------- | ---------- | -------------------- |
| v1.0.0  | 2026-06-29 | Initial API Document |

---

# End of Document
