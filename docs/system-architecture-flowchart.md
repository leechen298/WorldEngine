# WorldEngine System Architecture Flowchart

Status: target architecture planning artifact

This diagram describes the most reasonable target flow for WorldEngine without
treating the current codebase as the implementation source of truth. It keeps
the core product model focused on three primary modules:

- World Generation
- World Runtime
- Agent Runtime

Event contracts, state/diff/snapshot contracts, memory/evidence, persistence,
projection, and validation are shared infrastructure around those three
modules. Godot and other engines are projection clients, not core dependencies.

Mermaid source-only copy: `docs/system-architecture-flowchart.mmd`.

```mermaid
flowchart TD
  S0["WorldEngine System Architecture v0<br/>World Generation + World Runtime + Agent Runtime<br/>Reasoned target architecture, independent of current implementation"]

  S1["Core Boundary<br/>核心边界<br/>WorldEngine owns canonical world state, rules, events, Agent public state,<br/>provider calls, redaction, evidence, and validation contracts"]

  S2["External Consumer Boundary<br/>外部消费者边界<br/>Dashboard · Godot · validation clients · replay tools · other engines<br/>consume public APIs, projections, contracts, and redacted evidence"]

  S0 --> S1
  S0 -. "Public contracts only / 只通过公开契约" .-> S2

  subgraph INPUTS["0. Inputs, Contracts and Governance / 输入、契约与治理"]
    I0["User Direction<br/>用户方向输入<br/>worldview · constraints · generation intent · runtime guidance"]
    I1["Templates and Structured Inputs<br/>模板与结构化输入<br/>world template · generation plan · seed material · constraints"]
    I2["WorldEngine-owned Provider Boundary<br/>引擎拥有的 Provider 边界<br/>configured by core · redacted outputs · no external key ownership"]
    I3["Iteration Contracts<br/>迭代契约<br/>north star · scope boundaries · roadmap · package contracts"]
    I4["Public API and Schema Contracts<br/>公开 API 与 Schema 契约<br/>WorldSpec · Event · Agent · Memory · Projection · Evidence"]
  end

  S1 --> I3
  I3 -. "Constrains / 约束" .-> I4

  subgraph GENERATION["1. World Generation / 世界生成"]
    G0["Generation Request Intake<br/>生成请求入口<br/>template request · plan request · imported AI-assisted plan"]
    G1["Input Normalization<br/>输入归一化<br/>strip unsupported fields · normalize metadata · preserve provenance"]
    G2["Template Path<br/>模板路径<br/>reviewed generic templates · deterministic generation"]
    G3["Structured Plan Path<br/>结构化计划路径<br/>locations · entities · agents · resources · rules · constraints"]
    G4["AI-assisted Plan Import<br/>AI 辅助计划导入<br/>structured data only · redacted provenance · no raw prompt evidence"]
    G5["World Model Compiler<br/>世界模型编译器<br/>candidate WorldCell tree · entity refs · rule refs · projection hints"]
    G6["WorldSpec Validation<br/>WorldSpec 校验<br/>schema · references · recursion bounds · JSON compatibility · safety rules"]
    G7["Preview and Diagnostics<br/>预览与诊断<br/>human-readable preview · validation findings · regeneration hints"]
    G8["Regeneration Loop<br/>重新生成循环<br/>lineage · adjusted constraints · deterministic or provider-assisted retry"]
    G9["Runtime Readiness Gate<br/>运行就绪门禁<br/>loadable WorldSpec · runtime-context summary · no canonical mutation yet"]
    G10["Runnable WorldSpec<br/>可运行 WorldSpec<br/>public structured world model ready for session creation"]

    G0 --> G1
    G1 --> G2
    G1 --> G3
    G1 --> G4
    G2 --> G5
    G3 --> G5
    G4 --> G5
    G5 --> G6
    G6 -->|"valid / 有效"| G7
    G6 -->|"fixable findings / 可修复问题"| G8
    G8 --> G1
    G7 --> G9
    G9 -->|"ready / 就绪"| G10
  end

  I0 --> G0
  I1 --> G0
  I2 -. "Optional engine-owned generation / 可选引擎侧生成" .-> G4
  I4 -. "Schema contract / Schema 契约" .-> G6

  subgraph RUNTIME["2. World Runtime / 世界运行"]
    R0["Session Creation<br/>Session 创建<br/>world id · session id · initial runtime state · bounded controls"]
    R1["WorldSpec Loader and Runtime Context<br/>WorldSpec 加载与运行上下文<br/>validated spec · public summary · runtime handoff"]
    R2["Runtime Control Plane<br/>运行控制面<br/>step · run bounded ticks · pause · resume · reset · replay branch"]
    R3["Tick Scheduler<br/>Tick 调度<br/>world time · tick id · run budget · callbacks"]
    R4["Rule and Parameter Evaluation<br/>规则与参数评估<br/>world rules · parameters · direction queue · environmental pressure"]
    R5["Event Candidate Builder<br/>事件候选生成<br/>candidate facts · causes · affected refs · visibility · importance"]
    R6["Legality and Consequence Gate<br/>合法性与后果门禁<br/>rule evidence · probability · current state · no direct fact assignment"]
    R7["Diff Application<br/>Diff 应用<br/>state changes · parameter changes · world timeline updates"]
    R8["Canonical World State<br/>正典世界状态<br/>runtime state · params · public agent state · event timeline"]
    R9["Archive and Recovery<br/>归档与恢复<br/>snapshots · summaries · replay material · recovery checkpoints"]
    R10["Worldline Branching<br/>世界线分支<br/>replayable timelines · comparison · no parent/source semantics by default"]
    R11["Runtime Evidence<br/>运行证据<br/>events · diffs · snapshots · rule links · run metadata"]

    R0 --> R1
    R1 --> R2
    R2 --> R3
    R3 --> R4
    R4 --> R5
    R5 --> R6
    R6 -->|"legal / 合法"| R7
    R6 -->|"rejected / 拒绝"| R11
    R7 --> R8
    R8 --> R9
    R8 --> R10
    R8 --> R11
  end

  G10 --> R0
  I0 -. "Runtime guidance as external pressure / 运行期方向作为外部压力" .-> R4

  subgraph AGENT["3. Agent Runtime / Agent 运行"]
    A0["Agent Public Identity and State<br/>Agent 公开身份与状态<br/>agent id · role · needs · current state · public summaries"]
    A1["Perception Frame Builder<br/>感知帧构建<br/>public world state · recent events · visible refs · runtime context"]
    A2["Memory Context<br/>记忆上下文<br/>working memory · episodic memory · relationship records · bounded recall"]
    A3["Goal, Need and Feedback Context<br/>目标、需求与反馈上下文<br/>goals · constraints · prior results · environmental feedback"]
    A4["Intent Formation<br/>意图形成<br/>action intent · no-intent · rest/sleep intent · uncertainty"]
    A5["Action Request<br/>动作请求<br/>typed action · target refs · rationale · expected effect · provenance"]
    A6["Action Adapter<br/>动作适配器<br/>maps Agent intent to public runtime action contract"]
    A7["Action Legality and Result<br/>动作合法性与结果<br/>WorldEngine decides legality and consequences"]
    A8["Agent State Update<br/>Agent 状态更新<br/>public state · action result · feedback · relationship signals"]
    A9["Memory Write Boundary<br/>记忆写入边界<br/>public evidence refs · working / episodic records · no raw thought"]
    A10["Rest, Sleep and Consolidation<br/>休息、睡眠与巩固<br/>summaries · personality drift signals · self-narrative summaries"]
    A11["Agent Continuity Evidence<br/>Agent 连续性证据<br/>perception · intent · action result · memory/consolidation summary"]

    A0 --> A1
    A1 --> A2
    A2 --> A3
    A3 --> A4
    A4 --> A5
    A5 --> A6
    A6 --> A7
    A7 --> A8
    A8 --> A9
    A9 --> A10
    A10 --> A11
    A4 -->|"no-intent / 无行动"| A11
  end

  R8 -. "Visible public state / 可见公开状态" .-> A1
  R11 -. "Recent event evidence / 近期事件证据" .-> A1
  A7 -->|"submit to runtime legality gate / 提交运行时合法性门禁"| R6
  R6 -->|"action result / 动作结果"| A7
  A8 --> R8
  A11 --> R11

  subgraph SPINE["4. Shared Spine / 共享主脊柱"]
    E0["Event Contract<br/>事件契约<br/>type · refs · source · target · location · visibility · importance · causality"]
    E1["State, Diff and Snapshot Contract<br/>状态、Diff 与快照契约<br/>canonical state · applied diffs · snapshot material"]
    E2["Memory and Agent Evidence Contract<br/>记忆与 Agent 证据契约<br/>public summaries · evidence refs · bounded recall · consolidation records"]
    E3["Persistence Boundary<br/>持久化边界<br/>world specs · runtime state · events · snapshots · memory records · evidence"]
    E4["Redaction and Public Evidence<br/>脱敏与公开证据<br/>no secrets · no raw prompts · no private memory payloads · no raw thought"]
    E5["API Envelope and Discovery<br/>API 包装与发现<br/>manifest · routes · schemas · health · capabilities"]
    E6["Validation and Scorecard Contract<br/>验证与评分契约<br/>pass · fail · blocked · not_run · checker-readable artifacts"]
  end

  E0 -. "Constrains generated and runtime events / 约束生成与运行事件" .-> G5
  E0 -. "Event spine / 事件主脊柱" .-> R5
  E0 -. "Agent experiences are event-linked / Agent 经验关联事件" .-> A11
  E1 -. "State evidence / 状态证据" .-> R8
  E2 -. "Agent continuity evidence / Agent 连续性证据" .-> A9
  E3 -. "Stores / 存储" .-> G10
  E3 -. "Stores / 存储" .-> R9
  E3 -. "Stores / 存储" .-> A9
  E4 -. "Redacts / 脱敏" .-> G4
  E4 -. "Redacts / 脱敏" .-> R11
  E4 -. "Redacts / 脱敏" .-> A11
  E5 -. "Exposes / 暴露" .-> R2
  E5 -. "Exposes / 暴露" .-> G0
  E5 -. "Exposes / 暴露" .-> A5
  E6 -. "Classifies evidence / 分类证据" .-> R11

  subgraph PROJECTION["5. Projection, Debugging and External Consumers / 投影、调试与外部消费者"]
    P0["Projection Read Model<br/>投影读模型<br/>public state · event timeline · diffs · snapshots · Agent summaries"]
    P1["Dashboard<br/>控制台<br/>inspect · step · params · generation preview · evidence review"]
    P2["Godot Adapter<br/>Godot 适配器<br/>visualize world · render locations / actors / state · send public actions"]
    P3["Validation Client<br/>验证客户端<br/>operate public APIs · record logs · export evidence · no provider ownership"]
    P4["Narrative, Replay and Diagnostic Views<br/>叙事、回放与诊断视图<br/>read-only summaries · why changed · what Agent publicly knows"]
    P5["Other Engine Adapters<br/>其他引擎适配器<br/>Unity · Unreal · web canvas · CLI · custom clients"]
    P6["Client Operation Boundary<br/>客户端操作边界<br/>input becomes public API request, runtime control, or bounded direction"]
    P7["Evidence Export<br/>证据导出<br/>redacted bundle · operation log · API log · scorecard input"]

    P0 --> P1
    P0 --> P2
    P0 --> P3
    P0 --> P4
    P0 --> P5
    P1 --> P6
    P2 --> P6
    P3 --> P6
    P3 --> P7
    P4 --> P7
  end

  R8 --> P0
  R11 --> P0
  A11 --> P0
  P6 -->|"public API only / 仅公开 API"| R2
  P6 -->|"bounded direction / 有界方向"| R4
  P6 -->|"typed Agent action request / 类型化 Agent 动作请求"| A5
  R11 --> P7
  A11 --> P7
  E6 -. "checker input / checker 输入" .-> P7

  S2 -. "May observe and operate, but cannot own canonical mutation / 可观察和操作，但不拥有正典变更" .-> PROJECTION
```
