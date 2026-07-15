# Discovery Template

Use this template to capture findings during the Discovery phase.

**Project Name:** [Your project name]
**Date:** [Date]
**Facilitator:** [Who's leading this]

## How to Use This Template

- Focus on learning, context, and direction; avoid locking in requirements or architecture too early.
- Keep sections that clarify the problem, users, constraints, validation needs, or handoff to Requirements.
- Delete optional sections that do not apply; unused prompts create noise.
- Capture tempting solution ideas as working shape, not as commitments.

---

## Problem Statement

### Core Problem
*What is the fundamental problem you're trying to solve?*

### Why It Matters
*Why is solving this problem important? What's the impact?*

### Current State
*How is this problem being solved today? What's working? What's not?*

---

## Project Context

### Project Type
*Is this a new build, rewrite, migration, continuation, experiment, or something else?*

### Prior Art / Existing System
*What already exists? What should be kept, discarded, or rethought?*

| Source / Artifact | What It Shows | Keep / Discard / Rethink | Notes |
|-------------------|---------------|---------------------------|-------|
| | | | |

For a rewrite or migration, also capture the current user or data path, observed pain, affected owner, compatibility-sensitive behavior or data, and desired target outcome.

### Working Shape
*What does the solution seem to be, without locking in requirements or architecture too early?*

### First Useful Version
*What is the smallest version that would prove the core idea is worth continuing?*

### Explicitly Out of Scope
*What should not be included in the first useful version?*

- [Out of scope item]
- [Out of scope item]

---

## Users & Stakeholders

### Primary User / Operator
*Who is the first person this needs to work for? What do they need to do?*

### Future / External Users
*Who might benefit later, even if the first version is internal or operator-focused?*

### Stakeholders
*Who benefits, influences decisions, contributes, or is affected?*

| Stakeholder | Role | Needs | Constraints |
|-------------|------|-------|-------------|
| | | | |
| | | | |

### Decision Owner
*Who has the final say on whether we proceed?*

---

## Context & Constraints

### Timeline
- **Deadline:** [When do we need this?]
- **Time to market:** [How urgent?]
- **Phase-based release?** [If applicable]

### Resources
- **Budget:** [What's available?]
- **Team:** [Who's working on this?]
- **Infrastructure:** [What do we have?]

### Technical Constraints
- **Existing systems:** [What must we integrate with?]
- **Technology requirements:** [Any mandates?]
- **Scalability needs:** [How big will this get?]

### Organizational Constraints
- **Compliance/Regulatory:** [Any requirements?]
- **Organizational policies:** [Any constraints?]
- **Dependencies:** [What else depends on this?]

### Material Evidence and Uncertainty
*Classify only statements that could change scope, viability, safety, or later design.*

| Statement | Type | Source / Evidence | Confidence | What It Could Change |
|-----------|------|-------------------|------------|----------------------|
| | Measured / Sourced / Derived / Inferred / Assumed / Unknown / Conflict | | High / Medium / Low | |

---

## Success & Validation

### Success Metrics
*How will we know this project is working? What signals are measurable?*

| Metric / Signal | Target | How We'll Measure |
|-----------------|--------|-------------------|
| | | |

### Validation Strategy
*How will we test whether the idea is credible before investing in polish?*

### Evidence Needed Before Requirements
*What must be true, known, or decided before moving to Requirements?*

---

## Assumptions

### Key Assumptions
*What are you assuming to be true? What needs validation?*

| Assumption | Why We Believe It | Confidence | Validation Method | Owner | Decision Point |
|------------|-------------------|------------|-------------------|-------|----------------|
| | | | | | |
| | | | | | |

---

## Risks & Opportunities

### Risks
*What could prevent success?*

| Risk | Impact | Evidence / Assumption | Validation or Mitigation | Owner | Decision Point |
|------|--------|-----------------------|--------------------------|-------|----------------|
| | | | | | |

### Opportunities
*What unexpected benefits might emerge?*

---

## Loom Process Feedback

*Optional. Record only a phase-local observation when this phase exposed material Loom friction, a missing guardrail, repeated workaround, validation failure, or unnecessary ceremony. Put any reusable candidate in `docs/loom/pilot-feedback.md`; delete this section for a clean phase.*

| Observation | Evidence / Impact | Pilot Feedback Reference, if Reusable |
|-------------|-------------------|---------------------------------------|
| | | `docs/loom/pilot-feedback.md#...` |

---

## Phase Decisions

*Keep decisions that shaped this phase close to the phase artifact, even when they are also summarized in the root progress ledger.*

| Decision | Choice | Rationale | Owner |
|----------|--------|-----------|-------|
| | | | |

---

## Discovery Outputs

### Key Insights
*What did you learn during discovery?*

### Open Questions
*What still needs to be explored?*

Use this shape for each question that needs a decision:

| Question Summary | Options | Trade-offs | Recommendation | Owner / Status |
|------------------|---------|------------|----------------|----------------|
| | | | | |

### Requirements Handoff
*If approved, summarize the inputs Requirements should pull forward. Preparing this handoff does not close the phase gate or start Requirements by itself.*

- **Core problem:**
- **Primary user / operator:**
- **Future / external users:**
- **Working shape:**
- **First useful version:**
- **Explicitly out of scope:**
- **Success / validation signals:**
- **Material evidence, assumptions, and unknowns:**
- **Open questions carried forward:**

### Next Steps
*What needs to happen before Requirements?*

---

## Phase Gate

- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Remaining concerns:** TBD

---

*Save this document in your project repo for future reference.*
