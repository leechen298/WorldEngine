---
name: worldengine-iteration-docs
description: Use when creating, updating, reviewing, or preparing WorldEngine iteration packages, roadmap or governance docs, or documentation-stage review evidence before implementation.
---

# WorldEngine Iteration Docs

Use this skill only inside the WorldEngine repository.

This is the documentation-stage workflow. It prepares reviewable iteration or
governance documents before implementation starts.

## Required Reading

Before drafting or changing iteration-direction work, read as needed:

- `AGENTS.md` or `AGENTS.zh.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`

## Stage Boundary

- Documentation-only requests may update approved documentation scope.
- Code or mixed iteration requests must produce the full package before
  implementation: `README.md`, `intent.md`, `contract.md`,
  `technical-design.md`, `test-plan.md`, `plan.md`, and `review.md`.
- If the user asks to draft documents and implement in the same request, finish
  only the documentation stage and report that implementation waits for review.

## Hard Rules

- Do not modify runtime, schema, API, UI, fixture, migration, or test
  implementation files in this workflow.
- Do not mark code behavior, E2E, UI smoke, Agent smoke, or runtime behavior as
  passed unless that evidence exists from the current session.
- Keep package status honest: proposed or ready-for-review during drafting,
  ready-for-implementation only after the review gate is complete.
- If project direction conflicts with `docs/project-north-star.md`, stop and
  ask for the direction document to be changed first.

## Workflow

1. Check repository state with `git status --short --branch`.
2. Identify the active version and package directory.
3. Classify the work as documentation-only, code, or mixed.
4. Create or update the required package documents for that type.
5. Keep `review.md` in documentation-stage form until implementation actually
   runs.
6. Run documentation checks such as `git diff --check` and targeted searches
   for required terms or status consistency.
7. Report changed documentation, commands run, unrun implementation checks, and
   what must be reviewed before implementation can start.

## Handoff

When the package is reviewed and approved, implementation should use
`worldengine-iteration-dev`, not this skill.
