# Phase 6: Implementation

## Purpose

Implementation answers: **What is the smallest verified code change that satisfies the locked contract clearly and safely?**

Loom owns implementation scope, coordination, progress, deviations, the phase gate, and handoff. The local `software-engineering` router composes the technical work: TDD controls sequencing, Clean Code is the baseline for touched code, Design Patterns applies only to demonstrated source-level pressure, and System Design re-enters when a finding crosses a system boundary.

## Entry Gate

Do not change behavior-bearing implementation for a scope until its Contracts & Tests handoff provides one of two explicit entry paths.

The normal TDD path provides:

- Owner-approved coherent scope and explicit non-goals
- Applicable schema and compatibility rules
- Observable contract and clause-to-test trace
- All currently known executable tests
- Meaningful red for new or changed behavior, or a green characterization baseline for a refactor
- Exact focused command and observed result
- Any baseline failure that must remain distinguished

The exception path provides:

- Explicit owner-approved scope, non-goals, and observable contract
- Applicable schema and compatibility rules
- The non-TDD bypass reason and exactly which normal test or pre-state evidence is missing
- Available reduced evidence and checks
- Follow-up, owner, and decision point for closing the evidence gap

Do not describe that work as TDD.

Within work claimed as TDD, behavior-free scaffolding is the only pre-red exception. Under either path, an unresolved decision that implementation would necessarily settle keeps the gate closed.

## Implementation Loop

The red-green-refactor evidence below applies to standard TDD scopes. For an approved non-TDD scope, make the same narrow contract-backed change, run and record the exception's reduced checks, keep missing evidence visible, and do not manufacture or claim red-green provenance.

### 1. Confirm the Slice

Choose the highest-risk coherent contract-backed slice that can produce useful feedback. Identify the locked contract clauses it satisfies and the deferred decisions it must not encode.

Scope-level gating precedes slicing: a standard TDD increment cannot postpone an already known boundary or failure test, and an exception scope must keep every missing known case explicit in its approved evidence gap.

### 2. Make the Minimum Change

Write only the production behavior required to satisfy the locked clauses. Keep behavior changes distinguishable from mechanical movement, avoid unrelated cleanup, and do not add speculative configuration, extension points, abstractions, or cases.

For a standard TDD scope, run the focused tests after each meaningful increment. For a non-TDD exception, run the recorded reduced check. Do not weaken assertions, over-mock the subject, or change the contract merely to make the code pass.

### 3. Prove Green and Refactor

For a standard TDD scope, record the focused green result, then refactor names, duplication, boundaries, and structure only while the applicable tests remain green. For a non-TDD exception, record the reduced-check result and do not perform behavior-preserving structural refactoring without either a characterization baseline or a separately approved evidence exception. Re-run applicable checks after each meaningful refactor and broader checks in proportion to risk.

### 4. Reset the Gate When Scope Changes

If implementation discovers a new supported behavior, edge case, schema change, contract clause, failure rule, or cross-boundary decision:

1. Stop behavior-bearing implementation for the affected scope.
2. Return to the phase that owns the changed requirement or architecture decision when necessary.
3. Revise schema and contract in Contracts & Tests.
4. For the standard TDD path, update all currently known executable tests and record the new meaningful red or appropriate characterization baseline. For a non-TDD path, obtain a new explicit exception for the expanded scope and record the changed gaps and reduced checks; the prior exception does not silently expand.
5. Obtain required approval and resume only when the gate is open again.

A change in task order or private implementation detail may remain a Planning or Implementation deviation. A changed observable contract is not merely a deviation.

## Design Pressure and Patterns

Prefer direct, idiomatic code. Before adding a named pattern or new abstraction, identify:

- The concrete present pressure and realistic supported change scenario
- The stable contract and actual axis of variation
- The current/local solution, an existing language or framework mechanism, and the named-pattern option
- The concepts, files, runtime paths, lifecycle, concurrency, migration, and debugging cost added
- Why the chosen collaboration removes more relevant reasoning burden than it introduces
- Domain-named participants, ownership, effects, failure behavior, and a revisit or removal trigger

