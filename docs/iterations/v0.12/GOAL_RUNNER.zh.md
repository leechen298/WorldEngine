# Goal Runner

英文版本：`GOAL_RUNNER.md`。

状态：`closeout complete / PARTIAL`

## Goal Entry

本 campaign 覆盖的自然语言目标包括：

```text
完成 v0.12
开发 v0.12
生成 v0.12 文档
编写 v0.12 文档
启动 WorldEngine v0.12：MVP Agent Continuity And Validation Automation
```

当前 route 记录在 `CURRENT_STATE.md`。Implementation authorization 默认关闭。

## Route Selection

1. 读取 `CURRENT_STATE.md`。
2. 读取 `README.md`、`CAMPAIGN_PLAN.md` 和 `v0.12-plan.md`。
3. 在 implementation 或 evidence execution 前，把 active planned child 转成 concrete
   child package docs。
4. 对任何 child package，按顺序读取：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
5. active child review 记录 `implementation_authorized: yes` 前，不得实现。

## MVP Scope Rule

v0.12 是第一次可以声明 complete MVP validation 的地方。这个声明必须来自 exported public
artifacts 的 checker、scorecard 和 read-only review evidence。

在 v0.12 文档和证据中，除非明确写成“external validation agent”，否则“Agent”指世界内
Agent。Codex/OpenClaw 这类 Agent 从世界外操作。Narrative 和 diagnostic surfaces 可以面向用户，
但只能作为基于 public evidence 的 read-only inspection。

## Stop Conditions

以下情况必须在 implementation 或 closeout 前停止：

- active child 未授权就实现代码。
- 在 client 中脚本化 Agent autonomy。
- 泄露 raw thought、raw chain-of-thought、private memory、private goals、secrets、
  raw prompts、raw provider responses 或 hidden context。
- 默认把 diagnostic conversation 写入 in-world memory。
- narrative projection 修改 canonical state。
- 把 external validation agent 表述成世界内 Agent 或玩家。
- 使用 narrative 或 diagnostic surfaces 绕过 direction queue 引导世界演化。
- 在本仓库实现 Validation Client code。
- 没有 checker/scorecard/review evidence 就声明 MVP PASS。
