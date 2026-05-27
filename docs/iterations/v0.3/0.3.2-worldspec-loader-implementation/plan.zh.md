# 计划

## 文件

文档阶段创建：

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.zh.md`
- 对应英文文档。

文档阶段修改：

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

文档评审批准后的实现阶段创建：

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`

不得触碰：

- `backend/app/core/runtime_engine.py`
- API 路由模块。
- schema 模块，除非文档评审明确修订本包。
- 持久化、归档、参数、事件、前端、fixture、迁移和旧运行时实现文件。
- 具体外部验证世界或演示世界数据。

## 步骤

文档阶段：

1. 阅读 v0.3 里程碑文档、0.3.1 加载器契约和迭代标准。
2. 起草完整 0.3.2 package 文档，包含假设、风险、验收标准和验证命令。
3. 同步英文和中文镜像。
4. 在 package README 和里程碑索引中把 0.3.2 标记为 `ready for review` /
   `待评审`。
5. 运行文档和范围检查。
6. 在 `review.md` / `review.zh.md` 中记录当前会话文档证据。

文档评审批准后的实现阶段：

1. 重新阅读 `intent.md`、`contract.md`、`technical-design.md`、`test-plan.md`、
   `plan.md` 和 `review.md`。
2. 新增满足已评审契约的最小加载器模块。
3. 用中立输入数据新增聚焦加载器测试。
4. 运行 `test-plan.md` / `test-plan.zh.md` 中的聚焦和回归命令。
5. 更新 `review.md` / `review.zh.md`，记录变更文件、命令结果、兼容性评审、
   范围评审、未解决发现和最终判断。

## 验证

文档阶段使用 `test-plan.md` / `test-plan.zh.md` 中的文档检查。

实现阶段必须包含聚焦加载器测试、现有 schema smoke 测试、空白检查、导入 /
耦合检查、具体锚点扫描，以及实际影响范围要求的任何更广后端回归。
