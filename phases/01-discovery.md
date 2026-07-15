# Phase 1: Discovery

**Objective:** Understand the problem space, users, current-state evidence, constraints, validation needs, and first useful direction before committing to requirements or architecture.

---

## What is Discovery?

Discovery is about **learning before committing**. It clarifies the problem, current state, stakeholders, constraints, risks, and evidence needed to decide whether the project is worth shaping into requirements.

This phase can name a likely solution shape, but it should not lock in requirements or technical design too early. Use "working shape" to capture the current direction while keeping later phases free to refine it.

**Output:** A clear problem statement, project context, user and stakeholder picture, evidence and uncertainty inventory, constraints, validation strategy, key assumptions, risks, and a Requirements handoff.

---

## Key Activities

### 1. Define the Problem
- What core problem are we solving?
- Why does it matter?
- How is it solved today?
- What's working, broken, missing, or too costly in the current state?

### 2. Capture Project Context
- Is this a new build, rewrite, migration, continuation, experiment, or something else?
- What prior art or existing systems should be kept, discarded, or rethought?
- What is the likely working shape of the solution?
- What is the first useful version?
- What is explicitly out of scope for that first version?

### 3. Identify Users, Stakeholders, and Decision Owners
- Who is the primary user or operator this must work for first?
- Who might become a future or external user?
- Who benefits, influences decisions, contributes, or is affected?
- Who has final say on whether to proceed?

### 4. Document Context and Constraints
- Timeline and urgency
- Budget, team, infrastructure, and available resources
- Existing systems, technology constraints, and scale expectations
- Compliance, organizational policy, and dependency constraints
- For rewrites or migrations, the current path, pain point, affected owners, and contracts, data, or behavior that may need compatibility
- Source and confidence for any constraint that could materially change scope or design

### 5. Define Success and Validation
- What measurable signals show the idea is working?
- What evidence is needed before Requirements?
- How will we validate the idea before investing in polish?
- Which assumptions need proof, and how will we test them?

### 6. Identify Risks, Opportunities, and Process Learning
- What could prevent success?
- What opportunities might emerge?
- Which statements are measured or sourced facts, inferences, assumptions, unknowns, or conflicts?
- Who will validate each material assumption or risk, by what decision point?
- Did Loom expose material process friction worth recording? If not, add no feedback entry.

---

## Discovery Template

Use [discovery-template.md](../templates/discovery-template.md) to capture findings and produce the Requirements handoff.

---

## Success Criteria for Discovery

Before moving to Requirements, validate:

- ✅ Core problem, current state, and why it matters are clear
- ✅ Project type and meaningful prior art are documented
- ✅ Primary user/operator, future users, stakeholders, and decision owner are identified
- ✅ Working shape and first useful version are named without over-committing
- ✅ Explicit out-of-scope items are captured
- ✅ Constraints and dependencies are explicit
- ✅ Success metrics and validation strategy are measurable enough for Requirements
- ✅ Material facts, inferences, assumptions, unknowns, and conflicts are distinguished
- ✅ Material assumptions, risks, and open questions have validation owners and decision points
- ✅ Open questions that need user decisions include summaries, options, trade-offs, and recommendations
- ✅ Requirements handoff summarizes the inputs the next phase should pull forward
- ✅ Phase gate separates agent recommendation from owner approval

---

## Common Discovery Mistakes

❌ **Jumping to implementation** - Capture direction, but do not skip requirements and architecture
❌ **Treating working shape as a promise** - Discovery can suggest a path without freezing scope
❌ **Missing the first user** - "Everyone" is not a useful first operator
❌ **Letting nice-to-haves blur the first useful version** - Name what is out of scope early
❌ **Vague validation** - "Seems useful" is not enough evidence for Requirements
❌ **Treating assumptions as facts** - Label confidence and define how consequential uncertainty will be resolved
❌ **Turning Discovery into architecture** - Capture decision drivers without selecting topology or technology prematurely

## Loom Process Feedback

Record a phase-local observation only when Discovery exposed material Loom friction, a missing guardrail, a repeated workaround, or unnecessary ceremony. Put reusable candidates with evidence in `docs/loom/pilot-feedback.md`.

---

## Next Phase

Once Discovery has enough evidence, a clear handoff, and owner approval, move to **[Requirements](./02-requirements.md)**.
