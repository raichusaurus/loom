# Phase 4: Planning & Decomposition

## Purpose

Planning & Decomposition answers: **How will we divide, sequence, coordinate, validate, and integrate the work?**

It turns approved architecture into owned vertical slices for humans and agents. A good plan reduces context and coordination cost without reopening settled requirements or architecture, precommitting speculative abstractions, or authorizing implementation before the Contracts & Tests gate.

Use the local `software-engineering` router per workstream when a real technical decision is present. Record one lead and only necessary overlays; use `No engineering route` for coordination-only work. Planning itself does not ritualistically load every specialist.

## Key Questions

### Pull Forward the Architecture

- Which requirement and quality-driver IDs does this plan deliver?
- Which boundaries, contracts, ownership rules, risks, migration constraints, and non-goals must remain stable?
- Which architecture decisions may not be reopened without new evidence and owner review?
- What is the smallest vertical slice that validates the riskiest architecture claim or delivers an inspectable user outcome?

### Define Coherent Change Scopes

- What observable outcome and currently known behavior belongs to each scope?
- What is explicitly deferred or outside it?
- Which schema, contract, acceptance criteria, and validation evidence will Contracts & Tests need before behavior-bearing implementation?
- Can independent workstreams pass their own complete TDD gate without leaving known failure or boundary cases behind?
- Which scope is too coupled and must be split, or too fragmented and should remain together?

### Assign Ownership and Authority

- Who owns each outcome, decision, artifact, source area, test evidence, integration point, and progress scope?
- What actions and mutation paths are authorized, and what is prohibited?
- Which shared areas require coordination rather than overlapping ownership?
- What discovery should stop the work and return to Requirements, Architecture, or Contracts & Tests?

### Sequence Real Dependencies

- Which artifact, contract, owner decision, external dependency, or validation result blocks another slice?
- What merely feels convenient to sequence but can safely proceed in parallel?
- What unlock condition closes each dependency edge?
- Where do migration progression, reversal, recovery, or cleanup checkpoints belong?

### Plan Integration and Risk Retirement

- What evidence proves independently owned work integrates at stable boundaries?
- What checkpoints catch contract, data, compatibility, or architecture drift before a large merge?
- Which critical assumption can be tested cheaply before irreversible work?
- What threshold permits progression, requires reversal, or triggers an upstream decision?
- How will deviations be classified as planning-only, contract-changing, or architecture-changing?

## Outputs

- **Driver-to-work trace:** Every material requirement or quality driver has design treatment, owner, slice, and validation path.
- **Owned workstreams:** Clear outcome, scope, non-goals, authorized paths, shared areas, and escalation triggers.
- **Validation-oriented vertical slices:** Inspectable outcomes with prerequisites, contracts, risk to retire, required exit evidence, and reversal approach.
- **Dependency graph:** Real blocking edges, owners, unlock conditions, critical path, and safe parallel work.
- **Agent context packets:** Bounded briefs with relevant decisions, selected engineering route, authority, expected evidence, and handoff requirements.
- **Integration plan:** Checkpoints, stable-boundary tests or reviews, conflict handling, and cross-workstream ownership.
- **Contracts & Tests handoff:** Coherent change scopes, applicable schemas, observable contract candidates, all known behavior and failure cases, acceptance IDs, and harness needs.
- **Risk-validation plan:** Cheapest credible experiment, owner, acceptance or reversal threshold, and decision point.
- **Conditional migration plan:** Owned rollout, verification, abort, recovery, and cleanup work when Architecture requires it.
- **Proportionate progress map:** Child ledgers only for independently owned or independently evidenced scopes; smaller units stay rows in a parent.

## Context Packet Minimum

Each agent or contributor should receive:

- Goal and inspectable outcome
- Requirement and architecture references
- Coherent change scope and explicit non-goals
- Owned and prohibited mutation paths
- Stable schemas, contracts, and boundaries to preserve
- Selected engineering lead and overlays, with trigger and required evidence
- Dependencies, risks, assumptions, and integration checkpoint
- Stop and escalation triggers
- Expected patch, artifact, validation, and handoff

A context packet authorizes only the named work. Architecture or planning approval does not authorize bypassing Contracts & Tests or making unrelated external changes.

## Recursive Scope

A project may contain service-, feature-, migration-, or task-level Loom cycles. Create a nested cycle when a scope has enough independent uncertainty, ownership, contracts, or risk to benefit from its own gates. Do not create a mini-Loom or progress file for every class, helper, or task.

The first project pass may establish phases sequentially, but implementation should still be planned as small validation-oriented vertical slices rather than a batch waterfall. Later cycles reuse inherited evidence and reopen only the decisions they genuinely change.

## Planning Template

Use [planning-template.md](../templates/planning-template.md) to capture the workstream, vertical-slice, dependency, context-packet, integration, risk, and Contracts & Tests handoff.

## When Planning Is Ready for Owner Review

- Every material driver has an owner, architecture treatment, work slice, and validation path.
- Workstreams and coherent change scopes have explicit outcomes and non-goals.
- The first validating vertical slice and subsequent increment order are clear.
- Ownership, authorized paths, shared areas, and stop conditions are unambiguous.
- Real dependency edges, unlock conditions, critical path, and parallel work are understood.
- Context packets include the minimum technical and authority context.
- Contracts & Tests receives all currently known behaviors, failure cases, schemas, interfaces, and acceptance references for each scope.
- Integration, migration, and risk-validation checkpoints are owned and measurable where relevant.
- Progress scopes are proportionate; known work is traceable without speculative child documents.
- Material open questions use decision packets and do not leave implementation to decide them silently.
- The agent recommendation remains separate from owner approval and implementation authorization.

## Change Control

Planning may adjust task order, coordination mechanics, and ownership within its approved boundary. A changed product outcome returns to Requirements; a changed system boundary, compatibility rule, or migration design returns to Architecture; a changed schema, observable contract, or supported scenario returns to Contracts & Tests and resets its gate.

## Loom Process Feedback

Capture only a material phase-local observation here. Put any reusable evidence-backed candidate in `docs/loom/pilot-feedback.md`. A clean Planning phase needs no feedback note.

---

Move to [Contracts & Tests](./05-contracts-tests.md) after the owner approves the Planning gate.
