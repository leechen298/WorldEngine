# LLM-backed 生命周期验证规范与执行手册

状态：计划中的验证规范与执行手册，仅文档

英文镜像：`llm-backed-lifecycle-validation-plan.md`。

## 范围

本文定义下一步如何验证 WorldEngine 是否具备 LLM-backed lifecycle 能力。
它是测试计划，不是新的 WorldEngine 产品迭代，不是 Validation Client
milestone，也不是代码实现请求。

本次文档工作不授权：

- 运行 live DeepSeek 或其他 provider 调用。
- 修改 runtime、API、schema、checker、fixture、frontend 或 Validation Client
  代码。
- 生成新的 saved result artifacts。
- 声明 LLM-backed world creation、LLM-backed world evolution 或 Agent 持续性
  自主行为已经 PASS。

当前基线：

- `0.8.9` 已通过 basic full lifecycle autonomous validation rerun。
- DeepSeek 或任何真实 LLM provider 还没有通过 WorldEngine live call 被验证。
- 当前 basic evidence 证明了外部客户端可以创建世界、推进 tick、观察 event 和
  snapshot、捕获一个 WorldEngine-backed Agent action、提交 director guidance、
  导出 evidence，并通过 saved-result checker。
- 当前 basic evidence 不证明 LLM-backed world creation、规则驱动的 world
  evolution、generated rules 下的 event legality，或 Agent 持续性的 memory、
  thought、behavior 和 intent。

## 目标

目标是准备一套后续聊天可以执行或实现的验证计划。它要回答一个问题：

WorldEngine 是否可以从用户输入的基础世界观出发，通过 WorldEngine 自己管理的
provider 配置调用 LLM，生成 public world parameters 和 rules，随时间演化这些
参数，生成或选择符合规则的事件，并提供 public evidence 证明 Agent 是从持续状态
行动，而不是由客户端脚本直接驱动？

这套计划第一次执行时很可能发现 implementation gap。这是允许的，也是计划的目的。
发现 gap 后应该分类并路由，而不是用 deterministic fallback 把缺口掩盖掉。

## 权限边界

WorldEngine 拥有全部 LLM 行为：

- provider selection。
- provider API key handling。
- provider calls。
- prompts 和 prompt construction。
- raw provider responses。
- generation、evolution、legality、memory 和 Agent decision behavior。
- 判断 WorldEngine lifecycle evidence 的权威 checker 或 scorecard contract。

Validation Client 仍然只是外部观察和操作表面：

- 可以让用户输入基础世界观或后续外部方向。
- 可以展示 public WorldEngine state、events、snapshots 和 Agent evidence。
- 可以记录 operation logs，并导出 evidence bundles。
- 不得保存、展示、转发或管理 provider API keys。
- 不得直接调用 LLM provider。
- 不得生成权威世界内容。
- 不得作为权威 evaluator。

## 当前验证合同

以下内容定义本计划实现或执行前的当前预期状态。

- 当前 `GET /manifest` 只证明 provider environment readiness。它可以报告
  public provider class、readiness、credential source class 和 model label，
  但不证明 live provider call 已发生。
- 当前 `POST /worlds` 返回 public world creation response，但当前 response 是
  generic deterministic response，不证明 LLM-backed world creation。
- 当前 tick、event、snapshot 和 Agent action evidence 只证明 basic lifecycle
  flow，不证明 generated world rules、rule-driven parameter evolution、legal event
  generation 或 persistent Agent autonomy。
- 因此，第一版 LLM-backed lifecycle validation 可能合法返回 FAIL，因为实现能力
  缺失。
- 缺实现本身是有用证据。它应该被分类和路由，而不是被 deterministic fallback
  隐藏。

PASS 只能来自以下来源之一：

- documented checker 输出 PASS。
- scorecard summary 中所有 critical item 都是 `pass`。
- 第二 Agent 只读复核 evidence 和 checker result 后，没有发现 blocking P1 或 P2。

以下内容不得作为 PASS 来源：

- 只有 Validation Client UI smoke 通过。
- 只有 `/manifest` 显示 provider configured。
- 只有环境变量里存在 API key。
- deterministic mock 或 generic world 可以运行。
- 人或 Agent 主观觉得结果“像是调用了 LLM”。
- 用户方向被直接写成世界最终事实。

