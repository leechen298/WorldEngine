# Contract

## Public Concepts

- Independent review: reviewer reads source docs and code directly.
- Evidence-bearing command: a command run in the review session and recorded
  with result or blocker.
- Unsupported claim: a statement that is not supported by current evidence or
  conflicts with actual code behavior.
- Final recommendation: one of the allowed outcomes in the review template.

## Allowed Changes

During future execution, this package may:

- Fill `codex-autonomous-review.md`.
- Update `review.md`.
- Record files read, commands run, blockers, unsupported claims, findings, and
  recommendation.

## Forbidden Changes

- Do not modify implementation code.
- Do not modify tests.
- Do not modify runtime, schema, API, frontend, fixtures, migrations, or
  external repositories.
- Do not add demo-world details, UI selectors, seed data, or private oracle
  details.
- Do not repair findings in this package.
- Do not change v0.3 release status.
- Do not claim unrun commands succeeded.

## Compatibility Requirements

The future review must check:

- WorldSpec loader findings.
- runtime context bridge findings.
- API / schema / runtime compatibility findings.
- Event.refs compatibility findings.
- concrete demo-world regression check.
- unsupported claims.
- unresolved P1/P2/P3.

## Out-Of-Scope Follow-Ups

Final synthesis belongs to `05`. Any repair belongs to a future reviewed
repair package.
