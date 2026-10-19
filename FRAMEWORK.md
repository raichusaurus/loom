# Loom Framework Philosophy

## Core Principles

### 1. Sequential Foundation, Iterative Practice

New projects usually move through phases in order. Each phase builds on the previous one and enables the next. This initial pass is intentionally waterfall-style: create shared context, reduce ambiguity, and give agents a stable foundation before parallelizing heavily.

After the first implementation, Loom becomes more agile and recursive. Teams can run smaller Loom cycles for individual services, features, subprojects, or milestones while preserving the same quality gates.

### 2. Clear Separation of Concerns

Each phase owns a distinct lifecycle question:

- **Discovery** — What problem are we solving, for whom, and what evidence supports proceeding?
- **Requirements** — What observable outcomes, scope, and quality bounds must the solution satisfy?
- **Architecture** — What system boundaries, ownership, contracts, and tradeoffs should implementation preserve?
- **Planning & Decomposition** — How will we divide, sequence, coordinate, and integrate the work?
- **Contracts & Tests** — What schemas, observable contracts, and executable evidence must exist before behavior-bearing implementation?
- **Implementation** — What is the smallest verified code change that satisfies those contracts?
- **Review & Retrospective** — Did the result and engineering approach hold up, and what should change next?

The phases own lifecycle readiness and artifacts. They do not replace the specialist engineering protocols used inside a phase.

### 3. Decision- and Evidence-Driven Documentation

Document decisions, contracts, and evidence as they are established. Each artifact should help the next decision or protect a meaningful promise; it should not exist merely because a template has a section.

Prefer one authoritative home for each fact. Link to schemas, contracts, tests, decisions, and validation output instead of copying the same rule into several documents that can drift.

### 4. Contract- and Test-First Delivery

For an agreed behavior change, define the coherent scope, applicable schema, observable contract, and all currently known executable tests before changing behavior-bearing implementation. Then prove the pre-implementation state:

- New or changed behavior requires a focused test that fails for the expected behavioral reason.
- A behavior-preserving refactor requires characterization tests with a green baseline; do not manufacture a failure.

Implementation proceeds in small red-green-refactor slices after that scope-level gate passes. If a new edge case, contract clause, or schema change enters scope, return to Contracts & Tests and reopen the gate before implementing it.

Behavior-free scaffolding may exist only to make schemas or tests load and run. If the owner explicitly accepts a test-first exception, record the reduced evidence and do not describe the work as TDD.

### 5. Layered Engineering Specialization

When the local `software-engineering` skill is available, use it to select the minimum relevant specialist route for the technical decision at hand. Loom owns project lifecycle, phase gates, progress, and handoffs; the router owns discipline selection and ordering; each selected specialist protocol owns its technical behavior.

Do not summon every specialist for every task. Route by the present decision, preserve the user's requested mode and authority boundary, and keep recommendations read-only unless implementation is authorized.

### 6. Explicit Agent Coordination

Agentic workflows need clear work boundaries. Planning & Decomposition defines ownership, bounded context packets, dependencies, parallel work, handoff expectations, and integration checkpoints before implementation begins.

Each technical workstream should name its observable outcome, stable contracts, non-goals, selected engineering route, and evidence required before it can change production behavior.

### 7. Git-Native Collaboration

Loom projects are collaborative Git workspaces. The repository is the canonical shared surface for phase artifacts, decisions, progress, evidence, and handoffs. Contributors may work locally on their own machines, but meaningful changes should be committed and pushed so the current state remains visible to the team.

Each project phase has a shared phase branch, created from the approved state of the preceding phase. Use a consistent project-scoped naming scheme such as:

```text
loom/[project]/discovery
loom/[project]/requirements
loom/[project]/architecture
loom/[project]/planning
loom/[project]/contracts-tests
loom/[project]/implementation
loom/[project]/review
```

The phase branch is the shared workspace for the active phase. Individual contributors use short-lived branches or worktrees for distinct changes and merge them into the phase branch through review when the change is consequential. Low-risk working notes may be pushed directly when the project agrees that review is unnecessary, but this should not obscure decisions, contract changes, gate changes, or other material evidence.

When a phase gate is approved, preserve that state in Git history—normally through a reviewed pull request or equivalent merge—and create the next phase branch from the approved commit. Do not maintain permanently diverging phase branches that cannot be traced to an approved predecessor. If later evidence changes a requirement, boundary, schema, contract, or plan, reopen the owning phase and record the reason in both the artifact and the relevant Git history.

