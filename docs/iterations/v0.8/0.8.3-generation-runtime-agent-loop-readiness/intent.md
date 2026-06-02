# Intent

## Objective

Define and, after review, optionally implement the smallest generic
generation/runtime/Agent-loop readiness path that supports v0.8 without
turning WorldEngine into an external validator.

## Problem

v0.6 generation can create or preview `WorldSpec` material. Runtime readiness
can validate a candidate `WorldSpec` and summarize runtime context. The Agent
loop can build bounded perception and execute a deterministic `noop`. These
capabilities are adjacent but not yet packaged as one explicit core-side
readiness probe.

Without that probe, v0.8 cannot make a narrow current-session claim that a
candidate generated world can pass through the minimum generic core loop. At
the same time, implementing a full generated-world runtime, external
validator, product app, or live provider flow would exceed v0.8 current scope.

## Intended Outcome

After review, this package may authorize a read-only, isolated probe that:

1. accepts a generic generation preview input or candidate `WorldSpec`.
2. derives runtime readiness using existing loader/runtime-context semantics.
3. creates an isolated in-memory runtime context without mutating app runtime.
4. advances the isolated runtime once and records bounded event evidence.
5. runs the default Agent loop `noop` against bounded perception.
6. returns only redacted, generic evidence.

## Non-Goals

- No generated-world active runtime execution in the app runtime.
- No external validator implementation.
- No external application, UI, product workflow, or deployment.
- No public memory management API.
- No pseudo-self implementation, self-narrative, relationship history,
  personality drift, or long-term preference surface.
- No live AI provider call or generation-quality judgment.

## Handoff Criteria

The package may hand off to `0.8.4` only when review records either:

- implementation evidence for the bounded core-readiness probe, or
- an explicit deferral reason and the exact missing evidence that blocks the
  minimum loop claim.
