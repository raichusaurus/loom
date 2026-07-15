# Loom Progress Ledger Guidance

Use Loom progress to show what evidence exists, what remains, who owns the next decision, and whether the owner has closed a phase gate. The root ledger is a project cockpit, not a second source tree or a substitute for phase artifacts.

Copy [templates/progress-ledger-template.md](templates/progress-ledger-template.md) to `docs/loom/PROGRESS.md` in a project repository.

## What Progress Must Keep Separate

For each phase or independently tracked scope, distinguish:

- **Artifact readiness:** How complete and internally coherent the relevant artifact is.
- **Engineering evidence readiness:** How much of the applicable specialist evidence exists and has been inspected.
- **Agent recommendation:** Ready or not ready, with remaining concerns.
- **Owner decision:** Approved, needs revision, deferred, or pending.
- **Phase completion:** `100%` only when applicable artifact and engineering evidence are ready and the owner has approved the gate.

An artifact can be `100%` ready while the owner decision remains pending. A skill invocation, drafted plan, test count, or coverage percentage does not by itself increase engineering evidence readiness.

For a single headline phase number, use the lower of artifact readiness and applicable engineering evidence readiness. Cap that number at `99%` until the owner approves the gate; an approved gate with both readiness categories complete is `100%`. A deferred or needs-revision decision does not create completion credit by itself.

## Completion Values

Use percentages from `0` to `100` for artifact, evidence, and phase completion.

- `0%` — Not started; no direct evidence inspected.
- `25%` — Initial evidence exists; major known gaps remain.
- `50%` — Usable first pass; consequential gaps or validation remain.
- `75%` — Most applicable evidence exists; known closure work remains.
- `100%` — The named readiness category has complete applicable evidence.
- `N/A` — The category or phase truly does not apply and is excluded from calculations.
- `Unknown` — The scope exists but its evidence has not been inspected.
- `TBD` — The scope is planned but not defined enough to score.

Use exact percentages only when a more precise evidence basis exists, such as weighted requirement disposition, gated scope count, or implementation-slice weights. Document the basis; do not imply precision from intuition.

## Phase Evidence Rubric

| Phase | Evidence required for `100%` readiness before owner approval |
|-------|---------------------------------------------------------------|
| Discovery | Problem, users, current-state evidence, constraints, assumptions and unknowns, validation owners, non-goals, and Requirements handoff are coherent. |
| Requirements | Material scope has stable IDs; acceptance evidence is traceable; quality attributes are ranked, bounded, and sourced; compatibility, assumptions, and Architecture decisions are explicit. |
| Architecture | Applicable framing, evidence, alternatives, contract, risk, migration, and authority gates pass; boundaries, critical flows, validation, and Planning handoff agree. |
| Planning & Decomposition | Material drivers have owners and vertical slices; authority, dependencies, integration, risk validation, and coherent Phase 5 gate scopes are actionable. |
| Contracts & Tests | Every standard TDD scope has schema, observable contract, all currently known executable tests, clause trace, and meaningful red or characterization-green evidence; any owner-approved non-TDD scope records its reason, reduced evidence, missing signal, and follow-up. |
| Implementation | Standard TDD scopes have recorded red-green-refactor slices; approved non-TDD scopes have reduced-check evidence and visible gaps; gate resets are complete; proportionate checks pass; design claims and final clarity are validated. |
| Review & Retrospective | Outcomes and engineering evidence are reviewed; findings and risk are routed to owning phases; next cycles and evidence-backed process candidates are explicit where needed. |

For Contracts & Tests, a plan, candidate list, or unwritten test suite cannot score `100%`. For Implementation, a passing final suite without inspectable pre-state evidence may prove current behavior but cannot retroactively prove TDD provenance.

## Default Phase Weights

Use equal weights unless effort, risk, or delivered value makes another basis materially more honest.

