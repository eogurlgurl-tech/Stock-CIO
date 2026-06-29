# STOCK-CIO Version Policy

Version : v1.0.0

Last Update : 2026-06-29

---

# Purpose

본 문서는 STOCK-CIO 프로젝트의 버전 관리 정책을 정의한다.

버전은 Semantic Versioning(SemVer)을 기반으로 관리한다.

```
MAJOR.MINOR.PATCH
```

예)

```
v1.0.0
```

---

# Version Rule

## MAJOR

호환되지 않는 대규모 변경

예)

- Architecture 변경
- 핵심 Engine 변경
- 프로젝트 구조 변경

예)

```
v1.0.0

↓

v2.0.0
```

---

## MINOR

기능 추가

예)

- 새로운 Analyzer
- Dashboard
- Portfolio Manager
- Report 기능 추가

예)

```
v0.4.0

↓

v0.5.0
```

---

## PATCH

버그 수정

예)

- 오류 수정
- 성능 개선
- 문서 수정

예)

```
v0.5.0

↓

v0.5.1
```

---

# Release Policy

## Alpha

초기 개발 단계

특징

- 기능 개발 진행
- 구조 변경 가능
- 테스트 미완료

예)

```
v0.3.0-alpha
```

---

## Beta

기능 완료

특징

- 주요 기능 개발 완료
- 통합 테스트 진행
- 버그 수정 중심

예)

```
v0.9.0-beta
```

---

## Stable

정식 릴리즈

예)

```
v1.0.0
```

---

# Current Version

| Version      | Status | Description        |
| ------------ | ------ | ------------------ |
| v0.1.0       | ✅     | Project Initialize |
| v0.2.0       | ✅     | Framework 구축     |
| v0.3.0-alpha | 🚧     | Foundation 완료    |
| v0.4.0       | ⏳     | Decision Engine    |
| v0.5.0       | ⏳     | Analyzer 확장      |
| v0.6.0       | ⏳     | Portfolio Manager  |
| v0.7.0       | ⏳     | Dashboard          |
| v0.8.0       | ⏳     | Backtest           |
| v0.9.0-beta  | ⏳     | AI Advisor         |
| v1.0.0       | ⏳     | AI CIO Platform    |

---

# Release Checklist

## Documentation

- README
- PROJECT_CONTEXT
- PROJECT_STATUS
- Architecture
- API
- DataFlow
- CHANGELOG

---

## Code

- Build Success
- Unit Test Pass
- Lint Pass
- Type Check Pass

---

## Configuration

- YAML 검증 완료
- Config Version 확인

---

## Git

- Commit 완료
- Tag 생성
- Release Note 작성

---

# Tag Convention

예시

```
v0.4.0

v0.5.0

v1.0.0
```

---

# Branch Strategy

## main

안정 버전

---

## develop

개발 버전

---

## feature/*

기능 개발

예)

```
feature/decision-engine

feature/risk-analyzer

feature/dashboard
```

---

## hotfix/*

긴급 수정

예)

```
hotfix/report-error
```

---

# Commit Convention

| Prefix   | Description |
| -------- | ----------- |
| feat     | 기능 추가   |
| fix      | 버그 수정   |
| refactor | 구조 개선   |
| docs     | 문서 수정   |
| test     | 테스트 추가 |
| chore    | 환경 설정   |

---

# Release Goal

## v0.4

- Decision Engine
- Weight Engine
- Strategy Configuration

---

## v0.5

- Risk Analyzer
- Sector Analyzer
- Money Flow Analyzer

---

## v1.0

AI Chief Investment Officer

---

# Revision History

| Version | Date       | Description            |
| ------- | ---------- | ---------------------- |
| v1.0.0  | 2026-06-29 | Initial Version Policy |

---

# End of Document
