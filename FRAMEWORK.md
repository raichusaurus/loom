# Loom Framework Philosophy

## Core Principles

### 1. Sequential Progression
Projects move through phases in order. Each phase builds on the previous one and enables the next. Skipping phases creates technical debt and misalignment.

### 2. Clear Separation of Concerns
Each phase has distinct responsibilities:
- **Discovery** answers "What problem are we solving?"
- **Requirements** answers "What needs to be built?"
- **Architecture** answers "How will we build it?"
- **Contracts & Tests / CI/CD** answers "How do we verify it works?"
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

### 6. Continuous Feedback
The Orchestrator maintains context and asks clarifying questions. This creates a conversation, not a checklist.

## When to Deviate

The framework is flexible. Reasonable deviations:
- **Existing projects**: Jump to the phase you need help with
- **Tight deadlines**: Accelerate through phases but maintain documentation
- **Small features**: You may compress multiple phases into one session
- **Experimentation**: Discovery and architecture might be tighter loops

Avoid deviating from:
- **Skipping phases** - This creates technical debt
- **Implementing without contracts** - Tests should exist before code
- **Skipping retrospectives** - Learning is how we improve

## Success Metrics

A successful Loom project achieves:

✅ **Clear Requirements** - Everyone understands what's being built
✅ **Sound Architecture** - Technical design is documented and reviewed
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
