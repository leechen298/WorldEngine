# v0.13 Goal Runner

Chinese mirror: `GOAL_RUNNER.zh.md`.

Status: documentation preparation active

## Goal Entry

Run this campaign when the user asks to complete the minimum runnable MVP or
equivalent v0.13 goal.

## Current Route

`0.13.0-worldengine-runnable-anchor` is closed for its WorldEngine-side scope.
The active child is `0.13.1-godot-validation-client-anchor` in documentation
preparation only. `implementation_authorized`,
`external_repository_changes_authorized`, and `evidence_execution_authorized`
remain `no`; prepare and review the external milestone before changing any
external code or running Godot/checker evidence.

## State Machine

1. Read `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, `v0.13-plan.md`, and the active
   child package in this order.
2. Treat only `active_child` as implementation scope.
3. Complete and verify the active child documentation.
4. Request a read-only documentation/contract evaluator.
5. Do not implement until the active child review records
   `implementation_authorized: yes` after user approval.
6. Implement only the active child contract.
7. Request implementation-scope, code-review, validation-evidence, and
   closeout-consistency evaluators at the gates defined by
   `docs/iterations/AGENTS.md`.
8. Update the active child `review.md` with current commands and evidence.
9. Advance `CURRENT_STATE.md` only after the active child exit criteria pass or
   the package records an honest blocker.

## Risk-based Gate Order

For `0.13.0`:

```text
documentation contract
-> generic protocol schemas
-> deterministic generation/session boot
-> runtime/event/diff/snapshot spine
-> Agent experience-linked second decision
-> accepted/rejected intervention
-> administration console
-> focused tests and API/UI smoke
-> closeout
```

For `0.13.1`, first read the external repository's `AGENTS.md` and create its
own reviewed milestone documents before modifying Godot, checker, Web, or API
files.

## Stop Conditions

Stop and update the active documents before continuing if:

- the implementation requires a live provider for the required path.
- a concrete validation world would enter the WorldEngine repository.
- the administration console would write canonical state outside APIs.
- the public client protocol contains Godot-specific node, scene-tree,
  animation, collision-shape, or frame semantics.
- a client action or feedback event can mutate canonical state without rule
  evaluation and event evidence.
- Agent continuity can be proven only from private state or raw thought.
- a checker imports WorldEngine internals or accepts executor self-assertions.
- an unresolved P1/P2 finding remains.

## Evidence Rule

Historical results are never current v0.13 evidence. A PASS claim requires
commands and artifacts produced in the current package run.
