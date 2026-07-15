# Architecture Template

Use this template to record the smallest coherent architecture that satisfies approved requirements and can be planned, validated, operated, and evolved safely.

**Project Name:** [Project name]
**Date:** [Date]
**Architecture Lead:** [Lead]
**Operating Mode:** [New design / Evolution or migration / Decision support]

## How to Use This Template

For a focused decision, the minimum useful artifact is context and drivers, the decision and viable options, consequences, validation and revisit trigger, and a Planning handoff. Boundaries, contracts, critical flows, capacity, security, operations, and migration become required only when the decision affects them. Delete conditional modules that cannot affect the choice.

When the local `software-engineering` skill is available, System Design leads cross-component architecture. Loom owns this artifact and its owner gate. An approved design is not authorization to implement it.

## Scope and Inputs

### Requirements Inputs

- **MVP scope and non-goals:**
- **Requirement and acceptance IDs:**
- **Ranked quality-attribute IDs:**
- **Compatibility promises:**
- **Critical assumptions, unknowns, and risks:**
- **Open technical decisions:**

### Architecture Scope

- **Desired outcome:**
- **Current system or workflow:**
- **Proposed change:**
- **Actors, owners, systems, and data affected:**
- **Explicit non-goals:**
- **Delivery horizon, team, platform, and cost bounds:**

### Evidence and Uncertainty

| Statement / Input | Type | Source / Derivation | Confidence | What It Could Change | Validation or Decision Point |
|-------------------|------|---------------------|------------|----------------------|------------------------------|
| | Measured / Sourced / Derived / Inferred / Assumed / Unknown / Conflict | | High / Medium / Low | | |

### Driver Trace

| Driver ID | Requirement / Quality / Constraint / Risk | Rank | Architecture Treatment | Validation Method |
|-----------|-------------------------------------------|------|------------------------|-------------------|
| | | | | |

## Decision Summary

### Selected Architecture

[State the decision and why it best fits the ranked drivers.]

- **Decision ID(s):** DEC-001

```text
[Small diagram only when boundaries, flows, or states are clearer visually. Label current/proposed state, actors, direction, protocols, trust boundaries, and failure domains as applicable.]
```

### Consequential Options

Do not manufacture alternatives for trivial or mandated choices. Include current, simpler, managed, or no-change options when genuinely viable.

| Decision ID / Area | Driver IDs | Option | Correctness / Risk | Complexity / Operability | Migration / Cost / Lock-In | Evidence For or Against | Reversible? / Revisit Trigger |
|--------------------|------------|--------|--------------------|--------------------------|----------------------------|-------------------------|--------------------------------|
| | | | | | | | |

## Boundaries, Ownership, and Data

### Components and Responsibilities

Each boundary should have a present reason: independent responsibility, ownership, contract, scaling, release, isolation, data, or failure behavior.

| Component / Boundary | Responsibility | Operational Owner | Owned Data / Source of Truth | Dependencies | Trust / Failure Domain | Why Separate Now |
|----------------------|----------------|-------------------|------------------------------|--------------|------------------------|------------------|
| | | | | | | |

### Dependency and Boundary Rules

- [Rule, direction, and rationale]
- [What a component must not do]

### Data and State

| Data / State | Owner / Source of Truth | Identity / Invariant | Derived or Ephemeral? | Retention / Deletion / Residency | Consistency / Transaction Boundary | Migration / Compatibility |
|--------------|-------------------------|----------------------|-----------------------|----------------------------------|------------------------------------|---------------------------|
| | | | | | | |

### Provisional Source and Test Mapping

*Optional. Stop at independently owned or contract-bearing boundaries. Private classes, helpers, and exact test placement may remain `TBD`.*

| Stable Scope | Loom Progress Path | Likely Source Area | Stable Test Boundary | Confidence / Notes |
|--------------|--------------------|--------------------|----------------------|--------------------|
| | `docs/loom/system/.../PROGRESS.md` or Parent row | `src/...` or TBD | `tests/...` or TBD | |

## Critical Contracts

Capture only semantics that callers, consumers, operators, other components, or persisted data depend on. Phase 5 will turn approved clauses into executable contracts and tests.

| Contract ID | Boundary / Owner | Schema / Protocol / Version | Inputs / Outputs / Effects | Invariants / Errors | Auth / Limits | Consistency / Ordering / Delivery | Idempotency / Retry / Timeout / Backpressure | Compatibility |
|-------------|------------------|-----------------------------|----------------------------|---------------------|---------------|-----------------------------------|------------------------------------------------|---------------|
| | | | | | | | | |

### User and Operator Surfaces

| Surface | Actor | Purpose | Privilege / Trust Boundary | Success, Partial, and Failure Visibility |
|---------|-------|---------|----------------------------|------------------------------------------|
| CLI / UI / API / Worker / Event / Export | | | | |

## Critical Flows and Failure Behavior

### Primary Flows

| Flow | Driver / Contract IDs | Steps and Data Direction | State or Transaction Boundary | User / Operator Outcome |
|------|-----------------------|--------------------------|-------------------------------|-------------------------|
| | | | | |

### Scenario Challenge

Include only credible scenarios. Distributed systems may need duplicate, reorder, delay, replay, clock, partition, or concurrency cases; a local pure function does not.

| Flow / Scenario | Expected Observable or Degraded Behavior | Timeout / Retry / Backpressure Owner | Recovery / Reconciliation | Signal | Validation Method |
|-----------------|------------------------------------------|--------------------------------------|---------------------------|--------|-------------------|
| Normal success | | | | | |
| Boundary / invalid input | | | | | |
| Overload / quota / contention | | | | | |
| Dependency failure / partial completion | | | | | |
| Duplicate / reorder / concurrent update | | | | | |
| Recovery / replay / restore | | | | | |
| Plausible abuse / trust-boundary violation | | | | | |

