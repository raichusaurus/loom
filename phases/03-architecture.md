# Phase 3: Architecture

## Purpose

Architecture answers: **What system boundaries, ownership, contracts, and quality tradeoffs should implementation preserve?**

It translates Requirements into the smallest coherent technical design that Planning & Decomposition can turn into owned, verifiable work. It should make consequential decisions explicit without predesigning private classes, file trees, or pattern participants.

When a decision crosses components, data stores, externally visible contracts, migration, deployment, or operational boundaries, route it through the local `software-engineering` skill with System Design as the lead. Loom continues to own the artifact, phase gate, and handoff. Use Design Patterns here only when a concrete source-level collaboration is already in scope; do not design from a pattern catalog.

## Architecture Decision Gates

Before presenting a design as settled, pass the applicable gates:

- **Framing:** Ranked requirements, quality attributes, constraints, non-goals, and material unknowns are known or bounded by labeled assumptions.
- **Evidence:** Facts, measurements, estimates, inferences, assumptions, and unknowns are distinguished. Quantify only drivers that can change a decision.
- **Alternatives:** Consequential or hard-to-reverse choices compare viable options, including current, simpler, or no-change approaches when credible.
- **Contracts:** Critical ownership, interface, data, consistency, ordering, delivery, error, compatibility, limit, and security semantics are explicit where relevant.
- **Risk:** Each critical assumption or unresolved risk has evidence or a validation method, owner, and decision point.
- **Migration:** Stateful, externally visible, or incompatible change includes compatibility, verification, cutover, rollback, recovery, and retirement decisions.
- **Authority:** An approved architecture authorizes Planning, not implementation or production changes.

Apply these gates proportionally. A small local feature may need a focused decision record; a cross-system migration may need the full treatment.

## Key Questions

### Inputs and Drivers

- Which requirement, acceptance, quality-attribute, constraint, assumption, or risk IDs drive this design?
- What current system or workflow exists, and what outcome must change?
- What is explicitly outside this architecture scope?
- Which quality attributes conflict, and which ranks higher?
- Which unknowns would materially change a public contract, safety posture, irreversible choice, or order-of-magnitude cost?

### Boundaries, Ownership, and Data

- What are the smallest components or services that earn independent responsibility, ownership, scaling, release, isolation, or failure boundaries?
- Who operates each boundary, and what data or state does it own?
- What is the source of truth, what is derived or ephemeral, and what lifecycle, retention, deletion, residency, or migration rules apply?
- What dependency direction prevents circular or ambiguous ownership?
- Which trust and failure domains matter?
- What should remain deliberately direct or colocated for now?

### Critical Contracts and Flows

- What do users, operators, jobs, and external systems observe on success, delay, partial success, and failure?
- Which APIs, commands, queries, events, schemas, files, or control surfaces form stable boundaries?
- What inputs, outputs, effects, invariants, errors, authentication, authorization, versioning, limits, and compatibility rules apply?
- Where do consistency, ordering, transaction boundaries, idempotency, retries, timeouts, cancellation, backpressure, deduplication, or replay affect correctness?
- How do primary read, write, control, and background flows behave under normal load, overload, dependency failure, duplicate or reordered work, recovery, and plausible abuse?

### Options and Material Scale

- What is the simplest viable design?
- What alternatives solve the same present problem, and what correctness, complexity, operability, migration, cost, lock-in, or team-fit tradeoffs do they create?
- Which decisions are reversible, and what trigger would justify revisiting them?
- If scale changes the choice, what average, peak, burst, growth, payload, fan-out, retention, skew, quota, and headroom ranges matter?
- What is the first likely bottleneck, and does the recommendation change across plausible input ranges?

### Evolution, Operations, and Validation

- What smallest vertical slice can validate the riskiest architecture assumption?
- How will mixed versions, data movement, backfill, reconciliation, cutover, abort, rollback, recovery, and temporary-path retirement work when relevant?
- What deployment, configuration, feature control, observability, support, and recovery responsibilities are proportionate to this scope?
- Which user-visible outcomes become service indicators or local verification signals?
- What is the cheapest credible validation method for each critical risk: review, prototype, benchmark, contract test, fault injection, migration rehearsal, restore test, or security analysis?

## Outputs

By the end of Architecture, produce the proportionate subset of:

- **Driver trace:** Material requirement and quality IDs mapped to design treatment and validation.
- **Architecture decision:** Stable decision IDs, selected design, rationale, alternatives, tradeoffs, and revisit triggers.
- **Boundaries and ownership:** Components, responsibilities, operators, dependencies, trust or failure domains, and owned data.
- **Critical flows:** End-to-end success, degraded, failure, and recovery behavior.
- **Stable contracts:** Interfaces, schemas, invariants, compatibility, consistency, error, security, and delivery semantics needed by Contracts & Tests.
- **Data design:** Sources of truth, identity, lifecycle, retention, deletion, derived state, and migration expectations.
- **Risk and validation plan:** Evidence, assumptions, owners, methods, thresholds, and decision points.
- **Evolution plan:** Compatible increments, verification, cutover, rollback, recovery, and cleanup where relevant.
- **Planning inputs:** Owned work boundaries, first validating slice, dependencies, integration points, and decisions Planning must not reopen without new evidence.
- **Progress mapping:** Stable independently tracked scopes and provisional source/test evidence paths where known; private implementation remains `TBD`.

Use a diagram only when it makes several boundaries, flows, or state transitions materially clearer. Label current versus proposed state, actors, direction, protocols, trust boundaries, and failure domains as applicable.

## Architecture Template

Use [architecture-template.md](../templates/architecture-template.md). Keep its core drivers, decisions, boundaries, critical flows, risks, validation, and handoff; delete conditional modules that do not affect the design.

## When Architecture Is Ready for Owner Review

- The scope, non-goals, current state, ranked drivers, and material unknowns are explicit.
- Consequential decisions trace to requirements, constraints, evidence, or risk.
- Viable alternatives were compared for costly, irreversible, or operationally significant choices.
- Components earn their boundaries and have clear responsibilities, ownership, dependencies, and state.
- Critical interface and data semantics are explicit enough for Contracts & Tests.
- Representative success, overload, dependency-failure, degraded, recovery, and abuse scenarios were considered where credible.
- Critical assumptions and risks have evidence or a validation owner, method, threshold, and decision point.
- Stateful, external, or incompatible changes include a credible migration and rollback path.
- Planning receives owned vertical-slice inputs, not speculative private implementation structure.
- Open owner decisions use summaries, options, tradeoffs, recommendations, and revisit triggers.
- The agent recommendation remains separate from owner approval and does not authorize implementation.

## Common Architecture Mistakes

- **Architecture theater:** Adding queues, services, caches, or multi-region topology without a present driver and explicit semantics.
- **Boxes without contracts:** Naming components without ownership, data, interfaces, failure behavior, or a reason for the boundary.
- **Premature source design:** Freezing classes, patterns, or mirrored test directories before implementation pressure exists.
- **Decorative capacity math:** Producing unsupported point estimates that cannot change the decision.
- **One-way migrations:** Assuming perfect cutover or rollback without mixed-version and data-recovery behavior.
- **Design as authorization:** Starting implementation because a diagram was approved.

## Loom Process Feedback

Capture only a material phase-local observation here. Put any reusable evidence-backed candidate in `docs/loom/pilot-feedback.md`. A clean Architecture phase needs no feedback note.

---

Move to [Planning & Decomposition](./04-planning-decomposition.md) after the owner approves the Architecture gate.
