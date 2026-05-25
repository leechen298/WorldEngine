# External Fixture Boundary

Status: core boundary guide

WorldEngine core is a generic recursive world generation and runtime engine.
Concrete validation applications, fixture suites, and projection products are
external consumers. They may validate WorldEngine, but they must not become
part of the engine core or drive internal abstractions from private details.

## Core May Define

WorldEngine core may define:

- schemas.
- public APIs.
- CLI contracts.
- runtime contracts.
- event contracts.
- agent contracts.
- memory and self-continuity contracts.
- projection contracts.
- exported validation contracts.
- redacted report formats.

## Core Must Not Contain

WorldEngine core must not contain:

- concrete validation world seed data.
- domain-specific demo world names.
- characters.
- locations.
- story rules.
- game UI.
- application-specific backend logic.
- external validation oracle internals.
- hidden fixture reset logic.
- private runner state for external validation suites.

## Consumer Boundary

Future external fixture or validation repositories may contain concrete worlds.
WorldEngine core must interact with them only through public APIs, CLI
commands, schemas, exported contracts, or redacted reports.

When an external consumer reveals a missing engine capability, the core change
must be described in generic engine terms before implementation. Do not copy
consumer-specific entities, map concepts, story mechanics, UI selectors, seed
data, or validation oracle details into this repository.

## Evidence Boundary

The core repository may store redacted validation evidence that proves a public
contract was exercised. Evidence must describe public behavior, compatibility
impact, commands, pass/fail state, and unresolved findings without exposing
external consumer internals.
