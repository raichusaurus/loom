# Loom

Loom is a seven-phase workflow for turning a project idea or scoped software change into traceable decisions, executable evidence, verified implementation, and reusable learning.

The first pass establishes a stable foundation before heavy parallelism. Later passes can be smaller, faster Loom cycles around a feature, service, migration, or task while preserving the gates that still apply.

## The Seven Phases

1. **[Discovery](./phases/01-discovery.md)** — Understand the problem, users, current state, constraints, assumptions, and evidence needed to proceed.
2. **[Requirements](./phases/02-requirements.md)** — Define scoped observable outcomes, ranked quality attributes, acceptance criteria, and non-goals.
3. **[Architecture](./phases/03-architecture.md)** — Establish system boundaries, ownership, critical contracts, tradeoffs, failure behavior, and evolution decisions.
4. **[Planning & Decomposition](./phases/04-planning-decomposition.md)** — Create owned vertical slices, dependencies, context packets, and integration checkpoints.
5. **[Contracts & Tests](./phases/05-contracts-tests.md)** — Establish each change scope's schema, observable contract, all currently known executable tests, and meaningful pre-implementation evidence.
6. **[Implementation](./phases/06-implementation.md)** — Make the smallest contract-backed changes, prove green, and improve clarity without crossing active gates.
7. **[Review & Retrospective](./phases/07-review-retrospective.md)** — Evaluate outcomes and engineering evidence, prioritize findings, and shape the next cycle.

Agents may draft artifacts, run authorized checks, prepare handoffs, update evidence-based progress, and recommend readiness. The project owner approves, revises, or defers each phase gate.

## Engineering Skills Inside Loom

Loom owns the project lifecycle. When the local `software-engineering` skill is available, it routes technical decisions inside the active phase:

- **System Design** leads cross-component boundaries, data ownership, external contracts, quality attributes, failure behavior, operations, and migration.
- **TDD** controls schema-first, contract-first, test-first implementation sequencing. Loom activates this route by default for behavior-bearing software work.
- **Design Patterns** addresses demonstrated source-level collaboration pressure after stable boundaries and contracts are known.
- **Clean Code** is the baseline for authorized code changes and the final clarity pass.

The router selects one lead and only necessary overlays. It is not an additional Loom phase, does not broaden authorization, and does not approve gates. See [FRAMEWORK.md](./FRAMEWORK.md) for the composition and reopening rules.

## Repository Structure

This repository contains reusable framework guidance and templates:

```text
loom/
├── README.md
├── FRAMEWORK.md
├── ORCHESTRATOR.md
├── PROGRESS.md
├── phases/
│   ├── 01-discovery.md
│   ├── 02-requirements.md
│   ├── 03-architecture.md
│   ├── 04-planning-decomposition.md
│   ├── 05-contracts-tests.md
│   ├── 06-implementation.md
│   └── 07-review-retrospective.md
└── templates/
    ├── discovery-template.md
    ├── requirements-template.md
    ├── architecture-template.md
    ├── planning-template.md
    ├── contracts-tests-template.md
    ├── implementation-template.md
    ├── progress-ledger-template.md
    ├── pilot-feedback-template.md
    └── retrospective-template.md
```

Phase-specific agents are roles coordinated by the Orchestrator; this repository does not currently ship separate `agents/` definitions.

## Project Artifact Layout

Projects using Loom should keep their project-specific artifacts under `docs/loom/`:

```text
docs/loom/
├── README.md
├── PROGRESS.md
├── pilot-feedback.md                 # optional; only for material Loom feedback
├── phases/
│   ├── 01-discovery/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   ├── 02-requirements/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   ├── 03-architecture/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   ├── 04-planning/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   ├── 05-contracts-tests/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   ├── 06-implementation/
│   │   ├── README.md
│   │   └── PROGRESS.md
│   └── 07-review/
│       ├── README.md
│       └── PROGRESS.md
└── system/
    └── [independently-tracked-component]/
        └── PROGRESS.md
```

The `system/` tree follows stable architecture or delivery scopes, not every private class or test helper. A child ledger earns its file when it has independent ownership, contracts, blockers, scoring evidence, or a review path. Keep smaller units as evidence rows in the nearest parent.

Source paths, test paths, and Loom scopes must be traceable, but they do not need identical hierarchies. Tests should live at the highest stable boundary that proves the behavior, with narrower tests added when they improve design or diagnosis.

## How to Use Loom

### New Project

1. Tell the [Orchestrator](./ORCHESTRATOR.md) the desired outcome and known constraints.
2. Work through the first applicable phase and fill only the template sections that improve the decision.
3. At each transition, verify the phase artifact, applicable engineering evidence, remaining risks, and owner decision separately.
4. If later evidence changes a requirement, boundary, schema, or contract, reopen the phase that owns it and refresh dependent handoffs.
5. Finish with Review & Retrospective, even when the next result is another scoped Loom cycle.

### Existing Project or Small Change

Enter at the phase that owns the current uncertainty. Inspect inherited requirements, architecture, contracts, tests, and implementation evidence first. Several phase responsibilities may share one artifact or session, but applicable hard gates still hold.

### Progress

Use [PROGRESS.md](./PROGRESS.md) for scoring and recursive traceability. The root ledger is the project cockpit. Add phase and child ledgers in proportion to independent ownership and evidence; use `Unknown` or `TBD` rather than inventing implementation structure early.

### Process Feedback

Record feedback only when Loom creates material clarity or friction worth preserving. Keep a phase-local observation near the affected artifact. Put a reusable, evidence-backed candidate in `docs/loom/pilot-feedback.md` using [templates/pilot-feedback-template.md](./templates/pilot-feedback-template.md). A clean phase needs no feedback entry.

## Core Invariants

- Consequential decisions trace to requirements, constraints, evidence, or risk.
- By default, behavior-bearing implementation follows scope → schema → contract → all currently known executable tests → meaningful red → green → refactor; an owner-approved non-TDD exception must name its reduced evidence and may not claim that provenance.
- Behavior-preserving refactors establish a green characterization baseline instead of an artificial red state.
- A pattern or abstraction must solve demonstrated present pressure and remove more reasoning cost than it adds.
- Code changes preserve observable contracts unless a contract change is explicitly approved and regated.
- Agent recommendations, artifact readiness, engineering evidence readiness, and owner approval remain distinct.
- Artifacts and progress structure stay proportionate to the decisions and coordination they support.

## Collaborative Git Workflow

Loom projects use Git as the shared collaboration and audit surface. Each phase has a project-scoped shared branch, contributors work through short-lived branches or worktrees, and meaningful changes are committed and pushed for team visibility. Consequential changes move through review; approved phase gates are preserved in Git history, and the next phase branches from the approved predecessor state.

See [FRAMEWORK.md](./FRAMEWORK.md#7-git-native-collaboration) for the full collaboration model and its distinction between Git review and owner approval.

---

Start by telling the Orchestrator what you want to build or change and what evidence already exists.
