# Requirements Template

Use this template to define a bounded, traceable outcome for Architecture. Keep only sections that clarify scope, observable behavior, decision-driving quality attributes, validation, or compatibility.

**Project Name:** [Project name]
**Date:** [Date]
**Requirements Lead:** [Lead]

## Discovery Inputs

- **Core problem:**
- **Primary user or operator:**
- **Current state:**
- **Working shape:**
- **First useful version:**
- **Explicitly out of scope:**
- **Success and validation signals:**
- **Material evidence, assumptions, conflicts, and unknowns:**
- **Open questions carried forward:**

## Scope

### Outcome

[Describe the user, operator, or business outcome without selecting the architecture.]

### In Scope

- [Outcome or capability]

### Out of Scope

- [Explicit non-goal]

### Optional or Deferred

| Item | Status | Why Not Now | Revisit Trigger |
|------|--------|-------------|-----------------|
| | Optional / Deferred / Unnecessary | | |

### Current-State Compatibility

*Use for evolution, rewrite, migration, or replacement work. Delete for a truly greenfield scope.*

| ID | Current Contract, Data, or Behavior | Observed Pain / Constraint | Preservation Decision | Affected Owner / Consumer | Target Outcome |
|----|-------------------------------------|----------------------------|-----------------------|---------------------------|----------------|
| COMP-001 | | | Yes / No (owner-approved) / Unknown—owner decision required | | |

Architecture decides how to satisfy an approved compatibility promise; it does not decide whether product-visible behavior or data may break.

## Requirements Catalog

Assign stable IDs to material MVP requirements so Architecture, contracts, tests, validation, and review can cite the same promise. A small change may need only a few rows.

| ID | Actor / Surface | Observable Requirement | Priority | Origin / Evidence | Acceptance IDs | Notes |
|----|-----------------|------------------------|----------|-------------------|----------------|-------|
| FR-001 | | | Must / Should / Could / Won't | Discovery / source / owner decision | AC-001 | |

### Data and Output Fidelity

*Delete when no meaningful data or output contract exists.*

| ID | Surface / Data | Required Fidelity or Provenance | Stable Identity / Unknown Handling | Consumer |
|----|----------------|---------------------------------|------------------------------------|----------|
| DF-001 | | | | |

## Ranked Quality Attributes and Constraints

Keep only attributes that can influence design, acceptance, safety, or cost. Use scenarios and defensible bounds rather than generic categories or unsupported precision.

| ID | Attribute / Constraint | Rank | Scenario or Load Condition | Target or Bound | Source / Confidence | Conflict or Acceptable Compromise | Validation Method |
|----|------------------------|------|----------------------------|-----------------|---------------------|-----------------------------------|-------------------|
| QA-001 | Performance / Reliability / Security / Privacy / Accessibility / Compatibility / Recovery / Operability / Cost | 1 | | | Measured / Sourced / Derived / Assumed / Unknown; High / Medium / Low | | |

Examples of material prompts, only when they affect this project:

- **Performance and scale:** Average, peak, burst, growth, latency percentile, throughput, concurrency, data volume, skew, or downstream quota.
- **Reliability and recovery:** Availability, durability, degraded behavior, RTO, RPO, reconciliation, or restore expectation.
- **Security and privacy:** Authentication, authorization, tenancy, data sensitivity, retention, deletion, audit, abuse, or compliance obligation.
- **Accessibility:** User-facing standard and consequential interaction requirements.
- **Compatibility:** API, event, persistence, configuration, client, or mixed-version promise.
- **Cost and operability:** Recurring bound, approval threshold, support model, deployment constraint, or observability need.

## Acceptance and Validation

### Acceptance Criteria

Each acceptance criterion references the requirement or quality ID it proves. Given/When/Then is useful when it makes the scenario clearer, not as mandatory ceremony.

| Acceptance ID | Driver IDs | Preconditions / Scenario | Action or Event | Observable Result | Consequential Boundary or Failure |
|---------------|------------|--------------------------|-----------------|-------------------|-----------------------------------|
| AC-001 | FR-001, QA-001 | | | | |

### Success Signals

| Signal | Target or Decision Bound | Measurement Method | Source / Baseline | Owner | Decision Point |
|--------|--------------------------|--------------------|-------------------|-------|----------------|
| | | | | | |

Implementation completion is defined later by approved contracts, tests, code-quality checks, and owner gates. Do not make Requirements prescribe private implementation tasks.

## Dependencies, Risks, and Assumptions

### External Dependencies

| Dependency | Promise / Constraint | Owner | Evidence | Decision or Availability Date | Risk |
|------------|----------------------|-------|----------|-------------------------------|------|
| | | | | | |

### Risks

| Risk ID | Driver IDs | Impact | Evidence / Assumption | Validation or Mitigation | Owner | Decision Point |
|---------|------------|--------|-----------------------|--------------------------|-------|----------------|
| RISK-001 | | | | | | |

### Assumptions and Unknowns

| ID | Assumption / Unknown | Type | Source / Confidence | What It Could Change | Validation Plan | Owner | Decision Point |
|----|----------------------|------|---------------------|----------------------|-----------------|-------|----------------|
| ASM-001 | | Assumption / Unknown / Conflict | | | | | |

## Architecture Inputs

Architecture should resolve only technical decisions that are material to the requirements or risks.

| Question | Driver IDs | Plausible Options | Main Tradeoffs | Recommendation | Owner / Status | Revisit Trigger |
|----------|------------|-------------------|----------------|----------------|----------------|-----------------|
| | | Include current / simpler / defer when credible | Correctness / risk / speed / cost / reversibility | | | |

### Driver Summary for Architecture

- **Highest-ranked quality attributes:**
- **Contracts or compatibility promises to preserve:**
- **Critical assumptions or unknowns:**
- **Safety, privacy, or compliance constraints:**
- **Consequential edge cases:**
- **Decisions Architecture must not infer silently:**

## Progress Inputs

Capture coarse independently meaningful scopes. Architecture will decide stable boundaries; private modules and paths may remain `TBD`.

| Scope | Type | Driver IDs | Why Track It | Path Notes |
|-------|------|------------|--------------|------------|
| | Workstream / Surface / Integration / Candidate Component | | | Known / TBD |

## Requirement Change Log

Later phases may propose a requirement change but may not silently rewrite the approved promise.

| Date | Affected IDs | Proposed Change | Reason / New Evidence | Downstream Impact | Proposer | Owner Decision | Supersedes |
|------|--------------|-----------------|-----------------------|-------------------|----------|----------------|------------|
| | | | | | | Approved / Needs revision / Deferred | |

## Open Decisions

| Question | Options | Tradeoffs | Recommendation | Decision Owner | Decide By / Trigger | Status |
|----------|---------|-----------|----------------|----------------|---------------------|--------|
| | | | | | | |

## Next-Phase Handoff

Preparing this handoff does not close the phase gate or authorize Architecture.

- **Approved scope and non-goals:**
- **Requirement and acceptance IDs:**
- **Ranked quality drivers:**
- **Compatibility promises:**
- **Evidence, assumptions, and unknowns:**
- **Architecture decisions required:**
- **Validation signals:**

## Loom Process Feedback

*Optional. Record only a phase-local observation. Put any evidence-backed reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

## Phase Gate

- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD

Before recommending readiness, confirm that material scope has stable IDs, acceptance evidence is traceable, quality attributes are ranked and bounded, assumptions are labeled, and Architecture will not have to invent a product decision.
