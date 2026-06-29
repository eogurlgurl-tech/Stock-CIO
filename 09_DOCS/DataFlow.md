
# STOCK-CIO Data Flow

Version : v1.0.0

Last Update : 2026-06-29

---

# 1. Purpose

본 문서는 STOCK-CIO의 전체 데이터 흐름을 정의한다.

모든 데이터는 동일한 흐름을 따르며,
역방향 데이터 전달은 허용하지 않는다.

---

# 2. Overall Flow

```
External Data

↓

Collectors

↓

Raw Data

↓

Analyzers

↓

Scores

↓

Decision Engine

↓

Portfolio

↓

Reports

↓

User
```

---

# 3. Data Sources

## Market

- KRX
- Yahoo Finance
- NASDAQ
- S&P500
- SOX

---

## Macro

- FRED
- 한국은행
- 미국 국채금리
- CPI
- PPI
- PCE

---

## Currency

- USD/KRW
- DXY

---

## News

- Reuters
- Bloomberg
- Investing
- 연합
- 한국경제

---

# 4. Collector Layer

Collector는 데이터를 가져오기만 한다.

분석하지 않는다.

Output

```
Raw Market Data
```

예

```
NASDAQ

+2.15%

SOX

+3.52%

USD/KRW

1368.25
```

---

# 5. Analyzer Layer

Collector의 데이터를 분석한다.

생성 결과

- Macro Score
- Market Score
- Sector Score
- Money Flow Score
- News Score
- Risk Score

---

# 6. Score Integration

모든 점수는 Score Model로 통합한다.

```
Macro

+

Sector

+

Money Flow

+

News

+

Risk

↓

Score
```

---

# 7. Decision Engine

Score를 이용하여 투자 판단을 수행한다.

출력

- BUY
- HOLD
- SELL

추가 출력

- 투자등급
- 목표가
- 손절가
- 비중

---

# 8. Portfolio Layer

Decision 결과를 이용하여

- Portfolio 생성
- 비중 계산
- 리스크 계산
- 리밸런싱

을 수행한다.

---

# 9. Report Layer

생성되는 보고서

- Morning Brief
- Daily Report
- Weekly Report
- Monthly Report
- Portfolio Report

---

# 10. Automation Layer

자동 수행

- Morning Brief
- Daily Report
- Watch List
- Dashboard
- Alert

---

# 11. Error Flow

```
Collector Error

↓

Logging

↓

Retry

↓

Skip

↓

Continue
```

시스템은 하나의 오류 때문에 전체 작업을 중단하지 않는다.

---

# 12. Logging Flow

모든 단계는 Logging을 수행한다.

```
Collector

↓

Analyzer

↓

Decision

↓

Portfolio

↓

Report
```

로그 레벨

- INFO
- WARNING
- ERROR

---

# 13. Future Flow

향후 추가 예정

```
LLM

↓

AI Recommendation

↓

Decision

↓

Portfolio

↓

Auto Report
```

---

# 14. Data Flow Principles

1. 단방향 흐름 유지
2. Collector는 분석하지 않는다.
3. Analyzer는 판단하지 않는다.
4. Decision Engine만 투자판단을 수행한다.
5. Portfolio는 실행만 담당한다.
6. Report는 출력만 담당한다.

---

# Revision History

| Version | Date       | Description       |
| ------- | ---------- | ----------------- |
| v1.0.0  | 2026-06-29 | Initial Data Flow |

---

# End of Document
