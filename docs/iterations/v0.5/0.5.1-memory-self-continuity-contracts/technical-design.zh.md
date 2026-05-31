# 技术设计

状态：review complete

## 当前状态

v0.4 提供 request-driven Agent-in-World minimal loop，包括 bounded perception、
action intent/result contracts、经过验证的 `noop` 和 `params.patch`，以及
`POST /world/agent/loop/step`。v0.4 不包含 memory 或 self-continuity。

`0.5.0` 创建了 v0.5 campaign root，并保持 implementation authorization 关闭。
当前还不存在 v0.5 memory implementation files。

## 契约对齐与不变量

本包是 documentation-only。它保持以下不变量：

- 不修改 implementation file class。
- 不修改 runtime behavior。
- 不修改 public API。
- 不修改 test implementation。
- `implementation_authorized` 保持 `no`。
- working memory 和 episodic memory 是下一实现切片唯一可授权的概念，而且必须等
  `0.5.2` 通过自身 documentation/contract evaluator 后才能实现。
- relationship state、self-summary、reflection records 和 personality drift signals
  仍只保留 contract/schema semantics。

## 文档结构

本包文档组织如下：

- `README.md`：package goal、scope、deliverables 和 document list。
- `intent.md`：problem、goal、non-goals、roadmap relationship 和 handoff。
- `contract.md`：public concepts、authorization criteria、compatibility requirements、
  allowed changes、forbidden changes 和 follow-ups。
- `technical-design.md`：documentation structure 和 semantic design。
- `test-plan.md`：docs-only verification commands 和 not-run rationale。
- `plan.md`：ordered execution steps 和 stop conditions。
- `review.md`：evidence、evaluator findings、compatibility review、scope review、
  unresolved findings 和 final assessment。

每个文件都有 `.zh.md` 镜像。

## 概念模型

概念模型把 record types 与 behavior 分开：

- working memory：短期、bounded current-context record。
- episodic memory：event-linked experience record。
- relationship state：结构化关系语义，暂不实现 behavior。
- self-summary：continuity summary 语义，暂不生成。
- reflection record：self-assessment / feedback record 语义，暂不自动 reflection。
- personality drift signal：未来 behavior-drift signal 语义，暂不作为 action modifier。

## 计划中的 Schema 语义

后续 schema files 应使用 additive optional models 和 generic identifiers。
契约期望以下字段或等价语义：

- common fields：`memory_id`、`agent_id`、`world_id`、`source`、`created_at`、
  适用时的 `updated_at`，以及 evidence references。
- working memory fields：`content`、`priority`、`expires_at` 或 bounded lifetime metadata，
  以及 provenance。
- episodic memory fields：`summary`、`event_refs`、`tick`、`world_time`、
  optional action/outcome references，以及 provenance。
- follow-up concept fields：target references、summary facets、reflection triggers、
  drift dimensions、strengths 和 evidence references。

上述名称是计划语义，不是本包的 implementation commitment。`0.5.2` 必须在自己的已评审
technical design 中选择精确 model names 和 fields。

## 兼容性策略

由于本包只修改文档，兼容性通过范围控制来保持。下一个 implementation package 必须把以下表面视为敏感：

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- `LoopStep`
- `POST /world/agent/loop/step`
- params propose/apply route
- runtime tick/world time behavior
- event route serialization 和 optional `Event.refs`
- archive behavior
- API envelope/error shape

## 防漂移规则

- 不把 docs-only definitions 描述成已实现 runtime behavior。
- 不把 v0.4 evidence 描述成 v0.5 pass evidence。
- 保持英文与中文镜像语义等价。
- 明确 future-version ownership：v0.6 generation、v0.7 external validation readiness、
  v0.8 projection readiness。

## 风险

- 风险：概念语言暗示隐藏 behavior。
  缓解：每个概念都说明自己是否只是 record semantics。
- 风险：第一个实现扩大到 loop integration。
  缓解：authorization criteria 将 `0.5.2` 限制为 working/episodic memory substrate，
  并把 loop integration 放到 `0.5.3`。
- 风险：mirror drift。
  缓解：package 要求中文镜像，并运行 mirror/file existence check。
