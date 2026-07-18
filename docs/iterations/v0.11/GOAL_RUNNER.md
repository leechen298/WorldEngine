# Goal Runner

Chinese mirror: `GOAL_RUNNER.zh.md`.

Status: child package documentation review in progress

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.11
开发 v0.11
生成 v0.11 文档
编写 v0.11 文档
启动 WorldEngine v0.11：MVP Rule-Bound World Evolution
```

The current route is recorded in `CURRENT_STATE.md`. Implementation
authorization is closed by default.

## Route Selection

1. Read `CURRENT_STATE.md`.
2. Read `README.md`, `CAMPAIGN_PLAN.md`, and `v0.11-plan.md`.
3. Convert the active planned child into concrete child package docs before
   implementation or evidence execution.
4. For any child package, read files in this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
5. Do not implement until the active child review records
   `implementation_authorized: yes`.

## MVP Scope Rule

v0.11 is about world evolution, not Agent pseudo-self or final validation
automation. It must keep user direction as world-level guidance and make every
applied event/diff explainable through public rules, state, and legality
evidence.

Concrete boundary example: reject direct final facts such as "kill this Agent
now"; accept only processable pressure such as "this Agent may face
lightning-strike risk," and only if WorldEngine still evaluates outcome through
rules, state, probability, and legality.

## Stop Conditions

Stop before implementation or closeout if a task would:

- implement code before active child authorization.
- let user direction directly impose final facts.
- add player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- mutate Agent private state from direction guidance.
- leak raw provider data, secrets, private memory, raw thought, or hidden
  context.
- use hidden/private evaluator data as PASS evidence.
- claim Agent autonomy or complete MVP validation from v0.11 evidence.