## 脱敏合同

Evidence 只能记录 public、redacted、可复核的 summary。不得记录：

- API keys。
- authorization headers。
- raw prompts。
- raw provider requests。
- raw provider responses。
- raw provider traces。
- private Agent memory。
- private Agent goals。
- raw thought。
- raw chain-of-thought。
- hidden context。
- private evaluator data。
- private validation oracle logic。

允许的 provider evidence 只限 public 或 redacted 字段，例如：

- `provider_class`。
- `model_label`。
- `success` 或 `failure`。
- latency bucket 或 latency milliseconds。
- approximate token usage 或粗粒度 token buckets。
- public failure category。

允许的 Agent evidence 只限 public summary，例如：

- observed behavior。
- public action。
- public intent summary。
- public memory summary。
- public thought 或 reflection summary。
- public event reaction。

这些 summary 不得暴露 hidden internal state、private memory payloads 或 raw
reasoning text。

## 五个验证层级

| 层级 | 名称 | 核心问题 | 必要结果 |
| --- | --- | --- | --- |
| 1 | Provider live smoke | WorldEngine 是否能发起最小 live DeepSeek provider call，并且不泄露 secrets？ | 存在 redacted live call evidence，并通过 redaction。 |
| 2 | LLM-backed world creation | 用户 premise 是否能通过 WorldEngine-owned LLM behavior 生成 public、system-digestible world state 和 rule set？ | 结果和 premise 有实质关联，并且不是 deterministic generic response。 |
| 3 | LLM-assisted world evolution | tick 是否能通过 rules 推进 world parameters 和 events，而不是固定 counter？ | events、snapshots、diffs、replay evidence 能对应规则驱动变化。 |
| 4 | Agent autonomy evidence | Agent 是否能基于持续状态、memory summary、thought summary 和可选 intent 产生多轮 public behavior？ | actions 来自 WorldEngine public evidence，不是客户端脚本。 |
| 5 | Evidence review | 第一 Agent 能否操作流程、导出 evidence，第二 Agent 或 checker 能否验证？ | checker 或 scorecard PASS，且第二 Agent 只读复核无 blocking issue。 |

## Layer 1: Provider Live Smoke

### 目标

验证 DeepSeek provider environment variables 已配置，并且 WorldEngine 可以发起一个
最小 live provider call。

### 必要操作

- 用 WorldEngine 自己管理的环境变量启动 WorldEngine。
- 通过 WorldEngine public surface 读取 public provider readiness。
- 通过明确用于 provider smoke validation 的 WorldEngine-owned endpoint、command
  或 test hook，触发最小 live provider call。
- 记录 redacted provider live summary。

### 必要证据

- provider class，例如 `deepseek_api`。
- public 或 redacted model label。
- call status：`success`、`failure`、`blocked` 或 `not_configured`。
- latency。
- approximate token count 或 token bucket。
- provider 调用失败时的 public failure category。
- redaction flags，证明没有 key、raw prompt、raw response 或 authorization header。

### 禁止证据

- API key value。
- request authorization header。
- raw prompt。
- raw response。
- provider account id。
- provider raw trace。
- 完整 request 或 response body。

### PASS 条件

PASS 需要 checker 或 scorecard 确认 live provider call 是通过 WorldEngine 发起的，
调用成功，并且所有 redaction checks 通过。

### 预期当前缺口

当前 `GET /manifest` 只证明 environment readiness，不证明 live provider call。
如果不存在 smoke endpoint 或等价的 WorldEngine-owned call path，应根据缺失内容
分类为 `provider` 或 `checker_gap`：缺 runtime capability 就是 `provider`，
缺 testing infrastructure 就是 `checker_gap`。

## Layer 2: LLM-backed World Creation

### 目标

验证用户输入基础世界观后，WorldEngine 能生成 runtime 可消化的 public world state。

生成结果必须包含世界后续运行所需的基础，而不只是 labels 或 flavor text。

### 必须生成的内容

WorldEngine 应该生成：

- public world identity 和 premise summary。
- locations、entities、Agents、items 和相关 environment state。
- world runtime parameters。
- parameter meanings。
- initial parameter values。
- parameter evolution rules。
- boundary conditions。
- event legality rules。
- rule references 或 public rationale summaries。
- initial snapshot 和 visualization payload。

