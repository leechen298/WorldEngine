# WorldEngine Full Lifecycle Autonomous Validation

Status: saved-result-checker-supported

## Goal

Validate that WorldEngine can complete the minimum observable lifecycle needed
by an external validation client:

1. create a world from a user-provided world premise.
2. return a public initial state and visualization payload.
3. run the world forward across ticks.
4. produce event, snapshot, replay, and API evidence.
5. show Agent actions that are evidenced by WorldEngine, not directly scripted
   by the client.
6. accept natural-language direction only as external/world-environment
   guidance.
7. export redacted evidence for a second Agent review.

## Perspective

The autonomous tester operates the external validation client like an ordinary
observer/director user. It may use public evidence artifacts emitted by the
client and WorldEngine, but it must not use private engine internals, hidden
reset APIs, database state, provider raw traces, or private validation oracles.

## Allowed Operations

- UI operations in the Validation Client.
- CLI commands for starting services, running tests, and invoking the checker.
- Public API evidence captured as `api-summary.json`.
- Evidence bundle review through exported artifacts.

## Forbidden Operations

- Direct API calls recorded as Agent operation-log entries.
- Private prompts or provider raw responses in evidence.
- Direct Agent private-state mutation.
- Client-scripted Agent actions presented as WorldEngine autonomy.
- Concrete validation-world seed data stored in the WorldEngine repository.

## Required Coverage

- Open or create a Validation Client session connected to WorldEngine.
- Create a world through the public client flow.
- Observe a returned world id, public initial state, and visualization.
- Run enough ticks to show `tick_end > tick_start`.
- Observe at least one event and at least one snapshot.
- Observe at least one Agent action with WorldEngine-backed evidence.
- Submit one natural-language direction and verify it is recorded as external
  guidance, not direct Agent private-state mutation.
- Export evidence artifacts.
- Run `make validate-agent-autonomous-result RESULT_DIR=<dir>`.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log`
- `scorecard-summary.json`
- `api-summary.json`
- `world-lifecycle-summary.json`
- at least one screenshot

## `world-lifecycle-summary.json`

The lifecycle summary must contain passing sections:

- `world_creation`
- `runtime_progression`
- `agent_autonomy`
- `external_direction`
- `evidence_integrity`

The checker rejects missing Agent actions, client-scripted actions,
non-advancing ticks, no events, no snapshots, direct Agent private-state
mutation, or failed redaction evidence.

## PASS/FAIL Source

Saved-result checker:

```bash
make validate-agent-autonomous-result RESULT_DIR=<dir>
```

This scenario does not let Codex self-declare PASS. The checker validates
recorded evidence only; the live run still must be performed by a future
validation chat.
