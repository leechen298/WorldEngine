# Goal Runner

英文版本：`GOAL_RUNNER.md`。

状态：`closeout PASS / handed off to v0.11`

## Goal Entry

本 campaign 覆盖的自然语言目标包括：

```text
完成 v0.10
开发 v0.10
生成 v0.10 文档
编写 v0.10 文档
启动 WorldEngine v0.10：MVP Debug Contract And Runnable World Session
```

当前 route 记录在 `CURRENT_STATE.md`。Implementation authorization 默认关闭。

## Route Selection

1. 读取 `CURRENT_STATE.md`。
2. 读取 `README.md`、`CAMPAIGN_PLAN.md` 和 `v0.10-plan.md`。
3. 当前 route 是 `v0.10-closeout-pass-v0.11-handoff-ready`。
4. 如果未来 route 指向 `*-documentation-package-needed` child，先创建或确认该 child
   的完整 package document set，再进入 implementation 或 evidence execution。
5. 对任何 child package，按顺序读取：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
6. active child package 的 `review.md` 记录 `implementation_authorized: yes`
   前，不得实现。

## MVP Scope Rule

v0.10 优先做用户可见的 runnable session。不要把它扩展成 Agent autonomy、完整
LLM quality validation 或 external automated validation。用户/玩家保持为外部操作者；
v0.10 不得把用户变成世界内实体或 gameplay actor。

必需的用户可见流程：

```text
enter worldview -> create session -> run bounded ticks -> inspect timeline/state/snapshots
```

## Stop Conditions

以下情况必须在 implementation 或 closeout 前停止：

- active child 未授权就实现代码。
- 没有 live/checker evidence 就声明 LLM-backed generation quality。
- 在本仓库存 concrete demo-world content。
- 把 Validation Client implementation 或 provider ownership 移入 WorldEngine。
- 增加玩家投放物品、直接触发事件或 player-as-world-entity gameplay。
- 把 replay/worldline branches 描述成父子世界或源世界。
- 暴露 secrets、raw prompts、raw responses、raw thought、private Agent memory 或
  hidden context。
- 把 v0.10 evidence 当成 Agent autonomy 或完整 MVP validation PASS。
