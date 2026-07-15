# Loom Progress Ledger

Use this file as `docs/loom/PROGRESS.md`. It is the project cockpit; detailed evidence remains in phase artifacts, schemas, contracts, tests, validation output, source, and proportionate child ledgers.

The sample phase links below are relative to the copied `docs/loom/PROGRESS.md`; they are intentionally not repository-local links from this template file.

## Project Snapshot

**Project:** [Project]
**Date:** [YYYY-MM-DD]
**Owner:** [Owner]
**Current Focus:** [Phase, workstream, or evidence-changing push]
**Phase Completion:** [0–100% / Unknown / TBD]
**Child Rollup:** [0–100% / Unknown / TBD / N/A]
**Calculation Basis:** [Weights and formula]

## Phase Status

Keep artifact readiness, engineering evidence readiness, recommendation, and owner authority separate.

| Phase | Artifact Readiness | Engineering Evidence Readiness | Phase Completion | Weight | Agent Recommendation | Owner Decision | Evidence / Source | Remaining Concerns |
|-------|--------------------|--------------------------------|------------------|--------|----------------------|----------------|-------------------|--------------------|
| Discovery | 0% | N/A | 0% | 1 | TBD | Pending | [Phase progress](phases/01-discovery/PROGRESS.md) | |
| Requirements | 0% | N/A | 0% | 1 | TBD | Pending | [Phase progress](phases/02-requirements/PROGRESS.md) | |
| Architecture | 0% | 0% | 0% | 1 | TBD | Pending | [Phase progress](phases/03-architecture/PROGRESS.md) | |
| Planning & Decomposition | 0% | N/A | 0% | 1 | TBD | Pending | [Phase progress](phases/04-planning/PROGRESS.md) | |
| Contracts & Tests | 0% | 0% | 0% | 1 | TBD | Pending | [Phase progress](phases/05-contracts-tests/PROGRESS.md) | |
| Implementation | 0% | 0% | 0% | 1 | TBD | Pending | [Phase progress](phases/06-implementation/PROGRESS.md) | |
| Review & Retrospective | 0% | 0% | 0% | 1 | TBD | Pending | [Phase progress](phases/07-review/PROGRESS.md) | |

Phase completion reaches `100%` only when applicable artifact and evidence readiness are complete and the owner has approved the gate.

For a headline phase number, use the lower of artifact readiness and applicable engineering evidence readiness, capped at `99%` until owner approval. Treat `N/A` engineering evidence as excluded rather than zero.

## Scope Inventory

Inventory material scopes before deciding which ones earn child files. Source and test paths must be traceable, not structurally identical.

| Scope | Type | Parent | Source Evidence | Progress Location | Source Area | Stable Test Boundary | Inclusion Decision |
|-------|------|--------|-----------------|-------------------|-------------|----------------------|--------------------|
| | Phase / Workstream / Component / Feature / Migration / Unit | | | `system/.../PROGRESS.md` or Parent row | Known / TBD | Known / TBD | Child ledger / Parent row / Deferred |

## Progress Tree

| Scope | Type | Parent | Artifact Readiness | Engineering Evidence Readiness | Completion | Owner Gate / Status | Weight | Progress Location | Current Focus |
|-------|------|--------|--------------------|--------------------------------|------------|---------------------|--------|-------------------|---------------|
| | | | | | | | | | |

Create a child ledger only when a scope has independent ownership, a stable contract or separate TDD gate, blockers, material validation, or an independent review, migration, release, or recovery path.

For a child with a Loom gate, apply the `99%` cap until owner approval. For a nongated child, use the lower of applicable artifact and engineering evidence readiness and allow `100%` from complete direct evidence; record owner decision as `N/A`.

## Engineering Evidence

Invoking a skill earns no progress. Link the evidence required by the technical decision.

| Scope / Decision | Operating Mode | Lead / Overlays | Trigger | Required Evidence | Observed Evidence | Reopened Upstream Decision | Status |
|------------------|----------------|-----------------|---------|-------------------|-------------------|----------------------------|--------|
| | Design / Implement / Refactor / Review | System Design / TDD / Design Patterns / Clean Code / None | | | | | Unknown / In progress / Ready / Blocked |

## Next Evidence-Changing Actions