## Material Capacity and Performance

*Conditional. Estimate only inputs that can change a decision. Keep units visible and use ranges for uncertain values.*

| Driver | Average | Peak / Burst | Growth / Retention | Source / Confidence | Sensitivity / Decision Effect |
|--------|---------|--------------|--------------------|---------------------|-------------------------------|
| Request, event, job, concurrency, payload, state, fan-out, skew, or quota | | | | | |

- **First likely bottleneck:**
- **Safety headroom:**
- **Saturation signal and safe action:**
- **Performance acceptance IDs:**

## Security, Privacy, and Operations

*Conditional. Address obligations and credible threats, not a generic checklist.*

### Security and Privacy

- **Trust and tenant boundaries:**
- **Authentication and authorization:**
- **Secrets, keys, and encryption:**
- **Sensitive-data minimization, retention, deletion, and audit:**
- **Threat or misuse paths and controls:**
- **Qualified review still required:**

### Operability

- **Deployment / run owner:**
- **Configuration and feature control:**
- **User-visible service or local verification indicators:**
- **Logs, metrics, traces, audit events, dashboards, or runbooks:**
- **Quotas, cost controls, and scaling triggers:**
- **Rollback and support expectations:**

## Evolution and Migration

*Required for stateful, externally visible, or incompatible change; delete for a simple compatible greenfield design.*

| Increment | Independently Useful Outcome | Compatibility / Mixed-Version Rule | Data Movement / Backfill | Verification / Reconciliation | Progression Threshold | Abort / Reversal Threshold | Owner |
|-----------|------------------------------|------------------------------------|--------------------------|-------------------------------|-----------------------|----------------------------|-------|
| | | | | | | | |

- **Cutover:**
- **Rollback and recovery:**
- **Backup or restore validation:**
- **Temporary bridge or duplicated-state retirement:**
- **Old-path cleanup trigger:**

## Risk and Validation

### Risk Register

| ID | Risk / Assumption | Driver IDs | Evidence or Basis | Impact | Validation / Mitigation | Owner | Acceptance, Reversal, or Decision Point |
|----|-------------------|------------|-------------------|--------|-------------------------|-------|-----------------------------------------|
| ARCH-RISK-001 | | | | | | | |

### Architecture Validation Plan

Treat the design as a hypothesis. Use the cheapest credible evidence for the riskiest uncertainty.

| Driver / Risk / Decision | Validation Method | Acceptance Criteria | Evidence / Result | Owner | Required Before |
|--------------------------|-------------------|---------------------|-------------------|-------|-----------------|
| | Review / Prototype / Benchmark / Load / Contract / Fault / Migration / Restore / Security | | | | Planning / Contracts / Implementation / Release |

### Consistency Check

- [ ] Driver trace, decisions, boundaries, contracts, diagrams, flows, estimates, and migration steps agree.
- [ ] Material estimates show units, sources, ranges, and sensitivity.
- [ ] Critical assumptions have evidence or an owned validation step.
- [ ] Remaining unverified claims are explicit.

## Planning Inputs

- **Stable components or boundaries:**
- **Responsibilities and owners:**
- **First validating vertical slice:**
- **Likely workstreams:**
- **Real dependency and sequencing constraints:**
- **Safe parallel work:**
- **Schemas and contract IDs for Phase 5:**
- **Migration, verification, rollback, or cleanup work:**
- **Highest-risk validations to run early:**
- **Decisions Planning must not reopen without new evidence:**
- **Private implementation deliberately left open:**

## Progress Inputs

Create child ledgers only for independently owned or independently evidenced scopes. Keep smaller units in a parent row.

| Scope | Parent | Driver IDs | Progress Doc or Parent Row | Source / Test Evidence | Owner | Notes |
|-------|--------|------------|----------------------------|------------------------|-------|-------|
| | | | | Known / TBD | | |

## Decision and Change Log

| Date | Decision ID / Change | Driver IDs | Choice | Rationale / Evidence | Owner | Revisit Trigger | Downstream Artifacts to Refresh |
|------|----------------------|------------|--------|----------------------|-------|-----------------|---------------------------------|
| | DEC-001 | | | | | | |

## Open Decisions

| Question | Driver IDs | Options | Tradeoffs | Recommendation | Decision Owner | Decide By / Trigger |
|----------|------------|---------|-----------|----------------|----------------|---------------------|
| | | | | | | |

## Next-Phase Handoff

Preparing this handoff does not close the phase gate or authorize implementation.

- **Decision and driver trace:**
- **Boundaries, ownership, and data:**
- **Critical contracts and flows:**
- **Risks and validation:**
- **Migration or rollback obligations:**
- **Planning inputs and non-goals:**

## Loom Process Feedback

*Optional. Record only a phase-local observation. Put any evidence-backed reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

## Phase Gate

- **Framing gate:** [ ] Passed [ ] Not passed [ ] Not applicable
- **Evidence gate:** [ ] Passed [ ] Not passed
- **Alternatives gate:** [ ] Passed [ ] Not passed [ ] Not applicable
- **Contract gate:** [ ] Passed [ ] Not passed
- **Risk gate:** [ ] Passed [ ] Not passed
- **Migration gate:** [ ] Passed [ ] Not passed [ ] Not applicable
- **Authority gate:** [ ] Design approval remains distinct from implementation authorization
- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns and unverified claims:** TBD

Owner approval authorizes the next Loom phase, not implementation or external state changes.
