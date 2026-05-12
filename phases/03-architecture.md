# Phase 3: Architecture

## Purpose

Architecture answers: **How will we build this?** You're designing the system structure, data flow, and technical approach.

This phase focuses on:
- System design and structure
- Technology selection
- Data flow and integration points
- Scalability and reliability considerations
- Technical decision-making

## Key Questions

The Architecture Agent will help you explore:

### System Design
- How will the system be structured?
- What are the major components?
- How do they interact?
- Where's the complexity?

### Technology Decisions
- What tech stack?
- Why these choices?
- What are the tradeoffs?
- Are there alternatives?

### Data & Integration
- How does data flow through the system?
- What integrations are needed?
- What's the data model?
- How is state managed?

### Scalability & Reliability
- How will this scale?
- What are failure points?
- How do we handle errors?
- What's the recovery strategy?

### Deployment & Infrastructure
- How will this be deployed?
- What infrastructure is needed?
- What are the operational concerns?
- How is monitoring/logging set up?

## Outputs

By the end of Architecture, you'll have:

✅ **Architecture Diagram** - Visual representation of system structure
✅ **Technology Decisions** - Tech stack and justification
✅ **Data Flow Diagram** - How data moves through the system
✅ **Component Specifications** - What each component does
✅ **Deployment Plan** - How the system will be deployed
✅ **Design Decisions Document** - Key decisions and tradeoffs

## Architecture Template

See [architecture-template.md](../templates/architecture-template.md) for a detailed template.

## When Architecture is Complete

You're ready to move to Contracts & Tests / CI/CD when:

- ✅ System structure is clear
- ✅ Technology choices are justified
- ✅ Data flow is understood
- ✅ Integration points are identified
- ✅ Team agrees on the approach

## Tips

- **Draw it out** - Diagrams are your friend
- **Justify decisions** - Why this tech? What are the tradeoffs?
- **Think about failure** - What happens when things go wrong?
- **Consider scaling** - Will this work for 10x more users?
- **Get feedback** - Architecture review before implementation is valuable

---

**Next**: Move to [Contracts & Tests / CI/CD](./04-contracts-tests-cicd.md) once Architecture is complete.
