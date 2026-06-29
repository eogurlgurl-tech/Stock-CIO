# STOCK-CIO Architecture

Version : v1.0.0

Last Update : 2026-06-29

---

# 1. Project Overview

## Project Name

STOCK-CIO

## Purpose

STOCK-CIO는 개인 투자자를 위한 AI Chief Investment Officer(CIO) 시스템이다.

단순한 종목 추천 프로그램이 아니라 시장 데이터 수집부터 거시경제 분석, 종목 평가, 포트폴리오 관리, 투자 의사결정까지 하나의 일관된 분석 체계를 제공하는 것을 목표로 한다.

모든 기능은 확장 가능하고 자동화 가능한 구조를 기반으로 개발한다.

---

# 2. Project Vision

## Short Term

- Morning Brief 자동화
- Daily Report 자동화
- Portfolio 관리
- Watch List 관리
- Market Rulebook 구축

## Mid Term

- Market Data Collector
- News Collector
- Sector Analyzer
- Risk Analyzer
- Decision Engine

## Long Term

- AI Chief Investment Officer
- Desktop Application
- Web Dashboard
- Portfolio Optimizer
- AI Investment Platform

---

# 3. Design Philosophy

STOCK-CIO는 투자 프로그램이 아니다.

AI 기반 투자 운영체제를 만드는 프로젝트이다.

모든 기능은 아래 흐름을 따른다.

```
Data

↓

Information

↓

Insight

↓

Decision

↓

Execution

↓

Feedback
```

모든 분석은 근거를 기반으로 한다.

감정이 아닌 데이터를 우선한다.

자동화 가능한 구조를 유지한다.

사람과 AI가 모두 이해할 수 있는 구조를 유지한다.

---

# 4. Investment Analysis Flow

모든 투자 분석은 아래 순서를 따른다.

```
Macro Economy
      │
      ▼
Global Market
      │
      ▼
Sector Analysis
      │
      ▼
Foreign / Institutional Flow
      │
      ▼
Stock Analysis
      │
      ▼
Portfolio Management
      │
      ▼
Trading Decision
      │
      ▼
Review & Rule Update
```

순서를 변경하지 않는다.

---

# 5. Software Architecture

```
Market Data
      │
      ▼
Collectors
      │
      ▼
Analyzers
      │
      ▼
Score Engine
      │
      ▼
Decision Engine
      │
      ▼
Portfolio Manager
      │
      ▼
Report Generator
      │
      ▼
Dashboard
```

모든 데이터는 단방향으로 흐른다.

역방향 의존성은 허용하지 않는다.

---

# 6. Project Structure

```
STOCK-CIO
│
├── 01_PROJECT
├── 02_ANALYSIS
├── 03_PORTFOLIO
├── 04_REPORT
├── 05_DATA
├── 06_TEMPLATE
├── 07_AUTOMATION
├── 08_BACKTEST
├── 09_DOCS
├── 10_CONFIG
│
├── src
│   ├── analyzers
│   ├── collectors
│   ├── config
│   ├── core
│   ├── models
│   ├── reports
│   └── utils
│
├── tests
├── requirements.txt
└── app.py
```

---

# 7. Layer Responsibilities

## Collectors

역할

- 시장 데이터 수집
- API 호출
- 데이터 저장

금지

- 데이터 분석
- 투자 판단

---

## Analyzers

역할

- 데이터 분석
- 점수 계산
- 리스크 분석

금지

- API 호출
- 투자 판단

---

## Core

역할

- 시스템 실행
- 모듈 연결
- 전체 Workflow 관리

---

## Models

역할

- 데이터 객체 정의
- Dataclass 관리

---

## Reports

역할

- Morning Brief
- Daily Report
- Portfolio Report 생성

---

## Utils

역할

- 공통 함수
- Helper 함수
- Logging
- File 처리

---

# 8. Development Workflow

모든 개발은 아래 순서를 따른다.

```
Requirement

↓

Impact Analysis

↓

Architecture Review

↓

Implementation

↓

Test

↓

Documentation

↓

Git Commit
```

새로운 기능은 반드시 영향 파일을 먼저 분석한다.

임시 코드를 작성하지 않는다.

---

# 9. Development Principles

1. Clean Architecture 유지
2. SOLID 원칙 준수
3. Single Responsibility Principle 준수
4. 확장 가능한 구조 우선
5. YAML 기반 설정 관리
6. Hard Coding 금지
7. Temporary Code 금지
8. 문서와 코드 동시 관리
9. 테스트 가능한 구조 유지
10. Git Commit 규칙 준수

