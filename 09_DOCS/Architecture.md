
# STOCK-CIO Architecture

Version : v1.0

Last Update : 2026-07-02

---

# Purpose

This document defines the overall architecture of STOCK-CIO.

Every new feature must follow this architecture.

---

# Layer Architecture

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

---

# Directory Structure

src/

├── analyzers/

├── collectors/

├── config/

├── constants/

├── core/

├── dashboard/

├── models/

├── reports/

├── repositories/

├── services/

├── storage/

├── utils/

tests/

---

# Layer Responsibilities

## Collector

Collect external market data.

No business logic.

---

## Storage

Read / Write data.

No downloading.

---

## Repository

Single entry point for data access.

Determines

- Cache
- CSV
- Download

---

## Analyzer

Analyze collected data.

No downloading.

---

## Engine

Integrate analyzers.

Generate decisions.

---

## Dashboard

Display results.

---

## Report

Generate Markdown / Excel / PDF reports.

---

# Historical Data Flow

Yahoo Finance

↓

HistoricalDataLoader

↓

CSVStorage

↓

HistoricalRepository

↓

Backtest Engine

↓

Portfolio Optimizer

↓

AI CIO

---

# Repository Policy

Repository is the only entry point.

All modules access historical data through Repository.

---

# Testing Policy

Unit Test

↓

Repository Test

↓

CSV Test

↓

Integration Test

↓

Commit

---

# Roadmap

Sprint 8

✅ FEATURE-016 Historical Data Manager

↓

Sprint 9

FEATURE-017 Backtest Engine

↓

Sprint 10

FEATURE-018 Portfolio Optimizer

↓

Sprint 11

FEATURE-019 AI CIO

---

# Design Principles

- Single Responsibility
- Repository Pattern
- Dependency Injection
- Test First
- Build Green
- Modular Design

