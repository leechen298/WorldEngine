# Scope Boundaries

Status: authoritative boundary guide

## Global Rules

- WorldEngine must stay aligned with `docs/project-north-star.md`.
- WorldEngine core repository must not contain concrete demo worlds.
- External fixture and validation worlds must not be stored as core repository
  fixtures, acceptance targets, loader test inputs, or projection targets.
- External fixture and validation worlds may consume WorldEngine only through
  public APIs, CLI commands, schemas, exported contracts, and redacted
  validation reports.
- The core repository may define schemas, runtime contracts, event contracts,
  agent contracts, memory/self-continuity contracts, projection contracts, and
  redacted report formats.
- The core repository must not store external-world seed data, characters,
  locations, story rules, validation oracle internals, or
  application-specific backend logic.
- WorldEngine owns provider configuration and provider calls when core
  capabilities require LLM behavior. External clients must not become the
  authority for provider calls, provider keys, or evaluator decisions.
- Redacted public summaries are allowed. API keys, authorization headers, raw
  prompts, raw provider responses, raw provider traces, raw thought, private
  memory payloads, private goals, and hidden context must not become public
  evidence.
- Agent memory, personality, and skill changes must not be assumed to mutate
  automatically on every tick. Consolidation through sleep, rest, or
  low-activity phases must be explicit when a package owns that behavior.
- Narrative projection, replay views, and out-of-world diagnostic
  conversations are external inspection surfaces by default. They must not
  mutate canonical world state, world timelines, or Agent memory unless a
  reviewed package explicitly creates that bridge.
- In the MVP track, the user or player is an external operator, not an
  in-world entity. WorldEngine must not implement player item drops, direct
  detailed event triggering, or player-as-world-entity gameplay unless a
  later reviewed package explicitly changes that boundary.
- User guidance must not directly assign final facts. "This Agent dies now" is
  not valid direction; "this Agent may face a lightning-strike risk" may be
  accepted only as external pressure that WorldEngine evaluates through
  weather, location, probability, life state, and public rules.
- Worldline branches and forks are timeline branches for replay, comparison,
  and validation, similar to code branches. They must not be described as
  parent/child worlds, source worlds, or origin hierarchies unless a reviewed
  recursive-world package explicitly introduces that relationship.
- Documents and evidence must distinguish in-world Agents from external
  validation agents such as Codex or OpenClaw.
- Code work must be scoped to one iteration package.
- Schema changes must be additive unless the current contract allows breaking
  changes.
- Runtime behavior must be preserved unless the current contract explicitly
  changes it.

## v0.2 Does

v0.2 Recursive World Foundation may:

- add the north star and documentation governance.
- define WorldCell and WorldSpec at the schema/spec layer.
- define shared references such as EntityRef.
- add optional event structure fields.
- add generic schema smoke validation.
- define the boundary for external fixture and validation consumers.
- mark `backend/worldengine/` as legacy.
- preserve existing runtime behavior.

## v0.2 Does Not

v0.2 must not:

- fully migrate RuntimeEngine to WorldCell.
- implement agent inner-world as WorldCell.
- implement full world generation.
- implement demo-specific runtime.
- create a separate game repository.
- add vector memory.
- add multi-agent society simulation.
- implement agent pseudo-self continuity.
- modify the frontend dashboard unless an iteration contract explicitly says so.

## Future Boundaries

- v0.3 may bridge generic WorldSpec into runtime loading.
- v0.3.5 may define external fixture contract readiness.
- v0.4 may add the minimal agent-in-world loop.
- v0.5 may add memory and self-continuity.
- v0.6 may add world generation v1.
- v0.7 may prepare external validation and projection consumer readiness.
- v0.8 may prepare the core-side minimum working-state boundary and public
  surfaces needed by an external validation function.
- v0.9 may prepare the first LLM-backed lifecycle foundation, including
  WorldEngine-owned provider calls, generated world rules, bounded runtime
  control, world-level direction, rule-linked event legality, brain-inspired
  Agent continuity/consolidation evidence, and external narrative/diagnostic
  projection boundaries.
- v0.10 may start the MVP track by defining the public debug contract and
  first runnable world session, including bounded runtime controls,
  events/snapshots, public discovery, and replay/worldline branch terminology.
- v0.11 may make the MVP world evolve through public rules, parameters,
  direction boundaries, event legality, diffs, and worldview fidelity evidence.
- v0.12 may complete the MVP through public Agent continuity, memory/rest
  consolidation evidence, read-only narrative/diagnostic inspection, external
  validation-client evidence handoff, and checker-backed lifecycle
  classification.
- Post-v0.9 version boundaries are summarized here and governed in detail by
  `docs/project-plan.md`, `docs/roadmap.md`, and the matching
  `docs/iterations/v*/` package documents.
