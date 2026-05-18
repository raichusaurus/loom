# Phase 1: Discovery

**Objective:** Understand the problem space, users, constraints, validation needs, and first useful direction before committing to requirements or architecture.

---

## What is Discovery?

Discovery is about **learning before committing**. It clarifies the problem, current state, stakeholders, constraints, risks, and evidence needed to decide whether the project is worth shaping into requirements.

This phase can name a likely solution shape, but it should not lock in requirements or technical design too early. Use "working shape" to capture the current direction while keeping later phases free to refine it.

**Output:** A clear problem statement, project context, user and stakeholder picture, constraints, validation strategy, key assumptions, risks, and a Requirements handoff.

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

### 5. Define Success and Validation
- What measurable signals show the idea is working?
- What evidence is needed before Requirements?
- How will we validate the idea before investing in polish?
- Which assumptions need proof, and how will we test them?

### 6. Identify Risks, Opportunities, and Process Learning
- What could prevent success?
- What opportunities might emerge?
- What framework, template, or process lessons should Loom carry forward?

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
- ✅ Assumptions, risks, and open questions have validation paths
- ✅ Requirements handoff summarizes the inputs the next phase should pull forward

---

## Common Discovery Mistakes

❌ **Jumping to implementation** - Capture direction, but do not skip requirements and architecture
❌ **Treating working shape as a promise** - Discovery can suggest a path without freezing scope
❌ **Missing the first user** - "Everyone" is not a useful first operator
❌ **Letting nice-to-haves blur the first useful version** - Name what is out of scope early
❌ **Vague validation** - "Seems useful" is not enough evidence for Requirements
❌ **Dropping process lessons** - If the project teaches you about Loom, record it while it is fresh

---

## Next Phase

Once Discovery has enough evidence and a clear handoff, move to **[Requirements](./02-requirements.md)**.
