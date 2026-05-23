# Intent

## Problem

WorldEngine already has repository-owned skills for deterministic E2E and Agent
smoke execution:

- `worldengine-e2e-runner`
- `worldengine-agent-smoke-runner`

The project does not yet have repository-owned skills for the two upstream
workflow stages:

- writing and reviewing iteration documentation before implementation.
- implementing code only after the iteration package has been reviewed.

Without those project-local skills, an AI coding agent can still blur the
documentation stage and implementation stage, even though root guidance now
requires a two-stage gate.

## Outcome

Add a complete WorldEngine workflow skill set:

1. `worldengine-iteration-docs`
   Documentation-stage workflow for drafting or updating iteration packages,
   governance docs, roadmap docs, and package review evidence.
2. `worldengine-iteration-dev`
   Implementation-stage workflow for code or mixed packages. It reads approved
   iteration documents, implements narrowly, runs the listed verification, and
   does not create, repair, rewrite, or delete iteration documents.
3. `worldengine-e2e-runner`
   Existing deterministic browser E2E execution skill.
4. `worldengine-agent-smoke-runner`
   Existing basic Agent smoke execution and validation skill. This is only a
   lightweight autonomous operation check, not full Agent autonomous testing.
5. `worldengine-agent-autonomous-test-runner`
   Broader Agent autonomous test execution workflow for future scenario suites,
   scorecards, live autonomous runs, or multi-step evidence packages. If the
   required protocol or scenario docs do not exist, it must stop and report the
   missing test contract instead of treating Agent smoke as full coverage.

The result should be repository-owned, loaded from the project workspace, and
explicitly aligned with `AGENTS.md`, `CLAUDE.md`, `docs/iterations/README.md`,
and the WorldEngine north star. WorldEngine skills should not be duplicated
into personal skills by default.

## Non-Goals

- Do not create a plugin package in this iteration.
- Do not integrate with an MCP server, marketplace, hook system, or app.
- Do not change backend runtime behavior, frontend behavior, API semantics,
  schemas, fixtures, or product capability.
- Do not weaken existing E2E or Agent smoke evidence rules.
- Do not claim full Agent autonomous test coverage when only Agent smoke ran.
- Do not make Superpowers a dependency of WorldEngine workflow execution.
