# Contract

## Public Semantics

This package adds Codex workflow guidance and skill synchronization only. It
must not change WorldEngine runtime, API, UI behavior, WorldSpec semantics, or
product capability.

## Allowed Changes

- Add `.agents/skills/worldengine-e2e-runner/SKILL.md`.
- Add `.agents/skills/worldengine-agent-smoke-runner/SKILL.md`.
- Add a small sync script under `tools/testing/`.
- Add Make targets for skill validation and sync.
- Update v0.1 iteration index and review evidence.

## Forbidden Changes

- Do not add a plugin package or marketplace entry in this package.
- Do not change backend runtime behavior.
- Do not change frontend user-visible behavior.
- Do not change E2E scenario semantics.
- Do not weaken the Agent smoke validator.
- Do not modify `backend/worldengine/`.
- Do not claim live Agent smoke passed unless a real result directory validates
  through `make validate-agent-smoke-result RESULT_DIR=<dir>`.

## Skill Rules

The E2E skill must require deterministic command evidence from `make test-e2e`
or an equivalent explicitly named Playwright command.

The Agent smoke skill must require:

- UI or CLI operations only.
- `operation-log.jsonl` as the raw operation record.
- no direct API operations recorded as Agent operations.
- required evidence files from the v0.1.3 protocol.
- final PASS only from `tools/testing/validate_agent_smoke_result.py`.

## Compatibility

The sync command may copy project-local skills into a local Codex skills
directory, but the source of truth remains the repository copy under
`.agents/skills/`.
