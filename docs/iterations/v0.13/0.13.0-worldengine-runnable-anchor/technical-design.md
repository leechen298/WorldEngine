# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Position

This design is derived from the target living-world flow, not from existing
implementation structure. Implementation begins by auditing current code for
safe reuse; incompatible paths may be isolated behind the new versioned
surface but must not be destructively removed in this package.

## Planned Structure

The implementation should create one cohesive generic engine boundary under
the active `backend/app/` path. Planned responsibilities are:

```text
backend/app/engine/
  models.py             normalized canonical runtime records
  generation.py         deterministic WorldBrief -> RunnableWorldPackage
  rules.py              action/direction/feedback legality
  session.py            boot, lockstep step, state and revision ownership
  agent_runtime.py      public perception, deterministic policy, action chain
  evidence.py           events, diffs, snapshots, hashes, export

backend/app/schemas/engine_v1.py
backend/app/api/routes/engine_v1.py
backend/app/tests/test_engine_v1_*.py
```

Exact files may be adjusted after the implementation-stage code audit, but the
responsibilities must remain separated. Any material path or boundary change
requires a documentation update before implementation continues.

The administration console should add a focused operational surface under
`frontend/src/` with:

- structured world-brief and seed input.
- generated-package readiness and hash display.
- session boot and exact-step controls.
- canonical projection summary with tick/revision/state hash.
- Agent public state, latest perception/decision/action result, and experience
  references.
- active intervention window plus direction submission and judgment result.
- event/diff/snapshot timeline and evidence export.

It must not become a marketing page or game projection.

## Deterministic Generation

The required path uses only structured input and a fixed seed. It produces a
normalized package with these public sections:

```text
world_spec
rule_catalog
action_catalog
agent_seed_set
projection_manifest
evidence_policy
```

Normalization sorts identifiers and collections before hashing. Readiness
validation checks references, mutable fields, rule/action preconditions,
Agent seeds, and projection fields. Session boot accepts only a ready package
and stores `source_package_hash`.

The generator must not ship a concrete world fixture. Core tests construct
generic structured inputs in test code; the external repository later owns the
concrete anchor brief and visual assets.

## Session And Lockstep Runtime

The minimum runtime is process-local and command-driven:

1. Session boots as `ready` and paused.
2. A client requests `step_count` with `request_id` and optional
   `expected_revision`.
3. Each step opens or advances the explicit intervention window, consumes
   accepted queued direction, evaluates world rules, runs the Agent cycle,
   judges action/feedback candidates, applies accepted diffs, records rejected
   results, captures a snapshot, and publishes the new projection.
4. Tick, world time, event sequence, and revision increase monotonically.
5. `state_hash` is calculated from normalized canonical public state after the
   step.

A step is atomic for this MVP. A failure before commit leaves the previous
revision unchanged and records a safe diagnostic outside canonical history.

## Event, Diff, Snapshot, And Projection Spine

Every canonical mutation follows:

```text
request/candidate
-> rule judgment
-> accepted or rejected event
-> applied diff or explicit no-diff
-> canonical state
-> snapshot
-> public projection
```

Evidence uses stable correlation fields:

- `request_id`
- `package_id` and `package_hash`
- `world_id` and `session_id`
- `tick`, `event_sequence`, and `revision`
- `state_hash_before` and `state_hash_after`
- rule, action, direction, Agent, and event references.

Event polling uses `after_sequence`; WebSocket is intentionally deferred.

## Minimal Agent Runtime

The required Agent path is deterministic and provider-independent. It is not a
chat wrapper and does not expose private thought.

Cycle 1:

1. Build a public perception frame from projection, allowed actions, and recent
   public events.
2. Select a bounded public intent through a deterministic policy interface.
3. Produce an `ActionRequest`.
4. Let the rule service return an `ActionResult`.
5. Record public causal evidence and an `AgentExperienceRef`.

Cycle 2 or later:

- The public decision input contains the prior experience reference.
- The output records which prior reference affected the public decision.
- A test must observe a different decision/evidence outcome than the same
  decision path without the prior experience.

This is the minimum proof of continuity. Long-term memory, consolidation,
personality drift, and self-narrative are deferred.

## Operator Intervention

An intervention is accepted only in an explicit open window. Both required
requests use the same `window_id`:

- legal: bounded pressure/constraint that becomes a queued direction or event
  candidate and is evaluated in a later step.
- illegal: direct assignment of a final fact, inventory, death, teleport, or
  equivalent canonical patch. It is rejected with a stable semantic code and
  no diff.

Window-closed rejection is tested separately and cannot satisfy the illegal
direction acceptance criterion.

## Generic Client Boundary

The protocol is engine-neutral:

- HTTP JSON command/query operations.
- capability discovery before operation.
- request IDs for mutation idempotency.
- expected revision for optimistic concurrency.
- cursor polling for events.
- typed actions and feedback that always pass through WorldEngine judgment.

The administration console is the first consumer. Godot in `0.13.1` must be
able to implement the same flow without a private adapter service inside
WorldEngine.

## Error Handling

- Invalid world package: validation response with field diagnostics; no
  package readiness.
- Unknown package/session: `404`-class response.
- Duplicate mutation request ID: original result returned idempotently.
- Stale expected revision or closed intervention window: stable conflict code;
  no mutation.
- Illegal action/direction/feedback: domain-level rejected result, rejected
  event, reason code, and no applied diff.
- Atomic step failure: previous revision retained; no partial canonical diff.
- Evidence export gap: export reports incomplete status; later checker must not
  interpret it as PASS.

## Compatibility Strategy

- Introduce a clean versioned surface instead of forcing target concepts into
  historical routes.
- Register it alongside existing APIs during this package.
- Reuse internal code only after contract-level tests prove equivalence.
- Do not delete historical endpoints or dirty files in `0.13.0`.

## Anti-drift Rules

- No concrete external scenario in core tests or source.
- No live-provider fallback may become required for PASS.
- No frontend-only success path.
- No state change without event and diff evidence.
- No Agent action accepted from client-authored final outcome.
- No complete MVP claim before `0.13.2` external evidence.
