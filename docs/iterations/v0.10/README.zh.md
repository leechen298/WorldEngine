# v0.10 MVP 调试契约与可运行世界会话

英文版本：`README.md`。

状态：`closeout PASS / handed off to v0.11`
类型：Codex `/goal` development campaign 和 iteration package root
implementation_authorized: no
evidence_execution_authorized: no

## 目标

v0.10 开始 MVP 交付线。它的目标不是一次性完成完整产品，而是先把 public
debug 和 checker handoff contract 对齐，再把 WorldEngine 从一组分散能力，串成一个
用户能看见的可运行世界会话。

通俗地说：WorldEngine-Validation-Client 首先要能连接 WorldEngine、发现 MVP
surfaces，并导出诚实的 `blocked` 或 basic handoff result。然后用户输入基础世界观后，
可以创建一个世界会话；这个世界可以按有限 tick 运行、暂停、继续；页面或外部客户端
可以看到事件、快照和当前状态。

v0.10 故意比之前 v0.9 的完整产品规划更窄。它不要求证明高质量 LLM 生成、
深度 Agent 自主性、完成游戏客户端或完整外部自动验证。它只建立后续 MVP
版本可以继续加“生命感”和验证能力的第一条纵向链路。

## 来自 v0.9 的交接

v0.9 以 full LLM-backed lifecycle validation blocked 收口。它留下了有用基础：
provider readiness、worldview generation contract、world rules 和 direction
boundary、bounded runtime control、event legality、Agent continuity evidence
contract，以及 checker/evidence handoff 方向。

v0.10 的交接决策是：

- 把 v0.9 作为架构输入。
- 不等待 v0.9 full LLM-backed PASS 才开始 MVP。
- 不把 v0.9 的长期能力都塞进 v0.10。
- 优先做一个能跑的 session flow，而不是追求能力面完整。
- 先修正 MVP public manifest/version/discovery 语义，再依赖客户端自动化。

## 范围

通过子包评审后，v0.10 允许做：

- world session identity、lifecycle、public status 和内存态保存。
- MVP public manifest/version contract 和 external debug handoff fields。
- 用于 external debugging 的 replay 和 worldline branch labels，并使用类似代码分支的 branch
  terminology，避免父子/源语义。
- 从用户 worldview input 创建 runnable session。
- live provider 不可用时允许 deterministic/mock fallback，但必须清楚标记。
- 把 generated public world model 接入 runtime state、parameters、初始 Agent
  记录和可视化 projection。
- 通过后端和 dashboard 暴露 bounded run controls。
- 为每个 session 记录 event、diff、snapshot evidence。
- 简单 MVP dashboard 路径：创建世界、运行 tick、暂停或继续、查看 world
  state、查看 timeline。
- 为 WorldEngine-Validation-Client 暴露 manifest 和 artifact naming，让它能发现 MVP
  session surfaces，并导出诚实的 `blocked`、`fail`、`pass` 或 `not_run` 状态。

v0.10 禁止做：

- 不做精美游戏 UI、像素美术资产、Steam/native packaging 或 app-specific
  distribution。
- 不在本仓库存 concrete demo-world seed data。
- 没有当前 provider/checker evidence 时，不声明 live provider 或 LLM quality
  通过。
- 不声明 Agent pseudo-self、深层记忆/人格模拟或 autonomous validation PASS。
- 不做 player-as-world-entity gameplay、投放物品或直接触发细节事件。
- replay 或 worldline branch labels 不使用父子世界、源世界语义。
- 不在本仓库实现 Validation Client。
- evidence 中不得包含 raw prompt、raw provider response、secret、raw thought、
  private Agent memory 或 hidden context。
- 不在 `backend/worldengine/` 下新增 runtime feature。

## 计划子包

`v0.10-plan.md` 是详细 planned-package specification。里面的子包只是路线规格，
不等于 implementation authorization，也不是完整 child package docs。

计划顺序：

1. `0.10.0-mvp-debug-session-planning-and-v0.9-handoff`
2. `0.10.1-mvp-public-manifest-and-debug-handoff`
3. `0.10.2-world-session-contract-and-state-store`
4. `0.10.3-worldview-to-runtime-session-creation`
5. `0.10.4-bounded-session-runtime-and-snapshot-evidence`
6. `0.10.5-dashboard-mvp-session-flow`
7. `0.10.6-v0.10-validation-and-handoff`

## 当前状态

当前 active child package：
无。v0.10 closeout 已完成。

当前 route：

```text
v0.10-closeout-pass-v0.11-handoff-ready
```

Implementation authorization: no.

Evidence execution authorization: no.

## 验证边界

v0.10 PASS 不是产品质量或 LLM 质量通过。它只证明第一条 debug handoff 和 runnable
session 链路：

```text
client discovery -> worldview input -> world session -> bounded runtime -> events/snapshots -> dashboard/client inspection
```

WorldEngine 仍然是被验证对象。WorldEngine-Validation-Client 可以消费 public
surfaces 和 evidence，但不能拥有 provider calls、world generation、runtime mutation
或 authoritative evaluation。

v0.10 可以定义后续客户端用于 replay 和 branch inspection 的 debug vocabulary。该 vocabulary
必须把 branches 视为可比较的时间线分支，而不是父子世界或源世界层级。
