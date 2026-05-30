# External Fixture Runner Contract

Status: review complete

## Purpose

This contract defines how external fixture runners may consume WorldEngine
through public contracts without placing external fixture repositories,
concrete worlds, private oracle logic, or product validation applications
inside the WorldEngine core repository.

External fixture runners are consumers. They may exercise public WorldEngine
behavior and return redacted evidence, but they must not drive core
abstractions from private fixture internals.

## Public Concepts

- `ExternalFixtureRunner`: an external process, repository, or automation
  suite that invokes WorldEngine through public contracts.
- `ExternalSuiteId`: a stable abstract identifier for the external suite.
- `RedactedTargetId`: a stable abstract identifier for the target fixture or
  scenario after all consumer-specific naming has been removed.
- `PublicContractSurface`: a documented API, CLI, schema, or exported
  contract that an external runner is allowed to invoke.
- `RedactedValidationReport`: a report that records public behavior,
  pass/fail state, compatibility notes, and unresolved findings without
  leaking external-world internals.

## Allowed Consumption Surfaces

An external fixture runner may consume only public WorldEngine surfaces:

- public API routes documented or reviewed by the active package.
- public CLI contracts documented or reviewed by the active package.
- schema contracts under `docs/contracts/`.
- exported validation or report templates.
- redacted package review evidence.

For v0.3, the relevant public contract chain is:

1. `docs/contracts/worldspec-contract.md`
2. `docs/contracts/worldspec-loader-contract.md`
3. `docs/contracts/runtime-context-bridge-contract.md`
4. `docs/contracts/external-fixture-runner-contract.md`
5. `docs/validation-report-template.md`

The runner must not require private module imports, private reset endpoints,
database internals, UI selectors, hidden oracle state, or repository-local
fixture paths from WorldEngine core.

## Redacted Validation Report Shape

WorldEngine may accept or archive redacted external evidence only when it
follows `docs/validation-report-template.md` and includes:

- report id.
- engine commit.
- public API / CLI version or contract version.
- external suite id.
- redacted target id.
- capability area.
- abstract scenario id.
- high-level goal.
- status: `pass`, `fail`, or `blocked`.
- observed public behavior.
- redacted evidence summary.
- compatibility notes.
- unresolved issues.
- public contract exercised.
- core repository behavior affected.
- explicit redaction confirmation.

The report must describe any requested follow-up as a generic engine
capability or contract gap. It must not describe a consumer-specific feature
request as if it were an engine abstraction.

## Required Redaction Rules

External evidence stored in this repository must not contain:

- concrete external world names.
- character names.
- location names.
- story rules.
- seed data.
- validation oracle internals.
- UI selectors.
- hidden reset API details.
- private fixture repository paths.
- non-redacted transcripts.
- non-redacted event payloads from the external consumer.

Abstract identifiers such as `external-suite-001`, `target-redacted-001`, and
`scenario-001` are allowed.

## Compatibility Constraints

- WorldEngine core remains generic.
- External fixture runners remain consumers of public contracts.
- Loader and bridge behavior must not be narrowed to satisfy one external
  consumer.
- Runtime, schema, API, event, archive, params, frontend, fixture, migration,
  and legacy behavior are unchanged by this documentation-only contract.
- Any later code change requested by external evidence must go through a
  separate reviewed iteration package and must be described in generic engine
  terms.

## Forbidden Inferences

This contract does not authorize:

- creation of an external fixture repository inside WorldEngine.
- addition of concrete fixture data.
- addition of concrete external world names.
- loader, bridge, runtime, API, schema, event, archive, params, frontend,
  fixture, migration, or test implementation changes.
- reset API internals.
- private validation oracle behavior.
- product validation app implementation.
- projection API implementation.
- Agent-in-World loop, memory, self-continuity, story generation, NPC chat,
  or world generation.

## Acceptance Requirements

The contract is ready for review only if:

- allowed consumption surfaces are explicitly limited to public contracts.
- redacted report fields are testable against
  `docs/validation-report-template.md`.
- forbidden leaked details are explicitly listed.
- external runners are identified as consumers, not core implementation.
- examples use only abstract identifiers.
- the package review records documentation-only verification and states that
  runtime/build/test evidence was not run.

## Handoff

After review, future external fixture repositories may use this contract as
the public boundary for invoking WorldEngine. Any core change requested by
external evidence must be handled by a later reviewed package and must not
import private consumer details into this repository.
