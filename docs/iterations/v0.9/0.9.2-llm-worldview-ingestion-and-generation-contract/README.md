# 0.9.2 LLM Worldview Ingestion And Generation Contract

Chinese mirror: `README.zh.md`.

Status: ready for implementation
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Define the reviewed contract for turning a user's basic worldview premise into
a public, system-digestible, premise-specific generated world model through
WorldEngine-owned LLM-backed generation.

This package prepares and, after review authorization, may implement the first
LLM-backed world creation surface for v0.9. It must keep existing
deterministic world creation available and clearly labeled, and it must not
claim LLM-backed PASS from deterministic fallback or mock-only evidence.

## Scope

Allowed after documentation/contract review:

- Add worldview input schema and validation semantics.
- Add an LLM-backed world generation request path in the active `backend/app/`
  backend.
- Add public generated world model schemas and a
  `world_creation_summary`-style public artifact contract.
- Add generation provenance summary fields that prove the response is
  WorldEngine-owned, provider-classified, redacted, and either
  provider-backed, not configured, or blocked.
- Add validation metadata for premise specificity, system digestibility,
  runtime readiness, deterministic fallback labeling, and redaction.
- Add explicit fallback-vs-LLM classification fields such as `creation_mode`,
  `llm_backed`, `provider_backed`, and
  `deterministic_generic_fallback_detected`.
- Add focused backend tests for schema validation, API behavior, fallback
  classification, provider-blocked behavior, redaction, and existing
  deterministic `POST /worlds` compatibility.
- Add checker support or fixture contract updates only if needed to validate
  the public `world_creation_summary` artifact for this package.
- Update package `review.md` with implementation evidence after code work.

Forbidden:

- Do not expose, persist, log, or export raw prompts, raw provider requests,
  raw provider responses, provider traces, secrets, authorization headers,
  private evaluator data, hidden context, raw thought, chain-of-thought,
  private Agent memory, or private goals.
- Do not let Validation Client generate, rewrite, store provider keys for, or
  evaluate generated world content.
- Do not store concrete demo-world fixtures, external validation seed data,
  maps, characters, resources, story rules, oracle internals, or
  application-specific backend behavior in this repository.
- Do not present existing deterministic generic world creation as LLM-backed
  success.
- Do not treat `/provider/live-smoke` safe mock behavior as provider-backed
  world generation proof.
- Do not implement world rule evolution, event legality, bounded runtime
  control, Agent continuity, narrative projection, diagnostic dialogue, full
  LLM-backed checker, Validation Client evidence export, or lifecycle PASS.
- Do not modify `backend/worldengine/`.

## Deliverables

- Full package document set and Chinese mirrors.
- Reviewed implementation authorization before code changes.
- Public worldview ingestion request contract.
- LLM-backed generation request/response contract.
- Public generated world model summary and validation metadata contract.
- Redaction and deterministic fallback classification rules.
- Focused test plan and implementation plan.
- Documentation/contract evaluator evidence.

## Status Checklist

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation/contract evaluator complete.
- [x] Implementation authorized.
- [ ] Implementation complete.
- [ ] Focused verification complete.
- [ ] Review evidence updated.
- [ ] Handoff to `0.9.3` recorded.

## Final Assessment State

Current value: `ready for implementation`.

Implementation is authorized only for the reviewed non-live `0.9.2` scope.
Live provider calls remain closed unless this package is explicitly updated
and re-reviewed to authorize bounded live execution.
