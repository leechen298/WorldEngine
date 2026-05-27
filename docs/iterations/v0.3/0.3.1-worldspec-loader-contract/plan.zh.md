# 计划

## 文件

创建：

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.zh.md`

修改：

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

不触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- 实现测试、fixture、迁移、API 路由、schema、运行时服务、归档、参数、事件或
  持久化代码。

## 步骤

1. 阅读仓库和 v0.3 里程碑指导。
2. 在 `docs/contracts/` 中起草加载器契约。
3. 起草完整 0.3.1 迭代包文档，包含假设、风险和验证。
4. 同步英文和中文里程碑文档中的 package 状态。
5. 运行文档和范围检查。
6. 在 `review.zh.md` 中记录实际证据。

## 验证

使用 `test-plan.zh.md` 中列出的命令。除非误触实现文件，否则不计划运行运行时
或前端测试；如果误触实现文件，停止并报告范围违规。
