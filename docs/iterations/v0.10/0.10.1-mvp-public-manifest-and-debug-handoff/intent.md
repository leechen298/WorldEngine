# Intent

## Problem / Purpose

WorldEngine already exposes a public `/manifest`, but it still carries older
version semantics and does not yet clearly describe the v0.10 MVP debug
handoff. Later session, runtime, dashboard, and validation work should not
depend on ambiguous discovery or status vocabulary.

This package makes the public manifest honest and useful for external client
debugging without moving client implementation or evaluator authority into
WorldEngine.

## Why Now

v0.10 starts with public discovery and debug handoff before deeper session
features. `0.10.0` closed the planning/handoff baseline and selected this
package as the next documentation gate.

## Relationship To Roadmap

The roadmap says v0.10 should align the public manifest/debug handoff contract
before creating the first runnable session slice. This package owns that
alignment only. World session storage begins in `0.10.2`; worldview session
creation begins in `0.10.3`; bounded session runtime begins in `0.10.4`.

## Non-Goals

- Do not implement Validation Client behavior.
- Do not implement v0.10 sessions, runtime controls, dashboard flow, or
  validation closeout.
- Do not run provider live calls or claim provider readiness PASS.
- Do not change checker code or fixtures.
- Do not expose raw prompts, raw provider payloads, secrets, private Agent
  state, hidden context, or private evaluator data.
- Do not describe replay/worldline branches as parent/child worlds or source
  worlds.

## Expected Handoff

After this package closes, `/manifest` should be stable enough for
`0.10.2-world-session-contract-and-state-store` to add real session surfaces
without redefining status taxonomy, provider ownership, redaction posture, or
external client role.
