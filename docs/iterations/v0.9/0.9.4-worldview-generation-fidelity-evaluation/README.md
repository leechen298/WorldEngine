# 0.9.4 Worldview Generation Fidelity Evaluation

Chinese mirror: `README.zh.md`.

Status: implementation complete / non-live focused verification passed
Type: mixed validation/implementation package

## Goal

Define and implement deterministic public fidelity evaluation for generated
worldview output. The evaluator must decide whether a generated world remains
faithful to the user's public premise immediately after generation and, when
bounded runtime evidence is available, whether later public runtime behavior
contradicts that premise.

## Scope

This package may add public schemas, deterministic backend helpers, focused
tests, and package-local review evidence for:

- immediate premise coverage evaluation.
- deterministic generic fallback detection in fidelity scoring.
- public contradiction taxonomy.
- optional bounded-run consistency evaluation from already-public runtime
  summaries.
- PASS / FAIL / BLOCKED scorecard output that does not mutate world state.

`0.9.4` may classify run-based fidelity as `blocked` when bounded runtime
controls or run evidence are unavailable. It must not implement those controls;
that belongs to `0.9.5`.

## Deliverables

- Public fidelity schema additions in the active backend schema path.
- Deterministic fidelity evaluation helper in `backend/app/core/`.
- Focused backend tests for faithful output, missing premise coverage,
  contradictory runtime evidence, missing bounded-run evidence, generic
  fallback, and redaction failures.
- Review evidence recording changed files, commands, compatibility, scope, and
  subagent findings.

## Current Authorization

Documentation drafting is authorized by the parent v0.9 route.
Implementation is not authorized until this package review flips
`implementation_authorized` from `no` to `yes` after documentation/contract
review.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, and bounded runtime control
implementation are not authorized by this draft.

## Final Assessment State

Implementation complete for the reviewed non-live scope. Focused fidelity tests,
related v0.9 regression, backend regression, and documentation checks passed in
the current session.