World runtime rules 在 premise 允许的情况下，应尽量基于真实世界常识。必要规则类别包括：

- time 和 time progression。
- weather 和 environmental conditions。
- resources 和 scarcity。
- 适用时的 population 或 social pressure。
- life state 和 health constraints。
- spatial distance 和 reachability。
- causality 和 delayed effects。
- action 或 event preconditions。

### 必要操作

- 通过 Validation Client 或其他 public external surface 输入基础 world premise。
- 让 WorldEngine 生成 public world state 和 rule package。
- 将生成结果和 summary 作为 public evidence 导出。
- 将 response 与当前 deterministic generic response 对比。

### PASS 条件

PASS 需要 evidence 证明生成世界是 premise-specific、system-digestible、redacted，
并且不是 deterministic generic response。

可接受的证明包括：

- 同一轮或已接受的前置轮次中，live provider smoke 已 PASS。
- world creation evidence 记录了 redacted provider-backed generation status。
- 两个实质不同的 premise 生成实质不同的 world parameters、rules、entities 或
  initial conditions。
- generated output 包含后续 tick evolution 可消费的 rule 和 parameter structures。

### 禁止行为

- Validation Client 生成世界内容。
- deterministic fallback 被报告成 LLM-backed generation。
- generated text 存在，但 WorldEngine runtime 无法消费。
- raw prompt 或 raw response 被导出为 evidence。
- concrete validation world seed data 被存入 WorldEngine 仓库。

## Layer 3: LLM-assisted World Evolution

### 目标

验证 world evolution 不只是固定 tick counter。World parameters 必须由 WorldEngine
根据 rules 自动计算和演化。

### 必要演化行为

tick 推进时，WorldEngine 应展示：

- 根据 rules 推导的 parameter changes。
- 由 WorldEngine 生成或选择、可选由 LLM 辅助的 external events。
- environmental changes。
- 符合 preconditions 和 boundaries 的 state changes。
- 支持 replay 的 snapshots 和 diffs。
- 带 public rule references 或 public legality summaries 的 event records。

### 用户方向边界

用户方向只能影响 external events 和 world environment。它不得直接修改 Agent private
state，也不得把非法最终结果直接写入世界。

例子：

- 禁止：“Agent A 立刻死亡。”
- 允许作为 external direction：“Agent A 可能面临雷击风险。”

对于允许的方向，WorldEngine 必须基于 public world rules 自己决定是否发生影响，例如：

- weather。
- location。
- shelter。
- probability。
- life state。
- spatial reachability。
- causal timing。
- event severity。

### 必要操作

- 推进足够多 tick，以观察多次 state changes。
- 捕获 events、snapshots 和 diffs。
- 提交至少一条 natural-language direction，该 direction 产生 environmental risk，而不是
  直接指定最终结果。
- 验证最终 outcome 由 WorldEngine rules 决定。
- 验证 replay 或 diff evidence 能解释 state transition。

### PASS 条件

PASS 需要 events、snapshots、diffs 和 replay evidence 能对应 rule-driven changes。
固定 counters、静态 mock events，或直接插入用户期待结果都不足以通过。

### 预期当前缺口

当前 basic lifecycle evidence 有 tick progression 和 events，但还没有证明 world rules
驱动 parameter evolution，也没有证明 event legality 已被执行。

## Layer 4: Agent Autonomy Evidence

### 目标

验证 Agents 能从 WorldEngine public evidence 中体现持续行为。不能因为存在一次
`params.applied` event，就把 Agent 视为已具备 autonomy。

### 必要自主证据

至少一个 Agent 应展示多轮 evidence，包括：

- observation。
- memory summary continuity。
- public thought 或 reflection summary。
- 形成 tendency、concern、desire 或 goal candidate。
- intent generation 或明确的 absence of intent。
- action selection。
- action execution。
- 对 world events 的 reaction。
- event 之后 public state 或 memory summary 发生变化。

不要求每个 tick 都有 intent。只要和 Agent state 及 context 一致，“observe”、
“wait”和“no clear intent”都是合法 public states。

### 必要操作

