# v0.3 WorldSpec Loader and Runtime Bridge

Status: planned / in progress

## Goal

v0.3 establishes the path from the v0.2 recursive schema foundation toward a
validated generic WorldSpec loader and a minimal runtime context bridge while
preserving v0.1 runtime compatibility.

## Version Boundary

v0.3 may define and later implement:

- WorldSpec loader contract.
- minimal generic WorldSpec loader.
- runtime context bridge contract.
- minimal optional runtime context bridge.
- runtime, API, event, archive, params, frontend-facing, and legacy-path
  compatibility evidence.
- external fixture runner contract readiness.
- evidence and compatibility audit.
- release-candidate and final closeout documentation.

v0.3 must not implement:

- Agent-in-World loop.
- memory or self-continuity substrate.
- world generation.
- projection API for external product surfaces.
- product UI or game UI.
- concrete demo world fixture.
- concrete external validation world.
- external fixture repository.
- external validation repository.
- story generation.
- NPC chat system.
- self-awareness claims.

## Plan Sources

- Planning seed: `docs/iterations/v0.3/00-chatgpt-plan.md`
- Detailed package plan: `docs/iterations/v0.3/v0.3-plan.md`

## External Automation Consumption

WorldEngine provides iteration docs, package specs, verification expectations,
and review bundle templates that external automation controllers may consume.
WorldEngine does not implement the controller. Agent roles, retry loops,
scheduling, and orchestration belong to external automation.

## Why This Version Exists

v0.3 is infrastructure work, not product validation. It answers whether a
generic `WorldSpec` can move from schema data into the active runtime boundary
without breaking the v0.1 runtime scaffold.

The version should make later Agent and generation work possible by proving:

- a `WorldSpec` can be loaded and validated as generic engine input.
- loaded world data can become runtime context without replacing
  `RuntimeEngine`.
- existing runtime ticks, events, params, archive behavior, and API response
  shapes remain compatible.
- future external validation can consume public contracts instead of private
  core internals.

## Capability Progression

| Package | Capability question answered |
|---|---|
| 0.3.0 | Do we have the v0.3 boundary and compatibility gate? |
| 0.3.1 | Do we know what a WorldSpec loader must accept, return, and reject? |
| 0.3.2 | Can the core load and validate generic WorldSpec data? |
| 0.3.3 | Do we know how loaded world data may reach runtime context safely? |
| 0.3.4 | Can runtime hold optional world context without breaking old behavior? |
| 0.3.5 | Can external fixture runners consume only public contracts? |
| 0.3.6 | Do loader and bridge evidence prove compatibility and v0.4 handoff readiness? |
| 0.3.7 | Is the v0.3 release candidate reviewable? |
| 0.3.8 | Can v0.3 be closed out after review approval? |

## Package Index

### `0.3.0-v0.3-planning-and-compatibility-baseline`

Type: documentation-only
Status: review complete
Purpose: Establish v0.3 planning docs and the compatibility baseline without
implementing loader or bridge behavior.

### `0.3.1-worldspec-loader-contract`

Type: documentation-only
Status: review complete
Purpose: Define the WorldSpec loader contract before implementation.

### `0.3.2-worldspec-loader-implementation`

Type: mixed or code
Status: review complete
Purpose: Implement the minimal generic WorldSpec loader after the contract is
reviewed.

### `0.3.3-runtime-context-bridge-contract`

Type: documentation-only
Status: review complete
Purpose: Define how validated WorldSpec-derived context may reach the runtime
without changing runtime behavior yet.

### `0.3.4-runtime-context-bridge-implementation`

Type: mixed or code
Status: planned
Purpose: Implement the minimal optional runtime context bridge while preserving
existing runtime and API behavior.

### `0.3.5-external-fixture-contract-readiness`

Type: documentation-only or mixed
Status: planned
Purpose: Define how external fixture runners may consume public WorldEngine
contracts without creating external repositories inside core.

### `0.3.6-runtime-bridge-evidence-and-compatibility-audit`

Type: documentation-only or mixed
Status: planned
Purpose: Audit loader and bridge evidence, compatibility, and v0.4 handoff
readiness.

### `0.3.7-v0.3-release-candidate-bundle`

Type: documentation-only
Status: planned
Purpose: Prepare a release-candidate bundle for human / ChatGPT review without
declaring release status.

### `0.3.8-v0.3-final-closeout`

Type: documentation-only
Status: planned / gated
Purpose: Perform final closeout only after release-candidate review approval.
