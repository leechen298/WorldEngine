# v0.13 Minimum Runnable MVP Anchor

Chinese mirror: `README.zh.md`.

Status: documentation preparation / active child 0.13.1
Type: mixed goal campaign
implementation_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## Goal Entry

Natural-language goal aliases:

```text
complete v0.13 minimum runnable MVP
finish v0.13 minimum runnable MVP
完成 v0.13 最小可运行 MVP
做出一个能跑的 MVP 版本
```

Goal runner: `GOAL_RUNNER.md`.

## Goal

Deliver one small but complete vertical slice that proves this product loop:

```text
world brief
-> runnable world package
-> session boot
-> bounded world steps
-> Agent observes, decides, and proposes an action
-> WorldEngine accepts or rejects through public rules
-> one accepted and one rejected operator intervention
-> event, diff, snapshot, Agent experience, and projection evidence
-> administration console and generic client protocol observe the same run
-> external Godot executor and checker classify the run
```

The version optimizes for the smallest path that is unlikely to be blocked. It
must not depend on a live LLM provider, real-time networking, production
persistence, a polished game, or a third external repository before the core
loop can run.

## Direction Reset

The v0.10-v0.12 documents and implementation evidence remain historical
background. They do not define the v0.13 target architecture and do not prove
this anchor run. Existing code may be reused only after it is checked against
the v0.13 contract; it must not narrow or rewrite the target flow.

This reset does not delete or revert existing work. It creates a new reviewed
contract for deciding what is retained, replaced, or isolated.

## Repository Ownership

| Repository | Owns | Must not own |
| --- | --- | --- |
| `WorldEngine` | Generic world generation/runtime/Agent contracts, canonical history, public client protocol, administration console, public evidence export | Concrete validation world, Godot scenes, external oracle, client-authored canonical facts |
| `WorldEngine-Validation-Client` | Godot scenario executor, concrete external anchor world, operation capture, independent checker, final external result directory | Provider ownership, WorldEngine internals, direct database access, canonical mutation outside public APIs |

WorldEngine remains authoritative for canonical world facts and event legality.
The external checker is authoritative only for whether the recorded public
evidence supports this validation suite's verdict; it cannot redefine world
truth.

v0.13 does not create a third repository. The external repository must keep the
Godot executor and checker in separate packages/processes so the executor
cannot declare its own success.

## Package Sequence

1. `0.13.0-worldengine-runnable-anchor`
   - Closed: the WorldEngine-side headless loop, generic HTTP protocol,
     administration console, and public evidence bundle are verified for the
     package scope. Full backend regression remains `484 passed, 1 failed` and
     is not represented as a clean repository-wide PASS.
2. `0.13.1-godot-validation-client-anchor`
   - Current documentation-preparation child. Prepare and review the external
     milestone before authorizing any Godot, checker, Web, API, or external
     repository change.
3. `0.13.2-anchor-run-validation-and-closeout`
   - Run the same external scenario through WorldEngine, the administration
     console, Godot, and the checker; close as `PASS`, `PARTIAL`, `BLOCKED`, or
     `FAIL` from current evidence.

Only the active child may authorize implementation. Planned later children do
not authorize code or external-repository changes.

## Current Active Package

`0.13.0-worldengine-runnable-anchor` is closed for its WorldEngine-side scope.
The current active child is `0.13.1-godot-validation-client-anchor` in
documentation-preparation state only. Its implementation, external repository
changes, and evidence execution are not authorized. Complete v0.13 remains
unproven until the Godot/checker packages execute and `0.13.2` records the
correlated result.

## MVP Non-goals

- No live-provider dependency for the required acceptance path.
- No per-frame WorldEngine/Godot synchronization.
- No WebSocket requirement; cursor-based HTTP polling is sufficient.
- No production database, distributed runtime, multiplayer, or deployment.
- No polished game art, combat system, economy, full inventory simulation, or
  game distribution.
- No multi-Agent society, recursive child worlds, full personality model, raw
  thought, or private memory exposure.
- No concrete anchor-world content inside the WorldEngine repository.
- No claim that v0.10-v0.12 historical evidence passes v0.13.

## Campaign Exit Criteria

v0.13 is complete only when:

- the WorldEngine-side anchor loop runs from a clean start.
- the administration console operates only through public/control APIs.
- the generic client protocol is not Godot-specific.
- one legal intervention is accepted through rules and one direct-fact
  intervention is rejected with evidence.
- at least one later Agent decision cites a prior public event or experience.
- Godot observes the same public state and returns at least one typed feedback
  event through the public protocol.
- the independent checker correlates WorldEngine and Godot evidence and emits a
  current `PASS`, `PARTIAL`, `BLOCKED`, or `FAIL` result.
- no unresolved P1/P2 finding remains.
