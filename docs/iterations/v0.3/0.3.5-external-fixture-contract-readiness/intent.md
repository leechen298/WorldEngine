# Intent

## Problem

v0.3 has moved `WorldSpec` loading and runtime context bridging toward public
engine boundaries. The next risk is that future external validation work could
pull concrete fixture worlds, private oracle details, reset mechanics, or
product-specific assumptions into the core repository.

WorldEngine needs a clear public contract for external fixture runners before
external validation becomes operational.

## Intent

Define a documentation-only contract that lets external fixture runners
consume WorldEngine as public engine surface area:

- public API or CLI contracts.
- schema and exported contract docs.
- reviewed loader and runtime bridge contracts.
- redacted validation report templates.

The contract must keep external fixture repositories outside the core
repository and require reports to use abstract identifiers and redacted
evidence.

## Non-Goals

- Do not implement an external fixture runner.
- Do not create an external fixture repository.
- Do not add concrete fixture data or test inputs.
- Do not add concrete external world names, characters, locations, story
  rules, or seed data.
- Do not add private oracle behavior, reset API internals, or UI selectors.
- Do not change runtime, schema, API, event, archive, params, frontend,
  fixture, migration, or test implementation files.
- Do not implement projection, Agent-in-World loops, memory, self-continuity,
  story generation, NPC chat, or world generation.

## Acceptance

- The external fixture runner contract exists and uses only public WorldEngine
  concepts.
- The package docs are complete and ready for review.
- The package README and v0.3 milestone index mark 0.3.5 as
  `ready for review`.
- Verification requirements are testable with documentation checks.
- Assumptions and open risks are explicit.
