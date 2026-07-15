# Planning & Decomposition Template

Use this template to turn approved architecture into owned, validation-oriented vertical slices and a complete Contracts & Tests handoff.

**Project Name:** [Project name]
**Date:** [Date]
**Planning Lead:** [Lead]
**Loom Scope:** [Project / Service / Feature / Migration / Task]

## Inputs and Authority

- **Requirements artifact and approved IDs:**
- **Architecture artifact and decision IDs:**
- **Stable boundaries, contracts, and non-goals:**
- **Critical risks and validation obligations:**
- **Migration, rollback, or cleanup obligations:**
- **Owner-authorized planning scope:**

Planning may adjust coordination, ownership, and sequence within this scope. Product outcome changes return to Requirements; system boundary or compatibility changes return to Architecture; schema or observable behavior changes return to Contracts & Tests.

## Driver-to-Work Trace

Use inline references for a very small change; use this table when several drivers or workstreams need coordination.

| Driver ID | Architecture Treatment | Workstream / Slice | Owner | Validation Evidence | Status |
|-----------|------------------------|--------------------|-------|---------------------|--------|
| | | | | | |

## Workstreams

| Workstream | Inspectable Outcome | Driver IDs | Owner | Scope / Authorized Paths | Explicit Non-Goals / Prohibited Areas | Engineering Route / Trigger |
|------------|---------------------|------------|-------|--------------------------|--------------------------------------|-----------------------------|
| | | | | | | System Design / TDD / Design Patterns / Clean Code / No engineering route |

## Validation-Oriented Vertical Slices

Start with the smallest slice that validates a risky architecture claim or delivers an inspectable outcome. Do not use slices to postpone already known contract or failure cases.

| Slice | Inspectable Outcome | Driver IDs | Owner | Prerequisites / Stable Contracts | Explicit Deferred Decisions | Risk to Retire | Required Exit Evidence | Reversal / Recovery |
|-------|---------------------|------------|-------|----------------------------------|-----------------------------|----------------|------------------------|---------------------|
| | | | | | | | | |

### Increment Sequence

| Order | Slice | Can Start When | Why This Order | Parallel With |
|-------|-------|----------------|----------------|---------------|
| | | | | |

## Ownership and Traceability

### Ownership Map

Source and test paths must be traceable to stable scopes but do not need identical hierarchies. Exact private paths can remain `TBD`.

| Owner | Progress Scope | Docs / Decision Scope | Source Area | Stable Test Boundary | Responsibilities | Shared Areas / Coordination Rule |
|-------|----------------|-----------------------|-------------|----------------------|------------------|----------------------------------|
| | Child ledger or Parent row | | Known / TBD | Known / TBD | | |

### Progress Scope Decisions

Create a child ledger when a scope has independent ownership, contracts, blockers, scoring evidence, or a review path. Keep smaller units as rows in the nearest parent.

| Scope | Parent | Child Ledger? | Reason | Source / Test Evidence |
|-------|--------|---------------|--------|------------------------|
| | | Yes / Parent row | | Known / TBD |

## Dependencies and Critical Path

Distinguish a real blocker from convenient sequencing.

| Upstream Scope | Downstream Scope | Blocking Artifact / Decision / Dependency | Owner | Unlock Condition | Due or Decision Point | Critical? |
|----------------|------------------|-------------------------------------------|-------|------------------|-----------------------|-----------|
| | | | | | | Yes / No |

## Agent Context Packets

### Context Packet: [Workstream]

- **Owner / agent:**
- **Planned future work mode:** [Design / Tests only / Implement / Refactor / Review]
- **Currently authorized actions:** [Planning artifacts only / Schema-contract-tests only / Other explicit authority]
- **Implementation activation condition:** [Named Phase 5 scope passes its gate and the owner approves implementation]
- **Goal and inspectable outcome:**
- **Driver and acceptance IDs:**
- **Architecture decisions and boundaries:**
- **Coherent change scope:**
- **Explicit non-goals and prohibited paths:**
- **Owned progress, source, and test areas:**
- **Schemas, contracts, and compatibility to preserve:**
- **Engineering lead and overlays:**
- **Route trigger and required evidence:**
- **Dependencies and integration checkpoint:**
- **Risks, assumptions, and validation threshold:**
- **Stop and escalate when:** [Requirement / boundary / schema / contract / security / irreversible-change discovery]
- **Expected output and exact validation:**
- **Required handoff:**

