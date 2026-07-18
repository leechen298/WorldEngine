# Campaign Plan

Chinese mirror: `CAMPAIGN_PLAN.zh.md`.

Status: closeout PASS / handed off to v0.11

## Objective

Run v0.10 as a review-gated `/goal` campaign that creates the MVP debug
contract and first runnable world session.

The campaign objective is to make WorldEngine capable of:

- creating a session from worldview input.
- exposing a correct MVP manifest and checker handoff skeleton.
- loading initial public world state into runtime.
- running the session with bounded controls.
- recording events, diffs, and snapshots.
- preserving replay/worldline branch terminology as code-branch-like timeline
  branches, not parent/source-world relationships.
- showing the flow in the dashboard.
- exposing enough public discovery/evidence for external client debugging.

## Authoritative Inputs Read For Parent Drafting

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-plan.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`

## Campaign Rules

- Parent `v0.10` docs are the campaign entrypoint.
- Planned `0.10.x` sections in `v0.10-plan.md` do not authorize
  implementation.
- Code/mixed children require complete package docs and review before
  implementation.
- Validation Client remains external.
- The user/player remains an external operator; v0.10 must not implement
  player-in-world gameplay, item drops, or direct detailed event triggering.
- MVP claims must be backed by current-session command evidence.
- Chinese mirrors must preserve status, scope, forbidden changes,
  compatibility constraints, findings, and final assessment semantics.

## Campaign Exit Criteria

v0.10 can close only when:

- active child packages are review complete or explicitly deferred.
- a worldview can create a runnable session.
- bounded run controls and snapshots are evidenced.
- dashboard create/run/inspect flow is evidenced.
- manifest or public discovery identifies the session surfaces and preserves
  blocked/not_run/pass/fail status honestly.
- no P1/P2 finding remains without accepted rationale.

## Handoff

If v0.10 closes as PASS or acceptable PARTIAL, v0.11 starts from a runnable
session and adds rule-bound world evolution. Living Agent continuity remains a
v0.12 responsibility.
