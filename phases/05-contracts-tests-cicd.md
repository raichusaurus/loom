# Phase 5: Contracts & Tests / CI/CD

## Purpose

Before writing code, you define **how it will work** and **how you'll verify it works**. This phase takes the architecture and decomposition plan, then establishes contracts, test strategy, and CI/CD pipelines.

This phase focuses on:
- Defining API contracts and interfaces
- Writing tests (unit, integration, end-to-end)
- Setting up CI/CD pipelines
- Establishing code quality standards
- Automating verification
- Mapping tests and contracts to workstream ownership

## Key Questions

The Test & CI/CD Agent will help you explore:

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

### CI/CD Pipeline
- What runs on every commit?
- How do you validate code quality?
- What's the deployment strategy?
- How do you catch bugs early?

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
✅ **Unit Tests** - Test skeletons and strategy
✅ **CI/CD Pipeline** - GitHub Actions workflows configured
✅ **Code Quality Standards** - Linting, formatting, review requirements
✅ **Monitoring Plan** - Observability and alerting strategy
✅ **Ownership-Aligned Verification** - Tests and contracts mapped to workstreams

## Contracts & Tests Template

See [contracts-tests-template.md](../templates/contracts-tests-template.md) for a detailed template.

## When This Phase is Complete

You're ready to move to Implementation when:

- ✅ API contracts are defined
- ✅ Test strategy is clear
- ✅ CI/CD pipeline is set up
- ✅ Code quality standards are established
- ✅ Tests can be written and run automatically

## Tips

- **Tests before code** - This ensures you think about contracts first
- **Automate everything** - CI/CD should catch issues automatically
- **Make tests fast** - Developers should run tests frequently
- **Define success early** - Acceptance tests from Requirements become integration tests here
- **Think about edge cases** - What happens when things go wrong?

## The Philosophy

This phase is crucial because:
- **Clarity** - Contracts force you to think about interfaces before implementing
- **Confidence** - Tests give you confidence to refactor and change
- **Speed** - Automation catches bugs before code review
- **Quality** - Standards ensure consistency across the codebase

---

**Next**: Move to [Implementation](./06-implementation.md) once Contracts & Tests / CI/CD are complete.
