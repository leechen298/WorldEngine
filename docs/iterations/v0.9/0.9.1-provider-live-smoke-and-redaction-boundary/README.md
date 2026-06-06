# 0.9.1 Provider Live Smoke And Redaction Boundary

Chinese mirror: `README.zh.md`.

Status: implementation complete / non-live focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized: no

## Goal

Add the first WorldEngine-owned provider live smoke contract and
implementation path for v0.9, with redacted public evidence and safe
unconfigured behavior.

This package must prove only the provider boundary. It does not generate
worlds, evaluate worldview fidelity, evolve rules, create Agent continuity, or
claim LLM-backed lifecycle PASS.

## Scope

Allowed after documentation/contract review:

- Add or refine backend provider configuration helpers in the active
  `backend/app/` path.
- Add a minimal WorldEngine-owned provider smoke call path, preferably a
  public API endpoint such as `POST /provider/live-smoke` with operation id
  `provider_live_smoke`.
- Add a public redacted provider live summary schema.
- Add failure taxonomy for:
  - `not_configured`
  - `network`
  - `quota`
  - `provider_error`
  - `redaction_failure`
  - `unsupported_provider`
  - `blocked`
- Keep `/manifest` additive-compatible while making clear that manifest
  readiness is not live-call proof.
- Add focused backend tests for configured, not configured, safe mock, public
  response shape, and redaction.
- Add checker or fixture support only if needed to validate the redacted
  provider summary for this package.
- Update package `review.md` with implementation evidence after code work.

Forbidden:

- Do not expose, store, log, or export API keys, authorization headers, raw
  prompts, raw provider requests, raw provider responses, raw provider traces,
  account identifiers, private evaluator data, hidden context, raw thought, or
  private Agent memory.
- Do not make Validation Client own provider calls, provider keys, prompts, or
  evaluation authority.
- Do not implement LLM-backed world generation beyond a fixed minimal smoke
  prompt owned by WorldEngine.
- Do not add concrete demo-world names, maps, characters, resources, story
  rules, seed data, or application-specific backend behavior.
- Do not modify `backend/worldengine/`.
- Do not claim provider PASS, LLM-backed lifecycle PASS, external validation
  PASS, product readiness, API-wide PASS, E2E PASS, Agent smoke PASS, or
  autonomous PASS without current-session evidence.

## Deliverables

- Full package document set and Chinese mirrors.
- Reviewed implementation authorization before code changes.
- Minimal provider live smoke API or command.
- Public provider live summary schema.
- Redacted evidence contract and redaction tests.
- Focused backend tests and `/manifest` compatibility tests.
- Optional live smoke execution only when provider environment is configured
  and explicitly authorized by this package.

## Status Checklist

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation/contract evaluator complete.
- [x] Implementation authorized.
- [x] Implementation complete.
- [x] Focused verification complete.
- [x] Review evidence updated.
- [x] Handoff to `0.9.2` recorded.

## Final Assessment State

Current value: `implementation complete / non-live focused verification passed`.

This package implemented the reviewed provider smoke and redaction boundary
without running a real provider call. Live provider calls remain closed. The
next route is `0.9.2-llm-worldview-ingestion-and-generation-contract`
documentation package creation.
