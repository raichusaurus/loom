# Phase 7: Review & Retrospective

## Purpose

Review & Retrospective answers: **Did the outcome, contracts, architecture, and engineering evidence hold up, and what should happen next?**

This phase evaluates the result against requirements and real validation, then captures material product, technical, and process learning. Review is read-only unless the owner separately authorizes fixes. Findings should return to the phase that owns the affected decision rather than being patched around in the retrospective.

Use the local `software-engineering` router to select the discipline that matches the artifact under review. System Design reviews cross-boundary outcomes and operational evidence; TDD audits contract alignment and development provenance; Design Patterns reviews a claimed source-level collaboration; Clean Code reviews touched-code clarity and maintainability.

## Review Priorities

Review findings in this order:

1. Incorrect behavior, security or privacy exposure, data loss, broken contracts, or unsafe migration.
2. Lifecycle, concurrency, resource, ordering, retry, recovery, compatibility, or unbounded capacity risk.
3. A boundary or pattern that fails to isolate the claimed responsibility or directs dependencies incorrectly.
4. Missing behavioral evidence, excessive coupling, hidden effects, speculative indirection, or poor changeability.
5. Naming, documentation, diagram, formatting, and low-risk polish.

For each material finding, cite precise evidence, describe a realistic triggering scenario and impact, distinguish fact from inference, and propose the smallest credible correction or validation step.

## Key Questions

### Outcome and Traceability

- Did each material requirement, acceptance criterion, quality attribute, and non-goal reach the intended outcome?
- What evidence is measured, observed, derived, assumed, unknown, or not applicable?
- Are requirement, architecture, schema, contract, test, implementation, and progress artifacts aligned?
- What was deliberately deferred, and did implementation accidentally encode it?

### Test-First Provenance

- For each scope claimed as TDD, did the declared full scope, applicable schema, observable contract, and all currently known executable tests exist before any behavior-bearing implementation?
- For new or changed behavior, is there inspectable meaningful-red evidence from before implementation?
- For behavior-preserving refactors, is there a green characterization baseline from before restructuring?
- For TDD scopes, were all currently known executable tests present before implementation, and were gate resets recorded when scope changed?
- If the full pre-implementation sequence is missing, was an explicit owner-approved non-TDD exception recorded before implementation? Otherwise record a finding rather than relabeling the work afterward.
- Were tests weakened, over-mocked, rewritten silently, or coupled to private implementation?
- Do not retroactively call the work TDD or invent an exception when the required pre-state evidence does not exist.

### Architecture and Design Claims

- Did boundaries, ownership, sources of truth, critical contracts, failure behavior, and compatibility hold in the delivered system?
- Did material scale, reliability, security, migration, operational, or cost assumptions hold where applicable?
- If a pattern or abstraction was introduced, did it solve the documented pressure, localize the representative change, and earn its full economics?
- Are lifecycle, error, concurrency, cleanup, and dependency direction clear?
- What evidence or trigger should cause a design decision to be revisited or removed?

### Code and Validation Quality

- Is the touched code cohesive, direct, idiomatic, and understandable at the right abstraction levels?
- Are effects, state ownership, failure behavior, and boundary validation visible?
- Do exact focused and broader validation commands still pass?
- What remains unverified because of environment, external systems, time, or missing evidence?

### Process and Next Cycle

- Did ownership, context packets, engineering routing, phase gates, and integration checkpoints reduce rework?
- Did any route trigger too often or not often enough, conflict with another instruction, or allow a false claim?
- Which follow-up belongs in Requirements, Architecture, Planning, Contracts & Tests, Implementation, or a release/operations mini-cycle?
- Which process observation is severe or recurrent enough to become an evidence-backed improvement candidate?

## Outputs

- **Outcome report:** Requirements and success measures compared with actual evidence.
- **Integrated engineering review:** Schema, contract, tests, implementation, architecture, and validation alignment.
- **Prioritized findings:** Scenario, impact, evidence, smallest correction, and owning phase.
- **Remaining risk register:** Unknowns, validation gaps, deferred work, owners, and decision points.
- **Maintenance and evolution plan:** Follow-up Loom scopes and entry phases.
- **Retrospective:** Specific practices to keep, change, test, or retire.
- **Process improvement candidates:** High-signal evidence only, separated from automatic framework edits.

## Reopening Work

- A changed user outcome or acceptance criterion returns to Requirements.
- A changed system boundary, quality tradeoff, compatibility rule, or migration plan returns to Architecture.
- A changed work owner or sequence returns to Planning.
- Any behavior-affecting correction, including a defect whose public contract remains unchanged, returns to Contracts & Tests for a regression test and meaningful red before the fix.
- A behavior-preserving refactor returns to Contracts & Tests for a declared refactor scope and green characterization baseline.
- Only strictly non-behavioral or mechanical work may return directly to Implementation under existing evidence and separate authorization.

Do not implement a review finding unless that fix is separately authorized.

## Process Improvement Authority

Capture a reusable improvement candidate in `docs/loom/pilot-feedback.md` rather than editing Loom or shared specialist protocols automatically. Ordinary project authority does not authorize shared framework or protocol maintenance.

Promote a candidate only when one high-severity failure or near miss justifies it, or when the same ordinary problem recurs across two or three tasks. Record the raw task and evidence, classify the likely authoritative source, define observable expected behavior and regression scenarios, and request explicit maintenance authority. Forward-test and canary any accepted revision before keeping it.

For a clean run, add no process-feedback ceremony.

## Review & Retrospective Template

Use [retrospective-template.md](../templates/retrospective-template.md) for outcome traceability, integrated technical review, prioritized findings, next-cycle decisions, and evidence-backed process candidates.

## When Review Is Ready for Owner Closure

- Material requirements, acceptance criteria, quality attributes, and deferred items have evidence-backed disposition.
- Schema, contract, tests, implementation, and architecture agree, or discrepancies are explicit findings.
- TDD provenance is described honestly, including missing evidence or approved exceptions.
- Pattern and architecture claims were reviewed against real change, failure, and operational evidence where applicable.
- Findings are prioritized by impact and routed to the phase that owns the correction.
- Remaining risks, unverified areas, maintenance, and next-cycle scopes have owners or decisions.
- Process improvements are candidates with evidence, not unauthorized framework mutations.
- The final agent recommendation remains separate from owner closure.

---

An approved Review gate closes this Loom cycle. Any accepted follow-up begins a new scoped cycle at the phase that owns its uncertainty.
