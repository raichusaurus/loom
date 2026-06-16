# Phase 4: Planning & Decomposition

## Purpose

Planning & Decomposition answers: **How will we divide, sequence, and coordinate the work?** This is the phase where the architecture becomes an executable plan for humans and agents.

This phase is especially important for agentic workflows. Agents work best when they have clear ownership, bounded context, explicit handoffs, and known integration points.

This phase focuses on:
- Pulling forward Architecture handoff inputs before decomposing work
- Breaking the project into workstreams, subprojects, services, or features
- Defining ownership boundaries for humans and agents
- Identifying dependencies and sequencing
- Deciding what can happen in parallel
- Creating context packets for each workstream
- Establishing integration checkpoints and handoff expectations
- Identifying contract and test candidates for the next phase

## Key Questions

The Planning Agent will help you explore:

### Work Breakdown
- What did Architecture say Planning should build?
- What are the major workstreams?
- Which services, features, or modules need their own scoped plan?
- What is the smallest useful implementation slice?
- What can be deferred without blocking the core outcome?
- Which architecture decisions must Planning not reopen without new evidence?

### Ownership & Boundaries
- Who owns each workstream?
- Which agent or person is responsible for each service, module, or feature?
- What files, directories, APIs, or systems are inside each owner's scope?
- What Loom progress docs, source paths, and test paths belong to each owner?
- Which child progress docs should already exist before Contracts & Tests starts?
- Where might ownership overlap?

### Dependencies & Sequencing
- What must be built first?
- Which tasks depend on contracts, schemas, designs, or external systems?
- What is on the critical path?
- What can safely happen in parallel?

### Context Packets
- What does each agent need to know before starting?
- Which requirements, architecture decisions, constraints, and risks apply?
- What assumptions should the agent preserve or validate?
- What output should the agent return when finished?

### Integration Strategy
- When do we bring parallel work back together?
- What integration tests or manual checks prove the pieces work together?
- How do we resolve conflicts between planned design and implementation reality?
- What is the escalation path when an agent discovers a blocker?
- Which behaviors, schemas, interfaces, commands, or workflows should become contract/test candidates?

## Outputs

By the end of Planning & Decomposition, you'll have:

✅ **Work Breakdown** - Major workstreams, features, services, and implementation slices  
✅ **Ownership Map** - Clear responsibility boundaries for humans and agents  
✅ **Mirrored Tree Plan** - Progress docs, source paths, and test paths aligned by scope
✅ **Progress Drilldown Ownership** - Owners for each child progress doc and mirrored code/test area
✅ **Dependency Graph** - What blocks what, and what can run in parallel  
✅ **Context Packets** - Scoped briefs for each agent or subproject  
✅ **Integration Plan** - Checkpoints for merging, testing, and reconciling work  
✅ **Contract/Test Candidates** - Behaviors and interfaces to carry into Contracts & Tests
✅ **Delivery Plan** - Initial milestone order and release strategy  
✅ **Update Policy** - When Planning must change because architecture, contracts, ownership, or implementation reality changed
✅ **Open Decision Packets** - Remaining planning questions framed with options, trade-offs, and recommendations

## Recursive Scope

Loom can be applied recursively. A project may run one top-level Loom cycle while individual services, features, or subprojects run smaller scoped Loom cycles beneath it.

Common scopes:
- **Project-level Loom** - Overall product or system
- **Service-level Loom** - API service, worker, frontend app, data pipeline, or integration
- **Feature-level Loom** - A bounded feature inside an existing system
- **Task-level mini-Loom** - A compressed cycle for small changes

Use the full phase sequence when scope, risk, or coordination complexity is high. Compress phases when the work is small and the context is already clear.

## Initial Waterfall, Then Agile

The first pass through Loom is intentionally more waterfall-style. Early projects need a stable shared understanding before agents can safely work in parallel.

After the initial implementation, Loom should become more iterative:
- Discovery and Requirements become lighter for known problem areas
- Architecture evolves through decision records and targeted reviews
- Planning & Decomposition happens per milestone, service, or feature
- Contracts and tests are updated continuously as behavior changes
- Implementation proceeds in smaller slices
- Review and retrospective feed directly into the next cycle

Think of the first Loom cycle as establishing the foundation. Later cycles should feel more agile: smaller, faster, recursive, and guided by what the team learned.

## When This Phase is Complete

You're ready to move to Contracts & Tests when:

- ✅ Workstreams are clearly defined
- ✅ Ownership boundaries are explicit
- ✅ Progress docs, source paths, and test paths are mapped for each owned scope
- ✅ Known child progress docs are created or explicitly marked as pending with owner and reason
- ✅ Dependencies and critical path are understood
- ✅ Parallel work is identified
- ✅ Context packets are ready for agents or contributors
- ✅ Integration checkpoints are planned
- ✅ Open questions that need user decisions include summaries, options, trade-offs, and recommendations
- ✅ Contract and test candidates are ready for Contracts & Tests
- ✅ The delivery sequence is clear enough to begin contract and test design

## Tips

- **Name the boundaries** - Ambiguous ownership creates duplicated work and integration pain
- **Plan for parallelism** - Agentic workflows benefit when independent work is identified early
- **Keep context packets small** - Give agents enough context to succeed, not the whole universe
- **Expect feedback loops** - Implementation may reveal that the plan, architecture, or requirements need adjustment
- **Use recursion deliberately** - A subproject or service can run its own mini-Loom cycle when it has enough complexity

---

**Next**: Move to [Contracts & Tests](./05-contracts-tests.md) once Planning & Decomposition is complete.
