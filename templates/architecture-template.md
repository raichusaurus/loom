# Architecture Template

Use this template to design your system architecture and hand clear decisions to Planning & Decomposition.

**Project Name:** [Your project name]
**Date:** [Date]
**Architecture Lead:** [Who's leading this]

### How to Use This Template

- Keep sections that clarify structure, boundaries, decisions, risks, or planning inputs.
- Delete optional sections that do not apply; unused architecture prompts create noise.
- Prefer decisions and tradeoffs over exhaustive implementation detail.
- Capture deferred paths explicitly so Planning knows what to build now and what to avoid.

---

## Overview

### Inputs From Requirements
*Pull forward the requirements signals Architecture must honor.*

- **MVP scope:**
- **Key acceptance criteria:**
- **Non-functional constraints:**
- **Architecture inputs / open decisions:**
- **Optional or deferred work to avoid for now:**

### Problem
[Recap what we're building and why, in architecture terms.]

### Architectural Goals
[What goals should shape the design? Simplicity, speed, cost, reliability, extensibility, data fidelity, operability, etc.]

### Prior Art / Legacy Review Findings
*Optional. Use for rewrites, migrations, pilots, or projects with meaningful existing artifacts. Delete if not applicable.*

| Area / Artifact | Decision | Notes |
|-----------------|----------|-------|
| | Reuse / Discard / Rethink / Defer | |

---

## System Architecture

### High-Level Design
*Include a diagram or concise structure description.*

```text
[ASCII diagram or system outline]
```

### Major Components
| Component | Purpose | Responsibility |
|-----------|---------|----------------|
| | | |
| | | |

### Component Interactions
*How do components communicate, sequence work, share state, and handle failures?*

- [Interaction 1]
- [Interaction 2]

### Service / Interaction Diagrams
*Optional. Use when important workflows need more detail than the high-level diagram. Keep diagrams small and focused on call direction, state boundaries, or handoff points.*

#### [Workflow / Interaction Name]

```text
[Interface / caller]
  |
  v
[Application service / coordinator]
  |
  +--> [Dependency or repository]
  +--> [Domain service]
  |
  v
[Result / persisted state / output]
```

### Initial Service / Module Map
*Optional. Use when Planning needs a concrete starting map of modules, services, or classes. Names can change during implementation, but responsibility boundaries should stay intentional.*

| Area | Primary Modules / Services | Role |
|------|----------------------------|------|
| | | |

### Component Internal Contracts
*Optional. Use for components whose boundaries should feed Contracts & Tests. This is especially useful for services, APIs, repositories, workflows, models, queues, importers, and CLIs.*

#### [Component Name]

| Item | Detail |
|------|--------|
| Owns | |
| Inputs | |
| Outputs | |
| Must not do | |
| Contract tests | |

### Interfaces / Control Surfaces
*How do users, operators, jobs, external systems, or downstream consumers interact with the system?*

| Interface | Purpose | Primary Components / Services | Notes |
|-----------|---------|--------------------------------|-------|
| CLI / UI / API / Worker / Export | | | |

### Boundary Rules
*Define dependency direction and ownership rules that should shape implementation.*

- [Boundary rule 1, e.g., UI calls application services; services do not import UI code.]
- [Boundary rule 2, e.g., domain logic reads through repositories, not raw external clients.]

### Future Transition Boundaries
*Optional. Use when the MVP intentionally defers a surface, platform, or scale path but should preserve an easy transition later.*

| Future Need | Boundary Preserved Now | Trigger to Revisit |
|-------------|------------------------|--------------------|
| | | |

---

## Technology Stack

### Decisions by Layer
*Use project-specific layers. Examples: frontend, backend, CLI, mobile, worker, API, database, search, analytics, ML/model, integration, infrastructure.*

#### [Layer Name]
- **Technology:** [Choice]
- **Justification:** [Why this choice fits the requirements]
- **Alternatives Considered:** [Other viable options]
- **Tradeoffs:** [What this choice gives up]
- **Boundary Rule:** [Optional dependency or ownership rule]

#### [Layer Name]
- **Technology:** [Choice]
- **Justification:** [Why this choice fits the requirements]
- **Alternatives Considered:** [Other viable options]
- **Tradeoffs:** [What this choice gives up]
- **Boundary Rule:** [Optional dependency or ownership rule]

---

## Data Design

### Data Model
*Include an ER diagram, entity list, object model, document shape, event schema, or state model as appropriate.*

```text
[Data model outline]
```

### Entity / State Notes
*Explain important identity, ownership, lifecycle, retention, source-of-truth, or precision decisions.*

- **Source of truth:**
- **Stable identifiers:**
- **Derived / recalculable data:**
- **Retention / deletion expectations:**
- **Precision limits / unknowns not to invent:**

### Operational Modes / Runtime State
*Optional. Use for crawlers, sync systems, background workers, pipelines, schedulers, importers, queues, or long-running jobs.*

| Mode | Purpose | Expected Use | Primary State |
|------|---------|--------------|---------------|
| | | | |

### Runtime Controls
*Optional. Use when operators or automation need to adjust behavior during or between runs.*

- **Configurable limits:**
- **Runtime overrides:**
- **Backoff / slowdown behavior:**
- **Progress visibility:**
- **Owner component:**

### Data Flow
*How does data move through the system?*

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Storage Strategy
- **Application data:** [Where? How retained?]
- **Generated outputs:** [Where? Reproducible from source data?]
- **Logs:** [Where? How long retained?]
- **Backups:** [Frequency? Retention?]

---

## Integration Points

### External APIs / Services
| Service | Purpose | Integration Approach |
|---------|---------|----------------------|
| | | |

### Endpoint / Capability Coverage
*Optional. Use when the exact integration surface matters.*

- [Endpoint, capability, event, file, or protocol]
- [Endpoint, capability, event, file, or protocol]

### Database / Storage Integrations
| System | Type | Purpose |
|--------|------|---------|
| | | |

### Events and Queues
*Optional. Document async communication patterns or state-backed queues.*

- **Queue / topic / state table:**
- **Producer:**
- **Consumer:**
- **Retry / idempotency behavior:**

---

## Domain / Model Architecture
*Optional. Use when the project has important domain logic, workflow logic, ranking/scoring, rules engines, AI/model behavior, financial calculations, recommendation logic, search relevance, or similar complexity.*

### Baseline Approach
[Explain the first architecture-level shape of the domain/model logic.]

### Required Boundaries
- **Input:**
- **Output:**
- **Replaceability / extension path:**
- **What this logic must not depend on:**

### Explainability / Validation Context
*Optional. Use when outputs need provenance, confidence, evidence, auditability, or human inspection.*

- [Context signal 1]
- [Context signal 2]

---

## Scalability & Performance

### Expected Load
- **Users / operators:**
- **Request or job volume:**
- **Data growth:**
- **Concurrency expectations:**

### Scaling Strategy
[How should each important component scale, and what should stay deliberately simple for MVP?]

### Performance Targets
- **User-facing latency:**
- **Job / workflow runtime:**
- **Query or data-processing time:**
- **External service rate limits:**

### Bottlenecks & Solutions
| Potential Bottleneck | Solution |
|----------------------|----------|
| | |

---

## Security & Reliability

### Security Architecture
- **Authentication:**
- **Authorization:**
- **Secrets/config:**
- **Encryption:**
- **External/API security:**
- **Data handling:**

### Privileged vs Read-Only Access
*Optional. Use when admin/control actions and read-only/product surfaces have different risk profiles.*

- **Privileged controls:**
- **Read-only surfaces:**
- **Default binding / exposure:**
- **Access separation:**

### Reliability
- **Failure handling:**
- **Retries / idempotency:**
- **State recovery:**
- **Partial failure behavior:**

### Disaster Recovery
- **Backup strategy:**
- **Failover plan:**
- **RTO:**
- **RPO:**

### Monitoring & Observability
- **Metrics:**
- **Logs:**
- **Alerts:**
- **Tracing:**

---

## Deployment Architecture

### Environments
- **Development:**
- **Test:**
- **Staging:** [Delete if not needed]
- **Production:** [Delete if not needed]

### Deployment / Run Process
- **Build:**
- **Test:**
- **Run / deploy:**
- **Inspection / verification:**
- **Rollback:**

### Infrastructure as Code
*Optional. Delete if not needed yet.*

- **IaC approach:**
- **Provisioned resources:**
- **Deferred infrastructure:**

---

## Risk & Mitigation

### Architectural Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| | | |

### Technology Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| | | |

### Deferred Work Risks
*Optional. Use when deferring a feature, platform, or operational capability creates known risk.*

| Deferred Item | Risk | Revisit Trigger |
|---------------|------|-----------------|
| | | |

---

## Decision Log

### Key Decisions Made
| Decision | Rationale | Alternatives |
|----------|-----------|--------------|
| | | |

### Decisions Still Open
| Decision | Default for Planning | Revisit When |
|----------|----------------------|--------------|
| | | |

---

## Planning Inputs

*Hand the architecture to Planning & Decomposition as buildable work.*

- **Components / modules to build:**
- **Likely workstreams:**
- **Critical sequencing constraints:**
- **Parallelization opportunities:**
- **Contracts, schemas, or interfaces needing tests:**
- **Service/module boundaries to preserve:**
- **Highest-risk areas to isolate early:**
- **Decisions Planning must not reopen without new evidence:**

---

## Phase Gate

- **Ready to move to Planning & Decomposition?** [ ] Yes [ ] No
- **Remaining concerns:**
- **Owner decision:**

---

*Save this document and diagrams in your project repo for future reference.*