- 运行足够多 tick 或 interaction rounds，以观察至少两个 Agent decision moments。
- 捕获 event 前后的 public Agent evidence。
- 验证至少一个 action 来自 WorldEngine public evidence。
- 验证 Validation Client 没有脚本化 Agent action。

### PASS 条件

PASS 需要 checker 或 scorecard evidence 证明 Agent action 来自 WorldEngine public
evidence，并且 public summaries 展示了多轮 continuity。

### 禁止行为

- 客户端脚本写入 Agent actions，并把它呈现成 WorldEngine autonomy。
- 直接 private memory 或 private goal mutation。
- raw thought、raw chain-of-thought、private memory 或 hidden context 出现在 evidence 中。
- 单个孤立的 `params.applied` event 被视为充分 autonomy 证据。

## Layer 5: Evidence Review

### 目标

用双 Agent 工作流和 deterministic 或 scorecard checker 验证完整 lifecycle evidence。

### 必要复核流程

- 第一 Agent 以普通 human observer 或 director perspective 操作 Validation Client。
- 第一 Agent 导出完整 evidence bundle。
- WorldEngine checker 或 scorecard 验证 result directory。
- 第二 Agent 对 saved evidence 做只读复核。
- 最终 PASS 或 FAIL 基于 checker 或 scorecard output 加第二 Agent review，而不是第一
  Agent 自我声明。

### FAIL 必要分类

每个 FAIL 至少必须归入以下类别之一：

- `provider`。
- `world_creation`。
- `world_evolution`。
- `event_legality`。
- `agent_autonomy`。
- `redaction`。
- `client_evidence`。
- `checker_gap`。

## 能力矩阵

| 能力 | 当前已知状态 | LLM-backed 必要证据 | 缺失时的可能路由 |
| --- | --- | --- | --- |
| Provider env readiness | `/manifest` 可以从 env 报告 public readiness | Redacted live call summary | 缺 call path 则开 WorldEngine 实现迭代；接口完整但 provider 失败则记 provider/environment FAIL |
| LLM-backed creation | 当前 `POST /worlds` 是 generic deterministic | Premise-specific public world state 和 rule pack | WorldEngine 实现迭代 |
| Runtime parameters and rules | Basic lifecycle 不证明 rule schema | parameters、meanings、initial values、evolution rules、boundaries | WorldEngine 实现迭代 |
| Rule-driven evolution | Basic ticks 和 events 已存在 | diffs 和 snapshots 能关联 rules | WorldEngine 实现迭代 |
| Event legality | external direction 已能作为 guidance 接收 | 非法直接结果被拒绝；external risk 由 rules 解析 | WorldEngine 实现迭代 |
| Agent continuity | 观察到一个 WorldEngine-backed Agent action | 多轮 memory、thought、intent、action、reaction summaries | WorldEngine 实现迭代 |
| Client evidence | Validation Client 可导出 basic evidence | LLM-backed lifecycle evidence fields 和 operation logs | 缺展示/导出/日志字段则开 Validation Client milestone |
| Checker support | basic saved-result checker 已存在 | LLM-backed evidence 的 scenario 和 schema 支持 | `docs/testing` 和 `tools/testing` 测试资产增强 |

## Scenario Contracts

以下 scenario names 是后续 checker 或 saved result implementation 的权威名称。之后如果新增
checker 或 result schema，应沿用这些名称。

### `provider-live-smoke-deepseek`

Goal：

- 证明 WorldEngine 可以通过 WorldEngine-owned configuration 发起最小 live DeepSeek
  provider call，并且只返回 redacted public evidence。

Required operations：

- 用 DeepSeek environment variables 启动 WorldEngine。
- 读取 public provider readiness。
- 触发最小 WorldEngine-owned live provider smoke call。
- 捕获 redacted provider live summary。
- 对 saved evidence 运行 checker 或 scorecard validation。

Forbidden operations：

- Validation Client 直接调用 DeepSeek。
- Agent 读取或记录 API key values。
- operation log 存储 raw provider request、raw provider response、raw prompt、
  authorization header 或 provider trace。
- 只用 `/manifest` readiness 当作 live-call proof。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `api-summary.json`。
- `provider-live-summary.json`。
- `scorecard-summary.json` 或 checker output。
- redaction scan artifact。

