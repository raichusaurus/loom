# Phase 5: Contracts & Tests

## Purpose

Contracts & Tests answers: **What must be true before behavior-bearing implementation is allowed to begin?**

For each coherent change scope, this phase establishes the applicable schema and observable contract. Under Loom's default test-first policy, it also establishes all currently known executable tests and inspectable pre-implementation evidence; an explicit owner-approved non-TDD exception records any missing test or pre-state evidence instead. The local `software-engineering` router selects TDD as the sequencing lead for standard behavior work.

Loom owns the phase artifact, readiness recommendation, owner gate, and handoff. TDD owns the schema → contract → all-known-tests → pre-state sequence. Test tooling, layout, automation, and quality standards support that gate; a test plan or coverage target cannot substitute for it.

## Scope-Level Gate

Declare the full currently known scope before opening the gate. Independently owned workstreams may gate separately only when each scope is coherent and cannot silently settle a known deferred behavior.

For every standard TDD scope:

1. **Scope:** State the observable outcome, mode (`new behavior`, `changed behavior`, or `behavior-preserving refactor`), and explicit non-goals.
2. **Schema:** Create or identify the authoritative data shapes, states, constraints, identities, and compatibility rules. If no schema changes, name the existing schema and record that it remains stable.
3. **Contract:** Define inputs, outputs, effects, invariants, failures, absence or partial results, and relevant ordering, idempotency, timeout, cancellation, security, performance, or compatibility bounds.
4. **All known tests:** Write the complete currently known executable test set for the agreed scope. Known boundary and failure cases may not trail a happy-path implementation.
5. **Pre-implementation evidence:** Run the narrowest focused command and record the result.

An explicit owner-approved non-TDD exception does not waive the coherent scope, applicable schema, or observable contract. It may waive all-known-test timing or the meaningful pre-state only when the missing evidence, reduced checks, owner, and follow-up are recorded before implementation.

For standard TDD new or changed behavior, the relevant test must fail because the behavior is absent or incorrect. An import, collection, compilation, dependency, or environment failure is not a meaningful red signal. If a new test passes immediately, determine whether the behavior already exists or the test cannot detect its absence.

For a standard TDD behavior-preserving refactor, characterization tests must pass before restructuring. Record the green baseline and do not manufacture a failure.

```text
New or changed behavior:
Scope → Schema → Contract → All known tests → Meaningful red → Implementation slices

Behavior-preserving refactor:
Scope → Schema → Contract → Characterization tests → Green baseline → Refactor
```

Within work claimed as TDD, only test files, fixtures, declarative schemas or interfaces, test configuration, generated declarations, and the smallest behavior-free scaffold needed to load tests may precede the meaningful red. Defaults, validation policy, transformations, branching, persistence decisions, network decisions, UI behavior, and behavior-bearing wiring must wait.

## Key Questions

### Scope and Traceability

- Which Planning scope, requirement IDs, acceptance IDs, architecture contracts, and risks does this gate cover?
- What known behavior and consequential failure cases belong inside it?
- What is explicitly deferred, and can implementation avoid deciding it?
- Which producers, consumers, operators, or users observe the contract?

### Schema

- What fields, types, units, requiredness, defaults, allowed values, identities, relationships, and state transitions apply?
- Which API, persistence, event, configuration, or serialization shapes are authoritative?
- What versioning, migration, backward-compatibility, or runtime validation rules apply?
- Can the schema be validated or generated through the repository's established mechanism?

### Contract

- What are the accepted inputs, preconditions, outputs, postconditions, state changes, and external effects?
- What errors, absence, partial results, retries, timeouts, cancellation, ordering, idempotency, concurrency, or security behavior can callers observe?
- Which clauses are locked, approval-gated, or still flexible?
- Is any material owner decision still open that implementation would necessarily settle?

### Executable Evidence

