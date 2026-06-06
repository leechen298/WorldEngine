# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `provider readiness`: public environment-derived state from `/manifest`.
  It may report configured or not configured, but it is not proof of a live
  call.
- `provider live smoke`: the smallest WorldEngine-owned provider call used to
  prove live connectivity without generating a world.
- `redacted provider live summary`: public evidence of the smoke attempt,
  excluding raw prompts, raw requests, raw responses, raw traces, secrets, and
  account details.
- `provider blocked`: a classified state where environment, quota, network,
  provider availability, or redaction prevents live proof.
- `worldengine_owned_call`: a boolean in evidence proving the call was
  initiated by WorldEngine, not Validation Client.

## Public Provider Live Summary

The provider smoke response or artifact must contain only public/redacted
fields:

```text
schema_version
provider_class
model_label
call_attempted
call_status
latency_ms
token_usage_bucket
public_failure_category
worldengine_owned_call
redaction
```

Allowed `call_status` values:

```text
success
failure
blocked
not_configured
not_run
```

Allowed `public_failure_category` values:

```text
none
not_configured
network
quota
provider_error
redaction_failure
unsupported_provider
blocked
unknown
```

All redaction flags must be false for success:

```text
api_keys_included
authorization_headers_included
raw_prompts_included
raw_provider_requests_included
raw_provider_responses_included
provider_traces_included
private_agent_memory_included
raw_thought_included
hidden_context_included
```

## Allowed Changes

After review authorization, this package may modify:

- `backend/app/agent/llm_provider.py`
- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/schemas/`
- `backend/app/tests/`
- `tools/testing/validate_agent_autonomous_result.py` and focused tests only
  if the provider summary checker support is needed for this package.
- package `review.md` and `review.zh.md`.

The implementation may introduce a small helper module such as
`backend/app/agent/provider_config.py` or `backend/app/schemas/provider.py` if
that better matches the existing backend structure.

## Forbidden Changes

This package must not:

- modify `backend/worldengine/`.
- modify the Validation Client repository.
- add concrete worlds, maps, characters, resources, story rules, seed data, or
  application-specific backend behavior.
- implement LLM-backed world generation or prompt-driven world creation.
- expose or persist provider keys, authorization headers, raw prompts, raw
  provider requests, raw provider responses, provider traces, account ids,
  hidden context, private evaluator data, private Agent memory, raw thought,
  or chain-of-thought.
- let Validation Client call the provider or manage provider keys.
- make `/manifest` live-call proof.
- use deterministic mock output as provider live PASS.
- claim provider live PASS unless a live call succeeded and redaction checks
  passed in the current session.

## Compatibility Requirements

- Existing `/manifest` fields remain additive-compatible.
- Existing unconfigured provider state remains safe and testable.
- Existing `POST /worlds` deterministic generic world creation remains
  unchanged.
- Existing mock provider tests remain deterministic.
- Schema changes are additive unless this contract is updated and re-reviewed.
- Provider errors must return public failure categories, not private request or
  response details.

## Stop Rules

Stop implementation if:

- a live smoke call cannot be made without storing or exposing raw provider
  data.
- provider configuration requires secrets outside environment-owned runtime
  configuration.
- Validation Client changes are required.
- the implementation would need concrete world generation content.
- tests cannot prove not-configured behavior and redaction.
- implementation discovers the package needs a broader provider SDK or prompt
  architecture than this contract allows.
