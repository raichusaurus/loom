# Requirements Template

Use this template to define and document requirements for your project.

**Project Name:** [Your project name]
**Date:** [Date]
**Requirements Lead:** [Who's leading this]

### How to Use This Template

- Keep sections that clarify what must be built, how success will be validated, or what Architecture must decide next.
- Delete optional sections that do not apply; unused prompts create noise.
- Use **Optional / Not Needed Yet** to name tempting work that should not be part of the MVP.

---

## Overview

### Discovery Inputs
*Pull these forward from Discovery before writing new requirements.*

- **Core problem:**
- **Primary user / operator:**
- **Future / external users:**
- **Working shape:**
- **First useful version:**
- **Explicitly out of scope:**
- **Success / validation signals:**
- **Open questions carried forward:**

### Solution Vision
*High-level vision of what we're building, based on the Discovery inputs above.*

### Phase Updates
*Optional. Use this when later phases clarify or change requirements. Keep the original trail, but make the current requirement clear.*

- **[Date / Phase]:** [What changed, what it supersedes, and why]

---

## Scope Definition

### In Scope
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

*What are we definitely building?*

### Out of Scope
- Feature that could wait
- Nice-to-have that won't ship
- External integrations that are blocked

*What are we explicitly not doing?*

### MVP (Minimum Viable Product)
[What's the smallest version that solves the core problem?]

### Phased Releases (if applicable)
- **Phase 1:** [Features for initial release]
- **Phase 2:** [Features for follow-up]
- **Phase 3:** [Future enhancements]

### Optional / Not Needed Yet
*Use this to keep the MVP honest. Capture useful ideas that are intentionally deferred, experimental, or probably unnecessary.*

| Item | Status | Why not now? | Revisit when |
|------|--------|--------------|--------------|
| | Optional / Deferred / Unnecessary | | |

---

## Functional Requirements

### User Stories
*Format: As a [user type], I want [action] so that [benefit]*

#### Story 1
As a [user type], I want [action] so that [benefit]

Acceptance Criteria:

- Criterion 1
- Criterion 2
- Criterion 3

#### Story 2
As a [user type], I want [action] so that [benefit]

Acceptance Criteria:

- Criterion 1
- Criterion 2

*[Add more as needed]*

### Key Features
*Use a consistent priority scale such as Must / Should / Could / Won't for MVP.*

| Feature | Description | Priority | Notes |
|---------|-------------|----------|-------|
| | | | |
| | | | |

### Output Surfaces
*Where will users, operators, or downstream systems see the result? Delete this section if the project has no meaningful output surfaces beyond the primary product.*

| Surface | Purpose | Required Content | Consumer |
|---------|---------|------------------|----------|
| | | | |

### Data Fidelity
*For data-heavy projects, define what must be preserved versus what can be derived. Delete this section if it does not apply.*

- **Source facts to preserve:**
- **Derived data / recalculable outputs:**
- **Stable identifiers:**
- **Precision limits / unknowns not to invent:**

---

## Non-Functional Requirements

### Performance
- Load time targets: [e.g., < 2 seconds]
- Concurrent users: [e.g., 1000]
- Data throughput: [e.g., 1GB/day]

### Scalability
[How should this scale? What's the growth plan?]

### Security
- Authentication: [e.g., OAuth2]
- Authorization: [e.g., Role-based access]
- Data encryption: [At rest? In transit?]
- Compliance: [GDPR? HIPAA? etc.]

### Accessibility
- WCAG Level: [e.g., AA]
- Screen reader support: [Yes/No]
- Keyboard navigation: [Yes/No]

### Reliability
- Uptime target: [e.g., 99.9%]
- Backup strategy: [How often?]
- Recovery time objective: [RTO]

### Cost
- Recurring cost target: [e.g., local-only, free tier, <$X/month]
- Paid service approval threshold:
- Cost-related tradeoffs:

---

## Acceptance Tests

### Test Case 1: [Feature Name]
Given [precondition] When [user action] Then [expected result]

### Test Case 2: [Feature Name]
Given [precondition] When [user action] Then [expected result]

*[Add more as needed]*

---

## Success Criteria

### Measurable Goals
- [ ] All acceptance tests passing
- [ ] Performance targets met: [specific metrics]
- [ ] User satisfaction: [target score]
- [ ] Uptime: [target percentage]

### Validation Signals
*What evidence will prove the requirements are useful, not just implemented?*

- [ ] Required outputs are inspectable by the intended user/operator
- [ ] Results can be compared across runs, versions, users, or scenarios where stability matters
- [ ] Confidence, sample size, provenance, or other credibility context is visible where needed
- [ ] Outputs can be traced back to source data, user action, or acceptance criteria where needed

### Definition of Done
A feature is considered done when:
- [ ] Code is written and reviewed
- [ ] Tests are passing
- [ ] Documentation is complete
- [ ] Performance is acceptable
- [ ] Security review is complete

---

## Dependencies & Risks

### External Dependencies
| Dependency | Owner | Timeline | Risk |
|------------|-------|----------|------|
| | | | |

### Risks
| Risk | Mitigation | Owner |
|------|-----------|-------|
| | | |

### Assumptions
| Assumption | Validation Plan |
|-----------|-----------------|
| | |

### Prior Art / Legacy Inputs
*Optional. Use for rewrites, migrations, pilots, or projects with meaningful existing artifacts. Delete if not applicable.*

| Artifact | What it shows | Keep / Discard / Rethink | Notes |
|----------|---------------|--------------------------|-------|
| | | | |

---

## Architecture Inputs

*Capture important decisions Requirements surfaced but should not resolve. These become starting points for Architecture.*

Architecture should decide:

- [Decision area 1]
- [Decision area 2]
- [Tradeoff or unresolved design question]
- [Legacy/prior-art reuse decision, if applicable]

---

## Phase Gate

- **Ready to move to Architecture?** [ ] Yes [ ] No
- **Remaining concerns:**
- **Owner decision:**

---

*Save this document in your project repo. Reference these requirements during Architecture and Implementation.*
