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

```text
tests/
  unit/
  integration/
  contracts/
  fixtures/
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
| Area | Test Type | Owner | Required Before Merge |
|------|-----------|-------|-----------------------|
| | | | |

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

## Phase Gate

- **Ready to move to Implementation?** [ ] Yes [ ] No
- **Required tests/contracts identified?** [ ] Yes [ ] No
- **Automation/bootstrap handoff captured?** [ ] Yes [ ] No
- **Remaining concerns:**
- **Owner decision:**
