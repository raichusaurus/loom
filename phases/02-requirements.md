# Phase 2: Requirements

**Objective:** Translate Discovery into clear, testable scope: what must be built, what should wait, how success will be validated, and what Architecture must decide next.

---

## What is Requirements?

Requirements answer: **What exactly needs to be built, and how will we know it is useful?**

This phase should pull forward Discovery context before inventing new scope. It turns the core problem, primary user/operator, first useful version, validation signals, and open questions into a bounded product or system specification.

**Output:** Discovery inputs, solution vision, bounded MVP scope, stable requirement and acceptance IDs, ranked quality attributes, output surfaces, validation signals, risks, assumptions, and traceable Architecture inputs.

---

## Key Activities

### 1. Pull Forward Discovery Inputs
- What is the core problem?
- Who is the primary user or operator?
- Who might use this later?
- What was the working shape from Discovery?
- What is the first useful version?
- What was explicitly out of scope?
- Which validation signals and open questions carry forward?

### 2. Define Scope and MVP Boundaries
- What is definitely in scope?
- What is explicitly out of scope?
- What is the smallest version that solves the core problem?
- Which later phases or releases are worth naming?
- Which tempting ideas are optional, deferred, or unnecessary for now?

### 3. Define Functional Requirements
- What observable requirements describe the necessary behavior for each actor or surface?
- What acceptance criteria prove each requirement works?
- Which stable IDs let later decisions, contracts, tests, and validation cite each material requirement?
- Which features are Must, Should, Could, or Won't for the MVP?
- Where will users, operators, or downstream systems see outputs?
- What source facts, stable identifiers, or data fidelity constraints must be preserved?

### 4. Rank Quality Attributes and Constraints
- Which performance, scalability, reliability, security, privacy, accessibility, compatibility, recovery, operability, or cost attributes can change the design?
- How are the material attributes ranked when they conflict?
- What scenario, load condition, measurable target, or defensible bound defines each one?
- Is the target measured, sourced, derived, assumed, or still unknown, and with what confidence?
- Which constraints are real MVP requirements versus future concerns?

### 5. Define Acceptance and Validation
- What acceptance scenarios or criteria should Contracts & Tests turn into executable evidence?
- Which requirement and acceptance IDs does each scenario trace to?
- What measurable goals define done?
- What evidence proves the requirements are useful, not merely implemented?
- Where do outputs need provenance, confidence, sample size, comparison, or traceability?

### 6. Hand Decisions to Architecture
- Which decisions did Requirements surface but should not resolve?
- What tradeoffs should Architecture explore?
- Which prior-art or legacy reuse decisions need technical judgment?
- What requirements changed during later phases, and what did they supersede?
- Which coarse workstreams, surfaces, services, or components should Progress track now, even if source/test paths are still `TBD`?
- How does each open architecture decision trace to a requirement, quality attribute, constraint, assumption, or risk?

---

## Requirements Template

Use [requirements-template.md](../templates/requirements-template.md) to structure your requirements and create the Architecture handoff.

---

## Success Criteria for Requirements

Before moving to Architecture, validate:

- ✅ Discovery inputs are pulled forward and reflected in scope
- ✅ MVP, in-scope work, out-of-scope work, and optional/deferred work are explicit
- ✅ Observable requirements have testable acceptance criteria
- ✅ Material requirements, quality attributes, compatibility constraints, and acceptance criteria have stable IDs
- ✅ Features use a consistent priority scale
- ✅ Output surfaces and data fidelity needs are captured where relevant
- ✅ Consequential quality attributes are ranked, bounded, sourced, and explicit about tradeoffs
- ✅ Acceptance criteria, scenarios, and validation signals trace to the requirements they prove
- ✅ Dependencies, assumptions, risks, and prior-art inputs are documented
- ✅ Architecture inputs name unresolved technical decisions without prematurely solving them
- ✅ Open questions that need user decisions include summaries, options, trade-offs, and recommendations
- ✅ Coarse progress scopes are identified for obvious workstreams, surfaces, integrations, or service candidates
- ✅ Phase gate separates agent recommendation, owner decision, decision date, and remaining concerns

---

## Common Requirements Mistakes

❌ **Rewriting Discovery instead of using it** - Pull the handoff forward before expanding scope
❌ **Scope creep by politeness** - Use Optional / Not Needed Yet to protect the MVP
❌ **Vague acceptance criteria** - "It should be fast" is not testable
❌ **Hiding output expectations** - If someone consumes a result, define the surface
❌ **Inventing data** - State what must be preserved, derived, nullable, or unknown
❌ **Solving architecture too early** - Requirements should frame decisions Architecture must make
❌ **Generic quality checklists** - Keep only attributes that can affect a decision and state their rank, scenario, source, and bound
❌ **False precision** - Do not turn an unsupported guess into an authoritative-looking target

## Loom Process Feedback

Record only a phase-local observation when Requirements exposes material Loom friction. Put any reusable evidence-backed candidate in `docs/loom/pilot-feedback.md`. A clean phase needs no feedback note.

---

## Next Phase

Once Requirements are complete, Architecture inputs are clear, and the owner approves the gate, move to **[Architecture](./03-architecture.md)**.
