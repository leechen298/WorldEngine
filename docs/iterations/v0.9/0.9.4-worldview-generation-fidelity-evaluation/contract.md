# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`WorldviewFidelityScorecard`

- Public summary for one generated world.
- Reports `final_status` as `pass`, `fail`, `blocked`, or `not_run`.
- Includes immediate generation fidelity and bounded-run fidelity sections.
- Must include redaction flags and public failure categories.

`ImmediateWorldviewFidelityArtifact`

- Evaluates the generated public world model against the public premise.
- Checks premise coverage through public tokens, public digest tags, generated
  public model summaries, world creation metadata, and rule summary references.
- Fails or blocks deterministic generic fallback and non-digestible output.

`BoundedRunWorldviewFidelityArtifact`

- Evaluates public runtime summaries when supplied by a later bounded run.
- Reports `blocked` when bounded runtime evidence is missing or not supported.
- Must not run ticks, call providers, or mutate canonical state.

`WorldviewContradiction`

- Public taxonomy item for evidence that contradicts the premise or generated
  boundaries. Categories include `missing_premise`, `generic_fallback`,
  `runtime_contradiction`, `rule_contradiction`, `redaction`, `evidence_gap`,
  and `checker_gap`.

## Allowed Changes

- Additive schema models in `backend/app/schemas/world_generation.py`.
- A deterministic helper in `backend/app/core/worldview_fidelity.py`.
- Focused backend tests in `backend/app/tests/test_worldview_fidelity_evaluation.py`.
- Package-local documentation and review updates under this package directory.
- Parent v0.9 status updates only after package implementation is complete.

## Forbidden Changes

- No provider live calls.
- No raw prompt, raw provider request, raw provider response, provider trace,
  authorization header, API key, private evaluator oracle, private Agent memory,
  raw thought, chain-of-thought, hidden context, or private goal evidence.
- No concrete validation-world fixture data in core repository files.
- No changes under `backend/worldengine/`.
- No frontend dashboard, Validation Client, external repository, migration, or
  deployment changes.
- No bounded runtime control implementation.
- No rule-linked parameter evolution or event legality implementation.
- No subjective PASS based on a human or Agent impression.
- No claim that deterministic fallback is LLM-backed or provider-backed.

## Compatibility Requirements

- Existing `/world/generation/worldview`, `/worlds`, `/world/params`, provider
  readiness, and rule-parameter validation behavior must remain compatible.
- Schema changes must be additive and must forbid unexpected private fields
  where the new models accept public evidence.
- Fidelity helpers must be pure functions over supplied public evidence. They
  must not mutate world state, runtime stores, environment variables, provider
  config, or existing response objects.
- Existing tests for 0.9.1, 0.9.2, and 0.9.3 must continue to pass.

## Out-of-scope Follow-ups

- `0.9.5`: bounded runtime control and run budgets.
- `0.9.6`: natural-language world direction semantics.
- `0.9.7`: rule-linked evolution and event legality.
- `0.9.8`: Agent continuity and consolidation evidence.
- `0.9.10`: checker fixtures and scorecard support for the full LLM-backed
  autonomous scenario.
- `0.9.12`: live or explicitly blocked full lifecycle validation evidence.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove faithful output, missing premise output, generic fallback,
  contradictory runtime output, missing bounded-run evidence, and redaction
  failure handling.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.

