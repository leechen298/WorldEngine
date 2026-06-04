# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Summary

This package proposes a future public handoff manifest but does not implement
it. The manifest should be a redacted, public WorldEngine-owned document or
endpoint that an external validation client can consume before running Agent
autonomous validation.

## Future Handoff Manifest Shape

Future implementation may define a JSON schema with fields like:

```json
{
  "schema_version": "0.8.x",
  "generated_at": "2026-06-04T00:00:00Z",
  "worldengine_version": "v0.8",
  "provider": {
    "provider_class": "kimi_platform_api",
    "provider_readiness": "ready",
    "credential_source_class": "environment",
    "model_label": "redacted-or-public-model-label",
    "quota_status": "unknown|ready|limited|blocked",
    "rate_limit_note": "public summary only"
  },
  "public_surfaces": [],
  "evidence_refs": [],
  "redaction": {
    "secrets_included": false,
    "private_prompts_included": false,
    "provider_raw_traces_included": false,
    "private_validator_details_included": false
  },
  "blockers": [],
  "warnings": []
}
```

The final shape must be defined in a later reviewed package.

## Validation Client Discovery Requirement

The current external Validation Client discovers world creation from
WorldEngine OpenAPI. It needs one of the following:

- a POST path ending in `/worlds`.
- a POST operation id equal to `createWorld` or `create_world`.
- a POST operation tagged `worlds` with `create` in the operation id.

The recommended future public surface is:

```text
POST /worlds
```

Full autonomous validation also needs a public director guidance surface:

```text
POST /worlds/{world_id}/director-guidance
```

These surfaces must return public summaries only and must not expose provider
raw traces, private prompts, private Agent state, or credentials.

## Provider Evaluation Notes

### Kimi Code Subscription

Kimi Code documentation describes a developer programming service included in
Kimi membership, with API keys usable in third-party coding agents, OpenAI and
Anthropic compatible endpoints, and the stable model id `kimi-for-coding`.

Planning implication: Kimi Code is a good candidate for coding-agent tooling
or external operation agents. It may be less appropriate as a WorldEngine
runtime provider unless terms, quota, reliability, and product-integration
constraints are reviewed.

### Kimi Platform / Moonshot API

Kimi Platform / Moonshot API is the better candidate for product-style
programmatic runtime integration. It should be evaluated as a pay-as-you-go or
platform API provider controlled by WorldEngine environment configuration.

### DeepSeek API

DeepSeek API is a pay-as-you-go fallback option. DeepSeek's public pricing page
lists model, context, output, and token pricing details that can change over
time. Any live validation must use explicit budgets, max tokens, and stop
rules.

## External Validation Client Consumption

The external validation client may read:

- provider class.
- provider readiness.
- public model label.
- quota/rate-limit public note.
- public surface ids.
- redaction confirmation.
- blocked / skipped / unavailable reasons.

It must not read:

- API keys.
- provider account details.
- private prompts.
- raw provider traces.
- private validation scenarios.
- private evaluator oracle internals.

## Future Implementation Options

1. Documentation-only contract surface under `docs/contracts/`.
2. JSON schema and static manifest under `docs/contracts/`.
3. Public API endpoint that emits a live readiness summary.

Option 1 is safest and should happen first. Options 2 and 3 require reviewed
implementation packages and current-session tests.
