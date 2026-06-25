# Implementation Template

Use this template to track implementation work against the plan, contracts, and requirements.

**Project Name:** [Your project name]  
**Date:** [Date]  
**Implementation Lead:** [Who's leading this]

---

## Inputs

- Requirements document:
- Architecture document:
- Planning & Decomposition document:
- Contracts & Tests document:
- Check automation handoff:

---

## Workstream Status

| Workstream | Owner | Status | Branch/PR | Notes |
|------------|-------|--------|-----------|-------|
| | | | | |

---

## Implementation Notes

### Completed Work
- [ ] [Feature/service/module]

### Implementation Slices
| Slice | Status | Evidence | Notes |
|-------|--------|----------|-------|
| | | | |

### Deviations from Plan
| Deviation | Reason | Approved By | Follow-up |
|-----------|--------|-------------|-----------|
| | | | |

### Progress Tree Updates
*Keep progress docs, source paths, and test paths aligned as implementation reveals the real shape.*

| Scope | Progress Doc Path | Source Path | Test Path | Update Needed / Completed |
|-------|-------------------|-------------|-----------|---------------------------|
| | | | | |

### Blockers
| Blocker | Owner | Impact | Next Step |
|---------|-------|--------|-----------|
| | | | |

### Open Implementation Decisions
*Use this for blockers, deviations, scope choices, or implementation questions that need user input.*

| Question Summary | Options | Trade-offs | Recommendation | Owner / Status |
|------------------|---------|------------|----------------|----------------|
| | | | | |

---

## Verification

### Check Automation Bootstrap
*Use the Contracts & Tests handoff to make local checks reproducible once the scaffold can run them.*

- [ ] Dependency install / lockfile check works
- [ ] Test command works locally
- [ ] Format check works locally
- [ ] Lint check works locally
- [ ] CI/check workflow added when meaningful
- [ ] Live/external tests are opt-in by default

### Tests
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] End-to-end tests passing
- [ ] Manual validation complete

### Quality Checks
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Observability added
- [ ] Security concerns addressed

---

## Handoff Notes

### Integration Notes
[What should reviewers and downstream workstreams know?]

### Maintenance Notes
[What will future maintainers need to understand?]

### Release / Operations Follow-Up
*Optional. Use this when the project needs deployment, scheduling, monitoring, release automation, runbooks, or production support after implementation.*

| Follow-up | Reason | Suggested Starting Phase |
|-----------|--------|--------------------------|
| | | |

---

## Phase Decisions

*Keep decisions and approved deviations from implementation close to this artifact, even when they are also summarized in the root progress ledger.*

| Decision | Choice | Rationale | Owner |
|----------|--------|-----------|-------|
| | | | |

## Next Phase Handoff

*If approved, summarize what Review & Retrospective should use next. Preparing this handoff does not close the phase gate or start Review by itself.*

- **Decisions:**
- **Inputs:**
- **Open risks:**
- **Non-goals:**
- **Validation signals:**

## Loom Process Feedback

*If this phase exposed reusable Loom lessons, capture them here or link to `docs/loom/pilot-feedback.md`. Keep process feedback separate from product scope.*

| Observation | Suggested Template/Guide Improvement | Project-Specific? |
|-------------|--------------------------------------|-------------------|
| | | Yes / No |

---

## Phase Gate

- **Agent recommendation:** [ ] Ready [ ] Not ready
- **Owner decision:** [ ] Approved [ ] Needs revision [ ] Deferred
- **Decision date:** TBD
- **Loom feedback captured:** [ ] Not applicable [ ] In this phase artifact [ ] In `docs/loom/pilot-feedback.md`
- **Remaining concerns:** TBD
