# Agent Guide Index

Status: agent guidance index

This directory contains detailed instructions that are linked from
`AGENTS.md`. Keep `AGENTS.md` short and route-specific; put implementation
details, trigger examples, required outputs, and review gates in these guide
documents.

Chinese mirror: `README.zh.md`.

## Natural-Language Request Routing

| Request class | Guide | Primary workflow |
| --- | --- | --- |
| Iteration documentation | `natural-language-iteration-documentation-triggers.md` | `docs/iterations/AGENTS.md` |
| Iteration implementation | `natural-language-implementation-triggers.md` | `docs/iterations/AGENTS.md` |
| Product validation | `natural-language-validation-triggers.md` | `docs/testing/product-capability-validation-playbook.md` |
| Test documentation | `natural-language-test-documentation-triggers.md` | `docs/testing/test-documentation-playbook.md` |
| Code review | `natural-language-code-review-triggers.md` | `docs/testing/code-review-playbook.md` |

## Rules

- Natural-language triggers classify user intent; they do not by themselves
  authorize runtime, schema, API, frontend, test, fixture, migration, or external
  repository implementation.
- If a request combines documentation, implementation, validation, or review,
  run the relevant workflow in the order defined by the guide documents.
- Keep claims evidence-bounded. Do not report PASS, closeout, or implementation
  completion from a trigger phrase alone.