- Does each contract clause trace to an executable test or an explicit non-executable validation method?
- Do tests assert stable observable behavior rather than private call sequences or planned pattern participants?
- Are expected results independent of production helpers that could repeat the same mistake?
- Which realistic fixtures, counterexamples, properties, compatibility cases, migration cases, or integration boundaries are needed?
- What exact command proves meaningful red or a characterization baseline, and what did it show?

### Harness and Automation

- Can the focused tests load and reach an assertion today?
- What smallest behavior-free scaffold or development dependency is needed if not?
- Which local commands, schema checks, contract tests, type checks, formatters, linters, builds, or migration checks should Implementation automate?
- Which unstable or external checks remain opt-in?

## Outputs

- **Change-scope register:** Mode, outcome, explicit non-goals, owner, requirement and architecture references.
- **Schema inventory:** Authoritative artifacts, constraints, compatibility, producers, consumers, and validation result.
- **Observable contract register:** Clause IDs covering behavior, invariants, failures, and consequential boundary semantics.
- **Contract-to-test trace:** Every known contract clause mapped to executable evidence or an explicit validation method.
- **Executable tests and fixtures:** Located at the highest stable boundary that proves behavior, with narrower tests only where useful.
- **Pre-implementation evidence:** For standard TDD scopes, exact command, expected signal, observed assertion-level red or characterization-green baseline, and baseline-failure distinction; for exception scopes, the approved bypass and reduced checks.
- **Test harness and automation handoff:** Reproducible commands, allowed scaffold, external dependency policy, and deferred automation.
- **Progress update:** Direct evidence state for each gated scope; invocation of a skill alone earns no progress.
- **Implementation handoff:** Locked scope, schema, contract, tests or recorded gaps, pre-state or exception evidence, and remaining risks.

## Blocked and Exceptional Cases

- If the harness cannot reach behavioral evidence, repair it or mark the TDD gate blocked. Do not continue behavior-bearing implementation silently.
- If the existing suite is red, isolate and record baseline failures, then prove the new test adds the expected distinct signal.
- If the owner explicitly authorizes a test-first bypass, record the reason and reduced evidence. The resulting work is not TDD.
- If implementation later exposes a wrong or incomplete schema or contract, stop. Return here and revise schema → contract; then either update all currently known executable tests and observe the required new pre-state, or obtain a new explicit non-TDD exception for the changed scope. Only then resume.
- Never weaken, delete, over-mock, or rewrite a test merely to accommodate implementation.

## Contracts & Tests Template

Use [contracts-tests-template.md](../templates/contracts-tests-template.md). Its artifact order mirrors the gate and keeps tooling subordinate to behavioral evidence.

## When Contracts & Tests Is Ready for Owner Review

- Every independently gated scope has a coherent outcome, mode, explicit non-goals, and traceable drivers.
- The applicable schema exists, validates, and states compatibility; unchanged schemas are explicitly identified.
- The observable contract is complete enough that implementation will not decide an open behavior silently.
- Every standard TDD scope has all currently known executable tests before behavior-bearing implementation and traces each contract clause to executable evidence or an explicit validation method.
- Every approved non-TDD scope identifies the missing tests or trace evidence and the reduced validation that will be used instead.
- Every standard TDD scope has a focused meaningful red for new or changed behavior, or a green characterization baseline for a refactor.
- Test collection, import, dependency, compilation, or environment failures are not being counted as behavioral evidence.
- Scaffold exceptions are behavior-free and narrowly documented.
- Local commands and relevant automation/bootstrap work are reproducible or explicitly owned for Implementation.
- Any owner-approved non-TDD exception records its reason, reduced evidence, scope, follow-up, and missing normal gate signal without being mislabeled.
- The agent recommendation remains separate from owner approval and implementation authorization.

## Loom Process Feedback

Capture only a phase-local observation about material routing friction, a missing gate, repeated workaround, false evidence claim, validation failure, or ceremony whose cost exceeds its risk. Put any reusable evidence-backed candidate in `docs/loom/pilot-feedback.md`. A clean phase needs no feedback note.

---

Move to [Implementation](./06-implementation.md) only after the owner approves this gate and the handoff contains inspectable pre-implementation evidence.
