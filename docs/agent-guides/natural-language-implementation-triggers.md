# Natural-Language Implementation Triggers

Status: reusable agent routing guide

Chinese mirror: `natural-language-implementation-triggers.zh.md`.

Use this guide when a user makes a short implementation or completion request
such as:

```text
完成 <iteration-package>
实现 <iteration-package>
开发 <iteration-package>
complete <iteration-package>
implement <iteration-package>
develop <iteration-package>
```

## Primary Workflow

Run `docs/iterations/AGENTS.md`, then locate the named package under
`docs/iterations/**/<iteration-package>/`.

This trigger starts the iteration-package gate. It does not by itself authorize
runtime, schema, API, frontend, test, fixture, migration, or external repository
changes.

## Required Reading

Before planning or executing:

- read `AGENTS.md`.
- read `docs/iterations/README.md`.
- read `docs/iterations/AGENTS.md`.
- locate the matching package under `docs/iterations/**/<iteration-package>/`.
- if the package contains `README.md`, `GOAL_RUNNER.md`, `CURRENT_STATE.md`, or
  `CAMPAIGN_PLAN.md`, read those files before planning or executing.
- for implementation, read the package documents in order: `intent.md`,
  `contract.md`, `technical-design.md`, `test-plan.md`, `plan.md`, and
  `review.md`.

## Gate Rules

If the required iteration package or reviewed implementation-stage documents do
not exist, stop at the documentation stage and prepare the missing package
documents for review.

If implementation reveals a design gap, stop implementation, update the
relevant package documents, and resume only after the updated contract, design,
test plan, or execution plan is reviewed.

Keep implementation scoped to the active package. Do not implement adjacent
versions or convenient follow-on capabilities.