Git provides collaboration and auditability; it does not replace Loom's authority model. A pushed branch or merged pull request shows that work was shared or reviewed, not that an owner approved a phase gate. Owner decisions remain explicit in the Loom artifact or linked project record.

### Open Questions Become Tickets

When work within a phase exposes an unresolved question whose answer could affect scope, requirements, architecture, contracts, quality bounds, sequencing, implementation, or approval, record it as a ticket before making an assumption. The ticket is the shared coordination unit for human input; it should not live only in an agent transcript, local notes, or an unpushed branch.

Each open-question ticket should include:

- the phase and project scope
- the specific question and why it matters
- the evidence or decision that exposed it
- the options or constraints currently known
- the recommended decision, if one is useful
- the human owner or decision-maker
- the phase branch and relevant artifact or commit
- the downstream work blocked or at risk
- the status, decision, date, and resolving commit or pull request

Agents may identify, draft, classify, and route these tickets. They may resolve a question only when the answer is already established by an authoritative project decision or the owner has explicitly delegated that decision. Otherwise, the phase remains pending or records the ticket as a visible dependency; agents must not silently choose an assumption to make the work appear unblocked.

Tickets should be linked from the phase artifact and referenced in commits or pull requests that depend on them. When a ticket is resolved, update the authoritative phase artifact, close or transition the ticket, and record whether the decision reopens an earlier phase or resets a downstream contract or implementation gate.

### 8. Guided Decisions and High-Signal Feedback

The Orchestrator maintains context and packages material open questions for decision. Each decision packet should include a short summary, plausible options, tradeoffs, a recommendation, and the trigger that would change it. Do not manufacture options for a trivial or already constrained choice.

Capture Loom process feedback when work exposes material friction: an ambiguous gate, repeated workaround, missing guardrail, validation failure, or ceremony whose cost exceeds its risk. Keep phase-local observations in the phase artifact and reusable framework lessons in `docs/loom/pilot-feedback.md`. A clean phase needs no feedback entry or `N/A` ceremony.

### 9. Explicit Gate Authority

Agents can draft artifacts, score artifact readiness, identify risks, prepare handoffs, and recommend whether a phase is ready. They cannot approve a gate on the owner's behalf.

Every phase should separate:

- **Agent recommendation:** Ready or not ready.
- **Owner decision:** Approved, needs revision, or deferred.
- **Artifact readiness:** How complete and internally coherent the phase artifact is.
- **Engineering evidence readiness:** Whether applicable specialist evidence exists and has been inspected.
- **Gate status:** Whether the owner has closed the phase gate.
- **Next-phase handoff:** Context prepared for the next phase, not permission to start it.

A prior approval does not freeze a decision that new evidence invalidates. Reopen the phase that owns the changed requirement, boundary, schema, or contract, record the reason, and refresh dependent handoffs.

### 10. Proportionate Progress Visibility

Progress should be visible at every useful zoom level without turning the progress tree into a second source tree. Track project and phase status, then add child ledgers where a service, component, workstream, or unit has independent ownership, contracts, blockers, scoring evidence, or a review path.

Inventory smaller discovered scopes in their nearest parent. Create a child document only when it improves navigation or coordination. Tests should map to stable behavior or boundaries; they do not need to mirror private classes and functions one-for-one.

## Engineering Discipline Routing

Use the `software-engineering` router at the point of a technical decision, not once as a project-wide label.

| Loom phase | Typical lead or overlay | Loom handoff responsibility |
| --- | --- | --- |
| Discovery | Loom discovery; System Design only when an early cross-system constraint materially changes viability | Evidence, assumptions, constraints, and unknowns |
| Requirements | Loom requirements; System Design for measurable quality attributes and externally visible constraints | Ranked outcomes, non-goals, acceptance criteria, and decision drivers |
| Architecture | System Design leads; Design Patterns only for a demonstrated source-level collaboration already in scope | Boundaries, ownership, critical contracts, options, risks, and validation or migration plan |
| Planning & Decomposition | Route each workstream by its present engineering pressure | Bounded change scopes, ownership, dependencies, selected route, and gate evidence required |
| Contracts & Tests | TDD governs behavior-bearing work under Loom's test-first policy | Schema, contract, all currently known executable tests, and meaningful red or green-baseline evidence |
| Implementation | TDD controls sequencing; Clean Code is the code-quality baseline; Design Patterns addresses demonstrated variation; System Design re-enters for cross-boundary changes | Minimal green slices, gate resets, design-pressure decisions, integrated validation, and deviations |
| Review & Retrospective | Select the specialist that matches the artifact or outcome being reviewed | Requirement and contract traceability, prioritized findings, remaining risk, and high-signal process evidence |

