# Implementation Template

Use this template to implement approved contract-backed scopes, preserve the TDD gate, and hand one integrated evidence set to Review.

**Project Name:** [Project name]
**Date:** [Date]
**Implementation Lead:** [Lead]

## Inputs

- **Requirements and acceptance IDs:**
- **Architecture decisions, boundaries, and contract IDs:**
- **Planning scopes, owners, and context packets:**
- **Contracts & Tests gate artifact:**
- **Automation and integration handoff:**

## Entry Gate by Scope

No behavior-bearing implementation begins until every required field for that scope is inspectable and the owner has approved Phase 5.

| Scope ID | Owner Approval | Schema / Compatibility | Locked Contract / Trace | All Known Tests or Recorded Gap | Pre-State Signal or Approved Non-TDD Exception | Exact Focused Command / Reduced Check | Open Decision Code Would Settle? | Entry Status |
|----------|----------------|------------------------|-------------------------|---------------------------------|------------------------------------------------|---------------------------------------|----------------------------------|--------------|
| | | | | | | | No | Open / Passed / Blocked / Approved non-TDD exception |

## Workstream Status

| Workstream / Scope | Owner | Authorized Paths | Current Slice | Status | Branch / PR | Notes |
|--------------------|-------|------------------|---------------|--------|-------------|-------|
| | | | | | | |

## Implementation Slice Evidence Ledger

Each slice names the contract clauses it satisfies and deferred decisions it must not encode. Standard TDD scopes already have scope-level tests before the first slice; approved non-TDD scopes keep missing test/pre-state evidence visible and use their recorded reduced checks.

| Slice | Scope / Contract Clauses | Explicit Non-Goals / Deferred Decisions | Pre-State Evidence or Approved Exception | Minimum Behavior Added | Focused Green or Reduced Check / Result | Refactor / Clarity Evidence | Broader Validation | Status |
|-------|--------------------------|-----------------------------------------|------------------------------------------|------------------------|-----------------------------------------|-----------------------------|--------------------|--------|
| | | | | | | | | |

## Gate Reset Log

A new supported behavior, edge case, schema, contract clause, failure rule, or cross-system decision stops affected behavior-bearing implementation. Return to the owning phase and re-establish schema and contract, plus either all currently known executable tests and the required pre-state or a renewed owner-approved non-TDD exception with changed gaps and reduced checks.

| Trigger / Discovery | Affected Scope | Owning Phase Reopened | Schema / Contract / Test Updates | New Pre-State or Renewed Exception Evidence | Required Approval | Resume Status |
|---------------------|----------------|-----------------------|----------------------------------|---------------------------------------------|-------------------|---------------|
| | | Requirements / Architecture / Contracts & Tests | | | | Paused / Approved / Resumed |

## Design Pressure and Pattern Decisions

*Optional. Use only when a named pattern or new abstraction is proposed. Delete when direct code is sufficient.*

### Concrete Pressure

- **Current behavior or dependency that is difficult:**
- **Realistic supported change scenario:**
- **Stable contract and axis of variation:**

### Options and Economics

| Option | Present Benefit | New Concepts / Files / Indirection | Runtime / Lifecycle / Concurrency / Migration / Debugging Cost | Why It Fits or Fails |
|--------|-----------------|------------------------------------|---------------------------------------------------------------|---------------------|
| Focused local correction / direct code | | | | |
| Existing repository, language, or framework mechanism | | | | |
| Named pattern in the simplest idiomatic form | | | | |

### Decision and Design-Claim Validation

- **Chosen option or explicit no-pattern decision:**
- **Domain-named participants and ownership:**
- **State, effects, errors, lifecycle, and dependency direction:**
- **Representative change used to validate locality:**
- **Observed result:**
- **Revisit or removal trigger:**

## Deviations and Blockers

### Deviations

| Deviation | Type | Reason / Evidence | Approval | Affected Artifacts | Follow-Up |
|-----------|------|-------------------|----------|--------------------|-----------|
| | Planning-only / Architecture-changing / Contract-changing / Implementation detail | | | | |

Architecture- or contract-changing discoveries must appear in the Gate Reset Log; recording a deviation alone does not authorize continuation.

### Blockers and Material Decisions

