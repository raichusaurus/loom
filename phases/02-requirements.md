# Phase 2: Requirements

**Objective:** Translate Discovery into clear, testable scope: what must be built, what should wait, how success will be validated, and what Architecture must decide next.

---

## What is Requirements?

Requirements answer: **What exactly needs to be built, and how will we know it is useful?**

This phase should pull forward Discovery context before inventing new scope. It turns the core problem, primary user/operator, first useful version, validation signals, and open questions into a bounded product or system specification.

**Output:** Discovery inputs, solution vision, MVP scope, user stories, prioritized features, output surfaces, relevant non-functional requirements, acceptance tests, validation signals, risks, assumptions, and Architecture inputs.

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
- What user stories describe the necessary behavior?
- What acceptance criteria prove each story works?
- Which features are Must, Should, Could, or Won't for the MVP?
- Where will users, operators, or downstream systems see outputs?
- What source facts, stable identifiers, or data fidelity constraints must be preserved?

### 4. Establish Non-Functional Requirements
- What performance, scalability, reliability, security, accessibility, or cost constraints matter?
- Which constraints are real MVP requirements versus future concerns?
- What external dependencies, assumptions, or prior-art decisions affect scope?

### 5. Define Acceptance and Validation
- What Given/When/Then acceptance tests should Contracts & Tests inherit?
- What measurable goals define done?
- What evidence proves the requirements are useful, not merely implemented?
- Where do outputs need provenance, confidence, sample size, comparison, or traceability?

### 6. Hand Decisions to Architecture
- Which decisions did Requirements surface but should not resolve?
- What tradeoffs should Architecture explore?
- Which prior-art or legacy reuse decisions need technical judgment?
- What requirements changed during later phases, and what did they supersede?
- Which coarse workstreams, surfaces, services, or components should Progress track now, even if source/test paths are still `TBD`?

---

## Requirements Template

Use [requirements-template.md](../templates/requirements-template.md) to structure your requirements and create the Architecture handoff.

---

## Success Criteria for Requirements

Before moving to Architecture, validate:

- ✅ Discovery inputs are pulled forward and reflected in scope
- ✅ MVP, in-scope work, out-of-scope work, and optional/deferred work are explicit
- ✅ User stories have testable acceptance criteria
- ✅ Features use a consistent priority scale
- ✅ Output surfaces and data fidelity needs are captured where relevant
- ✅ Non-functional requirements are specific enough to guide design
- ✅ Acceptance tests and validation signals are measurable
- ✅ Dependencies, assumptions, risks, and prior-art inputs are documented
- ✅ Architecture inputs name unresolved technical decisions without prematurely solving them
- ✅ Open questions that need user decisions include summaries, options, trade-offs, and recommendations
- ✅ Coarse progress scopes are identified for obvious workstreams, surfaces, integrations, or service candidates
- ✅ Loom process feedback is captured or explicitly marked not applicable
- ✅ Phase gate separates agent recommendation, owner decision, decision date, and remaining concerns

---

## Common Requirements Mistakes

❌ **Rewriting Discovery instead of using it** - Pull the handoff forward before expanding scope
❌ **Scope creep by politeness** - Use Optional / Not Needed Yet to protect the MVP
❌ **Vague acceptance criteria** - "It should be fast" is not testable
❌ **Hiding output expectations** - If someone consumes a result, define the surface
❌ **Inventing data** - State what must be preserved, derived, nullable, or unknown
❌ **Solving architecture too early** - Requirements should frame decisions Architecture must make

---

## Next Phase

Once Requirements are complete, Architecture inputs are clear, and the owner approves the gate, move to **[Architecture](./03-architecture.md)**.
