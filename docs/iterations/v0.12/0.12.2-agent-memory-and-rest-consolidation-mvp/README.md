# 0.12.2 Agent Memory And Rest Consolidation MVP

Chinese mirror: `README.zh.md`.

Status: review complete
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Add minimal public memory summaries and rest/consolidation evidence for the
session Agent introduced in `0.12.1`.

This package should show that an Agent can carry public memory across ticks and
settle observations through rest. It must not expose private memory payloads,
raw thought, private goals, personality mutation, skill mutation, or deep
cognition claims.

## Scope

Allowed after review approval:

- Add public session Agent memory summary schemas and response artifacts.
- Store short-term public working summaries and episodic summaries through the
  existing in-memory memory substrate.
- Add session Agent memory read API under
  `/sessions/{session_id}/agents/{agent_id}/memory`.
- Extend session Agent step or add a consolidation endpoint to record rest /
  consolidation evidence when the Agent rests.
- Record public evidence events such as `world.agent.memory.recorded` and
  `world.agent.consolidation.recorded`.
- Add focused backend tests for public memory creation, multi-tick rest
  consolidation, redaction, no per-tick personality/skill mutation, evidence
  refs, and compatibility.

Forbidden:

- No raw private memory payloads, raw thought, chain-of-thought, private goals,
  hidden context, provider traces, raw prompts, raw provider responses, or
  secrets in public evidence.
- No automatic per-tick personality, skill, relationship, injury, death,
  inventory, or long-term memory mutation.
- No diagnostic conversation inserted into Agent memory.
- No frontend, persistence/migration, provider live, external Validation
  Client, checker automation, narrative/diagnostic, or complete MVP closeout
  work.
- No implementation under `backend/worldengine/`.

## Deliverables

- Public Agent memory summary API/artifacts.
- Rest/consolidation evidence tied to session Agent runtime refs.
- Public event evidence and memory evidence refs.
- Focused backend tests and review evidence.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Implementation authorized
- [x] Implementation complete
- [x] Tests complete
- [x] Review complete

## Final Assessment

Implementation-scope evaluator review passed. This package is complete for
the scoped Agent memory and rest consolidation MVP.
