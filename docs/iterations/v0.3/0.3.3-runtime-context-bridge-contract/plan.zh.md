# Plan

## 文件

创建：

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md`
- 对应的 `*.zh.md` 镜像。

修改：

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

不要触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- 测试实现、fixture、migration、API 路由、schema、运行时服务、归档、参数、
  事件或持久化代码。

## 步骤

1. 阅读仓库指导、v0.3 里程碑文档、加载器契约、加载器包评审和当前运行时
   实现文档。
2. 在 `docs/contracts/` 中起草运行时上下文桥接契约。
3. 起草完整 0.3.3 迭代包文档，包含假设、风险、验收标准和验证命令。
4. 同步英文和中文镜像。
5. 在迭代包 README 和里程碑索引中把 0.3.3 标记为 `ready for review`。
6. 运行文档和范围检查。
7. 在 `review.md` 中记录当前会话文档证据。

## 验证

使用 `test-plan.md` 中的文档检查。本包不修改实现文件，因此不计划运行运行时或
前端测试。