| Phase | Default Weight | Lower-Scope Note |
|-------|----------------|------------------|
| Discovery | 1 | Often inherited or `N/A` below project or novel-feature scope. |
| Requirements | 1 | May be inherited when parent IDs and non-goals clearly cover the scope. |
| Architecture | 1 | May be inherited for a local change inside a stable boundary. |
| Planning & Decomposition | 1 | May be lightweight when ownership and sequencing are obvious. |
| Contracts & Tests | 1 | Direct evidence is expected for behavior-bearing code; do not inherit it from a parent. |
| Implementation | 1 | Direct source and validation evidence is required; do not inherit it. |
| Review & Retrospective | 1 | May be a lightweight scoped review. |

### Rollups

```text
Phase Completion % =
  sum(applicable phase completion * phase weight)
  / sum(applicable phase weights)

Child Rollup % =
  sum(child completion * child weight)
  / sum(child weights)
```

For a child with its own Loom phase gate, calculate completion with the same readiness minimum and `99%` owner-approval cap. For a nongated delivery child, completion is the lower of its applicable artifact and engineering evidence readiness and may reach `100%` from complete direct evidence; set the owner decision to `N/A`. This gives every rolled-up child one inspectable completion value.

Do not silently exclude a weighted `Unknown` or `TBD` child. The default parent rollup remains `Unknown` while existing child evidence is uninspected and `TBD` while planned scope is not defined enough to score. If a stakeholder needs a partial view, report a separately labeled `Known-child rollup` with evidence coverage such as `4 of 6 child weights inspected`; do not present it as the total.

If a parent combines governance work and delivered child scopes, show both numbers before choosing a documented blend. Do not hide a blocked critical child behind a healthy average.

## Traceability Mapping

Loom scopes, source evidence, and test evidence must be linkable; they do not need identical directory hierarchies.

- Architecture defines stable components, ownership, contracts, and data boundaries—not private classes or a complete file tree.
- Planning maps owned workstreams and stable boundaries to likely source and test areas.
- Contracts & Tests chooses the highest stable test boundary that proves behavior.
- Implementation records actual paths and updates stale provisional mappings.
- Private classes, functions, helpers, fixtures, adapters, and test doubles remain evidence rows unless they have independent ownership, contracts, blockers, scoring evidence, or a review path.

Recommended artifact layout:

```text
docs/loom/
  README.md
  PROGRESS.md
  phases/
    01-discovery/{README.md,PROGRESS.md}
    02-requirements/{README.md,PROGRESS.md}
    03-architecture/{README.md,PROGRESS.md}
    04-planning/{README.md,PROGRESS.md}
    05-contracts-tests/{README.md,PROGRESS.md}
    06-implementation/{README.md,PROGRESS.md}
    07-review/{README.md,PROGRESS.md}
  system/
    [independently-tracked-component]/PROGRESS.md
```

Source and test layouts follow their language and framework conventions. Record their mapping in the ledger rather than forcing them to copy `docs/loom/system/`.

## When a Child Ledger Earns a File

Create a child `PROGRESS.md` when a scope has one or more of:

- Independent owner or decision authority
- Stable contract or separate TDD gate
- Blocker surface or critical dependency
- Material implementation and validation path
- Independent review, migration, release, or recovery path

Inventory every discovered material scope, but keep smaller scopes as rows in the nearest parent with `Parent row` and a short reason. Do not create a ledger merely because a class, function, schema, adapter, or test double exists.

Phase progress ledgers remain useful in a recursive project because each phase has distinct evidence and owner authority. System child ledgers are proportionate, not automatic.

## Scope Inventory

Build an inventory before creating child files:

| Scope | Type | Parent | Source Evidence | Progress Location | Source Area | Stable Test Boundary | Inclusion Decision |
|-------|------|--------|-----------------|-------------------|-------------|----------------------|--------------------|
| [Scope] | Phase / Workstream / Component / Feature / Migration / Unit | [Parent] | [Artifact, contract, source, or test] | [Child path or Parent row] | [Known / TBD] | [Known / TBD] | Child ledger / Parent row / Deferred |

