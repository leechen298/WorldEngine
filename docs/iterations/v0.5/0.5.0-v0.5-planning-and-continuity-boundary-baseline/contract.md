# Contract

Status: planned / ready for review

## Public Concepts

- `v0.5 Memory and Self-Continuity Substrate`: the version boundary for
  inspectable agent memory and engineered pseudo-self continuity.
- `Working memory`: bounded current-context memory with provenance and explicit
  lifetime semantics.
- `Episodic memory`: event-linked records of agent experience, action outcomes,
  world time, and evidence.
- `Relationship state`: structured relationship semantics between agents,
  entities, or world references, contract-only in the initial implementation
  slice.
- `Self-summary`: inspectable summary of an agent's continuity state,
  contract-only until summarization behavior is reviewed.
- `Reflection record`: reviewable record of agent self-assessment or feedback
  processing, contract-only until automatic reflection is reviewed.
- `Personality drift signal`: inspectable signal that may later inform future
  action, contract-only until action-modifier behavior is reviewed.

## Capability Split

| Capability | This package | First implementation candidate |
| --- | --- | --- |
| Working memory | define boundary | yes, in `0.5.2` |
| Episodic memory | define boundary | yes, in `0.5.2` |
| Relationship state | define boundary | no behavior yet |
| Self-summary | define boundary | no summarization yet |
| Reflection records | define boundary | no automatic reflection yet |
| Personality drift signals | define boundary | no action modifier yet |

## Compatibility Constraints

- Existing v0.4 Agent Loop schemas and APIs remain unchanged in `0.5.0`.
- `PerceptionFrame`, `ActionIntent`, `ActionResult`, request-scoped
  `LoopStep`, and `POST /world/agent/loop/step` are compatibility-sensitive.
- `/world/agent/params/propose-and-apply` remains available and unchanged.
- Runtime tick/time behavior, API envelope/error shape, event routes, params
  behavior, archive behavior, and optional `Event.refs` serialization remain
  compatibility-sensitive.
- Future schema changes must be additive unless a later reviewed child
  explicitly allows a breaking change.
- v0.4 and post-closeout command evidence is handoff evidence only, not current
  v0.5 pass evidence.

## Allowed Changes

- Create `docs/iterations/v0.5/**` documentation.
- Create parent campaign files, child package files, Chinese mirrors, review
  evidence, and package sequencing.
- Name planned future implementation paths without creating them:
  - `backend/app/schemas/agent_memory.py`
  - `backend/app/agent/memory.py` or equivalent approved path
  - `backend/app/tests/test_agent_memory_*.py`
- Record subagent/evaluator findings from read-only review.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, fixture,
  migration, generated result, external repository, or `backend/worldengine/`
  implementation files.
- Do not create planned future implementation paths in this package.
- Do not add memory store behavior, loop integration, action modifiers, public
  runtime APIs, durable persistence, migrations, frontend behavior, or tests.
- Do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, UI-specific app behavior, private validation oracle
  details, world generation, external validation readiness, or projection app
  readiness.

## North Star Check

This package aligns with the north star by preparing memory, relationship
history, self-narrative, and personality drift as inspectable engineered
contracts. It does not claim real consciousness and does not narrow
WorldEngine into a demo-specific or application-specific backend.

## Out-of-Scope Follow-ups

- `0.5.1`: public memory/self-continuity concept contracts and schema
  semantics.
- `0.5.2`: first working/episodic memory schema and in-memory substrate
  implementation.
- `0.5.3`: bounded read-only memory context in loop perception.
- Later packages: relationship behavior, self-summary generation, automatic
  reflection, and personality drift action modifiers.
- v0.6 world generation, v0.7 external validation readiness, and v0.8
  projection application readiness.

