# Contract

Status: not executed

## Public Concepts

- Independent review: the output produced by a separate Codex validation run.
- Review verification: checking whether the independent review actually read
  required files, ran commands or recorded blockers, checked release claims,
  and classified findings.
- Unsupported claim: a statement not backed by cited file reads or command
  evidence.

## Allowed Changes

During a later execution pass, update:

- `codex-autonomous-review.md`
- `review.md`

Only update broader validation summaries after the final bundle step.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  migrations.
- Do not accept a review that only repeats summaries.
- Do not accept a review that omits blockers for unrun commands.
- Do not accept unsupported success claims.

## Review Quality Checks

The execution review must check whether the independent review:

- read necessary files.
- ran commands or recorded blockers.
- checked release claims.
- checked concrete demo-world regression.
- classified P1/P2/P3.
- listed unsupported claims.

If the independent review only restates documentation, does not run tests, and
does not record blockers, classify the result as `blocked`.

## Compatibility Requirements

The autonomous execution package validates evidence only. It does not change
v0.2 release status or implementation.

## Out-of-Scope Follow-Ups

- Fixing findings.
- Rerunning E2E / API smoke unless explicitly part of the independent review.
- Creating external validation repositories.