---

# 10. Analysis Principle

모든 분석은 아래 순서를 따른다.

```
Background

↓

Trigger

↓

Market Impact

↓

Portfolio Impact

↓

Action

↓

Next Check Point
```

단순 뉴스 전달은 하지 않는다.

원인을 분석하고 투자 행동까지 연결한다.


# 11. Module Responsibilities

## analyzers

### Responsibility

시장 데이터를 분석하여 점수와 인사이트를 생성한다.

### Modules

- Macro Analyzer
- Sector Analyzer
- News Analyzer
- Money Flow Analyzer
- Risk Analyzer

### Output

- Macro Score
- Sector Score
- Risk Score
- News Score

---

## collectors

### Responsibility

외부 데이터를 수집한다.

### Data Source

- Yahoo Finance
- KRX
- 한국은행
- FRED
- 뉴스
- 환율
- 금리

### Output

Raw Data

---

## models

### Responsibility

프로젝트에서 사용하는 데이터 객체를 정의한다.

### Examples

- MarketSnapshot
- Score
- CIODecision
- Portfolio

---

## reports

### Responsibility

사용자에게 제공할 보고서를 생성한다.

### Reports

- Morning Brief
- Daily Report
- Weekly Report
- Monthly Report
- Portfolio Report

---

## config

### Responsibility

프로젝트의 모든 설정을 관리한다.

### Files

- app.yaml
- score.yaml
- market.yaml
- portfolio.yaml
- report.yaml
- news.yaml

---

## utils

### Responsibility

공통 기능 제공

### Examples

- Logger
- Date Helper
- File Helper
- Formatter

---

# 12. Configuration Policy

모든 설정은 10_CONFIG에서 관리한다.

Python 코드 내부에서 설정값을 직접 작성하지 않는다.

예)

GOOD

- score.yaml
- market.yaml
- report.yaml

BAD

- score = 80
- threshold = 0.75

새로운 설정이 필요한 경우 반드시 YAML 파일을 먼저 생성한다.

---

# 13. Dependency Rules

모든 의존성은 단방향을 유지한다.

```
Collector

↓

Analyzer

↓

Score

↓

Decision

↓

Portfolio

↓

Report
```

허용하지 않는 구조

- Collector → Analyzer 호출
- Analyzer → Collector 호출
- Report → Analyzer 호출
- Model → Collector 호출

순환 참조(Circular Dependency)는 허용하지 않는다.

---

# 14. Error Handling Policy

모든 예외는 처리한다.

예외를 무시하지 않는다.

print() 대신 Logging을 사용한다.

모든 오류는 원인을 확인할 수 있도록 기록한다.

---

# 15. Future Expansion

향후 추가 예정 기능

### Analysis

- AI News Analysis
- ETF Analysis
- Theme Analysis
- Earnings Analysis

### Portfolio

- Portfolio Optimizer
- Position Manager
- Risk Manager
- Rebalancing Engine

### Automation

- Telegram Bot
- Discord Bot
- Slack Notification
- Email Report

### Dashboard

- Desktop Dashboard
- Web Dashboard
- Mobile Dashboard

### AI

- LLM Investment Advisor
- AI Strategy Generator
- AI Portfolio Review
- AI Market Summary

---

# 16. Architecture Decision Records (ADR)

## ADR-001

모든 설정은 YAML에서 관리한다.

Reason

코드 수정 없이 전략을 변경할 수 있도록 하기 위함.

---

## ADR-002

Collector는 데이터만 수집한다.

Reason

SRP(Single Responsibility Principle)를 유지하기 위함.

---

## ADR-003

Analyzer는 분석만 수행한다.

Reason

분석과 의사결정을 분리하기 위함.

---

## ADR-004

Decision은 별도의 Engine에서 수행한다.

Reason

점수 계산과 투자 판단을 분리하기 위함.

---

## ADR-005

모든 문서는 Markdown으로 관리한다.

Reason

GitHub, AI, 개발자가 모두 동일한 문서를 사용할 수 있도록 하기 위함.

---

# Revision History

| Version    | Date       | Description              |
| ---------- | ---------- | ------------------------ |
| v0.1 Alpha | 2026-06-26 | Initial Architecture     |
| v1.0.0     | 2026-06-29 | Architecture Refactoring |

---

# End of Document