| Item | Impact | Options / Tradeoffs | Recommendation | Owner / Decision Point | Next Action |
|------|--------|---------------------|----------------|------------------------|-------------|
| | | | | | |

## Progress and Traceability

Map stable Loom scopes to actual source and test evidence. Do not create child ledgers for every private helper.

| Scope | Progress Doc or Parent Row | Source Evidence | Test Evidence | Contract / Gate Evidence | Update Needed |
|-------|----------------------------|-----------------|---------------|--------------------------|---------------|
| | | | | | |

## Integrated Validation

Record exact commands and results rather than generic checked boxes.

| Check | Exact Command or Procedure | Result | Evidence Link / Relevant Output | Required? | Remaining Gap |
|-------|----------------------------|--------|---------------------------------|-----------|---------------|
| Schema / generation | | | | | |
| Focused contract / unit | | | | | |
| Integration / end-to-end | | | | | |
| Type / format / lint | | | | | |
| Build / migration / compatibility | | | | | |
| Security / privacy | | | | | |
| Manual user or operator validation | | | | | |
| Live / external opt-in check | | | | | |

### Automation Bootstrap

- [ ] Dependency install and lock behavior is reproducible or not applicable.
- [ ] Focused test command works locally, or the approved exception's reduced check is reproducible.
- [ ] Applicable format, lint, type, build, and migration commands work.
- [ ] CI or equivalent checks are added when the project has meaningful stable commands.
- [ ] Live or external tests remain opt-in unless the project explicitly requires otherwise.

## Final Clarity and Diff Inspection

- [ ] Names and vocabulary communicate domain intent consistently.
- [ ] Routines and modules are cohesive and stay at understandable abstraction levels.
- [ ] State ownership, effects, validation, failure, retry, timeout, cancellation, and cleanup are visible where relevant.
- [ ] No speculative abstraction, ceremonial pattern participant, or unused extension point remains.
- [ ] Comments explain durable rationale rather than syntax; stale comments are removed.
- [ ] Public contracts, schemas, persistence, configuration, events, and machine-consumed errors did not drift accidentally.
- [ ] Dead code, debug output, secrets, generated noise, and unrelated churn are absent.
- [ ] Relevant tests were rerun after meaningful refactors, or approved reduced checks were rerun for an exception scope.

## Engineering Handoff to Review

- **Delivered scope and non-goals:**
- **Schema and observable contract:**
- **Original meaningful-red or characterization-baseline evidence, or approved non-TDD exception:**
- **Per-slice focused green evidence or approved reduced-check evidence:**
- **Broader validation commands and results:**
- **Gate resets and approved deviations:**
- **Pattern or no-pattern rationale and design-claim evidence:**
- **Final clarity and diff-inspection result:**
- **Remaining risk and unverified items:**
- **Integration and maintenance notes:**

## Release and Operations Follow-Up

*Optional. Capture needs outside the approved implementation scope as a focused next Loom cycle.*

| Follow-Up | Reason / Risk | Suggested Starting Phase | Owner |
|-----------|---------------|--------------------------|-------|
| | | Requirements / Architecture / Planning / Contracts & Tests / Implementation | |

## Decision Log

| Date | Decision | Evidence | Choice | Owner | Revisit Trigger |
|------|----------|----------|--------|-------|-----------------|
| | | | | | |

## Loom Process Feedback

*Optional. Record only a phase-local routing friction, mishandled gate reset, repeated workaround, false-confidence signal, validation failure, or excessive ceremony. Put any reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

## Phase Gate

- **All implemented scopes entered through an inspectable gate:** [ ] Yes [ ] No
- **Focused and proportionate broader checks pass:** [ ] Yes [ ] No
- **Tests were not weakened to accommodate implementation:** [ ] Yes [ ] No
- **New behavior or contract discoveries were regated:** [ ] Yes [ ] No [ ] None discovered
- **Pattern claims, when present, were validated:** [ ] Yes [ ] No [ ] Not applicable
- **Final clarity and diff inspection completed while applicable TDD tests were green or approved reduced checks passed:** [ ] Yes [ ] No
- **Remaining risks and validation gaps are explicit:** [ ] Yes [ ] No
- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD
