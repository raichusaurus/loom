# Contracts & Tests Template

Use this template to define how the system will be verified before implementation begins.

**Project Name:** [Your project name]  
**Date:** [Date]  
**Test Lead:** [Who's leading this]

### How to Use This Template

- Focus on behavior contracts, test strategy, fixtures, and quality gates before implementation.
- Keep CI/check automation to bootstrap/handoff planning unless the project already has a runnable scaffold and stable checks.
- Delete optional sections that do not apply; unused test prompts create noise.
- Treat tests as executable requirements, but allow approved updates when implementation reveals a better contract.

---

## Inputs

- Requirements document:
- Architecture document:
- Planning & Decomposition document:
- Architecture component/internal contracts:
- Planning contract/test candidates:

---

## Testing Decision

*Define the project's testing posture before implementation starts.*

- **Test-first policy:** [e.g., tests before implementation, tests alongside implementation, characterization tests first]
- **Required pre-implementation tests:** [What must exist before coding a slice?]
- **Allowed scaffold exceptions:** [What can be created before tests so tests can import/run?]
- **Network/external dependency policy:** [Mocked/fixture by default? Live tests opt-in?]
- **Approval policy for rewriting existing tests:** [Who approves, and what explanation is required?]

### Open Contract / Test Decisions
*Use this for unresolved test, fixture, automation, quality, or monitoring questions that need user input.*

| Question Summary | Options | Trade-offs | Recommendation | Owner / Status |
|------------------|---------|------------|----------------|----------------|
| | | | | |

### Contract Stability Register
*Optional. Use when some tests/contracts should be treated as locked while others may evolve.*

| Test / Contract Area | Stability | Notes |
|----------------------|-----------|-------|
| | Locked / Approval required / Flexible | |

### Accepted Test-Support APIs
*Optional. Name helper APIs, fixture builders, fake clients, or seed helpers that implementation may rely on.*

| API / Helper | Purpose |
|--------------|---------|
| | |

---

## Framework Recommendation

### Primary Test Stack
| Tool | Use | Recommendation |
|------|-----|----------------|
| | | |

### Test Layout

Mirror the intended source tree where practical. Tests may be grouped by category, but the architecture component or owned unit path should remain recognizable so Progress, source, and tests can be joined automatically.

```text
tests/
  unit/
    [architecture-component]/
      test_[owned-unit].py
  integration/
    [architecture-component]/
      [workflow-or-subcomponent]/
        test_[scenario].py
  contracts/
    [architecture-component]/
      [owned-unit]/
        test_[contract].py
  fixtures/
    [architecture-component]/
      [owned-unit]/
```

### Naming Conventions
- **Test files:**
- **Fixture files:**
- **Golden files:**

---

## Test Categories

| Category | Purpose | Speed | External Dependencies | Required in CI / Automation |
|----------|---------|-------|------------------------|-----------------------------|
| Unit tests | | Fast | None | Yes |
| Contract tests | | Fast to medium | None | Yes |
| Integration tests | | Medium | Local only | Yes |
| End-to-end workflow tests | | Medium to slow | Prefer fixtures | Project-dependent |
| Live/external smoke tests | | Slow/variable | External systems | No, opt-in by default |

---

## Contracts & Interfaces

### API / Service Contracts
| Contract | Owner | Consumers | Inputs | Outputs | Error Cases |
|----------|-------|-----------|--------|---------|-------------|
| | | | | | |

### Component / Class Contracts
| Component / Class | Required Test Focus |
|-------------------|---------------------|
| | |

### CLI / UI / Workflow Contracts
*Optional. Use for command names, routes, forms, workflow steps, events, exports, or other user/operator-facing contracts.*

| Surface | Contract | Required Evidence |
|---------|----------|-------------------|
| | | |

---

## Data Contracts

### Schema / Model Contracts
| Schema / Event / Model | Owner | Fields | Compatibility Notes |
|------------------------|-------|--------|---------------------|
| | | | |

### Constraint Contracts
*Optional. Use when primary keys, uniqueness, idempotency, foreign keys, retention, raw data preservation, or compatibility matter.*

| Contract Area | Required Test Evidence |
|---------------|------------------------|
| | |

### Identity / Key Contracts
*Optional. Use when stable IDs or derived keys must be shared across components.*

- **Key format:**
- **Stability rules:**
- **Unknown / nullable value handling:**
- **Display label vs. identifier rules:**

---

## Test Strategy

### Coverage Matrix
| Area | Progress Doc Path | Source Path | Test Path | Test Type | Owner | Required Before Merge |
|------|-------------------|-------------|-----------|-----------|-------|-----------------------|
| | | | | | | |

### Required Fixtures
*Optional. Use fixtures to cover important source payloads, workflow states, user scenarios, or edge cases.*

| Fixture | Purpose |
|---------|---------|
| | |

### Acceptance Tests
| Requirement | Test | Evidence |
|-------------|------|----------|
| | | |

### Integration Tests
| Integration Point | Test Scenario | Owner |
|-------------------|---------------|-------|
| | | |

### Progress Tree Updates
*Add scopes that became contract-ready because tests, fixtures, or contract expectations now exist.*

| Scope | Type | Progress Doc Path | Source Path | Test Path | Progress Update |
|-------|------|-------------------|-------------|-----------|-----------------|
| | System Component / Subcomponent / Unit | `docs/loom/system/.../PROGRESS.md` | | | |

---

## Check Automation Handoff

*Do not require full CI/check automation during this phase unless the project already has enough scaffold to run meaningful checks. Capture what should be automated once implementation or bootstrap work makes it possible.*

### Current Status
- **Runnable scaffold exists?** [ ] Yes [ ] No
- **Dependency lockfile exists?** [ ] Yes [ ] No
- **Tests currently expected to pass?** [ ] Yes [ ] No
- **CI/check workflow exists?** [ ] Yes [ ] No

### Automation Bootstrap Plan
| Check | Add When | Blocking? |
|-------|----------|-----------|
| Install / dependency lock check | | |
| Format check | | |
| Lint check | | |
| Unit / contract tests | | |
| Integration tests | | |
| Type checking | | |
| Migration / schema check | | |
| Security checks | | |

### Suggested Local Commands
```bash
[local test command]
[local lint command]
[local format check command]
```

### Deployment / Release Automation
*Usually belongs to a later release/operations pass, not this contracts phase. Capture known needs without forcing setup now.*

- **Deployment target:** [None yet / local / staging / production]
- **Promotion flow:** [If known]
- **Rollback expectation:** [If known]
- **Deferred release automation:**

---

## Observability

### Metrics, Logs, and Alerts
| Signal | Purpose | Alert Threshold / Local Warning |
|--------|---------|---------------------------------|
| | | |

---

## Phase Decisions

*Keep decisions that shaped contracts and tests close to this artifact, even when they are also summarized in the root progress ledger.*

| Decision | Choice | Rationale | Owner |
|----------|--------|-----------|-------|
| | | | |

## Next Phase Handoff

*If approved, summarize what Implementation should use next. Preparing this handoff does not close the phase gate or start Implementation by itself.*

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
- **Required tests/contracts identified?** [ ] Yes [ ] No
- **Automation/bootstrap handoff captured?** [ ] Yes [ ] No
- **Remaining concerns:** TBD
