# Phase 6: Implementation

## Purpose

Now you build. Implementation is taking the architecture, decomposition plan, and contracts, then writing the actual code that fulfills requirements and passes tests.

This phase focuses on:
- Writing clean, testable code
- Following established contracts
- Respecting ownership boundaries
- Maintaining code quality
- Keeping tests passing
- Documentation and comments

## Key Questions

The Implementation Agent will help you navigate:

### Code Organization
- How should code be organized?
- What naming conventions?
- How do we keep it maintainable?
- Where does each piece belong?
- How do we avoid crossing another workstream's ownership boundary without coordination?

### Quality Standards
- How do we write good code?
- What code review looks like?
- What makes code "done"?
- How do we catch bugs?

### Testing During Development
- Writing unit tests as you go?
- Integration tests for new features?
- How do you verify contracts?
- What's the development workflow?

### Problem-Solving
- How do we handle unexpected complexity?
- When do we deviate from design?
- How do we communicate changes?
- When do we update documentation?
- When does a subproject or service need its own mini-Loom cycle?

### Performance & Optimization
- Are there performance concerns?
- When do we optimize?
- How do we measure impact?
- What's premature optimization vs. necessary?

## Outputs

By the end of Implementation, you'll have:

✅ **Working Code** - Features implemented per requirements
✅ **Passing Tests** - All tests passing, coverage targets met
✅ **Code Documentation** - Comments and docstrings where needed
✅ **PR/Commit History** - Clear history of changes
✅ **Integration Complete** - All pieces working together
✅ **Updated Handoffs** - Deviations, blockers, and integration notes captured

## Implementation Guidelines

### During Development
- **Write tests as you go** - Don't leave testing for the end
- **Keep commits clean** - Small, focused commits are easier to review
- **Reference requirements** - Tie code to acceptance tests
- **Communicate changes** - If you're deviating from design, flag it
- **Review your own code first** - Catch obvious issues before review

### Code Quality
- **Follow conventions** - Use established naming and patterns
- **Make it readable** - Code is read more than it's written
- **Keep it simple** - Complex solutions often hide better approaches
- **Document the why** - Comments should explain decisions, not what code does

### Testing Strategy
- **Unit tests** - Test individual components in isolation
- **Integration tests** - Test how components work together
- **End-to-end tests** - Test full workflows
- **Manual testing** - Especially for UI/UX validation

## When Implementation is Complete

You're ready to move to Review & Retrospective when:

- ✅ All requirements are implemented
- ✅ All tests are passing
- ✅ Code quality standards are met
- ✅ Documentation is complete
- ✅ Code review is done and approved
- ✅ Workstream handoffs and integration notes are complete

## Tips

- **Start with the hardest part** - Get risky pieces done first
- **Implement incrementally** - Smaller chunks are easier to test and review
- **Keep refactoring in scope** - Clean code matters
- **Don't optimize prematurely** - But don't ignore obvious inefficiencies
- **Ask for help** - Code review should catch issues and share knowledge

---

**Next**: Move to [Review & Retrospective](./07-review-retrospective.md) once Implementation is complete.
