# Contract

## Public Concepts

This package may introduce or refine these public manifest concepts:

- `mvp_contract_version`: the public MVP debug contract version, expected to
  identify v0.10 without changing existing legacy fields.
- `worldengine_version`: must advance public discovery to `v0.10` while
  preserving additive compatibility.
- `manifest_status`: one of `pass`, `fail`, `blocked`, or `not_run`; the
  current manifest may honestly be `blocked` or `not_run` for future session
  surfaces.
- `status_taxonomy`: public definitions for `pass`, `fail`, `blocked`, and
  `not_run` so clients do not invent UI-only meanings.
- `mvp_debug_surface`: a discoverable public API surface with path, method,
  operation id, availability, maturity, validation status, and whether it is
  required for the v0.10 MVP path.
- `checker_handoff`: a redacted public skeleton naming checker-compatible
  artifacts, expected result values, evaluator authority, and unsupported
  items.
- `validation_client_role`: `display_export_only`.
- `provider_owner`: `worldengine`.
- `evaluator_role`: `worldengine_checker_or_second_agent_review`.
- `worldline_branch_semantics`: branches are comparable timeline branches for
  replay/debugging, not parent/child worlds, source worlds, or origin trees.

## Compatibility Requirements

- Existing manifest fields remain available and additive-compatible:
  `schema_version`, `worldengine_version`, `provider`, `public_surfaces`,
  `redaction`, `blockers`, and `warnings`.
- Existing public surface entries remain valid for current consumers.
- Existing provider readiness behavior remains a redacted readiness summary,
  not live-call proof.
- New fields must be optional/defaulted in schema terms so older tests and
  clients can ignore them.
- Status values must preserve `pass`, `fail`, `blocked`, and `not_run`; do not
  map them to UI-only labels.
- Public payloads must not include provider secrets, raw model labels, raw
  prompts, raw responses, raw traces, private memory, hidden context, raw
  thought, or private evaluator data.

## Allowed Changes

- Extend `backend/app/schemas/world.py` with additive manifest/debug handoff
  models and fields.
- Update `backend/app/api/routes/world.py` `/manifest` construction and public
  surface metadata.
- Update `backend/app/tests/test_public_handoff_contract_api.py` with focused
  tests for v0.10 manifest fields, compatibility, status taxonomy, redaction,
  blocked/not_run honesty, and branch terminology.
- Update package and parent v0.10 docs/reviews.

## Forbidden Changes

- Do not implement Validation Client repository behavior.
- Do not implement session storage, session APIs, session runtime, snapshot
  evidence, dashboard flow, persistence, migrations, generated-result writing,
  provider live calls, checker fixtures, or external validation.
- Do not modify files outside the allowed file list unless a documentation
  review records and approves the scope change first.
- Do not add concrete demo worlds, maps, characters, locations, resources,
  story rules, seed data, UI selectors, or application-specific backend logic.
- Do not change `backend/worldengine/`.
- Do not claim v0.10 runnable session PASS, dashboard PASS, external
  validation PASS, provider live PASS, Agent autonomy PASS, or full MVP PASS.

## North Star Check

This package strengthens WorldEngine as a generic engine by making public
discovery and evidence handoff explicit. It keeps external clients as
consumers and exporters of public evidence, not owners of provider behavior,
world generation, runtime mutation, or evaluation authority.

## Out-of-Scope Follow-ups

- `0.10.2`: actual world session contract and state store.
- `0.10.3`: worldview input to runnable session creation.
- `0.10.4`: bounded session runtime and snapshot evidence.
- `0.10.5`: dashboard MVP session flow.
- `0.10.6`: v0.10 validation and handoff.