PASS source：

- documented checker 或 scorecard PASS，确认 live call success 且 redaction pass。

FAIL taxonomy：

- `provider`：configuration、network、quota、provider response 或 live call 失败。
- `redaction`：secret 或 raw provider content 出现。
- `checker_gap`：没有 supported checker 或 schema 能验证 evidence。
- `client_evidence`：required operation evidence 缺失。

Redaction requirements：

- 只记录 provider class、model label、success/failure、latency、approximate token
  statistics 和 public failure category。
- 不记录 API key、raw prompt、raw response、authorization header 或 raw provider trace。

### `llm-backed-world-creation`

Goal：

- 证明基础 user worldview 可以通过 WorldEngine 生成 public、system-digestible、
  LLM-backed world state。

Required operations：

- 通过 external client 或 public surface 输入基础 world premise。
- 通过 WorldEngine 创建世界。
- 捕获 public initial state、entities、items、Agents、locations、world parameters、
  rule definitions、boundary conditions 和 visualization payload。
- 与 deterministic generic world response 对比。

Forbidden operations：

- Validation Client 生成或改写 world content。
- deterministic fallback 被标记为 LLM-backed。
- raw prompt 或 raw response 被导出。
- user premise 被直接复制成 final state，而没有 WorldEngine generated structure。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `api-summary.json`。
- `world-creation-summary.json`。
- `world-rule-summary.json`。
- `initial-snapshot.json` 或等价 public snapshot artifact。
- `scorecard-summary.json` 或 checker output。

PASS source：

- checker 或 scorecard PASS，证明 world 是 premise-specific、system-digestible、
  redacted，且不是 deterministic generic output。

FAIL taxonomy：

- `world_creation`：creation 是 deterministic、generic、non-digestible 或不是 provider-backed。
- `provider`：provider-backed creation 因 live provider access 失败而无法运行。
- `redaction`：raw prompt、raw response 或 private provider data 泄露。
- `client_evidence`：required public evidence 缺失。
- `checker_gap`：checker 无法区分 generic deterministic output 和 LLM-backed output。

Redaction requirements：

- 只保存 public generated state 和 public rule summaries。
- 不保存 raw prompts、raw provider responses、private traces 或 hidden generation
  internals。

### `world-rule-parameter-evolution`

Goal：

- 证明 generated world parameters 会跨 tick 根据 WorldEngine rules 演化，而不是静态
  counter 或 hard-coded mock behavior。

Required operations：

- 从包含 public parameters 和 rules 的 LLM-backed world 开始。
- 推进多个 ticks。
- 捕获 parameter diffs、events、snapshots 和 replay references。
- 验证每个 material parameter change 都有 public rule reference 或 public legality
  explanation。

Forbidden operations：

- static counter-only tick progression 被报告为 rule evolution。
- 没有 rule evidence 的直接 mutation 被报告为有效。
- Validation Client 计算权威 world parameter changes。
- hidden implementation details 被导出为 proof。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `api-summary.json`。
- `rule-parameter-summary.json`。
- `world-lifecycle-summary.json`。
- `diff-replay-summary.json`。
- events 和 snapshots artifacts。
- `scorecard-summary.json` 或 checker output。

PASS source：

- checker 或 scorecard PASS，证明跨 ticks 存在 rule-linked parameter changes。

FAIL taxonomy：

- `world_evolution`：parameters 不演化、只按 fixed counter 演化，或缺少 rule linkage。
- `world_creation`：必要 rules 或 parameters 从未生成。
- `redaction`：private prompts、raw responses 或 hidden internals 出现。
- `client_evidence`：diffs、snapshots 或 event evidence 缺失。
- `checker_gap`：无法验证 rule linkage。

Redaction requirements：

- 允许 public rule ids、public explanations、parameter names、values 和 diffs。
- 禁止 private provider traces、raw prompt text 和 hidden reasoning。

### `rule-compliant-event-generation`

Goal：

- 证明 random events 和 user-directed external guidance 会受到 world rules 约束，
  用户不能直接强制非法最终结果。

Required operations：

- 运行带 public event legality rules 的世界。
- 捕获至少一个 WorldEngine-generated 或 selected random event。
- 提交至少一个 natural-language external direction，它描述 risk、pressure 或
  environmental tendency，而不是 final outcome。
