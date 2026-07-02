# STOCK-CIO Change Log

Version : v1.0.0

Last Update : 2026-06-29

---

# About

본 문서는 STOCK-CIO 프로젝트의 모든 변경 사항을 기록한다.

변경 이력은 Git Commit과 함께 관리하며, 주요 기능 추가 및 구조 변경을 추적하기 위한 문서이다.

---

# v1.0.0 (2026-06-29)

## Documentation

### Added

- PROJECT_CONTEXT.md
- PROJECT_STATUS.md
- README.md
- Architecture.md
- DataFlow.md
- API.md
- Roadmap.md

### Updated

- Project Documentation Structure
- Documentation Standard
- Development Workflow

### Architecture

- Investment Flow 정의
- Software Architecture 정의
- Layer Responsibility 추가
- Dependency Rule 추가
- Configuration Policy 추가

---

# v0.3.0-alpha

## Foundation

### Added

- MarketSnapshot Model
- Score Model
- CIODecision Model

### Added

- Morning Brief

### Added

- Daily Report Framework

### Added

- YAML Configuration

---

# v0.2.0

## Initial Framework

### Added

- Project Directory
- src Structure
- tests Structure
- Config Directory
- Report Directory

---

# v0.1.0

## Project Initialize

### Added

- Git Repository
- Python Environment
- Basic Project Structure

---

# Commit Convention

## feat

새로운 기능 추가

---

## fix

버그 수정

---

## refactor

구조 개선

---

## docs

문서 수정

---

## test

테스트 추가

---

## chore

환경 및 설정 변경

---

# Release Policy

Patch

버그 수정

예)

v0.4.1

---

Minor

기능 추가

예)

v0.5.0

---

Major

대규모 구조 변경

예)

v1.0.0

---

# Upcoming Release

## v0.4

예정 기능

- Decision Engine
- Weight Engine
- Strategy Configuration

---

## v0.5

예정 기능

- Risk Analyzer
- Sector Analyzer
- Money Flow Analyzer

---

## v0.6

예정 기능

- Portfolio Manager
- Performance Analysis

---

## v0.7

예정 기능

- Dashboard
- Alert System

---

## Revision History

| Version | Date       | Description        |
| ------- | ---------- | ------------------ |
| v1.0.0  | 2026-06-29 | Initial Change Log |

---

# End of Document

# STOCK-CIO ARCHITECTURE

Version : v1.0 (Draft)

Last Update : 2026-07-02

---

# Purpose

본 문서는 STOCK-CIO 시스템의 전체 아키텍처를 정의한다.

모든 신규 Feature는 본 문서의 구조를 따른다.

아키텍처 변경은 신규 Feature 개발보다 우선 검토되어야 한다.

---

# Development Principles

* Single Responsibility Principle
* Feature Development Only
* One Feature At A Time
* Full-file Replacement Preferred
* Build Must Stay Green
* Unit Test Required
* Integration Test Required
* No Circular Dependency

---

# Layer Architecture

```
Collector

↓

Storage

↓

Repository

↓

Analyzer

↓

Engine

↓

Dashboard

↓

Report
```

각 Layer는 자신의 바로 아래 Layer만 호출할 수 있다.

---

# Directory Structure

```
src/

├── analyzers/
├── collectors/
├── dashboard/
├── engines/
├── models/
├── reports/
├── repositories/
├── storage/
├── utils/

tests/
```

---

# Layer Responsibilities

## Models

역할

* 데이터 객체 정의
* Business Logic 없음

예시

* MarketSnapshot
* Score
* News
* HistoricalPrice

---

## Collectors

역할

* 외부 데이터 수집

허용

* Yahoo Finance
* KRX
* API

금지

* CSV 저장
* Score 계산
* 분석

---

## Storage

역할

* 데이터 저장
* 데이터 읽기

예시

* CSVStorage

금지

* 다운로드
* 분석

---

## Repository

역할

Collector와 Storage를 통합 관리한다.

Analyzer는 Repository만 호출한다.

Repository 내부에서

* CSV 존재 여부 확인
* 다운로드 여부 판단
* Cache 사용 여부 판단

을 수행한다.

---

## Analyzer

역할

수집된 데이터를 분석한다.

예시

* MacroAnalyzer
* NewsAnalyzer
* MarketAnalyzer

Analyzer는 Collector를 직접 호출하지 않는다.

---

## Engine

역할

여러 Analyzer 결과를 통합한다.

예시

* ScoreEngine
* DecisionEngine

---

## Dashboard

역할

Console 출력

사용자 확인용 화면 생성

---

## Report

역할

Markdown

PDF

Excel

등 최종 결과 생성

---

# Historical Data Flow

```
Yahoo Finance

↓

HistoricalDataLoader

↓

CSVStorage

↓

HistoricalRepository

↓

Analyzer

↓

Backtest

↓

Portfolio Optimizer

↓

AI CIO
```

---

# Repository Policy

Repository는 단일 진입점이다.

모든 Historical 데이터는 Repository를 통해 접근한다.

예시

```
repository.load("005930.KS")
```

Analyzer는 CSV 또는 Yahoo를 직접 호출하지 않는다.

---

# Cache Policy

Repository는 Memory Cache를 사용할 수 있다.

동일 Symbol은 동일 실행 중 한 번만 다운로드한다.

예시

```
NVDA

↓

Download

↓

Memory Cache

↓

재사용
```

---

# Storage Policy

저장 위치

```
20_DATA/

└── historical/
```

파일명

```
005930.KS.csv

NVDA.csv

AAPL.csv
```

CSV 형식

```
Date
Open
High
Low
Close
Volume
```

---

# Testing Strategy

개발 순서

```
Model

↓

Loader

↓

Unit Test

↓

Storage

↓

Unit Test

↓

Repository

↓

Unit Test

↓

Integration Test

↓

Commit
```

모든 신규 Feature는 Unit Test를 포함한다.

Build는 항상 Green 상태를 유지한다.

---

# Roadmap

Sprint 8

FEATURE-016

Historical Data Manager

---

Sprint 9

FEATURE-017

Backtest Engine

---

Sprint 10

FEATURE-018

Portfolio Optimizer

---

Sprint 11

FEATURE-019

AI CIO

---

# Design Goals

* 높은 유지보수성
* 계층 분리
* 테스트 용이성
* 데이터 재사용
* 최소한의 의존성
* AI CIO 확장 지원

---

# Architecture Rule

Collector는 저장하지 않는다.

Storage는 다운로드하지 않는다.

Repository는 판단한다.

Analyzer는 분석만 한다.

Engine은 결과를 통합한다.

Dashboard는 표시만 한다.

Report는 문서만 생성한다.