# 0.8.2 Core Observable Surface Boundary

Status: review complete
Type: documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## Goal

Define the public core-side runtime, event, generation, Agent loop,
memory-context, archive, and read-model surfaces that a future external
validator may observe without making the validator, a projection application,
or product-specific behavior part of the core repository.

This package defines the observable surface boundary only. It does not
implement schemas, checkers, API routes, frontend behavior, tests, evidence
artifacts, external validation logic, or external application behavior.

## Observable Surface Boundary

Later reviewed packages may expose or harden these generic, read-only,
redacted surface families:

| Surface family | Public source boundary | Allowed observable summary |
| --- | --- | --- |
| runtime state | `/runtime/state`, `/runtime/step` evidence | tick, world time, public params summary, runtime-context summary, blocker status |
| event timeline | `/world/events`, `/world/event-steps` | event counts, event type summaries, tick ranges, public event refs |
| generation readiness | `/world/generation/*` | generation id, template/plan status, validation diagnostics, runtime-readiness status |
| Agent loop | `/world/agent/loop/step` | perception boundary, intent type, action result status, public evidence refs |
| memory context | existing bounded perception context only | counts, scope ids, provenance summaries, redacted bounded memory context |
| archive | `/world/snapshots`, `/world/summaries` | snapshot/summary ids, tick ranges, summary text, event counts |
| projection/read-model | v0.7 projection contracts | read-only family ids, allowed fields, redaction notes, no-write capability |
| handoff/readiness | v0.7 report/manifest contracts and later v0.8 handoff docs | public surface ids, evidence refs, status taxonomy, blockers, redaction confirmation |

Every future observable surface must be:

- generic to WorldEngine core.
- public and redacted.
- read-only unless a later reviewed package explicitly authorizes a generic
  write contract.
- additive and versioned when implemented.
- tied to current-session evidence before any pass claim is made.

## Forbidden Exposure

Observable surfaces must not expose:

- concrete validation worlds, app names, maps, locations, characters,
  resources, story rules, seed data, product routes, UI selectors, or private
  transcripts.
- hidden reset APIs, private runner state, private repository paths, oracle
  internals, provider traces, prompts, secrets, or non-redacted external event
  payloads.
- raw memory records, unrestricted memory export, pseudo-self internals,
  relationship history, reflection records, or personality drift internals
  beyond current reviewed contracts.
- write APIs, reset APIs, migrations, persistence, product UI, projection app
  behavior, or consumer-specific backend behavior.

## Scope

Allowed scope:

- Create this package document set and Chinese mirrors.
- Define generic observable surface families, public source boundaries,
  allowed summary classes, forbidden exposure, versioning rules, and
  implementation authorization criteria for later packages.
- Synchronize parent v0.8 route/status surfaces after review.
- Record documentation checks and evaluator findings.

Forbidden scope:

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  or `backend/worldengine/` implementation files.
- Do not add or edit `docs/contracts/` schemas, `tools/testing` checkers,
  API routes, service helpers, frontend routes, E2E tests, or evidence
  artifacts.
- Do not claim core observable surface readiness, runtime/API/frontend pass,
  minimum working-state evidence, external validation PASS, product readiness,
  projection readiness, or release readiness.

## Final Assessment State

Current value: `review complete`.

This package defines the observable surface boundary and hands off to
`0.8.3-generation-runtime-agent-loop-readiness` for reviewed implementation
planning and any future core-readiness hardening.
