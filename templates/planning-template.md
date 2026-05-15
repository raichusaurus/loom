# Planning & Decomposition Template

Use this template to turn architecture into an executable plan for humans and agents.

**Project Name:** [Your project name]  
**Date:** [Date]  
**Planning Lead:** [Who's leading this]

---

## Scope

### Planning Scope
[Project, service, feature, subproject, or task-level mini-Loom]

### Inputs
- Discovery document:
- Requirements document:
- Architecture document:
- Architecture planning inputs:

### Decisions Made
*What is settled for this planning pass? Planning should not reopen these without new evidence.*

- [Decision 1]
- [Decision 2]

### Open Decisions
*What still needs to be resolved during Contracts/Tests, implementation, or a future phase?*

- [Open decision 1]
- [Open decision 2]

### Architecture Handoff Summary
*Pull this from the Architecture document before decomposing work.*

- **Components / modules to build:**
- **Likely workstreams:**
- **Critical sequencing constraints:**
- **Parallelization opportunities:**
- **Contracts, schemas, or interfaces needing tests:**
- **Service/module boundaries to preserve:**
- **Highest-risk areas to isolate early:**
- **Decisions Planning must not reopen without new evidence:**

---

## Work Breakdown

### Workstreams
| Workstream | Purpose | Owner | Scope | Notes |
|------------|---------|-------|-------|-------|
| | | | | |

### Implementation Slices
| Slice | Outcome | Depends On | Priority |
|-------|---------|------------|----------|
| | | | |

---

## Ownership Boundaries

### Ownership Map
| Owner | Files/Modules/Services | Responsibilities | Out of Scope |
|-------|------------------------|------------------|--------------|
| | | | |

### Shared Areas
| Shared Area | Owners | Coordination Rule |
|-------------|--------|-------------------|
| | | |

### Boundary / Contract Alignment
*Which architecture boundaries, dependency rules, or component contracts must the plan preserve?*

- **Source architecture sections:**
- **Dependency rules:**
- **Interfaces / schemas / commands to keep stable:**
- **Architecture updates required before changing:**

---

## Dependencies & Sequencing

### Dependency Graph
[Diagram or list the dependency order]

### Critical Path
[What must happen first, and what blocks delivery?]

### Parallel Work
| Workstream | Can Start When | Integration Point |
|------------|----------------|-------------------|
| | | |

---

## Agent Context Packets

### Context Packet: [Workstream Name]
- **Owner:** [Agent/person]
- **Goal:** [What this workstream must accomplish]
- **Relevant requirements:** [Links or references]
- **Relevant architecture decisions:** [Links or references]
- **Owned files/services/modules:** [Scope]
- **Contracts to preserve:** [APIs, schemas, events, interfaces]
- **Risks and assumptions:** [Known concerns]
- **Expected output:** [Patch, design, test plan, report, etc.]
- **Handoff notes required:** [What must be reported when done]

*[Duplicate for each workstream]*

---

## Integration Plan

### Checkpoints
| Checkpoint | Purpose | Required Evidence | Owner |
|------------|---------|-------------------|-------|
| | | | |

### Conflict Resolution
[How do we handle overlapping edits, contract changes, or design deviations?]

### Escalation Path
[When should an agent stop and ask for direction?]

### Contract / Test Candidates
*Carry these into Contracts & Tests. Include behavior that should become fixtures, contract tests, smoke tests, schema checks, command contracts, or API expectations.*

| Candidate | Source | Why it matters | Suggested test shape |
|-----------|--------|----------------|----------------------|
| | | | |

---

## Delivery Plan

### Milestones
| Milestone | Outcome | Workstreams Included | Exit Criteria |
|-----------|---------|----------------------|---------------|
| | | | |

### Initial Sequential Plan
[For first implementation, what is the safest waterfall-style order?]

### Later Agile Cycles
[After the foundation exists, what smaller loops should continue iteratively?]

---

## Update Policy

*Use Planning as the implementation coordination map. Update this document when architecture decisions change, workstream ownership changes, contract boundaries move, or real implementation findings force a better slice order.*

---

## Phase Gate

- **Ready to move to Contracts & Tests?** [ ] Yes [ ] No
- **Remaining concerns:**
- **Owner decision:**

---

*Save this document in your project repo. Use it to brief agents and coordinate implementation.*
