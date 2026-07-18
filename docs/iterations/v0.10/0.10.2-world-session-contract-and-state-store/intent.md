# Intent

## Problem / Purpose

v0.10 needs one stable unit that external clients and the dashboard can
create, inspect, run later, and export. Existing world and runtime surfaces are
useful but are not tied together as a single session.

## Why Now

`0.10.1` made session surfaces discoverable but unavailable. The next step is
to make the session identity and status store real before worldview creation
and bounded runtime attach to it.

## Relationship To Roadmap

This package implements the v0.10 planned "World Session Contract And State
Store" slice only. `0.10.3` owns worldview-to-runtime session creation.
`0.10.4` owns bounded session runtime and snapshot evidence.

## Non-Goals

- No generated world content from worldview input.
- No runtime execution through sessions.
- No dashboard UI.
- No durable database.
- No provider live calls or quality claims.
- No Validation Client implementation or external validation PASS.

## Expected Handoff

After closeout, `0.10.3` can create sessions from worldview input using this
public session unit instead of inventing a separate identity/status contract.
