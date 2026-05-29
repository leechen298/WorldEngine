# Intent

## Problem / Purpose

v0.3 final closeout recorded no fresh runtime, API, frontend, schema, fixture,
migration, build, E2E, Agent smoke, or backend regression execution during
0.3.8. This package defines the validation plan needed before a future
execution package can produce independent evidence.

## Why Now

v0.3 delivered loader and bridge infrastructure. The remaining validation
risk is not whether the docs say v0.3 closed, but whether a fresh validation
run can recheck the loader, bridge, runtime/API compatibility, Event.refs
response shape, and E2E availability without relying only on historical package
evidence.

## Relationship To Roadmap

This package protects the handoff from v0.3 to v0.4. v0.4 may still start only
through its own reviewed iteration package.

## Non-Goals

- Execute tests.
- Repair implementation.
- Change runtime behavior.
- Add or change API routes.
- Add fixtures or demo-world content.
- Create external repositories.
- Change v0.3 release status.

## Expected Handoff

After review, `02-e2e-validation-execution` can use this plan to run or block
the validation commands and fill its report.