`Deferred` means the scope is known but intentionally outside the active cycle. `Unknown` means evidence has not yet been inspected. Neither is `N/A`.

## Engineering Evidence Ledger

Track route evidence only when technical work in the scope needs it. This is evidence, not a skill-usage scorecard.

| Scope / Decision | Operating Mode | Lead / Overlays | Trigger | Required Evidence | Observed Evidence | Reopened Upstream Decision | Status |
|------------------|----------------|-----------------|---------|-------------------|-------------------|----------------------------|--------|
| | Design / Implement / Refactor / Review | System Design / TDD / Design Patterns / Clean Code / None | | | | | Unknown / In progress / Ready / Blocked |

Examples of direct evidence:

- **System Design:** Driver trace, options, contracts, critical-path challenge, validation, and conditional migration or rollback.
- **TDD:** Scope, schema, contract, all currently known executable tests, meaningful red or characterization baseline, per-slice green, and final broader green.
- **Design Patterns:** Demonstrated pressure, direct and idiomatic alternatives, economics, domain participants, and validation of claimed change locality.
- **Clean Code:** Stable contract, narrow diff, proportionate checks, final clarity pass, and diff inspection.

## Phase-by-Phase Population

| Phase | Honest Progress-Tree Maturity |
|-------|-------------------------------|
| Discovery | Project-level status and obvious existing systems or surfaces; implementation paths remain unknown. |
| Requirements | Coarse workstreams, surfaces, integrations, compatibility needs, and candidate components; paths can be `TBD`. |
| Architecture | Stable independently owned or contract-bearing boundaries and provisional evidence mapping; no forced private units. |
| Planning & Decomposition | Owned workstreams, vertical slices, gate scopes, dependency and integration evidence, and proportionate child decisions. |
| Contracts & Tests | Direct schema, contract, all-known-test, and pre-state evidence for every gated scope. |
| Implementation | Actual source and test evidence, slice status, gate resets, validation, and mapping corrections. |
| Review & Retrospective | Final evidence disposition, remaining risk, owning follow-up phases, and unnecessary child-ledger cleanup. |

## Refresh Workflow

When building or refreshing progress:

1. Read the phase artifacts and existing owner decisions.
2. Inspect applicable schemas, contracts, tests, validation output, and source evidence.
3. Build or update the scope inventory.
4. Update artifact readiness, engineering evidence readiness, recommendation, and owner gate separately.
5. Create or retain child files only where independent tracking earns them.
6. Link parents and children in both directions.
7. Record the next evidence-changing action, owner, blocker, and decision point.
8. Use `Unknown`, `TBD`, `N/A`, or `Deferred` honestly.
9. Recalculate rollups and state their weighting basis.
10. Inspect for stale paths, unsupported scores, duplicate facts, and hidden critical blockers.

Update progress when a phase gate changes, a scope or owner changes, a TDD gate moves from incomplete to meaningful pre-state or green, implementation evidence lands, a gate resets, validation changes confidence, or review changes disposition.

## Gate Record

| Phase / Scope | Artifact Readiness | Engineering Evidence Readiness | Agent Recommendation | Owner Decision | Decision Date | Remaining Concerns |
|---------------|--------------------|--------------------------------|----------------------|----------------|---------------|--------------------|
| | 0–100% / N/A | 0–100% / N/A | Ready / Not ready / TBD | Approved / Needs revision / Deferred / Pending | | |

The owner decision closes a gate; the agent does not infer it from a score. New evidence may reopen the owning phase and dependent readiness scores.

## Template

Use [templates/progress-ledger-template.md](templates/progress-ledger-template.md) for the project cockpit and child-ledger shape. Keep detailed evidence in the owning phase artifact or linked source/test output rather than copying it into every ledger.
