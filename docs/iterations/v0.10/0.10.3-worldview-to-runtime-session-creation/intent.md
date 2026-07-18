# Intent

## Problem / Purpose

Users need to turn a worldview premise into a session unit. Existing
worldview generation returns public generated-world data, and `0.10.2`
created sessions, but the two are not connected.

## Why Now

`0.10.2` created session identity/status. The next MVP step is creating a
session from worldview input before bounded runtime attaches in `0.10.4`.

## Relationship To Roadmap

This package implements only the `0.10.3` planned slice. `0.10.4` owns
session run/snapshot evidence and `0.10.5` owns dashboard flow.

## Non-Goals

- No live provider quality claim.
- No runtime execution or snapshot creation.
- No dashboard UI.
- No Validation Client or checker implementation.

## Expected Handoff

`0.10.4` receives sessions that can carry public generation metadata and can
be driven by bounded runtime controls later.
