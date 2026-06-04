# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `Public director guidance explanation`: a public-facing status sentence that
  says director guidance was accepted as external/world-environment guidance
  without naming private or internal WorldEngine markers.
- `Public evidence marker`: any marker rejected by the autonomous checker or
  external evidence redaction pipeline, including `api_key`, `apikey`,
  `authorization`, `credential`, `hidden_context`, `private_prompt`,
  `provider_secret`, `raw_request`, `raw_response`, `self_state`, and
  equivalent private Agent internals.
- `Direct API operation-log rejection`: full lifecycle operation logs must not
  record direct API calls as Agent operations. Public API evidence belongs in
  `api-summary.json`.

## Allowed Changes

Implementation may modify only these WorldEngine files and surfaces:

```text
backend/app/api/routes/world.py
backend/app/tests/test_public_handoff_contract_api.py
tools/testing/validate_agent_autonomous_result.py
tools/testing/test_validate_agent_autonomous_result.py
docs/iterations/v0.8/0.8.9.2-director-guidance-public-redaction-repair/
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
docs/testing/results/2026-06-04-worldengine-full-lifecycle-validation.md
docs/testing/results/2026-06-04-worldengine-full-lifecycle-validation.zh.md
```

The testing tool files may change only if current tests or checker behavior do
not already prove direct API operation-log rejection for the full lifecycle
scenario.

## Forbidden Changes

- Do not modify `backend/worldengine/`.
- Do not modify the Validation Client repository.
- Do not modify frontend code.
- Do not modify provider credential storage or add live provider calls.
- Do not add concrete demo-world content, validation-world seed data, private
  validation oracle logic, app-specific backend behavior, maps, characters,
  locations, resources, or story rules.
- Do not relax redaction, evidence integrity, or operation-log rules to make a
  failing run pass.
- Do not change unrelated WorldEngine API response shapes.
- Do not claim external validation PASS, Codex autonomous validation PASS,
  human validation PASS, product readiness, or v0.8 final closeout changes.

## Compatibility Requirements

- `POST /worlds/{world_id}/director-guidance` must remain OpenAPI-discoverable
  with operation id `submit_director_guidance`.
- The endpoint must continue to accept public direction and append a public
  `director.guidance.accepted` event.
- The event payload must continue to omit the raw `instruction_text`.
- The public response must remain additive-compatible with
  `DirectorGuidanceResponse`.
- Existing `/world/*`, `/worlds`, `/manifest`, runtime, generation, and Agent
  loop endpoints must keep their existing behavior.

## North Star Check

This package keeps WorldEngine generic. It repairs the public contract used by
external validation consumers without adding external application logic or
concrete validation-world content to the core repository.

## Exit Criteria

- Documentation/contract evaluator records no P0/P1 and no blocking P2.
- Implementation authorization is explicitly recorded before code changes.
- A focused test fails before the public wording repair and passes afterward.
- Focused backend tests pass.
- Saved-result checker behavior for full lifecycle evidence integrity is
  verified with exact commands.
- Focused repair closeout may complete without a live full lifecycle rerun when
  `evidence_execution_authorized: yes` is absent, provided `review.md` records
  the rerun as not authorized and keeps the package verdict limited to focused
  repair evidence.
- Full lifecycle PASS closeout requires review-recorded
  `evidence_execution_authorized: yes` and a fresh full lifecycle rerun that
  either passes the checker or is recorded as blocked with exact unavailable
  dependencies.

## Out-of-Scope Follow-ups

- Validation Client evidence exporter changes.
- Human validation.
- Live provider validation.
- Future direct Agent memory/self-continuity implementation.
- Product readiness or release recertification.
