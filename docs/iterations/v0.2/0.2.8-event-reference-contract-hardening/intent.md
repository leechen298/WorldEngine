# Intent

## Problem

v0.2 introduced optional structured event references through `EventRef` and
`Event.refs`. Future memory, causality, projection, and agent-in-world systems
will need a clear reference contract, but v0.2 must not implement those
systems yet.

The current schema already supports event construction without refs, refs with
generic `id`, `kind`, optional `role`, default metadata, nested event pages,
and model dump / validate round trips. The remaining risk is that future work
could infer resolver behavior, timeline causality, runtime WorldCell binding,
or domain-specific reference kinds from an under-documented additive field.

## Goal

Define the documentation and implementation plan for hardening EventRef and
Event.refs as additive, event-local, domain-neutral reference structures with
testable acceptance criteria.

The successful implementation state is:

- `docs/contracts/event-ref-contract.md` documents EventRef and Event.refs.
- focused compatibility tests prove optional refs, default behavior,
  validation boundaries, nested event containers, and serialization round
  trips.
- existing event dictionaries without refs continue to validate.
- no resolver, causality engine, runtime binding, memory behavior, projection
  behavior, or domain-specific reference catalog is introduced.

## Non-goals

- Do not implement a referential integrity resolver.
- Do not implement a timeline causality engine.
- Do not bind refs to live WorldCell runtime state.
- Do not implement Agent action consequence logic.
- Do not implement memory, self-continuity, projection, generation, or
  world loading behavior.
- Do not modify API routes or API response shapes.
- Do not modify frontend behavior.
- Do not add concrete external-world fixtures, seed data, roles, locations,
  resources, story rules, product UI, or application-specific backend logic.
- Do not create external repositories.

## Why Now

0.2.7 hardened the recursive schema contracts. 0.2.8 is the matching event
contract hardening step before 0.2.9 audits schema, event, external boundary,
and legacy boundary evidence. Stable event reference semantics reduce risk
before v0.3 loader and later agent/memory/projection work begins.

## North Star Alignment

This package supports WorldEngine's event spine by clarifying how events can
carry structured references for future world, agent, memory, and projection
systems. It keeps the engine generic and does not narrow the repository into
a demo-specific backend or implement future runtime behavior early.
