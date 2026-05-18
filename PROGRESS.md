# Loom Progress Ledger

Use this document to track completion at every useful scope: project, service, component, class, workflow, or task-level mini-Loom. The goal is to make progress visible at each zoom level without pretending every scope needs every phase.

Copy this file into a project repo and update it throughout the Loom cycle.

---

## How to Score Progress

### Completion Values

Use percentages from `0` to `100`.

- `0%` = not started
- `25%` = drafted or started, major gaps remain
- `50%` = usable first pass, important gaps remain
- `75%` = mostly complete, known cleanup or validation remains
- `100%` = phase gate is satisfied for this scope
- `N/A` = phase does not apply to this scope and is excluded from calculations

Use exact percentages when you have a better signal, such as task counts, test pass counts, implementation slices, or reviewed deliverables.

### Default Phase Weights

Use equal weights unless the project has a reason to weight phases differently.

| Phase | Default Weight | Notes |
|-------|----------------|-------|
| Discovery | 1 | Often `N/A` below project or feature level |
| Requirements | 1 | Can be lighter for existing services/classes |
| Architecture | 1 | Can be `N/A` for simple classes with obvious design |
| Planning & Decomposition | 1 | Usually applies when ownership or sequencing matters |
| Contracts & Tests | 1 | Minimum expected phase for services, components, and classes |
| Implementation | 1 | Minimum expected phase for services, components, and classes |
| Review & Retrospective | 1 | Can be a lightweight review at lower scopes |

### Rollup Formula

For any scope:

```text
Phase Total % =
  sum(applicable phase percent * phase weight)
  / sum(applicable phase weights)
```

For parent scopes with children:

```text
Child Rollup % =
  sum(child total percent * child weight)
  / sum(child weights)
```

Use `Total %` as the scope's headline progress number.

```text
Total % =
  Phase Total %
```

If a scope has meaningful children and you want the parent total to reflect delivery progress, use:

```text
Total % =
  (Phase Total % * scope weight + Child Rollup % * child rollup weight)
  / (scope weight + child rollup weight)
```

Default to `scope weight = 1` and `child rollup weight = 1`. Change the weights when the parent phases are mostly governance and the child scopes represent most of the work.

### Scope Weights

Child weights can be equal by default. Use effort, risk, complexity, user value, or critical-path weight when equal weighting would misrepresent reality.

Document the weighting basis in the notes for the parent scope.

---

## Project Snapshot

**Project:** [Project name]
**Date:** [Date]
**Owner:** [Owner]
**Current Focus:** [Phase, service, component, or class]
**Total Complete:** [0-100%]
**Calculation Basis:** [Equal phase weights / weighted phase scores / child rollup blend]

### Top-Level Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | 0% | 1 | [Discovery document] | |
| Requirements | 0% | 1 | [Requirements document] | |
| Architecture | 0% | 1 | [Architecture document] | |
| Planning & Decomposition | 0% | 1 | [Planning document] | |
| Contracts & Tests | 0% | 1 | [Contracts & Tests document] | |
| Implementation | 0% | 1 | [Implementation document / PRs] | |
| Review & Retrospective | 0% | 1 | [Retrospective document] | |
| **Phase Total** | **0%** | | | |

### Top-Level Child Rollup

| Scope | Type | Weight | Phase Total | Child Rollup | Total | Owner | Notes |
|-------|------|--------|-------------|--------------|-------|-------|-------|
| [Service / feature / subsystem] | Service | 1 | 0% | 0% | 0% | | |
| [Service / feature / subsystem] | Service | 1 | 0% | 0% | 0% | | |
| **Child Rollup** | | | | | **0%** | | |

---

## Service Progress

Duplicate this section for each service, feature, subsystem, app, worker, API, integration, or data pipeline.

### Service: [Service Name]

**Purpose:** [What this service owns]
**Owner:** [Owner]
**Total Complete:** 0%
**Phase Total:** 0%
**Child Rollup:** 0%
**Weighting Basis:** [Equal components / effort / risk / critical path]

#### Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | N/A | | | |
| Requirements | 0% | 1 | | |
| Architecture | 0% | 1 | | |
| Planning & Decomposition | 0% | 1 | | |
| Contracts & Tests | 0% | 1 | | Minimum expected phase |
| Implementation | 0% | 1 | | Minimum expected phase |
| Review & Retrospective | 0% | 1 | | |
| **Phase Total** | **0%** | | | |

#### Components

| Component | Weight | Phase Total | Child Rollup | Total | Owner | Notes |
|-----------|--------|-------------|--------------|-------|-------|-------|
| [Component name] | 1 | 0% | 0% | 0% | | |
| [Component name] | 1 | 0% | 0% | 0% | | |
| **Child Rollup** | | | | **0%** | | |

---

## Component Progress

Duplicate this section for each component, module, package, workflow, route group, repository, model area, or UI area.

### Component: [Component Name]

**Parent Service:** [Service name]
**Purpose:** [What this component owns]
**Owner:** [Owner]
**Total Complete:** 0%
**Phase Total:** 0%
**Child Rollup:** 0%
**Weighting Basis:** [Equal classes / effort / risk / critical path]

#### Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | N/A | | | |
| Requirements | 0% | 1 | | |
| Architecture | 0% | 1 | | |
| Planning & Decomposition | 0% | 1 | | |
| Contracts & Tests | 0% | 1 | | Minimum expected phase |
| Implementation | 0% | 1 | | Minimum expected phase |
| Review & Retrospective | 0% | 1 | | |
| **Phase Total** | **0%** | | | |

#### Classes / Smallest Owned Units

| Class / Unit | Weight | Phase Total | Total | Owner | Notes |
|--------------|--------|-------------|-------|-------|-------|
| [Class, function group, command, hook, view, model, schema, or adapter] | 1 | 0% | 0% | | |
| [Class, function group, command, hook, view, model, schema, or adapter] | 1 | 0% | 0% | | |
| **Child Rollup** | | | **0%** | | |

---

## Class / Unit Progress

Duplicate this section for the smallest units worth tracking. Do not track every class by default; track classes, functions, schemas, commands, views, adapters, or workflows when their completion status matters independently.

### Class / Unit: [Name]

**Parent Component:** [Component name]
**Purpose:** [What this unit owns]
**Owner:** [Owner]
**Total Complete:** 0%
**Calculation Basis:** [Usually phase total only]

#### Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
| Discovery | N/A | | | |
| Requirements | N/A | | | |
| Architecture | N/A | | | |
| Planning & Decomposition | N/A | | | |
| Contracts & Tests | 0% | 1 | | Minimum expected phase |
| Implementation | 0% | 1 | | Minimum expected phase |
| Review & Retrospective | 0% | 1 | | Lightweight review is enough |
| **Phase Total** | **0%** | | | |

#### Breakdown

| Item | Complete | Evidence / Source | Notes |
|------|----------|-------------------|-------|
| Contract or expected behavior is defined | 0% | | |
| Tests or verification evidence exist | 0% | | |
| Implementation is complete | 0% | | |
| Integrated with parent component | 0% | | |
| Reviewed or accepted | 0% | | |

---

## Decisions and Adjustments

Use this section when scores change for a reason other than normal task progress.

| Date | Scope | Change | Reason | Owner |
|------|-------|--------|--------|-------|
| | | | | |

---

## Open Progress Questions

| Scope | Question | Needed To Score Accurately | Owner |
|-------|----------|----------------------------|-------|
| | | | |
