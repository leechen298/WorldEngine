# 0.3.4 运行时上下文桥接实现

状态：`review complete`

类型：混合或代码

## 目标

把已验证的 `WorldSpec` 加载器输出桥接为最小的可选、惰性运行时
上下文，同时保持 v0.1 运行时、API、事件、参数、归档、前端可见形状和
遗留行为兼容。

## 范围

本包为小型运行时上下文边界准备已评审的实现契约。运行时上下文可以从
成功的加载器输出派生，并且只有作为可选惰性上下文时才可以被
`RuntimeEngine` 持有。

本包不得把 `WorldCell` 变成运行时模块，不得生成世界，不得驱动 tick
逻辑，不得改变既有 API 响应形状，不得发出新事件，不得改变归档或参数
行为，不得添加前端行为，不得创建 fixture，也不得实现 Agent、记忆、
自连续性、投影、故事或 NPC 行为。

## 文档

- [x] `intent.zh.md`
- [x] `contract.zh.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.zh.md`
- [x] `plan.zh.md`
- [x] `review.zh.md`

由于这是混合或代码包，必须包含 `technical-design.zh.md` 和
`test-plan.zh.md`。

## 交付物

- `backend/app/core/runtime_context.py`
- 仅在评审后的设计需要时添加聚焦的桥接集成修改。
- `backend/app/tests/test_runtime_context_bridge.py`
- 运行时、API、事件、参数、归档、前端可见形状和遗留边界的兼容证据。
- 本包文档及匹配的英文镜像。

## 状态清单

- [x] 文档已起草
- [ ] 契约已评审
- [ ] 技术设计已评审
- [ ] 测试计划已评审
- [ ] 实现完成
- [ ] 实现证据完成
- [ ] 评审完成

## 交接

只有在本文档包通过评审后才可以开始实现。文档起草阶段不得把本包标记为
`ready for implementation`；该状态只属于评审后的闸门。
