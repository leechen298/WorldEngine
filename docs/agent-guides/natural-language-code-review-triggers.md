# Natural-Language Code Review Triggers

Status: reusable agent routing guide

Chinese mirror: `natural-language-code-review-triggers.zh.md`.

Use this guide when a user makes a short code-review request such as:

```text
审核 <version> 代码
review <version> code
审核 <iteration-package> 代码
代码审核 <feature-or-package>
```

## Primary Workflow

Run `docs/testing/code-review-playbook.md`.

This trigger is separate from final closeout, validation, and test-documentation
triggers. It reviews implementation reliability against the active contracts.
It does not by itself claim product validation has passed or tests have run.

## Required Reading

Before reporting a result:

- read the active version or package state.
- read `CURRENT_STATE.md`, `GOAL_RUNNER.md`, `CAMPAIGN_PLAN.md`, version plan,
  and code-bearing child package documents when they exist.
- map implementation files from package `review.md`, contracts, test plans, and
  current git state.
- do not treat final-closeout status as a substitute for code review.

## Review Scope

Inspect the implementation surfaces in scope for the reviewed version, package,
feature, or current implementation surface:

- runtime code.
- schemas.
- API routes.
- frontend surfaces.
- tests.
- checkers.
- fixtures.
- compatibility boundaries.
- evidence and artifact rules when implementation affects them.

## Subagents And Verification

Use a code-review subagent/evaluator when available and authorized, including
Superpowers code-review workflows where applicable.

Run focused commands only when needed to verify a finding or claim. Otherwise
state which tests were not run and why.

## Findings-First Output

Report findings first, ordered by severity:

- P0.
- P1.
- P2.
- P3.

Each finding should include:

- file and line reference.
- scope assessment.
- evidence gap or behavioral risk.
- why it matters.
- whether tests were run to verify it.

Keep summaries secondary. If no issues are found, say that clearly and list
remaining test gaps or residual risks.

## Repair Boundary

If the code review discovers issues that require implementation changes, do not
silently repair them inside a review-only request.

Before changing runtime, schema, API, frontend, test, fixture, migration, or
durable evidence behavior, create or use the required iteration package and
obtain the appropriate implementation authorization.
