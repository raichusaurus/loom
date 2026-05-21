# Loom Progress Ledger

Project-specific completion ledger for [Project Name]. This root file is the project cockpit: snapshot, rollups, next score-changing actions, decisions, and open questions. Detailed evidence lives in the phase, system component, subcomponent, and unit ledgers beneath it.

## Project Snapshot

**Project:** [project-slug]
**Date:** [YYYY-MM-DD]
**Owner:** [Owner names]
**Current Focus:** [Current phase, workstream, or score-changing push]
**Total Complete:** [0-100%]
**Calculation Basis:** [Equal phase weights / weighted phase scores / child rollup blend / custom basis]

## Top-Level Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | 0% | 1 | [Discovery Progress](phases/01-discovery/PROGRESS.md) | |
| Requirements | 0% | 1 | [Requirements Progress](phases/02-requirements/PROGRESS.md) | |
| Architecture | 0% | 1 | [Architecture Progress](phases/03-architecture/PROGRESS.md) | |
| Planning & Decomposition | 0% | 1 | [Planning Progress](phases/04-planning/PROGRESS.md) | |
| Contracts & Tests | 0% | 1 | [Contracts & Tests Progress](phases/05-contracts-tests/PROGRESS.md) | |
| Implementation | 0% | 1 | [Implementation Progress](phases/06-implementation/PROGRESS.md) | |
| Review & Retrospective | 0% | 1 | [Review Progress](phases/07-review/PROGRESS.md) | |
| **Phase Total** | **0%** | | | [Calculation note, such as rounded from 0 / 700.] |

## Top-Level Child Rollup

| Scope | Type | Weight | Phase Total | Child Rollup | Total | Owner | Notes |
|-------|------|--------|-------------|--------------|-------|-------|-------|
| [System Component](system/[architecture-component]/PROGRESS.md) | System Component | 1 | 0% | 0% | 0% | [Owner] | |
| [Delivery Workstream](phases/[phase]/PROGRESS.md) | Workstream | 1 | 0% | 0% | 0% | [Owner] | |
| **Child Rollup** | | | | | **0%** | | [Calculation note, such as rounded equal-weight average.] |

## Next Score-Changing Actions

| Action | Phase / Area | Expected Score Impact | Owner |
|--------|--------------|-----------------------|-------|
| [Next concrete action] | [Phase / system component] | [How this changes the score or unlocks scoring evidence] | [Owner] |
| [Next concrete action] | [Phase / system component] | [How this changes the score or unlocks scoring evidence] | [Owner] |

## Decisions and Adjustments

| Date | Scope | Change | Reason | Owner |
|------|-------|--------|--------|-------|
| [YYYY-MM-DD] | [Scope] | [What changed] | [Why the score, structure, or plan changed] | [Owner] |

## Open Progress Questions

| Scope | Question | Needed To Score Accurately | Owner |
|-------|----------|----------------------------|-------|
| [Scope] | [Open question] | [What evidence or decision is needed] | [Owner] |
