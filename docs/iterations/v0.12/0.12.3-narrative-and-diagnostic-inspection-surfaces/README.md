# 0.12.3 Narrative And Diagnostic Inspection Surfaces

Chinese mirror: `README.zh.md`.

Status: review complete
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Add lightweight read-only narrative and diagnostic inspection surfaces for
session/world behavior and public Agent evidence.

This package should let a human or validator inspect what happened through
readable projections without changing canonical world state, timeline events,
or Agent memory. It builds on the earlier world-level projection boundary and
extends it toward v0.12 session, tick-range, branch, and Agent-focused
inspection.

## Scope

Allowed after review approval:

- Add session-scoped narrative projection and diagnostic inspection schemas.
- Add request fields for session ID, tick range, branch ID, Agent focus, and
  bounded public source refs.
- Add read-only API surfaces or artifacts under existing WorldEngine route
  boundaries.
- Reuse or extend existing `external_projection` boundary helpers.
- Add manifest/public-surface discovery for new inspection surfaces.
- Add focused backend tests for session/tick-range/branch/Agent-focused
  queries, public evidence provenance, redaction, read-only behavior, and
  compatibility.

Forbidden:

- No narrative mutation of canonical world state.
- No diagnostic conversation inserted into the world timeline or Agent memory.
- No raw thought, chain-of-thought, private memory, private goals, hidden
  context, provider traces, raw prompts, raw provider responses, secrets, or
  private evaluator data in requests, responses, events, tests, or evidence.
- No gameplay dialogue, concrete demo content, player records, frontend,
  persistence/migration, provider live call, external Validation Client,
  checker automation, or complete MVP closeout work.
- No implementation under `backend/worldengine/`.

## Deliverables

- Session/tick-range/branch/Agent-focused narrative projection API/artifacts.
- Out-of-world diagnostic inspection summary API/artifacts.
- Provenance and redaction fields that identify public evidence inputs.
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

## Current Assessment

Implementation-scope evaluator review passed after P2 repairs. This package is
complete for the scoped read-only session narrative and diagnostic inspection
surfaces.