- 验证 WorldEngine 根据 public rules 接受、拒绝、延迟、转换或解析该 direction。
- 捕获 event legality summaries 以及 resulting diffs 或 snapshots。

Forbidden operations：

- user direction 不经 rule adjudication 直接杀死、治愈、传送、改写或强制 Agent final state。
- Validation Client 创建权威 events。
- impossible events 没有 legality status 却通过。
- raw prompt 或 response 被用作 public proof。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `api-summary.json`。
- `event-legality-summary.json`。
- event artifacts。
- snapshot 和 diff artifacts。
- `scorecard-summary.json` 或 checker output。

PASS source：

- checker 或 scorecard PASS，证明 external direction 只影响 external events 或
  environment，并且 WorldEngine 通过 rules 决定 final outcomes。

FAIL taxonomy：

- `event_legality`：非法直接结果被接受，或缺少 rule adjudication。
- `world_evolution`：events 没有产生 coherent state changes。
- `agent_autonomy`：event handling 直接修改 private Agent intent 或 memory。
- `redaction`：private state 或 provider raw content 泄露。
- `client_evidence`：event evidence 不完整。
- `checker_gap`：无法检查 legality。

Redaction requirements：

- 允许 public legality summaries、event ids、rule references 和 public outcomes。
- 禁止 private Agent memory、private goals、hidden context、raw thought、raw prompt
  和 raw response。

### `agent-persistent-autonomy-evidence`

Goal：

- 证明至少一个 Agent 在多轮中展示持续性的 public autonomy evidence。

Required operations：

- 创建或加载至少包含一个 Agent 的 LLM-backed world。
- 推进足够多 ticks，以观察多个 Agent decision moments。
- 捕获 observation、memory summary、public thought 或 reflection summary、intent 或
  no-intent state、selected action、executed action 和 event reaction。
- 验证 action source 是 WorldEngine public evidence，而不是 client script。

Forbidden operations：

- 单个 `params.applied` event 被当作 persistent autonomy。
- Validation Client 脚本化 Agent action，并记录成 WorldEngine action。
- 直接 private memory、private goal 或 hidden context mutation。
- raw chain-of-thought 被导出。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `api-summary.json`。
- `agent-autonomy-summary.json`。
- Agent event artifacts。
- Agent decision moments 前后的 snapshots。
- `scorecard-summary.json` 或 checker output。

PASS source：

- checker 或 scorecard PASS，证明 multi-round continuity 且没有 client-scripted Agent action。

FAIL taxonomy：

- `agent_autonomy`：actions 缺失、只有单轮、由客户端脚本化，或无法关联 WorldEngine
  public evidence。
- `world_evolution`：没有可供 Agent 观察的 world change。
- `redaction`：private memory、private goal、hidden context、raw thought 或 raw
  chain-of-thought 泄露。
- `client_evidence`：operation logs 或 Agent evidence 缺失。
- `checker_gap`：无法验证 continuity。

Redaction requirements：

- 允许 public memory summaries、public thought summaries、public intent summaries、
  public action summaries 和 public reactions。
- 禁止 private memory payloads、private goals、raw thoughts、raw chain-of-thought、
  hidden context 和 private relationship internals。

### `llm-backed-full-lifecycle-autonomous`

Goal：

- 证明完整 LLM-backed lifecycle：provider live smoke、LLM-backed creation、
  rule-driven evolution、rule-compliant events、persistent Agent autonomy evidence、
  evidence export、checker PASS 和第二 Agent 只读复核。

Required operations：

- 运行 `provider-live-smoke-deepseek`，或消费同 session 中已接受的 provider live
  smoke prerequisite。
- 从基础 user premise 创建 LLM-backed world。
- 推进 ticks，直到可见 rule-driven parameter evolution、events、snapshots 和 diffs。
- 提交至少一条 external environmental direction，并验证 legality。
- 观察 multi-round Agent autonomy evidence。
- 从 Validation Client 导出 evidence bundle。
- 对 result directory 运行 WorldEngine checker 或 scorecard。
- 运行第二 Agent 只读 evidence review。

Forbidden operations：

