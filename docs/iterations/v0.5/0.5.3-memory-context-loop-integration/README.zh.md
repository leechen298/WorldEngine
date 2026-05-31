# 0.5.3 Memory Context Loop Integration

状态：review complete
类型：mixed
implementation_authorized: yes

## 目标

使用 `0.5.2` in-memory substrate，将 bounded read-only memory context 接入
Agent Loop perception path，并且不改变 action semantics。

该集成必须是 additive：existing loop requests 继续可用，existing action types 和 result
behavior 保持不变，memory context 只作为 read-only perception data 暴露。

## 范围

允许：

- 给 `PerceptionFrame` 添加 additive memory context schema field。
- 扩展 `PerceptionBuilder`，使其可选地从 in-memory substrate 读取 bounded memory context。
- 只为了 perception context 所需的内部依赖，把 in-memory store wired into backend app。
- 添加 focused perception/loop/API compatibility tests。
- 更新 package docs 和中文镜像。

禁止：

- 不修改 `ActionIntent`、`ActionResult`、accepted action types、action adapter behavior
  或 `params.patch` semantics。
- 不添加 public memory APIs 或 loop request fields。
- 不在 loop step 中写 memory。
- 不实现 relationship behavior、self-summary generation、automatic reflection、
  personality drift action modifiers、durable persistence、migrations、frontend behavior、
  concrete world content 或 private validation oracle details。
- 不修改 `backend/worldengine/`。

## 交付物

- Additive perception memory context schema。
- Perception path 中的 read-only bounded memory context assembly。
- Focused tests，证明旧 loop requests 仍兼容、memory context 有边界且被 copy、
  action semantics 不变。
- 包含必需 evaluator checkpoints 的 review evidence。

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

Documentation/contract gate 已通过，implementation 已授权。Implementation 必须先执行
required TDD red run，再修改 production code。
