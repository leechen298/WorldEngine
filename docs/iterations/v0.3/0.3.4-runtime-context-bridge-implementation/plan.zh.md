# 计划

## 文件

创建：

- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md`
- 匹配的 `*.zh.md` 镜像。

文档阶段修改：

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

评审后的预期实现阶段文件：

- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`，仅在需要可选惰性上下文存储时触及。
- `backend/app/tests/test_runtime_context_bridge.py`

文档阶段不得触及：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- 实现测试、fixture、migration、API route、schema、运行时服务、归档、参数、事件或
  持久化代码。

## 步骤

1. 阅读仓库指南、v0.3 里程碑文档、0.3.2 加载器实现/评审、0.3.3 桥接契约/评审和当前
   运行时实现文件。
2. 起草完整 0.3.4 包文档，包含假设、风险、验收标准、实现边界和验证命令。
3. 同步英文和中文镜像。
4. 在包 README 和里程碑索引中将 0.3.4 标记为 `ready for review`。
5. 运行文档和范围检查。
6. 在 `review.md` 中记录当前会话文档证据。

## 评审后的实现计划

1. 添加纯运行时上下文桥接模块。
2. 添加聚焦桥接单元测试。
3. 仅在已评审设计要求时添加可选惰性运行时上下文存储。
4. 运行 `test-plan.md` 中列出的聚焦桥接测试和兼容测试。
5. 更新 `review.md`，记录变更文件、命令、结果、兼容评审、范围评审、未解决发现和
   最终评估。

## 验证

评审前使用 `test-plan.md` 中的文档阶段检查。文档阶段未修改实现文件，因此不计划运行
运行时和前端行为测试。