- 把 UI smoke 当作 full lifecycle PASS。
- 把 provider readiness 当作 live call proof。
- 把 deterministic generic world output 当作 LLM-backed。
- direct API calls 被记录为 Agent operation-log operations。
- client-scripted Agent actions。
- user direction 被直接写为 final state。
- evidence 中出现 raw prompt、raw response、API key、private memory、raw thought 或
  hidden context。

Required artifacts：

- `result.json`。
- `operation-log.jsonl`。
- `transcript.md`。
- `console.log`。
- screenshots。
- `api-summary.json`。
- `provider-live-summary.json`。
- `world-creation-summary.json`。
- `world-rule-summary.json`。
- `rule-parameter-summary.json`。
- `event-legality-summary.json`。
- `agent-autonomy-summary.json`。
- `world-lifecycle-summary.json`。
- `validation-client-evidence-bundle.json`。
- `scorecard-summary.json`。
- 第二 Agent 只读 review report。

PASS source：

- WorldEngine checker 或 scorecard 对所有 critical items 输出 PASS，并且第二 Agent 只读
  复核没有 blocking P1 或 P2 issue。

FAIL taxonomy：

- `provider`。
- `world_creation`。
- `world_evolution`。
- `event_legality`。
- `agent_autonomy`。
- `redaction`。
- `client_evidence`。
- `checker_gap`。

Redaction requirements：

- 所有 component scenarios 的 redaction requirements 都适用。
- 任何 API key、authorization header、raw prompt、raw response、provider trace、
  private memory、private goal、raw thought、raw chain-of-thought 或 hidden context
  泄露，都立即 FAIL。

## 推荐 Result Layout

推荐 live result directory：

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

推荐 durable result summaries：

```text
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md
```

推荐 result files：

```text
result.json
operation-log.jsonl
transcript.md
console.log
api-summary.json
provider-live-summary.json
world-creation-summary.json
world-rule-summary.json
rule-parameter-summary.json
event-legality-summary.json
agent-autonomy-summary.json
world-lifecycle-summary.json
validation-client-evidence-bundle.json
scorecard-summary.json
second-agent-review.md
screenshots/
raw/
```

`raw/` directory 可以包含来自 WorldEngine 和 Validation Client 的 raw public artifacts。
但它仍然必须遵守 redaction，不得包含 provider raw requests、provider raw responses、
raw prompts、API keys、authorization headers、private Agent memory、private Agent
goals、raw thought 或 hidden context。

## 建议 Scorecard Items

完整 lifecycle scorecard 应包括以下 critical items：

- `provider_live_smoke`：只有 WorldEngine-owned live provider call 成功且 evidence
  redacted 时才 pass。
- `world_creation_llm_backed`：只有 public world creation 是 premise-specific 且不是
  deterministic generic output 时才 pass。
- `world_rules_generated`：只有 parameters、meanings、initial values、evolution
  rules 和 boundaries 都存在时才 pass。
- `parameter_evolution_rule_linked`：只有 tick changes 能关联 public rules 时才 pass。
- `event_legality_enforced`：只有 random 和 user-guided external events 都服从 world
  rules 时才 pass。
- `agent_persistent_autonomy`：只有存在 multi-round Agent public evidence 且不是
  client-scripted 时才 pass。
- `diff_replay_available`：只有 events、diffs 和 snapshots 支持 replay 或 state
  inspection 时才 pass。
- `redaction_clean`：只有 forbidden private/provider content 都不存在时才 pass。
- `client_evidence_complete`：只有 operation log、API summary、screenshots、
  transcript 和 evidence bundle 都存在时才 pass。
- `second_agent_review_clean`：只有只读复核没有 blocking P1 或 P2 issue 时才 pass。

## 建议执行顺序

后续正式验证应按以下顺序运行：

1. Preflight：确认 WorldEngine 和 Validation Client repositories 的状态足够干净，
   可以生成 scoped evidence。
2. Provider smoke：运行 `provider-live-smoke-deepseek`。
3. World creation：运行 `llm-backed-world-creation`。
4. Evolution：运行 `world-rule-parameter-evolution`。
5. Event legality：运行 `rule-compliant-event-generation`。
6. Agent autonomy：运行 `agent-persistent-autonomy-evidence`。
7. Full lifecycle：运行 `llm-backed-full-lifecycle-autonomous`。
8. Checker：运行 documented WorldEngine checker 或 scorecard command。
9. Second-Agent review：对 result directory 做只读复核。
10. Durable result：在 `docs/testing/results/` 下写 result summary。

