# Phase 5: Contracts & Tests

## Purpose

Before writing code, you define **how it will work** and **how you'll verify it works**. This phase takes the architecture and decomposition plan, then establishes behavior contracts, test strategy, fixtures, and the verification handoff for implementation.

This phase focuses on:
- Defining API contracts and interfaces
- Writing tests (unit, integration, end-to-end)
- Defining test fixtures and contract stability
- Capturing check automation needs for implementation/bootstrap
- Establishing code quality standards
- Mapping tests and contracts to workstream ownership

## Key Questions

The Contracts & Tests Agent will help you explore:

### Contracts & Interfaces
- What are the API contracts?
- What inputs/outputs does each component have?
- What are the error cases?
- How do components communicate?
- Which workstream owns each contract?

### Test Strategy
- What needs to be tested?
- What's the test coverage target?
- What types of tests (unit/integration/e2e)?
- What are the happy paths vs. edge cases?
- Which tests validate integration between independently owned workstreams?
- Which tests should exist before implementation starts?
- Which tests are locked contracts versus flexible implementation aids?

### Check Automation Handoff
- What local commands should developers run?
- What checks should eventually run on every commit or pull request?
- When can those checks become blocking?
- Which checks are deferred until scaffold, lockfile, or first implementation slice exists?
- Which live/external tests must stay opt-in?

### Code Quality
- Linting standards?
- Code review requirements?
- Documentation standards?
- Performance benchmarks?

### Monitoring & Observability
- How will you know if something breaks in production?
- What metrics matter?
- What logs are needed?
- What alerts should trigger?

## Outputs

By the end of this phase, you'll have:

✅ **API Contracts** - Defined interfaces between components
✅ **Test Plan** - What gets tested and how
✅ **Contract/Test Candidates** - Behavior that should become executable checks
✅ **Fixture Plan** - Source payloads, scenarios, and edge cases to preserve
✅ **Check Automation Handoff** - Local and CI checks to bootstrap when the project can run them
✅ **Code Quality Standards** - Linting, formatting, review requirements
✅ **Monitoring Plan** - Observability and alerting strategy
✅ **Ownership-Aligned Verification** - Tests and contracts mapped to workstreams

## Contracts & Tests Template

See [contracts-tests-template.md](../templates/contracts-tests-template.md) for a detailed template.

## When This Phase is Complete

You're ready to move to Implementation when:

- ✅ API contracts are defined
- ✅ Test strategy is clear
- ✅ Required contract/test candidates are captured
- ✅ Automation/bootstrap handoff is captured
- ✅ Code quality standards are established
- ✅ The first implementation slice knows which failing tests or checks to create first

## Tips

- **Tests before code** - This ensures you think about contracts first
- **Plan automation honestly** - CI/check automation may need to wait until the scaffold and lockfile exist
- **Make tests fast** - Developers should run tests frequently
- **Define success early** - Acceptance tests from Requirements become integration tests here
- **Think about edge cases** - What happens when things go wrong?

## The Philosophy

This phase is crucial because:
- **Clarity** - Contracts force you to think about interfaces before implementing
- **Confidence** - Tests give you confidence to refactor and change
- **Speed** - Local checks and later CI automation catch bugs before review
- **Quality** - Standards ensure consistency across the codebase

---

**Next**: Move to [Implementation](./06-implementation.md) once Contracts & Tests are complete.