| Action | Phase / Scope | Evidence or Score Changed | Owner | Blocker / Decision Point |
|--------|---------------|---------------------------|-------|--------------------------|
| | | | | |

## Decisions and Reopened Gates

| Date | Scope | Decision / Change | Reason / New Evidence | Owning Phase Reopened | Downstream Artifacts to Refresh | Owner |
|------|-------|-------------------|-----------------------|-----------------------|---------------------------------|-------|
| | | | | | | |

## Open Progress Questions

Only material questions that prevent honest scoring need a decision packet.

| Scope | Question | Options | Tradeoffs | Recommendation | Evidence Needed | Decision Owner / Point |
|-------|----------|---------|-----------|----------------|-----------------|------------------------|
| | | | | | | |

---

## Child Progress Ledger Shape

Copy the following shape only for a scope that earns independent tracking.

```md
# Progress: [Scope]

**Type:** [Phase / Workstream / Component / Feature / Migration / Unit]
**Parent:** [Parent progress]([relative-path-to-parent-PROGRESS.md])
**Owner:** [Owner]
**Current Focus:** [Next evidence-changing action]
**Last Updated:** [YYYY-MM-DD]
**Artifact Readiness:** [0–100% / Unknown / TBD / N/A]
**Engineering Evidence Readiness:** [0–100% / Unknown / TBD / N/A]
**Completion:** [0–100% / Unknown / TBD]
**Agent Recommendation:** [Ready / Not ready / TBD]
**Owner Decision:** [Approved / Needs revision / Deferred / Pending / N/A]

## Navigation

- **Parent:** [Parent progress]([relative-path-to-parent-PROGRESS.md])
- **Children:** [Child progress docs, if any]
- **Owning phase artifacts:** [Links]
- **Relevant schemas, contracts, tests, source, and validation:** [Links]

## Phase Status

| Phase | Artifact Readiness | Engineering Evidence Readiness | Phase Completion | Weight | Agent Recommendation | Owner Decision | Evidence / Source | Notes |
|-------|--------------------|--------------------------------|------------------|--------|----------------------|----------------|-------------------|-------|
| Discovery | N/A | N/A | N/A | | N/A | N/A | | |
| Requirements | N/A | N/A | N/A | | N/A | N/A | | |
| Architecture | N/A | N/A | N/A | | N/A | N/A | | |
| Planning & Decomposition | N/A | N/A | N/A | | N/A | N/A | | |
| Contracts & Tests | 0% | 0% | 0% | 1 | TBD | Pending | | |
| Implementation | 0% | 0% | 0% | 1 | TBD | Pending | | |
| Review & Retrospective | 0% | 0% | 0% | 1 | TBD | Pending | | |

## Local Scope Inventory

| Scope | Type | Source Evidence | Progress Location | Source Area | Stable Test Boundary | Inclusion Decision |
|-------|------|-----------------|-------------------|-------------|----------------------|--------------------|
| | | | Child path / Parent row | Known / TBD | Known / TBD | Child ledger / Parent row / Deferred |

## Engineering Evidence

| Decision / Change Scope | Operating Mode | Lead / Overlays | Required Evidence | Observed Evidence | Gate Status |
|-------------------------|----------------|-----------------|-------------------|-------------------|-------------|
| | | | | | |

## Children

| Scope | Type | Weight | Artifact Readiness | Engineering Evidence Readiness | Completion | Progress Doc | Notes |
|-------|------|--------|--------------------|--------------------------------|------------|--------------|-------|
| | | | | | | | |

## Next Evidence-Changing Actions

| Action | Phase / Area | Expected Evidence Change | Owner |
|--------|--------------|--------------------------|-------|
| | | | |

## Blockers, Decisions, and Gate Resets

| Item | Impact | Owning Phase | Owner | Next Step / Decision Point |
|------|--------|--------------|-------|----------------------------|
| | | | | |

## Gate Record

| Artifact Readiness | Engineering Evidence Readiness | Agent Recommendation | Owner Decision | Decision Date | Remaining Concerns |
|--------------------|--------------------------------|----------------------|----------------|---------------|--------------------|
| 0–100% / Unknown / TBD / N/A | 0–100% / Unknown / TBD / N/A | Ready / Not ready / TBD | Approved / Needs revision / Deferred / Pending / N/A | | |
```
