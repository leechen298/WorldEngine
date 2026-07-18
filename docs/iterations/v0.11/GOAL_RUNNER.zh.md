# Goal Runner

英文版本：`GOAL_RUNNER.md`。

状态：`child package documentation review in progress`

## Goal Entry

本 campaign 覆盖的自然语言目标包括：

```text
完成 v0.11
开发 v0.11
生成 v0.11 文档
编写 v0.11 文档
启动 WorldEngine v0.11：MVP Rule-Bound World Evolution
```

当前 route 记录在 `CURRENT_STATE.md`。Implementation authorization 默认关闭。

## Route Selection

1. 读取 `CURRENT_STATE.md`。
2. 读取 `README.md`、`CAMPAIGN_PLAN.md` 和 `v0.11-plan.md`。
3. 在 implementation 或 evidence execution 前，把 active planned child 转换成 concrete
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

v0.11 关注 world evolution，不是 Agent pseudo-self 或最终 validation automation。用户 direction
必须保持 world-level guidance；每个 applied event/diff 都必须能通过 public rules、state 和
legality evidence 解释。

具体边界例子：拒绝“让这个 Agent 现在死亡”这类 direct final facts；只接受“这个 Agent
可能面临雷击风险”这类可处理压力，并且 WorldEngine 仍必须通过 rules、state、probability
和 legality 判断结果。

## Stop Conditions

以下情况必须在 implementation 或 closeout 前停止：

- active child 未授权就实现代码。
- user direction 直接施加 final facts。
- 增加玩家投放物品、直接触发细节事件或 player-as-world-entity gameplay。
- direction guidance 修改 Agent private state。
- 泄露 raw provider data、secrets、private memory、raw thought 或 hidden context。
- 用 hidden/private evaluator data 当 PASS evidence。
- 从 v0.11 evidence 声明 Agent autonomy 或 complete MVP validation。