Duplicate only for independently owned workstreams.

## Contracts & Tests Handoff

Each row declares a coherent gate scope. Include all currently known behavior and consequential failure cases; do not send only the happy path.

| Gate Scope | Mode | Driver / Acceptance IDs | Observable Outcome | Applicable Schema / Compatibility | Known Contract Clauses and Failures | Explicit Non-Goals | Owner | Harness Need |
|------------|------|-------------------------|--------------------|-----------------------------------|-------------------------------------|--------------------|-------|--------------|
| | New / Changed / Refactor | | | | | | | |

### Integration Evidence Candidates

| Boundary / Workflow | Driver or Contract IDs | Scenario | Expected Observable Evidence | Owner |
|---------------------|------------------------|----------|------------------------------|-------|
| | | | | |

## Integration Plan

| Checkpoint | Participating Scopes | Purpose | Required Evidence | Owner | Stop / Escalation Trigger |
|------------|----------------------|---------|-------------------|-------|---------------------------|
| | | | | | |

### Conflict and Deviation Handling

- **Overlapping edits:**
- **Planning-only sequence or ownership deviation:**
- **Requirement-changing discovery:** Return to Requirements.
- **Boundary, compatibility, or migration discovery:** Return to Architecture.
- **Schema, contract, or supported-scenario discovery:** Return to Contracts & Tests and reset its gate.

## Risk Validation

Run the cheapest credible validation before an irreversible or expensive commitment.

| Risk / Assumption | Driver IDs | Validation Method | Owner | Acceptance / Progression Threshold | Reversal / Escalation Threshold | Decision Point |
|-------------------|------------|-------------------|-------|------------------------------------|---------------------------------|----------------|
| | | | | | | |

## Migration and Rollout Work

*Conditional. Pull from Architecture; delete when not applicable.*

| Increment | Owner | Compatibility / Mixed-Version Work | Verification / Reconciliation | Progression Threshold | Abort / Recovery | Temporary-Path Cleanup |
|-----------|-------|------------------------------------|-------------------------------|-----------------------|------------------|------------------------|
| | | | | | | |

## Milestones

| Milestone | Inspectable Outcome | Slices | Driver IDs | Exit Evidence | Owner |
|-----------|---------------------|--------|------------|---------------|-------|
| | | | | | |

## Decision and Change Log

| Date | Decision / Change | Source Driver or Evidence | Choice | Owner | Affected Artifacts | Upstream Approval Needed? |
|------|-------------------|---------------------------|--------|-------|--------------------|---------------------------|
| | | | | | | |

## Open Decisions

Only material blockers should halt work.

| Question | Options | Tradeoffs | Recommendation | Decision Owner | Decide By / Trigger | Blocks |
|----------|---------|-----------|----------------|----------------|---------------------|--------|
| | | | | | | |

## Next-Phase Handoff

Preparing this handoff does not close the phase gate or authorize behavior-bearing implementation.

- **Approved change scopes and non-goals:**
- **Driver and acceptance trace:**
- **Owners and context packets:**
- **Dependency and integration checkpoints:**
- **Schema, contract, behavior, and failure candidates:**
- **Risk-validation and migration obligations:**
- **Open decisions that Phase 5 must not infer:**

## Loom Process Feedback

*Optional. Record only a phase-local observation. Put any evidence-backed reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

## Phase Gate

- **Every material driver has treatment, owner, slice, and validation:** [ ] Yes [ ] No
- **Each gate scope has known behavior, failures, schema, and non-goals:** [ ] Yes [ ] No
- **Ownership, authority, dependencies, and integration are actionable:** [ ] Yes [ ] No
- **Conditional migration and risk validation are owned:** [ ] Yes [ ] No [ ] Not applicable
- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD

Owner approval authorizes Contracts & Tests, not behavior-bearing implementation.
