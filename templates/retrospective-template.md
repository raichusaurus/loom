# Review & Retrospective Template

Use this template to evaluate delivered outcomes and engineering evidence, route findings to the phase that owns them, and shape the next Loom cycle. Review is read-only unless fixes are separately authorized.

**Project Name:** [Project name]
**Date:** [Date]
**Review Lead:** [Lead]

## Outcome Trace

| Driver / Acceptance ID | Intended Outcome or Bound | Actual Evidence / Result | Met? | Evidence Type | Notes / Owning Follow-Up Phase |
|------------------------|---------------------------|--------------------------|------|---------------|--------------------------------|
| | | | Yes / No / Partial / Deferred | Measured / Observed / Derived / Assumed / Unknown | |

### Deferred and Unverified Work

| Item | Deliberately Deferred or Evidence Missing? | Impact / Risk | Owner | Decision Point / Next Cycle |
|------|-------------------------------------------|---------------|-------|-----------------------------|
| | | | | |

## Integrated Engineering Review

### Schema, Contract, Tests, and Implementation

- [ ] Applicable schemas, constraints, and compatibility rules agree with delivered behavior.
- [ ] Observable contracts, tests, implementation, and user/operator outcomes agree.
- [ ] For every scope claimed as TDD, the declared scope, applicable schema, observable contract, and all currently known executable tests existed before any behavior-bearing implementation.
- [ ] New or changed behavior has inspectable pre-implementation meaningful-red evidence, or is honestly labeled non-TDD.
- [ ] Every non-TDD label traces to an explicit owner-approved exception recorded before implementation; missing authorization is a finding.
- [ ] Behavior-preserving refactors have a pre-refactor green characterization baseline.
- [ ] Gate resets exist for newly discovered behavior, edge cases, schema changes, or contract changes.
- [ ] Tests were not weakened, over-mocked, or coupled unnecessarily to private structure.
- **Evidence and gaps:**

### Architecture and Operations

- [ ] Boundaries, ownership, data sources of truth, dependency direction, and critical contracts held up.
- [ ] Representative success, overload, dependency-failure, degraded, recovery, and abuse behavior was validated where applicable.
- [ ] Compatibility, migration, cutover, rollback, recovery, and cleanup evidence is adequate where applicable.
- [ ] Security, privacy, operability, observability, capacity, and cost assumptions were validated in proportion to risk.
- **Evidence and gaps:**

### Pattern or Abstraction Claims

*Delete when no named pattern or material new abstraction was introduced.*

| Decision | Documented Pressure / Change Scenario | Did Change Localize as Claimed? | Lifecycle / Failure / Economics Evidence | Keep, Simplify, or Remove | Revisit Trigger |
|----------|----------------------------------------|---------------------------------|------------------------------------------|---------------------------|-----------------|
| | | | | | |

### Code Clarity

- [ ] Names, cohesion, abstraction levels, state ownership, effects, and failure behavior are understandable.
- [ ] No speculative indirection, obsolete path, debug residue, stale comment, accidental contract drift, or unrelated churn remains.
- [ ] Exact focused and broader validation commands still pass.
- **Evidence and gaps:**

### Release or Local Workflow Validation

Choose the applicable path; do not force production ceremony on a local MVP.

| Path | Applicable? | Validation Performed | Result | Remaining Risk |
|------|-------------|----------------------|--------|----------------|
| Local run / inspection workflow | Yes / No | | | |
| Deployment / release smoke test | Yes / No | | | |
| Monitoring / alert review | Yes / No | | | |
| Rollback / recovery confirmation | Yes / No | | | |

## Prioritized Findings

Order findings by correctness and safety; lifecycle, concurrency, recovery, compatibility, and capacity; boundary or pattern failure; missing evidence and maintainability; then polish.

| Priority / Severity | Artifact / Evidence | Triggering Scenario | Observable Impact | Fact or Inference | Smallest Correction or Validation | Owning Phase |
|---------------------|---------------------|---------------------|-------------------|-------------------|-----------------------------------|--------------|
| | | | | | | Requirements / Architecture / Planning / Contracts & Tests / Implementation |

No material findings: [ ] Yes. If yes, list what was not reviewed or could not be validated.

## Process Retrospective

### Practices to Keep or Expand

| Practice | Evidence / Outcome | Where to Reuse |
|----------|--------------------|----------------|
| | | |

### Friction and Rework

| Friction | Trigger / Evidence | Impact | One-Off or Recurrent | Candidate Next Experiment |
|----------|--------------------|--------|----------------------|---------------------------|
| | | | | |

### Ownership and Routing Review

- Did workstream ownership and context packets prevent overlap?
- Did selected engineering routes match the decisions actually made?
- Did a route trigger too often, too little, or in the wrong order?
- Did integration checkpoints catch drift early?
- Which ceremony did not earn its cost?

## Actions and Next Cycles

| Action / Outcome | Starting Phase | Owner | Evidence Needed | Decision Point / Due Date |
|------------------|----------------|-------|-----------------|---------------------------|
| | | | | |

Material fixes are not authorized by this review alone. Any behavior-affecting correction, including an unchanged-contract defect, returns to Contracts & Tests for regression evidence and meaningful red. A behavior-preserving refactor returns there for a declared refactor scope and green characterization baseline. A cross-boundary change returns to Architecture; only strictly non-behavioral or mechanical work may return directly to Implementation.

## Process Improvement Candidates

Ordinary project authority does not authorize shared Loom, router, or specialist protocol edits. Put reusable candidates in `docs/loom/pilot-feedback.md`; delete this section for a clean run.

| Candidate | Raw Evidence | Severity / Occurrences | Likely Authoritative Source | Expected Observable Behavior | Maintenance Authority Needed? |
|-----------|--------------|------------------------|-----------------------------|------------------------------|-------------------------------|
| | | | Loom / Router / Specialist / Skill metadata / Repository / Tool or environment | | Yes |

## Open Follow-Up Decisions

| Question | Options | Tradeoffs | Recommendation | Decision Owner | Decision Point | Owning Phase |
|----------|---------|-----------|----------------|----------------|----------------|--------------|
| | | | | | | |

## Final Gate

- **Outcome and engineering evidence reviewed:** [ ] Yes [ ] No
- **TDD provenance described honestly:** [ ] Yes [ ] No [ ] Not applicable
- **Findings are prioritized and routed to owning phases:** [ ] Yes [ ] No
- **Remaining risk and unverified areas are explicit:** [ ] Yes [ ] No
- **Next cycles and owners are identified where needed:** [ ] Yes [ ] No [ ] None needed
- **Agent recommendation:** [ ] Ready to close [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD
