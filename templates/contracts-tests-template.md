# Contracts & Tests Template

Use this template to pass Loom's pre-implementation gate for each coherent change scope. The standard TDD artifact order is deliberate: scope → schema → observable contract → all currently known executable tests → meaningful red or characterization baseline. An explicit owner-approved non-TDD exception keeps scope, schema, and contract mandatory while recording missing test/pre-state evidence and reduced checks.

**Project Name:** [Project name]
**Date:** [Date]
**Contracts & Tests Lead:** [Lead]

## How to Use This Template

- Complete a separate gate row for each independently coherent scope.
- For standard TDD scopes, write all currently known executable tests before behavior-bearing implementation; known failure and boundary cases may not trail the happy path.
- Use the repository's canonical schema, contract, and test mechanisms.
- Permit only the smallest behavior-free scaffold needed to load schemas or reach a test assertion.
- If later evidence invalidates the contract, stop implementation and revise schema → contract; then either update all currently known executable tests and observe the required new pre-state, or obtain a new explicit non-TDD exception for the changed scope.
- Delete optional tooling and observability modules that do not affect this scope.

## Inputs

- **Requirements artifact and driver IDs:**
- **Architecture artifact, contract IDs, and compatibility decisions:**
- **Planning gate scopes and owners:**
- **Integration, migration, and risk-validation obligations:**
- **Repository schema and test conventions:**

## Change-Scope Register

| Scope ID | Mode | Observable Outcome | Driver / Acceptance IDs | Explicit Non-Goals | Owner | Independent Gate Rationale |
|----------|------|--------------------|-------------------------|--------------------|-------|----------------------------|
| SCOPE-001 | New behavior / Changed behavior / Behavior-preserving refactor | | | | | |

Do not split a scope if one part would silently decide a known deferred behavior. Do not combine unrelated work merely to create one large gate.

## 1. Schema Gate

### Schema Inventory

For logic with no new structured data, cite the existing input, output, or state schema and mark it unchanged. Do not invent a schema file for ceremony.

| Schema ID | Scope ID | Authoritative Artifact / Reference | Fields, Types, Units, Constraints, or States | Identity / Relationships | Compatibility / Migration | Producers / Consumers | Validation Command and Result |
|-----------|----------|------------------------------------|----------------------------------------------|--------------------------|---------------------------|-----------------------|-------------------------------|
| SCH-001 | SCOPE-001 | | | | | | |

### Schema Questions

- Requiredness, defaults, allowed values, and invalid states:
- Persistence, API, event, configuration, or serialization shape:
- Runtime validation at untrusted boundaries:
- Generated declarations and source-of-truth rule:
- Unchanged schema statement, if applicable:

## 2. Observable Contract Gate

Define behavior at a stable caller, consumer, user, or operator boundary. Do not expose planned pattern machinery unless it is genuinely part of the public semantic contract.

| Clause ID | Scope / Schema IDs | Boundary / Consumer | Inputs / Preconditions | Outputs / Postconditions | State / External Effects | Failures / Absence / Partial Result | Ordering / Idempotency / Retry / Timeout / Cancellation | Security / Performance / Compatibility Bound | Stability |
|-----------|--------------------|---------------------|------------------------|--------------------------|--------------------------|--------------------------------------|--------------------------------------------------------|----------------------------------------------|-----------|
| CON-001 | SCOPE-001, SCH-001 | | | | | | | | Locked / Approval-gated / Flexible |

### Open Contract Decisions

Implementation may not begin while an unresolved decision would necessarily be encoded by the code.

| Question | Affected Scope / Clause | Options | Tradeoffs | Recommendation | Decision Owner | Status / Decision Point |
|----------|-------------------------|---------|-----------|----------------|----------------|-------------------------|
| | | | | | | |

## 3. All-Known-Tests Gate

### Contract-to-Test Trace

Every known contract clause needs executable evidence or a named non-executable validation method. Start at the highest stable boundary that proves the behavior.

| Clause ID | Executable Test / Property | Test Path | Normal, Boundary, or Failure Case | Fixture / Independent Oracle | Expected Signal Before Implementation | Non-Executable Validation, if Any | Status |
|-----------|----------------------------|-----------|-----------------------------------|------------------------------|---------------------------------------|-----------------------------------|--------|
| CON-001 | | | | | | | Written / Validated |

### Acceptance and Integration Trace

| Driver / Acceptance ID | Scope / Clause IDs | Test or Validation | Owner | External or Mixed-Version Dependency |
|------------------------|--------------------|--------------------|-------|--------------------------------------|
| | | | | |

### Fixtures and Test Doubles

Use realistic fixtures derived from the schema. Fake unstable or expensive boundaries, not the behavior under test.

| Fixture / Double | Purpose | Source / Representativeness | Boundary Replaced | Failure Cases Included |
|------------------|---------|---------------------------|-------------------|------------------------|
| | | | | |

## 4. Pre-Implementation Evidence

### Baseline Suite

| Command | Result | Pre-Existing Failures / Notes | Evidence Link |
|---------|--------|-------------------------------|---------------|
| | | | |

### Gate Evidence by Scope

For standard TDD new or changed behavior, record an assertion-level failure caused by absent or incorrect behavior. Import, collection, compilation, dependency, or environment failures do not count. For a standard TDD refactor, record a green characterization baseline and never manufacture red. For an approved non-TDD scope, record the exception and reduced checks instead.

