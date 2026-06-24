# Stock-CIO Architecture

Version: v0.1 Alpha

Last Update: 2026-06-26

---

# 1. Project Overview

## Project Name

Stock-CIO

## Purpose

Stock-CIO는 AI를 활용하여 개인 투자자의 의사결정을 지원하는 CIO(Chief Investment Officer) 시스템이다.

단순한 종목 추천이 아닌, 거시경제부터 포트폴리오까지 하나의 흐름으로 분석하여 일관된 투자 의사결정을 지원하는 것을 목표로 한다.

---

# 2. Project Goal

## Short Term

* Morning Brief 구축
* Daily Report 구축
* Portfolio 관리
* Watch List 관리
* Market Rulebook 구축

## Mid Term

* Python 자동화
* 뉴스 자동 수집
* 경제지표 자동 분석
* 투자 보고서 자동 생성

## Long Term

* AI 기반 투자 플랫폼 구축
* Stock-CIO Desktop Application 개발
* 개인 CIO 운영체제(OS) 구축

---

# 3. System Architecture

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

모든 분석은 반드시 위 순서를 따른다.

---

# 4. Project Structure

```
01_PROJECT
프로젝트 관리 문서

02_ANALYSIS
시장 분석 및 투자 규칙

03_PORTFOLIO
포트폴리오 관리

04_REPORT
Daily / Weekly / Monthly Report

05_DATA
시장 데이터 및 원본 데이터

06_TEMPLATE
보고서 템플릿

07_AUTOMATION
Python 및 자동화 모듈

08_BACKTEST
전략 검증

09_DOCS
프로젝트 설계 문서
```

---

# 5. Daily Workflow

## Before Market

1. 미국시장 분석
2. 거시경제 분석
3. 주요 뉴스 분석
4. 반도체 및 AI 분석
5. 환율 및 금리 분석
6. 외국인 수급 예상
7. Morning Brief 작성

---

## During Market

1. 관심종목 모니터링
2. 외국인 수급 확인
3. 기관 수급 확인
4. 매매 판단
5. 리스크 관리

---

## After Market

1. 시장 총평
2. 외국인 분석
3. 기관 분석
4. 업종 분석
5. 포트폴리오 평가
6. Daily Report 작성
7. Rulebook 업데이트

---

# 6. Analysis Principle

모든 분석은 아래 구조를 따른다.

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

단순 뉴스 전달은 하지 않는다.

원인을 분석하고 투자 행동까지 연결한다.

---

# 7. Automation Roadmap

Phase 1

Markdown 기반 운영

Phase 2

Python 자동화

Phase 3

뉴스 자동 수집

Phase 4

Morning Brief 자동 생성

Phase 5

Portfolio Dashboard

Phase 6

Desktop Application

---

# 8. Development Principle

모든 기능은 아래 원칙을 따른다.

1. 근거 기반 분석
2. 데이터 기반 의사결정
3. 동일한 분석 구조 유지
4. 자동화 가능한 문서 작성
5. 사람이 읽기 쉽고 AI도 읽기 쉬운 구조 유지

---

# 9. Investment Philosophy

투자는 예측이 아니라 확률이다.

감정이 아닌 데이터로 판단한다.

모든 매매는 기록한다.

같은 실수를 반복하지 않는다.

시장을 이기려 하지 않고 시장을 이해한다.

---

# 10. Project Mission

Stock-CIO의 목표는 단순한 투자 기록 프로그램이 아니다.

AI와 데이터를 활용하여 개인 CIO 시스템을 구축하고, 장기적으로는 자동화된 투자 분석 플랫폼으로 발전시키는 것을 최종 목표로 한다.
