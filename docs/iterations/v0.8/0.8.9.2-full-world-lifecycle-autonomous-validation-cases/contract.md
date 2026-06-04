# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `worldengine-full-lifecycle-autonomous`: autonomous saved-result scenario for
  complete WorldEngine lifecycle validation through an external client surface.
- `world_lifecycle_summary`: redacted artifact proving world creation, runtime
  progression, Agent autonomy evidence, external direction boundaries, and
  evidence integrity.
- `api_summary`: redacted public API evidence separate from the Agent operation
  log.
- `agent_autonomy_evidence`: public evidence that Agent actions came from
  WorldEngine state/event surfaces and were not directly scripted by the
  client.

## Compatibility Constraints

- Existing autonomous saved-result scenarios must remain valid.
- Existing result schema extensions must be additive.
- Existing checker behavior for dashboard scenarios must remain compatible.
- Direct API calls must remain forbidden as Agent operation-log entries.
- API evidence for this scenario must remain in artifacts, not hidden logs.

## Allowed Changes

- `docs/testing/agent-autonomous/README.md`
- `docs/testing/agent-autonomous/scorecard.md`
- `docs/testing/agent-autonomous/result-schema.json`
- `docs/testing/agent-autonomous/scenarios/`
- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/`
- `Makefile`
- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- this package's review evidence.

## Forbidden Changes

- Do not modify WorldEngine runtime, schemas, API routes, provider code,
  frontend, migrations, or `backend/worldengine/`.
- Do not modify the Validation Client repository.
- Do not add concrete validation world content, named characters, maps,
  location seed data, story rules, or app-specific backend logic.
- Do not expose provider keys, authorization headers, raw requests, raw
  responses, private prompts, private Agent memory, private goals, relationship
  internals, `self_state`, hidden context, private file paths, or validation
  oracle internals.
- Do not claim live WorldEngine PASS, Codex autonomous PASS, human validation
  PASS, or product readiness from fixtures.

## North Star Check

The package improves evidence for generated worlds, runtime progression, and
Agent-in-world behavior while keeping application and validation details
outside the core engine.

## Out-of-Scope Follow-ups

- Live autonomous run through the Validation Client.
- Second-Agent evidence review.
- Human validation.
- Runtime repairs discovered by the live validation.
- Provider heartbeat or provider-cost governance beyond scenario stop rules.
