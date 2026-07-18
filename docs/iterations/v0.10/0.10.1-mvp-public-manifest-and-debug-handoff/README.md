# 0.10.1 MVP Public Manifest And Debug Handoff

Chinese mirror: `README.zh.md`.

Status: implementation complete / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Align the MVP public manifest, debug handoff vocabulary, discoverable surface
metadata, honest status taxonomy, and checker-handoff skeleton before later
v0.10 session features depend on them.

In practical terms, `/manifest` should say that this is the v0.10 MVP debug
contract, list the public MVP/debug surfaces that currently exist or are
planned, preserve `pass`, `fail`, `blocked`, and `not_run` semantics, expose
redacted checker handoff metadata, and keep provider ownership and evaluator
authority inside WorldEngine/checker contracts rather than the external
Validation Client.

## Scope

Allowed implementation scope after documentation review:

- Additive fields on the public handoff manifest schema.
- Additive MVP/debug surface metadata for existing public routes and planned
  v0.10 session routes.
- Public status taxonomy values and meanings for `pass`, `fail`, `blocked`,
  and `not_run`.
- Minimal checker-handoff skeleton metadata that preserves artifact names and
  redaction expectations.
- Replay/worldline branch terminology that uses branch-like timeline wording
  and avoids parent/source-world semantics.
- Focused backend tests for manifest compatibility, status taxonomy, redaction
  flags, blocked/not_run honesty, and no secret/raw provider leakage.

Allowed files:

- `backend/app/schemas/world.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- this package directory and Chinese mirrors.
- v0.10 parent status/review docs for route and evidence updates.

Forbidden scope:

- No Validation Client repository implementation.
- No provider live calls or provider credential handling changes.
- No runtime session implementation, session store, worldview-to-session
  creation, bounded session runtime, snapshot/diff engine, dashboard flow,
  durable persistence, migration, generated result, or external validation.
- No checker implementation or fixture changes unless this package is revised
  and reviewed again.
- No raw prompts, raw provider requests/responses, provider traces, secrets,
  private Agent memory, hidden context, raw thought, or private evaluator data.
- No `backend/worldengine/` changes.

## Deliverables

- Reviewed package document set and mirrors.
- Additive v0.10 MVP manifest/debug contract schema.
- Updated `/manifest` payload with discoverable MVP/debug surfaces and
  checker-handoff skeleton.
- Focused backend tests proving compatibility and redaction behavior.
- Review evidence with exact commands and results.

## Status Checklist

- [x] Package documents drafted.
- [x] Documentation / contract evaluator complete.
- [x] Implementation authorized.
- [x] Implementation complete.
- [x] Focused verification complete.
- [x] Implementation-scope evaluator complete.
- [x] Code-review/evidence evaluator complete.
- [x] Review evidence updated.

## Final Assessment State

Current value: `implementation complete / focused verification passed`.

This package is complete for the focused public manifest/debug handoff scope.
It does not claim runnable session, dashboard, provider-live, checker,
external-validation, Agent autonomy, or full MVP PASS.
