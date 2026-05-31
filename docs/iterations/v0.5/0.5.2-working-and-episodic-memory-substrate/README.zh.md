# 0.5.2 Working And Episodic Memory Substrate

状态：review complete
类型：mixed
implementation_authorized: yes

## 目标

为 WorldEngine agents 实现第一层 additive generic working-memory 与
episodic-memory substrate。

本实现刻意保持 non-public 和 in-memory only。它只添加 generic schemas、小型
in-memory substrate service/store 和 focused backend tests。不添加 public APIs、
loop integration、persistence、frontend behavior、relationship behavior、
self-summary generation、reflection 或 personality drift behavior。

## 范围

允许：

- 添加 `backend/app/schemas/agent_memory.py`。
- 添加 `backend/app/agent/memory.py`。
- 在 `backend/app/tests/test_agent_memory_*.py` 下添加 focused backend tests。
- 更新本包 docs、review evidence 和中文镜像。
- 运行 focused backend memory tests 以及相邻 v0.4 loop/perception/API compatibility tests。

禁止：

- 不修改 `backend/worldengine/`。
- 不添加 public runtime APIs 或 routes。
- 不把 memory 接入 `POST /world/agent/loop/step`；该范围属于 `0.5.3`。
- 不修改 `ActionIntent`、`ActionResult`、accepted action types 或 `params.patch` semantics。
- 不实现 relationship behavior、self-summary generation、automatic reflection、
  personality drift action modifiers、durable persistence、migrations、frontend behavior、
  concrete world content 或 private validation oracle details。

## 交付物

- Additive working-memory 和 episodic-memory schema models。
- Generic in-memory memory substrate/store。
- Focused backend tests，证明 schema semantics、bounded working-memory selection、
  episodic event references、copy isolation，以及按 `agent_id`/`world_id` 做 generic scoping。
- 现有 Agent Loop 和 perception behavior 的相邻兼容性证据。
- Review evidence，包含 documentation/contract evaluator、TDD red/green evidence、
  implementation-scope evaluator、code-review evaluator、validation-evidence evaluator 和
  closeout consistency evaluator。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 当前评估

本包已 review complete。Memory substrate implementation 保持在 approved new
schema/store/test files 内，focused 和相邻 compatibility evidence 已记录在 `review.md`。
