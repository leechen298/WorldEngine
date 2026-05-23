# 0.1.4 Codex Test Skills

Status: ready for implementation

## Purpose

Add project-local Codex skills for WorldEngine E2E execution and Agent smoke
execution. The package makes the v0.1.3 verification rules easier for Codex to
follow consistently without changing runtime or product behavior.

## Package Type

Mixed package: project skill documentation plus a small sync script and Make
targets.

## Scope

- Add project-local skills under `.agents/skills/`.
- Add a sync command that copies the project skills into a local Codex skills
  directory.
- Document the skill behavior, validation commands, and review evidence.

## Non-goals

- No runtime features.
- No WorldSpec, WorldCell, recursive runtime, village, or game behavior.
- No changes under `backend/worldengine/`.
- No plugin package or marketplace entry.
