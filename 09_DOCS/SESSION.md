
# STOCK-CIO Session

Version : v2.0.0

Last Update : 2026-06-30

---

# Sprint

Sprint 5

Status : READY

Progress : 40%

---

# Current Feature

FEATURE-003

US Market Loader Enhancement

---

# Current Task

Waiting for source file

---

# Current File

src/collectors/us_loader.py

---

# Last Completed

## Documentation

- README.md
- PROJECT_CONTEXT.md
- PROJECT_STATUS.md
- Architecture.md
- DataFlow.md
- API.md
- Roadmap.md
- CHANGELOG.md
- Version.md

## Configuration

- weight.yaml
- strategy.yaml

## Engine

- ScoreEngine Refactoring
- DecisionEngine YAML Integration

## Model

- MarketSnapshot Model Expansion

## Refactoring

- Project Import Standardization

---

# Next Task

Feature

FEATURE-003

Target File

src/collectors/us_loader.py

Action

전체 파일 교체

Goal

- nasdaq_change 추가
- sp500_change 추가
- sox_change 추가
- vix_change 추가

Current Status

사용자가 us_loader.py 전체 코드를 공유하면 작업 시작

Expected Commit

feat: add US market change data

---

# After Current Task

FEATURE-004

KRX Loader Enhancement

↓

FEATURE-005

Macro Analyzer Refactoring

↓

FEATURE-006

Decision Engine Enhancement

↓

FEATURE-007

CIO Engine Refactoring

---

# Project Progress

Documentation : 100%

Configuration : 100%

Collectors : 60%

Models : 80%

Analyzers : 35%

Engines : 30%

Reports : 50%

Dashboard : 0%

Backtest : 0%

---

# Working Rules

## Development Rules

1. 한 번에 하나의 작업만 수행한다.
2. 현재 작업이 끝나기 전에는 다른 작업으로 이동하지 않는다.
3. 새로운 기능 개발 전 반드시 영향받는 파일을 확인한다.
4. 기존 파일을 먼저 검토한 후 전체 파일 교체 방식으로 수정한다.
5. 부분 코드(Snippet) 수정은 사용하지 않는다.
6. 모든 설정값은 YAML에서 관리한다.
7. Commit 후 SESSION.md와 NEXT_TASK.md를 반드시 업데이트한다.

---

## Response Rules

모든 작업은 아래 형식을 따른다.

[FEATURE-XXX]

파일

작업

영향 파일

전체 교체

Commit

SESSION.md 업데이트

NEXT_TASK.md 업데이트

---

## New Chat Rules

새로운 채팅에서는 아래 순서를 따른다.

"STOCK-CIO 이어서 진행"

입력

SESSION.md 전체 붙여넣기

NEXT_TASK.md 전체 붙여넣기

현재 작업부터 바로 시작

별도의 프로젝트 설명은 하지 않는다.

---

## Project Principles

- Clean Architecture 유지
- SOLID 원칙 준수
- 확장 가능한 구조 우선
- 임시 코드 작성 금지
- Hard Coding 최소화
- Documentation First
- Config First
- Testable Code
- AI와 사람이 모두 이해할 수 있는 구조 유지

---

# End of Session
