# Goal Runner

Chinese mirror: `GOAL_RUNNER.zh.md`.

Status: closeout complete / PARTIAL

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.12
开发 v0.12
生成 v0.12 文档
编写 v0.12 文档
启动 WorldEngine v0.12：MVP Agent Continuity And Validation Automation
```

The current route is recorded in `CURRENT_STATE.md`. Implementation
authorization is closed by default.

## Route Selection

1. Read `CURRENT_STATE.md`.
2. Read `README.md`, `CAMPAIGN_PLAN.md`, and `v0.12-plan.md`.
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

v0.12 is the first place where complete MVP validation can be claimed. That
claim requires checker, scorecard, and read-only review evidence from exported
public artifacts.

In v0.12 documents and evidence, "Agent" means an in-world Agent unless the
text explicitly says "external validation agent." Codex/OpenClaw-style agents
operate outside the world. Narrative and diagnostic surfaces may be user-facing,
but only as read-only inspection over public evidence.

## Stop Conditions

Stop before implementation or closeout if a task would:

- implement code before active child authorization.
- script Agent autonomy in the client.
- leak raw thought, raw chain-of-thought, private memory, private goals,
  secrets, raw prompts, raw provider responses, or hidden context.
- turn diagnostic conversation into in-world memory by default.
- mutate canonical state from narrative projection.
- represent an external validation agent as an in-world Agent or player.
- use narrative or diagnostic surfaces to steer world evolution outside the
  direction queue.
- implement Validation Client code inside this repository.
- claim MVP PASS without checker/scorecard/review evidence.