Pattern analysis may occur after the pressure and stable contract are known, but behavior-bearing participants wait for the applicable Implementation entry gate. Validate the design claim: a representative supported change should be localized where intended, and callers should not need pattern-specific knowledge. Remove ceremonial participants and speculative extension points.

## Final Clarity Pass

Read the touched code as a future maintainer would while the applicable TDD tests are green or the approved exception's reduced checks pass:

- Names and vocabulary communicate domain intent consistently.
- Routines and modules are cohesive and stay at understandable abstraction levels.
- State ownership, effects, validation, errors, retries, timeouts, cancellation, and cleanup are visible where relevant.
- Nesting, duplication, coupling, and comments represent real knowledge rather than cosmetic rules.
- Public contracts, serialized shapes, persistence, configuration, events, and machine-consumed errors did not drift accidentally.
- Dead code, debug output, stale comments, unused abstractions, secrets, generated noise, and unrelated churn are absent.

This is one proportionate engineering pass, not a demand for broad cleanup.

## Integrated Validation and Handoff

Record one evidence set for Implementation and Review:

- Schema and contract established
- Meaningful-red or characterization-baseline command and result, or the approved non-TDD exception and reduced checks
- Per-slice focused green commands and results for TDD scopes, or per-slice reduced-check results for exception scopes
- Applicable schema, contract, unit, integration, end-to-end, type, format, lint, build, migration, security, and manual checks with exact results
- Pattern design-claim evidence when a pattern or abstraction was introduced
- Final clarity and diff-inspection result
- Gate resets, approved deviations, remaining risk, and anything unverified

Run focused checks first, then broaden in proportion to contract surface and risk. Coverage percentages are supporting signals only; contract and behavioral evidence determine confidence.

## Outputs

- Working implementation for the approved scope
- Per-slice contract and non-goal evidence, plus pre-state, green, and refactor evidence for TDD scopes or reduced-check evidence for approved exception scopes
- Updated local and CI/check automation where the scaffold now supports meaningful checks
- Evidence-backed pattern or no-pattern decisions when relevant
- Final clarity and diff inspection
- Traceable progress, gate-reset, deviation, integration, and maintenance notes
- A self-contained Review & Retrospective handoff

## When Implementation Is Ready for Owner Review

- Every TDD-implemented behavior traces to an approved scope, schema, contract clause, and pre-implementation test; every non-TDD behavior traces to an explicit owner-approved bypass and reduced-evidence record.
- Focused and proportionate broader checks pass; exact commands and results are recorded.
- Tests were not weakened to accommodate implementation.
- Newly discovered behavior or contract changes were regated before implementation continued.
- Pattern or abstraction choices answer demonstrated pressure and their design claim was validated.
- The touched code received a proportionate clarity pass while applicable TDD tests were green or approved reduced checks passed.
- Progress and traceability reflect delivered reality without forcing private structures into child ledgers.
- Approved deviations, remaining risks, and unverified items are explicit.
- Integration handoffs are complete and applicable automation works or has an owner and reason for deferral.
- The agent recommendation remains separate from owner approval.

## Release and Operations Follow-Up

If implementation exposes deployment, scheduling, monitoring, runbook, release automation, or production-support needs outside the approved scope, capture a focused follow-up Loom cycle. Do not silently broaden a local-first or MVP implementation.

## Loom Process Feedback

Capture only a phase-local observation about material routing friction, a mishandled gate reset, repeated workaround, false confidence, validation failure, or excessive ceremony. Put any reusable evidence-backed candidate in `docs/loom/pilot-feedback.md`. A clean phase needs no feedback note.

---

Move to [Review & Retrospective](./07-review-retrospective.md) after the owner approves the Implementation gate.