开发过程中可以分阶段验证，但正式验证时不应该让用户手动一阶段一阶段地下指令。
后续一条验证指令应能驱动完整 staged sequence，直到 PASS、classified FAIL 或触发
stop rule。

## Stop Rules

出现以下情况时立即停止并分类：

- evidence 包含 API key、authorization header、raw prompt、raw response、provider
  trace、private memory、private goal、raw thought、raw chain-of-thought 或 hidden
  context。
- provider cost、rate limit 或 quota risk 超出已配置 validation budget。
- 不存在 WorldEngine-owned live provider call path。
- 唯一可用的 world creation output 是 deterministic generic output。
- user direction 不经 rule adjudication 就直接成为 final world fact。
- Agent action 是 client-scripted，或无法关联 WorldEngine public evidence。
- required artifacts 缺失，且无法从同一 run 中重新生成。

## 后续路由规则

如果缺口只是 checker、scenario、fixture 或 saved-result schema support，应路由到
测试资产增强：

- `docs/testing`。
- `tools/testing`。

这种情况不默认算 WorldEngine 产品迭代。

如果缺少以下能力，应开 WorldEngine 实现迭代：

- provider live smoke endpoint 或 command。
- provider call abstraction。
- LLM redacted evidence schema。
- LLM-backed world creation behavior。
- world parameter 和 rule schema。
- world rule evolution engine。
- event legality engine。
- Agent persistent memory evidence。
- Agent persistent action evidence。

如果缺少以下能力，应开 Validation Client milestone：

- LLM-backed lifecycle evidence 的 UI 展示。
- evidence bundle fields。
- Agent operation log export。
- API summary export。
- external evidence review 所需的 replay、diff 或 snapshot display。

如果 DeepSeek 调用失败，但 WorldEngine 已具备必要 interface 和 redacted evidence path，
记录为 provider/environment validation FAIL。不要为了让 provider 通过而直接修改产品代码。

如果 raw prompt、raw response、API key、authorization header、private Agent memory、
private Agent goal、raw thought、raw chain-of-thought 或 hidden context 泄露，立即分类为
`redaction` FAIL，并优先修 redaction boundary。

## 假设

- DeepSeek API key 由 WorldEngine environment variables 管理。
- Validation Client 不保存、不展示、不转发 provider keys。
- Validation Client 仍是外部客户端，不拥有 LLM generation 或权威 evaluation。
- 第一版 LLM-backed validation 可以发现缺口。缺口分类后，再决定是否开 WorldEngine
  实现迭代，例如 `0.8.10`，Validation Client milestone，例如 `v0.8`，或 testing
  asset enhancement。
- 当前任务是 documentation-only，不运行 live DeepSeek tests，不修改 runtime、API、
  checker、fixture、frontend 或 Validation Client code。
- 当前验证重点是功能链路能否跑通，不要求一步证明世界规则和 Agent 行为质量已经达到最终
  游戏体验。

## 后续验证聊天提示词

当必要实现和 checker support 已存在后，可使用这个提示词：

```text
/goal Run llm-backed-full-lifecycle-autonomous validation.

Read:
- docs/testing/llm-backed-lifecycle-validation-plan.md
- docs/testing/agent-autonomous/scorecard.md
- docs/testing/product-capability-validation-playbook.md
- the current WorldEngine implementation package documents if a package created
  the LLM-backed provider/world/evolution/Agent surfaces.

Run the staged validation from provider live smoke through full lifecycle.
Use WorldEngine-owned provider calls only. Do not let the Validation Client
own LLM generation or evaluation. Export evidence under:

test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/

Then run the documented checker or scorecard. Ask a second Agent for read-only
review of the saved evidence. Write durable result summaries under:

docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md

Report PASS only from checker or scorecard PASS plus no blocking second-Agent
review issue. If FAIL, classify it as provider, world_creation,
world_evolution, event_legality, agent_autonomy, redaction, client_evidence,
or checker_gap.
```