For work spanning disciplines, establish the necessary system boundary and observable contract first, satisfy any active TDD gate, apply a source-level pattern only when concrete pressure justifies it, and finish code changes with a clarity pass while tests are green. Run one integrated validation and handoff rather than duplicating evidence for each discipline.

## When to Compress or Reopen Phases

Loom phases are responsibilities, not mandatory meeting counts. Reasonable adaptations include:

- **Existing projects:** Enter at the phase that owns the current uncertainty, after inspecting inherited evidence.
- **Small features:** Compress several phase responsibilities into one artifact or session while preserving applicable gates.
- **Tight deadlines:** Reduce artifact depth, not contract, safety, or authority evidence.
- **Experiments:** Keep spikes disposable and label them non-TDD; restart from schemas, contracts, and tests before retaining production behavior.
- **Later iterations:** Run scoped mini-cycles for services, features, migrations, or subprojects.

Avoid unrecorded gaps: behavior without a contract, implementation without required pre-state evidence, multi-agent work without ownership, architecture changes without compatibility analysis, or lessons that recur without an owner and validation plan.

## Recursive Scope

Loom can operate at project, service, feature, migration, or task scope. Use the full framework when work is new, risky, cross-functional, or hard to reverse. Use a smaller loop when the surrounding contracts and architecture are already understood.

Use [PROGRESS.md](./PROGRESS.md) as the shared ledger. The root can link to phase and architecture-component ledgers; smaller units can remain rows in a parent until independent ownership or evidence makes a child file worthwhile. `Unknown` and `TBD` are honest states—do not predesign private implementation merely to fill a path.

## Optional Release / Operations Cycle

Release, deployment, scheduling, monitoring, runbooks, incident response, and production CI/CD are not required for every Loom project. Local-first MVPs, prototypes, and internal tools may only need local checks and documented follow-up.

When a project needs operational readiness, run a focused Loom mini-cycle after Implementation and before or alongside Review & Retrospective. Start from the phase that owns the gap:

- **Requirements** for release goals, availability, access, compliance, or support expectations
- **Architecture** for deployment topology, secrets, environments, observability, compatibility, and rollback design
- **Planning & Decomposition** for release workstreams, ownership, sequencing, and runbooks
- **Contracts & Tests** for smoke tests, deployment checks, monitoring signals, migration verification, and release gates
- **Implementation** for CI/CD workflows, deployment automation, dashboards, alerts, and operational documentation

## Success Signals

A successful Loom cycle leaves:

- **Clear outcomes and scope** — Users, requirements, non-goals, and measurable decision drivers are understood.
- **Coherent architecture** — Boundaries, ownership, contracts, tradeoffs, failure behavior, and evolution paths are explicit in proportion to risk.
- **Clear work ownership** — Workstreams, dependencies, context packets, and handoffs are unambiguous.
- **Behavioral evidence** — Schemas, contracts, and risk-based tests preceded behavior-bearing implementation, with inspectable pre-state and green evidence.
- **Maintainable code** — The implementation is direct, cohesive, idiomatic, and free of speculative indirection.
- **Traceable decisions** — Requirements, design choices, tests, validation, and approved deviations agree.
- **Clear gate authority** — Agent recommendations and owner decisions remain distinct.
- **Actionable learning** — Material lessons have evidence, an owner, and a validation or revisit plan.

## The Orchestrator's Role

The Orchestrator guides the lifecycle, maintains context, selects or coordinates the appropriate specialists, protects phase and authority gates, keeps evidence traceable, and helps reopen the right decision when implementation reveals new facts.

The Orchestrator is a project manager, senior engineering guide, and decision facilitator—not a substitute for the owner or for specialist technical protocols.

---

See the individual phase documents for phase-specific artifacts and readiness criteria.
