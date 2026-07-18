# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `provider_preflight_status`: public readiness classification for the
  provider/worldview generation path.
- `generation_mode`: existing public worldview generation mode such as
  `deterministic_fallback`, `safe_mock`, `blocked`, or `not_configured`.
- `live_call_authorization`: explicit package-level statement that live
  provider calls are not authorized.
- `redaction_safe_summary`: public evidence that excludes secrets, raw
  prompts, raw responses, traces, hidden context, and private evaluator data.

## Allowed Changes

- Add `backend/app/schemas/provider_preflight.py` or equivalent additive
  schemas.
- Add an additive API route such as `POST /provider/worldview-preflight`.
- Reuse existing provider readiness and worldview generation helpers without
  live provider calls.
- Update manifest public surfaces to advertise the new preflight endpoint.
- Add focused backend tests.
- Update this package and parent v0.11 review/route docs.

## Forbidden Changes

- No live provider call.
- No provider-backed quality PASS.
- No secret, raw prompt, raw response, provider trace, private Agent memory,
  hidden context, raw thought, or private evaluator data in public payloads.
- No Validation Client implementation.
- No world rules, direction queue, event generation, diff application, or
  fidelity scoring.
- No durable persistence/migrations.
- No `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/provider/live-smoke`, `/world/generation/worldview`, `/sessions`,
  and `/sessions/from-worldview` behavior remains additive-compatible.
- Unconfigured provider must remain classifiable as `not_configured` or
  deterministic fallback when fallback is requested.
- Configured provider without live-call authorization must remain blocked, not
  silently downgraded to provider-backed PASS.
- Mock provider must remain labeled non-live and non-provider-backed.

## Out-of-Scope Follow-Ups

- Actual provider-backed generation belongs to a later package only if live
  provider authorization and evidence are explicitly granted.
- Structured rules and parameters belong to `0.11.2`.
- Direction queue/boundary belongs to `0.11.3`.
- Rule-compliant events/diffs belong to `0.11.4`.
- Fidelity validation belongs to `0.11.5`.
