# Project Plan

英文版本：`project-plan.md`。

状态：`authoritative project planning overview`

## 用途

本文档是 WorldEngine 整体项目目标和交付计划的入口，给人和 Agent 快速理解项目方向使用。

它不替代更详细的项目文档：

- `project-north-star.md` 定义长期方向。
- `product-model.md` 定义产品是什么、不是什么。
- `scope-boundaries.md` 定义仓库硬边界。
- `roadmap.md` 定义版本级交付路线。
- `docs/iterations/` 定义 review-gated implementation packages。

当问题是“我们到底在做什么、为什么做、现在实际该怎么推进”时，先读本文档。

## 整体目标

WorldEngine 是一个通用的世界生成与运行引擎。它的长期目标是创建世界、让世界随时间运行，
并让 Agent 在世界中生活，形成记忆、连续性、受反馈影响的行为，以及可检查的工程化
pseudo-self。

项目不是只做 demo、只做故事生成器、只做 NPC 聊天系统、也不是只做游戏客户端。这些都可以是
WorldEngine 的消费者，但 core repository 必须保持为可复用的 engine。

## 产品方向

WorldEngine 最终应支持这些主要能力：

1. **世界创建**：把用户方向、模板、结构化输入和 WorldEngine-owned LLM calls 转成 public、
   validated、runnable world models。
2. **世界运行**：推进时间、评估规则、应用后果、记录事件、创建快照，并支持 replay/recovery。
3. **规则约束演化**：让世界参数、环境、事件和状态变化通过明确规则和合法性证据演化。
4. **Agent 生活**：让 Agent 观察、形成意图或无意图、行动、反应、记忆、休息、睡眠，并随时间沉淀经验。
5. **投影和检查**：把运行中的世界暴露给 dashboard、game、validation client、小说式 narrative
   projection、diagnostic conversation 和 replay tools，但这些 surface 默认不能变成
   canonical world。
6. **验证和证据**：产出 public、redacted evidence，让 external client 和 checker 可以把结果分类为
   `pass`、`fail`、`blocked` 或 `not_run`。

## 当前实际策略

之前的规划更接近一次性描述完整产品级世界模拟。当前计划故意缩小：

> 通过多个有门禁的迭代，做出一个完整 MVP。

MVP 不是“智能程度已经完成”。MVP 是一条完整可见闭环：

```text
client discovery
-> create world from worldview input
-> run bounded ticks
-> produce rule-linked events and diffs
-> show Agent public behavior and memory evidence
-> export evidence through WorldEngine-Validation-Client
-> classify the result with checker / scorecard / read-only review
```

这样可以先让 engine 能调试、能自动化验证，再继续打磨世界质量、Agent 深度和产品表现。

## MVP 交付计划

### v0.10 - MVP Debug Contract And Runnable World Session

目标：让 WorldEngine 先变得可发现、可调试、可作为 session 运行。

这个版本应先对齐 WorldEngine-Validation-Client 需要的 public manifest/debug handoff
contracts，然后实现第一条用户可见流程：输入 worldview、创建 world session、运行 bounded
ticks、检查 events/snapshots/state，并能在 dashboard 或 external client 中看到。

成功含义：世界可以被创建和运行，并且可调试。不声明 Agent autonomy、LLM quality 或完整 MVP
validation。

### v0.11 - MVP Rule-Bound World Evolution

目标：让运行中的世界因为可检查的原因而变化。

这个版本应加入诚实的 provider/worldview preflight、结构化世界规则和参数、作为 bounded
world-level guidance 的自然语言 direction、合法事件生成/应用、public diffs、replay evidence
和 worldview fidelity checks。

成功含义：验证者可以理解世界为什么变化。不声明完整 Agent continuity 或完整外部自动化。

### v0.12 - MVP Agent Continuity And Validation Automation

目标：完成 MVP 闭环。

这个版本应加入最小 public Agent state 和 runtime behavior、short-term memory 与 rest/sleep
consolidation evidence、read-only narrative 和 diagnostic inspection surfaces、稳定的
WorldEngine-Validation-Client evidence handoff，以及 full lifecycle checker/scorecard review。

成功含义：MVP 可以通过导出的 public evidence 被操作和自动分类。如果 provider、client 或
checker capability 缺失，closeout 应诚实报告 `PARTIAL`、`BLOCKED` 或 `FAIL`。

### v0.13 - 最小可运行 MVP 锚点

目标：停止继续抽象扩张整体架构，先构建一条足够小、当前可运行、可被独立验证的纵向切片。

