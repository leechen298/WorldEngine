# Scope Boundaries

Status: authoritative boundary guide

## Global Rules

- WorldEngine must stay aligned with `docs/project-north-star.md`.
- The first game surface must not redefine the engine as a village-game
  backend.
- Tiny Village may be used early as a reference fixture or acceptance target,
  but it must not become game-specific runtime logic before an iteration
  contract explicitly allows that work.
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
- add a reference WorldSpec fixture.
- mark `backend/worldengine/` as legacy.
- preserve existing runtime behavior.

## v0.2 Does Not

v0.2 must not:

- fully migrate RuntimeEngine to WorldCell.
- implement agent inner-world as WorldCell.
- implement full world generation.
- implement village game runtime.
- create a separate game repository.
- add vector memory.
- add multi-agent society simulation.
- implement agent pseudo-self continuity.
- modify the frontend dashboard unless an iteration contract explicitly says so.

## Future Boundaries

- v0.3 may bridge WorldSpec into runtime loading.
- v0.4 may add the minimal agent-in-world loop.
- v0.5 may add memory and self-continuity.
- v0.6 may add world generation v1.
- v0.7 may build the reference village world.
- v0.8 may start the first game surface.