| Scope ID | Required Signal | Exact Focused Command | Expected Reason | Observed Result / Relevant Failure | Distinct From Baseline? | Evidence Link | Gate Status |
|----------|-----------------|-----------------------|-----------------|------------------------------------|-------------------------|---------------|-------------|
| SCOPE-001 | Meaningful red / Characterization green | | | | Yes / No | | Open / Passed / Blocked / Approved non-TDD exception |

### Signal Review

- **If the new test passed immediately:** [Behavior already exists / Test cannot detect absence / Investigating]
- **If the command failed before an assertion:** [Smallest behavior-free harness repair / Gate blocked]
- **If the existing suite is red:** [How the distinct new signal was isolated]
- **Behavior-free scaffold added:** [Files and why they contain no defaults, policy, transformations, or decisions]

## Test Harness and Strategy

### Primary Stack and Commands

| Tool / Command | Purpose | Local / CI | Current Result | Owner |
|----------------|---------|------------|----------------|-------|
| | Schema / Contract / Unit / Integration / E2E / Type / Format / Lint / Build / Migration | | | |

### Test Layout

Map tests to stable behaviors and boundaries. The test tree need not mirror private source classes or helpers.

```text
tests/
  [category-or-stable-boundary]/
    [behavior-or-scenario]
  fixtures/
    [representative-data]
```

### Risk-Based Evidence Plan

Coverage thresholds are repository constraints when mandated, not substitutes for contract evidence.

| Risk / Contract Area | Why It Matters | Evidence Type | Required Before Merge / Release | Owner |
|----------------------|----------------|---------------|---------------------------------|-------|
| | | Example / Property / Compatibility / Migration / Fault / Manual | | |

### External Dependency Policy

- **Default fake or fixture approach:**
- **Live or external tests:** [Opt-in command and environment]
- **Network, time, randomness, and concurrency controls:**
- **Secrets and sensitive test-data policy:**

## Check Automation Handoff

Full CI is not required before a runnable scaffold exists. The focused pre-state command is required for a passed TDD gate.

### Current Status

- **Runnable scaffold exists:** [ ] Yes [ ] No
- **Dependency lockfile exists:** [ ] Yes [ ] No [ ] Not applicable
- **Focused behavioral tests reach assertions:** [ ] Yes [ ] No
- **CI or check workflow exists:** [ ] Yes [ ] No

### Automation Plan

| Check | Exact Command | Add or Enable When | Blocking? | Owner |
|-------|---------------|--------------------|-----------|-------|
| Schema / generation | | | | |
| Contract / unit | | | | |
| Integration | | | | |
| Type / format / lint | | | | |
| Build / migration | | | | |
| Security | | | | |

## Observability and Operational Contracts

*Conditional. Include when a metric, log, trace, audit event, alert, reconciliation signal, or smoke test is part of observable correctness.*

| Signal / Check | Contract or Risk ID | Expected Behavior / Threshold | Test or Validation | Owner |
|----------------|---------------------|-------------------------------|--------------------|-------|
| | | | | |

## Progress Evidence

Invoking TDD or writing a plan earns no progress by itself. Link direct schema, contract, test, and pre-state evidence.

| Scope | Progress Doc or Parent Row | Schema | Contract | All Known Tests | Pre-State Evidence | Evidence Readiness |
|-------|----------------------------|--------|----------|-----------------|--------------------|--------------------|
| | | | | | | 0–100% |

## Decision and Exception Log

| Date | Scope | Decision / Exception | Reason and Reduced Evidence | Owner Approval | Follow-Up / Expiry |
|------|-------|----------------------|-----------------------------|----------------|--------------------|
| | | | | | |

An owner-approved bypass is reported as non-TDD. It does not become a reusable default.

## Implementation Handoff

Preparing this handoff does not close the phase gate or authorize work outside the approved scope.

- **Passed scope IDs and explicit non-goals:**
- **Schema artifacts and compatibility:**
- **Locked contract clauses:**
- **All-known-test trace:**
- **Exact meaningful-red or characterization-baseline evidence, or approved non-TDD exception:**
- **Allowed behavior-free scaffold:**
- **Baseline failures and approved exceptions:**
- **Focused and broader commands:**
- **Gate-reset triggers:**
- **Remaining risks and unverified evidence:**

## Loom Process Feedback

*Optional. Record only a phase-local routing miss, ambiguous gate, repeated workaround, false evidence claim, validation failure, or excessive ceremony. Put any reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

## Phase Gate

- **All gate scopes are declared with explicit non-goals:** [ ] Yes [ ] No
- **Applicable schemas exist and validate:** [ ] Yes [ ] No
- **Observable contracts are complete and traceable:** [ ] Yes [ ] No
- **Every standard TDD scope has all currently known executable tests before implementation; every non-TDD exception identifies missing tests and reduced validation:** [ ] Yes [ ] No
- **Every scope has meaningful red or a characterization baseline, or an explicit owner-approved non-TDD exception with reduced evidence:** [ ] Yes [ ] No
- **No unresolved decision would be settled silently by implementation:** [ ] Yes [ ] No
- **Exceptions and validation gaps are explicit:** [ ] Yes [ ] No
- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD
