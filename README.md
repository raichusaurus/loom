# Loom

A step-by-step workflow framework and orchestration system for building projects with clear separation of responsibilities between agents.

## Overview

Loom is a structured methodology for project development that guides you through each phase with dedicated agents handling specific responsibilities. The framework ensures consistency, clarity, and quality across all projects.

## The Loom Framework

The framework consists of **7 core phases**:

1. **[Discovery](./phases/01-discovery.md)** - Explore the problem space, gather context, identify stakeholders and constraints
2. **[Requirements](./phases/02-requirements.md)** - Define what needs to be built, success criteria, and scope boundaries
3. **[Architecture](./phases/03-architecture.md)** - Design the system structure, data flow, and technical approach
4. **[Planning & Decomposition](./phases/04-planning-decomposition.md)** - Break the work into owned streams, context packets, dependencies, and integration checkpoints
5. **[Contracts & Tests / CI/CD](./phases/05-contracts-tests-cicd.md)** - Define interfaces, write tests, and set up automated pipelines
6. **[Implementation](./phases/06-implementation.md)** - Build the actual services and features
7. **[Review & Retrospective](./phases/07-review-retrospective.md)** - Evaluate the outcome, document learnings, and plan improvements

The first Loom pass is usually more waterfall-style, especially for a new project: establish the shared foundation before parallelizing heavily. Once the foundation exists, Loom becomes more agile and recursive: services, features, and subprojects can run smaller Loom cycles inside the larger project cycle.

## The Orchestration Agent

The **Orchestrator** is your guide throughout the Loom process. It works directly with you to:

- Walk you through each phase sequentially
- Answer questions and provide guidance
- Kick off specialized agents for specific phases
- Track progress and maintain context
- Facilitate transitions between phases

See [ORCHESTRATOR.md](./ORCHESTRATOR.md) for detailed information.

## Project Structure

```
loom/
├── README.md (this file)
├── FRAMEWORK.md (framework philosophy and principles)
├── ORCHESTRATOR.md (orchestration agent documentation)
├── phases/
│   ├── 01-discovery.md
│   ├── 02-requirements.md
│   ├── 03-architecture.md
│   ├── 04-planning-decomposition.md
│   ├── 05-contracts-tests-cicd.md
│   ├── 06-implementation.md
│   └── 07-review-retrospective.md
├── agents/
│   ├── orchestrator/ (main orchestration agent)
│   ├── discovery/ (discovery phase specialist)
│   ├── requirements/ (requirements phase specialist)
│   ├── architecture/ (architecture phase specialist)
│   ├── planning/ (planning & decomposition specialist)
│   ├── contracts-tests-cicd/ (testing & CI/CD specialist)
│   ├── implementation/ (implementation phase specialist)
│   └── review/ (review & retrospective specialist)
└── templates/
    ├── discovery-template.md
    ├── requirements-template.md
    ├── architecture-template.md
    ├── planning-template.md
    ├── contracts-tests-template.md
    ├── implementation-template.md
    └── retrospective-template.md
```

## How to Use Loom

### For a New Project

1. **Start the Orchestrator** - Tell the orchestration agent you're starting a new project
2. **Follow the phases** - Move through each phase sequentially
3. **Specialized agents assist** - Phase-specific agents provide deeper guidance and expertise
4. **Documents are created** - Templates and outputs are generated as you progress
5. **Complete the cycle** - Finish with review and retrospective

### For Existing Projects

You can jump into any phase in the framework if your project is already underway. The Orchestrator will help you catch up.

## Key Principles

- **Clear Separation of Concerns** - Each phase has distinct responsibilities
- **Guided Progress** - The Orchestrator keeps you moving forward
- **Documentation First** - Decisions and reasoning are captured at each stage
- **Testability** - Contracts and tests are defined before implementation
- **Continuous Improvement** - Retrospectives inform future projects

---

**Ready to get started?** Ask the Orchestrator to begin!
