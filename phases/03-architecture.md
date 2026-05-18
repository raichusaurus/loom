# Phase 3: Architecture

## Purpose

Architecture answers: **How will we build this, and what boundaries should implementation preserve?**

This phase translates Requirements into a technical design that Planning & Decomposition can turn into workstreams. It should prefer clear decisions, tradeoffs, boundaries, and handoff inputs over exhaustive implementation detail.

This phase focuses on:
- System structure, component responsibilities, and interaction patterns
- Technology choices by layer, with alternatives and tradeoffs
- Data model, data flow, state ownership, and fidelity constraints
- Interfaces, control surfaces, and dependency direction
- Component contracts that should feed Contracts & Tests
- Scalability, performance, security, reliability, and operational shape
- Deferred paths and future transition boundaries
- Planning inputs for workstream decomposition

## Key Questions

The Architecture Agent will help you explore:

### Inputs From Requirements
- What MVP scope must Architecture honor?
- Which acceptance criteria shape technical design?
- What non-functional constraints are real for this pass?
- What optional or deferred work should the architecture avoid building now?
- Which open decisions did Requirements hand forward?

### System Structure and Boundaries
- What are the major components, modules, services, or classes?
- What does each component own?
- How do components communicate, sequence work, share state, and handle failure?
- What must each component not do?
- What dependency direction and ownership rules should implementation preserve?
- Which future transition boundaries should be protected without overbuilding?

### Interfaces and Control Surfaces
- How do users, operators, jobs, external systems, or downstream consumers interact with the system?
- Which CLI, UI, API, worker, export, or scheduled surfaces exist?
- Which surfaces are privileged controls versus read-only or product surfaces?
- What access separation or default exposure decisions matter?

### Technology Decisions
- What technology fits each layer?
- Why this choice?
- What alternatives were considered?
- What tradeoffs does each choice create?
- What boundary rule comes with the choice?

### Data, Runtime State, and Integrations
- What is the data model or state model?
- What is the source of truth?
- Which identifiers must stay stable?
- What data is derived or recalculable?
- What precision limits or unknown values must not be invented?
- What external APIs, storage systems, queues, events, or protocols are involved?
- What operational modes, runtime controls, backoff behavior, or progress visibility are needed?

### Domain or Model Logic
- Is there domain logic, workflow logic, ranking, scoring, AI/model behavior, search relevance, or another complex decision engine?
- What are its inputs and outputs?
- How replaceable or extensible should it be?
- What must the logic not depend on?
- What explainability, provenance, confidence, evidence, or audit context is required?

### Risk, Operations, and Handoff
- What bottlenecks, failure modes, and recovery paths matter?
- What security and reliability choices are required?
- What deployment/run process is enough for the current scope?
- What risks come from deferred work?
- What decisions are settled, and what remains open?
- What should Planning & Decomposition build, sequence, parallelize, and protect?

## Outputs

By the end of Architecture, you'll have:

✅ **Architecture Overview** - Problem recap, goals, and requirement inputs
✅ **System Design** - Components, interactions, diagrams, interfaces, and boundary rules
✅ **Technology Decisions** - Choices by layer with justification, alternatives, tradeoffs, and boundary implications
✅ **Data Design** - Model, source of truth, identifiers, data flow, storage, and runtime state
✅ **Integration Design** - External services, endpoints, events, queues, and storage integrations
✅ **Component Contracts** - Inputs, outputs, ownership, and test candidates for Contracts & Tests
✅ **Security & Reliability Plan** - Access, secrets, failure handling, recovery, and observability
✅ **Decision Log** - Key decisions, open decisions, defaults, and revisit triggers
✅ **Planning Inputs** - Components, workstreams, sequencing, parallelism, contracts, boundaries, and highest-risk areas

## Architecture Template

See [architecture-template.md](../templates/architecture-template.md) for a detailed template.

## When Architecture is Complete

You're ready to move to Planning & Decomposition when:

- ✅ Requirements inputs and MVP constraints are reflected in the design
- ✅ Components, modules, services, and responsibilities are clear enough to decompose
- ✅ Interaction patterns, interfaces, and control surfaces are documented
- ✅ Boundary rules and ownership rules are explicit
- ✅ Data model, state ownership, and integration points are understood
- ✅ Technology choices are justified with tradeoffs and alternatives
- ✅ Component contracts and contract-test candidates are identified
- ✅ Security, reliability, operational, and deferred-work risks are captured
- ✅ Planning inputs name workstreams, sequencing constraints, parallelization opportunities, and decisions Planning must not reopen

## Tips

- **Design the boundaries, not every line of code** - Planning and Implementation need shape more than exhaustive detail
- **Make deferred paths visible** - Future work is easier when the MVP explicitly avoids and preserves the right things
- **Treat contracts as handoff material** - Component inputs, outputs, and "must not do" rules feed Contracts & Tests
- **Name control surfaces carefully** - Operator controls, read-only outputs, and external APIs often carry different risks
- **Capture defaults for open decisions** - Planning can move forward when it knows the current default and revisit trigger
- **Prefer diagrams that clarify ownership** - Small interaction diagrams beat large decorative maps

---

**Next**: Move to [Planning & Decomposition](./04-planning-decomposition.md) once Architecture is complete.
