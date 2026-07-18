# Contract

Chinese mirror: `contract.zh.md`.

## Final Classification Rule

Final closeout must be one of:

- `PASS`: complete current external evidence exists and passes checker,
  scorecard, and read-only evaluator review.
- `PARTIAL`: WorldEngine-side capabilities and deterministic checker evidence
  are present, but fresh external validation evidence is missing or incomplete.
- `BLOCKED`: required provider/client/checker/environment capability prevents
  meaningful current validation.
- `FAIL`: current evidence proves a blocking product or contract failure.

Given `0.12.5`, this package must close as `PARTIAL` unless new current external
result evidence appears and is checked before closeout.

## Allowed Changes

- Closeout docs.
- Roadmap status update.
- Parent v0.12 status/review update.
- Documentation verification commands.

## Forbidden Changes

- No runtime, API, schema, frontend, checker, fixture, provider, or Validation
  Client implementation changes.
- No provider live-call.
- No external validation execution.
- No MVP PASS without current external result evidence.

## Required Evidence

- package status summary for v0.10, v0.11, and v0.12.
- `0.12.5` PARTIAL/BLOCKED evidence.
- commands run for closeout verification.
- commands not run and rationale.
- known gaps and next owner.
