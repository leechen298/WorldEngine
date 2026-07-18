# Goal Runner

Chinese mirror: `GOAL_RUNNER.zh.md`.

Status: closeout PASS / handed off to v0.11

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.10
开发 v0.10
生成 v0.10 文档
编写 v0.10 文档
启动 WorldEngine v0.10：MVP Debug Contract And Runnable World Session
```

The current route is recorded in `CURRENT_STATE.md`. Implementation
authorization is closed by default.

## Route Selection

1. Read `CURRENT_STATE.md`.
2. Read `README.md`, `CAMPAIGN_PLAN.md`, and `v0.10-plan.md`.
3. The current route is `v0.10-closeout-pass-v0.11-handoff-ready`.
4. If a future route points to a `*-documentation-package-needed` child, create or
   confirm that child's complete package document set before implementation or
   evidence execution.
5. For any child package, read files in this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
6. Do not implement until the active child package review records
   `implementation_authorized: yes`.

## MVP Scope Rule

v0.10 optimizes for a visible runnable session. Do not expand it into Agent
autonomy, full LLM quality validation, or external automated validation.
The user/player remains external; v0.10 must not turn the user into an
in-world entity or gameplay actor.

Required user-visible flow:

```text
enter worldview -> create session -> run bounded ticks -> inspect timeline/state/snapshots
```

## Stop Conditions

Stop before implementation or closeout if a task would:

- implement code before active child authorization.
- claim LLM-backed generation quality without live/checker evidence.
- create concrete demo-world content in this repository.
- move Validation Client implementation or provider ownership into
  WorldEngine.
- add player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- describe replay/worldline branches as parent/child worlds or source worlds.
- expose secrets, raw prompts, raw responses, raw thought, private Agent
  memory, or hidden context.
- treat v0.10 evidence as Agent autonomy or full MVP validation PASS.
