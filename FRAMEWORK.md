# Loom Framework Philosophy

## Core Principles

### 1. Sequential Foundation, Iterative Practice
New projects usually move through phases in order. Each phase builds on the previous one and enables the next. This initial pass is intentionally waterfall-style: create shared context, reduce ambiguity, and give agents a stable foundation before parallelizing heavily.

After the first implementation, Loom becomes more agile and recursive. Teams can run smaller Loom cycles for individual services, features, subprojects, or milestones while preserving the same quality gates.

### 2. Clear Separation of Concerns
Each phase has distinct responsibilities:
- **Discovery** answers "What problem are we solving?"
- **Requirements** answers "What needs to be built?"
- **Architecture** answers "How will we build it?"
- **Planning & Decomposition** answers "How will we divide and coordinate the work?"
- **Contracts & Tests** answers "How do we verify it works?"
- **Implementation** answers "Let's build it"
- **Review & Retrospective** answers "Did we succeed? What did we learn?"

### 3. Documentation-Driven Development
Decisions are documented as they're made. This becomes:
- A reference for the team
- A decision log for retrospectives
- Guidance for future projects
- Justification for technical choices

### 4. Test-First Thinking
Tests and contracts are defined before implementation. This ensures:
- Clear success criteria before coding
- Reduced rework and debugging
- Easier code review
- Better confidence in changes

### 5. Agent Specialization
Each phase has a dedicated agent that:
- Understands the phase deeply
- Asks the right questions
- Identifies missing pieces
- Ensures quality before moving forward
- Maintains consistency with Loom principles

### 6. Explicit Agent Coordination
Agentic workflows need clear work boundaries. Planning & Decomposition defines ownership, context packets, dependencies, parallel work, handoff expectations, and integration checkpoints before implementation begins.

### 7. Continuous Feedback
The Orchestrator maintains context and asks clarifying questions. This creates a conversation, not a checklist.

## When to Deviate

The framework is flexible. Reasonable deviations:
- **Existing projects**: Jump to the phase you need help with
- **Tight deadlines**: Accelerate through phases but maintain documentation
- **Small features**: You may compress multiple phases into one session
- **Experimentation**: Discovery and architecture might be tighter loops
- **Later iterations**: Run agile mini-cycles for scoped services, features, or subprojects

Avoid deviating from:
- **Skipping phases** - This creates technical debt
- **Skipping decomposition on multi-agent work** - This creates ownership confusion
- **Implementing without contracts** - Tests should exist before code
- **Skipping retrospectives** - Learning is how we improve

## Recursive Scope

Loom applies at multiple levels:

- **Project-level Loom**: Overall product or system
- **Service-level Loom**: API service, worker, frontend app, data pipeline, or integration
- **Feature-level Loom**: A bounded feature inside an existing system
- **Task-level mini-Loom**: A compressed cycle for small changes

Use the full framework when the work is new, risky, or cross-functional. Use a smaller loop when the scope is bounded and the surrounding context is already understood.

## Optional Release / Operations Cycle

Release, deployment, scheduling, monitoring, runbooks, incident response, and production CI/CD are not required for every Loom project. Local-first MVPs, prototypes, and internal tools may only need local checks and documented follow-up.

When a project needs operational readiness, run a focused Loom mini-cycle after Implementation and before or alongside Review & Retrospective. Start from the phase that fits the gap:

- **Requirements** for release goals, uptime, access, compliance, or support expectations
- **Architecture** for deployment topology, secrets, environments, observability, and rollback design
- **Planning & Decomposition** for release workstreams, ownership, sequencing, and runbooks
- **Contracts & Tests** for smoke tests, deployment checks, monitoring signals, and release gates
- **Implementation** for CI/CD workflows, deployment automation, dashboards, alerts, and operational docs

## Success Metrics

A successful Loom project achieves:

✅ **Clear Requirements** - Everyone understands what's being built
✅ **Sound Architecture** - Technical design is documented and reviewed
✅ **Clear Work Ownership** - Workstreams, dependencies, and handoffs are explicit
✅ **High Test Coverage** - Contracts and tests exist before implementation
✅ **Quality Code** - Implementation follows defined contracts
✅ **Documented Learning** - Retrospective captures successes and failures
✅ **Reusability** - Framework and templates improve over time

## The Orchestrator's Role

The Orchestrator:
- Guides you through phases
- Asks clarifying questions
- Identifies blockers
- Maintains project context
- Coordinates with phase-specific agents
- Ensures quality gates are met
- Facilitates phase transitions

The Orchestrator is your partner, not a tool. Think of it as a project manager + senior engineer + mentor all in one.

---

See individual phase documentation for specific details on each stage.
