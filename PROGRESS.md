# Loom Progress Ledger

Use this document to track completion at every useful scope: project, service, component, class, workflow, or task-level mini-Loom. The goal is to make progress visible at each zoom level without pretending every scope needs every phase.

Copy this file into a project repo and update it throughout the Loom cycle.

This root file is the project cockpit. It can stand alone for small projects, or act as an index into a recursive progress tree for larger projects. When a project asks for recursive progress, populate the drilldown tree automatically instead of waiting for follow-up prompts at each level.

Update this document whenever changes land on the project's main branch, especially when:

- A phase gate opens or closes
- A workstream, service, component, or smallest tracked unit is added, removed, split, or merged
- Contracts/tests move from planned to executable, or from red to green
- Implementation scope lands
- CI/check automation changes status
- Review, acceptance, or retrospective evidence changes a score

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
- `Unknown` = scope exists but evidence has not been inspected yet; treat as a scoring gap to resolve, not as `N/A`
- `TBD` = scope is expected or planned but not yet defined enough to score

Use exact percentages when you have a better signal, such as task counts, test pass counts, implementation slices, or reviewed deliverables.

Contract readiness is not the same as product readiness. A scope can be `100%` complete for Contracts & Tests while still being `0%` complete for Implementation.

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

Lower-level scopes may inherit Requirements, Architecture, and Planning credit from parent phase documents when those documents clearly define the scope, boundaries, contracts, and work ownership. Do not inherit Contracts & Tests or Implementation credit unless that lower-level scope has direct evidence.

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

## Recursive Progress Tree

Use one root `PROGRESS.md` first for a small project or quick status pass. When the user asks for drilldowns, a progress tree, zoom levels, a visual system map, or recursive progress, create and populate child progress docs for every discovered phase and scope by default.

Do not stop after the root file. The root is an index and rollup; the child files are the zoomable progress surface.

Recommended project layout:

```text
docs/loom/
  PROGRESS.md
  phases/
    discovery/PROGRESS.md
    requirements/PROGRESS.md
    architecture/PROGRESS.md
    planning/PROGRESS.md
    contracts-tests/PROGRESS.md
    implementation/PROGRESS.md
    review/PROGRESS.md
  scopes/
    services/
      [service-name]/PROGRESS.md
    components/
      [service-name]/[component-name]/PROGRESS.md
    units/
      [service-name]/[component-name]/[unit-name]/PROGRESS.md
```

Each child progress document should include:

- Link back to its parent progress document
- Links to child progress documents when they exist
- Phase scores relevant to that zoom level
- Evidence links for each score
- Blockers, open questions, and next score-changing actions

Use this rule of thumb for whether a scope needs ongoing independent maintenance:

> If a scope has its own owner, contracts, implementation path, blocker surface, or review path, it can earn its own `PROGRESS.md`.

When first auto-populating a recursive tree, be more inclusive than that rule of thumb:

- Create phase progress docs for all seven Loom phases, even if some are lightweight.
- Create service/workstream progress docs for every service, app, worker, API, integration, data pipeline, or major delivery stream named in Architecture or Planning.
- Create component progress docs for every component/module/package/workflow/control surface named in Architecture, Planning, Contracts & Tests, or the source tree.
- Create unit progress docs for every class, command, function group, schema, model, repository, adapter, workflow, test double, or other smallest owned unit named in contracts/tests or exposed by the source tree.
- If a unit seems too small after inspection, keep it in the nearest parent table with `No child doc` and explain why. Do not silently omit it.
- Use `Unknown` when evidence has not been inspected yet. Use `N/A` only when a phase truly does not apply.

### Auto-Population Workflow

When building or refreshing a recursive progress tree:

1. Read the phase docs, especially Requirements, Architecture, Planning, Contracts & Tests, and Implementation.
2. Read existing tests and contract fixtures to discover expected services, components, and units.
3. Inspect the source tree, public classes/functions, CLI commands, schemas, repositories, adapters, and workflows.
4. Build a scope inventory before writing progress docs.
5. Create the root `PROGRESS.md` rollup and tree index.
6. Create child phase progress docs under `phases/*/PROGRESS.md`.
7. Create child scope progress docs under `scopes/services`, `scopes/components`, and `scopes/units`.
8. Link every child from its parent and every parent from its child.
9. Mark scores with evidence links, `Unknown`, `TBD`, or `N/A`; do not leave discovered scopes unrepresented.
10. Add open progress questions for anything that could not be scored confidently.

