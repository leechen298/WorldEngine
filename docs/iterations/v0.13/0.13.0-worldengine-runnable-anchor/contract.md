# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `WorldBrief`: structured, provider-independent world direction with a fixed
  seed, scale bounds, premise, and constraints.
- `RunnableWorldPackage`: immutable generated handoff containing public world
  spec, rules, actions, Agent seeds, projection manifest, and evidence policy.
- `package_hash`: canonical hash over the normalized runnable package. Session
  boot must cite the exact hash it loaded.
- `WorldSession`: one process-local canonical run with lifecycle state, source
  package hash, tick, world time, revision, and state hash.
- `InterventionWindow`: an explicit tick-boundary window identified by
  `window_id` and `open_tick` in which operator direction may be submitted.
- `BoundedDirection`: operator pressure or constraint that does not directly
  assign a final world fact.
- `DirectionDecision`: accepted, translated, rejected, or deferred result with
  stable reason code, rule references, and applied-diff references when any.
- `ActionRequest`: typed Agent or client request that proposes a world change
  without applying it.
- `FeedbackEvent`: typed client observation of a historically meaningful local
  result; it remains a candidate until WorldEngine accepts it.
- `PublicProjection`: redaction-safe session read model with session ID, tick,
  revision, state hash, public entities/Agents, allowed actions, and event
  cursor.
- `AgentExperienceRef`: public reference from a later Agent decision to prior
  accepted events/action results. It is not private memory or raw thought.
- `EvidenceBundle`: public package, event, diff, snapshot, Agent, direction,
  projection, and request-correlation evidence for an external checker.

## Protocol Operations

The implementation may refine resource names during documentation review, but
it must preserve these generic operations:

```text
GET  /health
GET  /api/v1/capabilities
GET  /openapi.json
POST /api/v1/world-packages
GET  /api/v1/world-packages/{package_id}
POST /api/v1/sessions
GET  /api/v1/sessions/{session_id}
POST /api/v1/sessions/{session_id}/steps
POST /api/v1/sessions/{session_id}/directions
POST /api/v1/sessions/{session_id}/actions
POST /api/v1/sessions/{session_id}/feedback
GET  /api/v1/sessions/{session_id}/projection
GET  /api/v1/sessions/{session_id}/events?after_sequence={sequence}
GET  /api/v1/sessions/{session_id}/evidence
```

The capability manifest must identify the engine build, running instance,
contract/schema version, and every public operation by `operation_id`, method,
path, and maturity.

The public contract must not contain Godot node, scene-tree, animation,
collision-shape, frame, or engine-specific types.

## Required Behavior

1. The same normalized `WorldBrief` and seed produce the same
   `RunnableWorldPackage.package_hash`.
2. A ready session records the exact `source_package_hash`; its initial
   snapshot, canonical state, and public projection share revision and state
   hash.
3. `step N` advances exactly N ticks. Tick, world time, event sequence, and
   revision are monotonic.
4. Every accepted canonical mutation has an accepted event and non-empty
   applied diff. Rejected requests have a public reason and no applied diff.
5. At least one Agent cycle records perception, decision/intent,
   `ActionRequest`, rule judgment, `ActionResult`, event, and diff references.
6. A later Agent decision contains at least one `AgentExperienceRef` to a prior
   public event or action result and changes its public decision evidence in a
   machine-observable way.
7. The same `InterventionWindow` accepts one bounded direction and rejects one
   direct-final-fact request. The rejection must be semantic, not merely
   "window closed."
8. Accepted direction enters a queue or candidate path and is applied only by
   later rule evaluation. It cannot directly patch canonical state.
9. `ActionRequest` and `FeedbackEvent` use request IDs. Duplicate IDs are
   idempotent and return the original public result.
10. A stale expected revision is rejected with a stable conflict result rather
    than silently overwriting newer state.
11. The administration console performs all mutations through these APIs and
    displays the same session ID, tick, revision, and state hash returned by
    the public projection.
12. A black-box client with only base URL and capability manifest can generate,
    boot, step, submit both directions, inspect the Agent, poll events, and
    export evidence.

## Allowed Changes

- Add new generic engine modules under `backend/app/`.
- Add versioned schemas under `backend/app/schemas/`.
- Add a versioned router under `backend/app/api/routes/` and register it in the
  active app factory.
- Add process-local stores required by the deterministic MVP.
- Add administration-console API client, page, components, and navigation under
  `frontend/src/`.
- Add focused backend tests under `backend/app/tests/` and frontend/E2E tests
  under `frontend/`.
- Update v0.13 docs and project entrypoints listed by this package review.

## Forbidden Changes

- No new runtime feature under `backend/worldengine/`.
- No concrete demo/validation world, character, map, location, item, story rule,
  or visual asset in WorldEngine source or tests.
- No Godot code, scene, project, or engine-specific schema in WorldEngine.
- No external repository changes during `0.13.0`.
- No live-provider requirement, provider key, raw prompt/response, provider
  trace, raw thought, chain-of-thought, private memory, private goal, or hidden
  context in public state or evidence.
- No client-provided state patch, final fact, Agent thought, action result, or
  checker verdict accepted as canonical truth.
- No direct frontend access to storage or core Python objects.
- No production persistence, migration, distributed execution, deployment, or
  complete v0.13 PASS claim.
- No deletion or reversion of pre-existing dirty work solely to make the new
  package easier.

## Compatibility Requirements

- The new contract is design-first and may use a new `/api/v1` surface rather
  than inheriting current endpoints.
- Existing public surfaces must remain available during `0.13.0` unless this
  contract is explicitly revised and approved to deprecate them.
- Existing dirty files are user-owned and must be incorporated or left alone.
- Reused code must pass v0.13 tests; historical tests alone are insufficient.
- Event and evidence additions must be public, deterministic, and redaction
  safe.

## Out-of-Scope Follow-ups

- Godot executor and external checker: `0.13.1`.
- Full cross-client run and final classification: `0.13.2`.
- Live LLM generation/decision quality, persistence, recovery, branches,
  recursive worlds, multi-Agent behavior, and deeper pseudo-self: later
  reviewed versions after the anchor passes.

## Exit Criteria

- User approves this contract, design, test plan, and plan.
- Read-only documentation/contract evaluator reports no P1/P2.
- `implementation_authorized: yes` is recorded before code changes.
- Current focused verification proves all required behavior owned by this
  package.
- Review records exact changed files, commands, tests, compatibility, scope,
  and evaluator evidence with no unresolved P1/P2.