必过路径采用 deterministic、provider-independent 方案，避免开发被 live model access 阻断。
它使用一个 fixed-seed runnable package、一个 Session、精确 lockstep steps、一个 Agent causal
loop、同一明确窗口里一次 accepted 和一次 rejected intervention、public
event/diff/snapshot evidence、通用客户端协议和 WorldEngine 管理控制台。

WorldEngine 侧 contract 通过后，在既有外部 `WorldEngine-Validation-Client` 仓库中增加 Godot
executor 和隔离 checker。旧 Web executor 保持 legacy，不得对新运行自证通过。

成功含义：WorldEngine、管理控制台和 Godot 对同一个 session、tick、revision、state hash、
Agent evidence 和 intervention result 达成一致，并由独立 checker 对当前 sealed evidence 分类。
v0.13 package 位于 `docs/iterations/v0.13/`。

## WorldEngine-Validation-Client 的角色

WorldEngine-Validation-Client 是外部消费者和验证界面。它帮助人和 Agent 操作、检查、记录、
回放并导出 WorldEngine 的证据。

它可以：

- 连接 WorldEngine public APIs。
- 从 manifest 发现 public surfaces。
- 像客户端一样操作世界。
- 记录 operation logs 和 API logs。
- 导出 evidence bundles。
- 支持 Agent-operated autonomous validation。

它不能：

- 拥有 provider keys 或 provider calls。
- 生成 canonical world content。
- 绕过 public APIs 修改世界。
- 成为 authoritative evaluator。
- 保存 raw prompts、raw provider responses、private Agent memory、raw thought、hidden
  context、secrets 或 private evaluator data。

## 玩家、引导、Agent 和分叉边界

MVP track 默认把玩家或用户视为外部操作者，而不是世界内实体。用户可以通过外部 world-level
guidance 引导世界方向，但不能直接向世界投放物品、直接触发细节事件，或直接指定最终事实。

例如，“让这个 Agent 现在死亡”不是合法的世界引导。“这个 Agent 可能面临雷击风险”可以作为外部压力
被接受，但实际结果仍必须由 WorldEngine 根据天气、位置、概率、生命状态和 public world rules
自行决定。

分叉世界线类似代码分支：它们是可 replay、可比较的时间线分支。除非后续 reviewed package
明确引入另一套 recursive-world relationship，否则文档和证据不应把分叉描述成父子世界、源世界或
起源层级。

项目文档必须区分“Agent”的两种含义：

- **世界内 Agent**：生活在 WorldEngine 里的模拟实体。
- **外部验证 Agent**：Codex、OpenClaw 或其他从世界外操作客户端并 review evidence 的工具。

小说式 narrative projection 和 diagnostic conversation 默认是外部检查 surface。它们可以帮助人
判断世界是否运行得合理，但不能修改 canonical world timeline 或 Agent memory，除非后续 reviewed
bridge 明确允许这种行为。
用户可以把它们作为 read-only session/tick-range/branch/Agent-focused views 来请求。任何想改变
未来世界的请求都必须离开 diagnostic surface，进入 v0.11 风格的 direction queue。

## 开发工作流

所有 code 或 mixed work 都必须保持 iteration-gated：

1. 创建或确认 active package documents。
2. Review `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md`。
3. 只在 active package 内授权 implementation。
4. 实现 scoped package。
5. 按需运行 focused verification 和 broader regression。
6. 在 `review.md` 记录 evidence。
7. 以诚实的 `PASS`、`PARTIAL`、`BLOCKED` 或 `FAIL` 收口。

Documentation-only planning 可以更新 project plans、roadmap、scope 和 iteration package
documents，但不能偷偷修改 runtime、API、schema、frontend、tests、fixtures、migrations、
generated results 或 external repositories。

## MVP Track 的非目标

MVP track 不应扩大成：

- polished game release。
- core repository 内的 concrete demo-world content。
- Steam/native distribution。
- real-consciousness claims。
- unbounded provider-cost execution。
- raw prompt/response logging。
- private Agent memory 或 raw thought exposure。
- external client ownership of WorldEngine behavior。
- 玩家作为世界内实体的 gameplay、投放物品或直接触发细节事件。
- full recursive worlds 或 subjective inner-world cells，除非后续 reviewed package 明确重开范围。

## 决策规则

当需要在“大而精美的功能”和“小而完整的切片”之间选择时，优先选择能强化这条闭环的完整切片：

```text
create -> run -> evolve -> Agent reacts -> evidence -> external validation
```

这条闭环就是当前 MVP 的实际定义。
