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
- v0.8 may prepare the first external projection application.