### Scope Inventory

Use this table before or inside the root progress file to show that the tree was populated from evidence rather than vibes.

| Scope | Type | Parent | Source Evidence | Progress Doc | Inclusion Decision |
|-------|------|--------|-----------------|--------------|--------------------|
| [Scope name] | Phase / Workstream / Service / Component / Unit | [Parent] | [Doc/test/source path] | [Path or No child doc] | Included / Rolled into parent / Deferred |

### Progress Tree Index

Use this table in the root file to make drilldowns clickable. Keep the root concise; let child progress docs carry deep detail.

| Scope | Type | Parent | Total | Current Focus | Progress Doc | Notes |
|-------|------|--------|-------|---------------|--------------|-------|
| Discovery | Phase | Project | 0% | | `phases/discovery/PROGRESS.md` | Create in recursive mode |
| Requirements | Phase | Project | 0% | | `phases/requirements/PROGRESS.md` | Create in recursive mode |
| Architecture | Phase | Project | 0% | | `phases/architecture/PROGRESS.md` | Create in recursive mode |
| Planning & Decomposition | Phase | Project | 0% | | `phases/planning/PROGRESS.md` | Create in recursive mode |
| Contracts & Tests | Phase | Project | 0% | | `phases/contracts-tests/PROGRESS.md` | Create in recursive mode |
| Implementation | Phase | Project | 0% | | `phases/implementation/PROGRESS.md` | Create in recursive mode |
| Review & Retrospective | Phase | Project | 0% | | `phases/review/PROGRESS.md` | Create in recursive mode |
| [Service name] | Service | Project | 0% | | `scopes/services/[service-name]/PROGRESS.md` | |
| [Component name] | Component | [Service name] | 0% | | `scopes/components/[service-name]/[component-name]/PROGRESS.md` | |
| [Class / unit name] | Unit | [Component name] | 0% | | `scopes/units/[service-name]/[component-name]/[unit-name]/PROGRESS.md` | |

### Child Progress Template

Use this shape for any phase, service, component, or unit-level progress document.

```md
# Progress: [Scope Name]

**Type:** [Phase / Service / Component / Unit]
**Parent:** [Parent scope](../PROGRESS.md)
**Owner:** [Owner]
**Total Complete:** 0%
**Current Focus:** [What is changing next]
**Last Updated:** [Date]

## Navigation

- **Parent:** [Parent progress](../PROGRESS.md)
- **Children:** [Child progress docs, if any]
- **Related phase docs:** [Requirements / Architecture / Planning / Contracts / Implementation]

## Phase Completion

| Phase | Complete | Weight | Evidence / Source | Notes |
|-------|----------|--------|-------------------|-------|
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

| Scope | Type | Source Evidence | Progress Doc | Inclusion Decision |
|-------|------|-----------------|--------------|--------------------|
| | | | | |

## Next Score-Changing Actions

| Action | Phase / Area | Expected Score Impact | Owner |
|--------|--------------|-----------------------|-------|
| | | | |

## Blockers and Questions

| Item | Impact | Owner | Next Step |
|------|--------|-------|-----------|
| | | | |
```

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

## Workstream Progress

Use this compact matrix for the main implementation or delivery workstreams. Workstreams can be services, feature slices, platform areas, CI/bootstrap tracks, documentation tracks, or any other owned stream that helps explain delivery progress.

| Workstream | Requirements | Architecture | Planning | Contracts & Tests | Implementation | Review | Total | Evidence |
|------------|--------------|--------------|----------|-------------------|----------------|--------|-------|----------|
| [Workstream name] | 0% | 0% | 0% | 0% | 0% | 0% | 0% | |
| [Workstream name] | 0% | 0% | 0% | 0% | 0% | 0% | 0% | |

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

Duplicate this section for the smallest units discovered in contracts/tests, architecture/planning docs, or the source tree. In recursive mode, include every discovered class, function group, schema, command, view, adapter, workflow, repository, model, or test double somewhere in the progress tree. Create a child progress doc when useful; otherwise keep the unit in its parent table with evidence and an explicit `No child doc` note.

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
