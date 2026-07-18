# Current State

Chinese mirror: `CURRENT_STATE.zh.md`.

campaign_status: documentation preparation / active child 0.13.1
active_child: 0.13.1-godot-validation-client-anchor
implementation_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## Current Decision

`0.13.0-worldengine-runnable-anchor` is closed for its WorldEngine-side scope.
Its focused backend, frontend, E2E, black-box, browser, and evaluator gates
passed; the unrelated full-backend result remains recorded as
`484 passed, 1 failed`. The campaign now prepares `0.13.1` documentation so the
Godot adapter and independent checker can consume the generic protocol without
redefining it.

## Historical Evidence Policy

- v0.10-v0.12 documents and command results are archived background for this
  campaign.
- They do not prove v0.13 behavior.
- Existing implementation can be retained only after current tests prove that
  it satisfies the v0.13 contract.
- No existing dirty file may be reverted or overwritten merely because the new
  package chooses a different architecture.

## Next Action

Read the external repository governance and prepare the complete reviewed
`0.13.1-godot-validation-client-anchor` documentation package. Do not modify
Godot, checker, legacy Web/API, or any external repository file until that
package passes its documentation evaluator and receives explicit
implementation and external-repository authorization.
