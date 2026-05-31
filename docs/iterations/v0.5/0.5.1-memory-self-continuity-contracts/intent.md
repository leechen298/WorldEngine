# Intent

Status: review complete

## Problem

v0.5 needs memory and self-continuity concepts to be precise before code
exists. Without a contract-first package, later implementation could blur
working memory, event-linked memory, relationship state, self narrative,
reflection, and drift into hidden side effects that are hard to inspect or
test.

The risk is higher because these concepts point toward agent pseudo-self.
WorldEngine must define them as engineered, inspectable records and signals,
not as claims of consciousness and not as application-specific behavior.

## Goal

After this package, WorldEngine has a stable public contract for:

- working memory.
- episodic memory.
- relationship state.
- self-summary.
- reflection record.
- personality drift signal.

The package also defines what `0.5.2` must prove before it may implement only
working memory and episodic memory substrate code.

## Non-goals

- Do not implement any backend schema, store, service, route, frontend, test,
  fixture, migration, or durable persistence behavior.
- Do not integrate memory context into `POST /world/agent/loop/step`.
- Do not modify action semantics, accepted action types, params patch
  semantics, event behavior, runtime tick behavior, or API envelope shape.
- Do not implement relationship behavior, self-summary generation, automatic
  reflection, or personality drift action modifiers.
- Do not add concrete world content, external validation internals, or
  application-specific backend logic.

## Why Now

The v0.5 roadmap goal is Memory and Self-Continuity Substrate. `0.5.0`
created the campaign boundary and split the version into review-gated child
packages. This package is the required contract layer between that planning
baseline and the first implementation package.

## North Star Alignment

The north star calls for agents that can accumulate memory, update through
feedback, and develop sustained pseudo-self through identity continuity,
self-narrative, relationship history, personality drift, and decision
patterns. This package supports that direction by defining inspectable
contracts while preserving the explicit boundary that WorldEngine does not
claim real consciousness.

## Expected Handoff

If reviewed successfully, this package hands off to
`0.5.2-working-and-episodic-memory-substrate` with implementation limited to
additive generic working-memory and episodic-memory schemas, an in-memory
substrate, and focused backend tests.
