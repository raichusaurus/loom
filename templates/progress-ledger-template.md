# Loom Progress Ledger

Project-specific completion ledger for [Project Name]. This root file is the project cockpit: snapshot, rollups, next score-changing actions, decisions, and open questions. Detailed evidence lives in the phase, system component, subcomponent, and unit ledgers beneath it.

Use this file as the default top-level `docs/loom/PROGRESS.md`. For recursive progress, create child phase and system ledgers from the shapes below. If a discovered scope does not need its own file, keep it in the nearest parent table and write `No child doc` with the reason.

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

## Scope Inventory

Use this table to show that the progress tree was populated from evidence rather than vibes.

| Scope | Type | Parent | Source Evidence | Progress Doc | Intended Source Path | Intended Test Path | Inclusion Decision |
|-------|------|--------|-----------------|--------------|----------------------|--------------------|--------------------|
| Discovery | Phase | Project | [Discovery artifact] | `phases/01-discovery/PROGRESS.md` | N/A | N/A | Included |
| Requirements | Phase | Project | [Requirements artifact] | `phases/02-requirements/PROGRESS.md` | N/A | N/A | Included |
| Architecture | Phase | Project | [Architecture artifact] | `phases/03-architecture/PROGRESS.md` | N/A | N/A | Included |
| Planning & Decomposition | Phase | Project | [Planning artifact] | `phases/04-planning/PROGRESS.md` | N/A | N/A | Included |
| Contracts & Tests | Phase | Project | [Contracts artifact] | `phases/05-contracts-tests/PROGRESS.md` | N/A | N/A | Included |
| Implementation | Phase | Project | [Implementation artifact] | `phases/06-implementation/PROGRESS.md` | N/A | N/A | Included |
| Review & Retrospective | Phase | Project | [Review artifact] | `phases/07-review/PROGRESS.md` | N/A | N/A | Included |
| [Architecture component] | System Component | Project | [Architecture / planning / source evidence] | `system/[architecture-component]/PROGRESS.md` | `src/...` | `tests/...` | Included |
| [Owned unit or subcomponent] | Unit / Subcomponent | [Architecture component] | [Contract / source / test evidence] | `system/[architecture-component]/[owned-unit-or-subcomponent]/PROGRESS.md` or `No child doc` | `src/...` or TBD | `tests/...` or TBD | Included / Rolled into parent / Deferred |

## Progress Tree Index

Keep this table compact and clickable. Put deeper scoring evidence in child ledgers.

| Scope | Type | Parent | Total | Current Focus | Progress Doc | Notes |
|-------|------|--------|-------|---------------|--------------|-------|
| Discovery | Phase | Project | 0% | | [Progress](phases/01-discovery/PROGRESS.md) | |
| Requirements | Phase | Project | 0% | | [Progress](phases/02-requirements/PROGRESS.md) | |
| Architecture | Phase | Project | 0% | | [Progress](phases/03-architecture/PROGRESS.md) | |
| Planning & Decomposition | Phase | Project | 0% | | [Progress](phases/04-planning/PROGRESS.md) | |
| Contracts & Tests | Phase | Project | 0% | | [Progress](phases/05-contracts-tests/PROGRESS.md) | |
| Implementation | Phase | Project | 0% | | [Progress](phases/06-implementation/PROGRESS.md) | |
| Review & Retrospective | Phase | Project | 0% | | [Progress](phases/07-review/PROGRESS.md) | |
| [Architecture component] | System Component | Project | 0% | | [Progress](system/[architecture-component]/PROGRESS.md) | |
| [Owned unit or subcomponent] | Unit / Subcomponent | [Architecture component] | 0% | | [Progress](system/[architecture-component]/[owned-unit-or-subcomponent]/PROGRESS.md) or `No child doc` | |

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

| Scope | Question Summary | Options | Trade-offs | Recommendation | Needed To Score Accurately | Owner |
|-------|------------------|---------|------------|----------------|----------------------------|-------|
| [Scope] | [Open question] | [Option A / Option B / Defer] | [Cost, risk, scope, quality, speed, reversibility] | [Recommended option and why] | [What evidence or decision is needed] | [Owner] |

---

## Child Progress Ledger Shape

Use this shape for any phase, system component, subcomponent, or unit-level progress file.

```md
# Progress: [Scope Name]

**Type:** [Phase / System Component / Subcomponent / Unit]
**Parent:** [Parent scope](../PROGRESS.md)
**Owner:** [Owner]
**Total Complete:** 0%
**Current Focus:** [What is changing next]
**Last Updated:** [YYYY-MM-DD]

## Navigation

- **Parent:** [Parent progress](../PROGRESS.md)
- **Children:** [Child progress docs, if any]
- **Related phase docs:** [Requirements / Architecture / Planning / Contracts / Implementation]

## Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | N/A | | | |
| Requirements | N/A | | | |
| Architecture | N/A | | | |
| Planning & Decomposition | N/A | | | |
| Contracts & Tests | 0% | 1 | | |
| Implementation | 0% | 1 | | |
| Review & Retrospective | 0% | 1 | | |
| **Phase Total** | **0%** | | | |

## Children

| Scope | Type | Weight | Total | Progress Doc | Notes |
|-------|------|--------|-------|--------------|-------|
| | | | | | |

## Local Scope Inventory

| Scope | Type | Source Evidence | Progress Doc | Intended Source Path | Intended Test Path | Inclusion Decision |
|-------|------|-----------------|--------------|----------------------|--------------------|--------------------|
| | | | | | | |

## Next Score-Changing Actions

| Action | Phase / Area | Expected Score Impact | Owner |
|--------|--------------|-----------------------|-------|
| | | | |

## Blockers and Questions

| Item | Impact | Owner | Next Step |
|------|--------|-------|-----------|
| | | | |
```
