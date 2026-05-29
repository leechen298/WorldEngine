# Contract

Status: planned / ready for review

## Public Concepts

- Independent reviewer: a Codex run that validates evidence directly.
- Unsupported claim: a statement not backed by files read or commands run.
- Blocker: missing dependency, command failure, absent file, or environment
  issue that prevents validation.
- Final recommendation: one of `passed`, `passed with P3`, `blocked`,
  `failed`, or `not executed`.

## Reviewer Inputs

The independent Codex reviewer must inspect:

- `README.md`
- `docs/releases/v0.2.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/scope-boundaries.md`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/`

Missing files must be recorded as blockers or findings.

## Reviewer Requirements

- Do not rely on implementer summaries.
- Read docs and code directly.
- Run available validation commands or record blockers.
- Do not modify code.
- Do not claim unrun tests succeeded.
- Output an independent review.
- Check release claims.
- Check concrete demo-world regression.
- Classify unresolved findings as P1/P2/P3.

## Allowed Changes

This planning package may only define autonomous validation instructions.

## Forbidden Changes

- Do not execute autonomous validation here.
- Do not modify runtime, schema, API, frontend, tests, fixtures, or migrations.
- Do not blur Codex reviewer work with WorldEngine Agent-in-World behavior.

## Compatibility Requirements

The reviewer validates claims against current files and command evidence. It
does not change v0.2 status or implementation.

## Out-of-Scope Follow-Ups

- Fixing findings.
- Running external validation worlds.
- Adding new tests or tooling.
