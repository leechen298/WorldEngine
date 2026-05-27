# 计划

## 文件

- 创建：
  - `docs/iterations/v0.3/evidence-index.md`
  - `docs/iterations/v0.3/evidence-index.zh.md`
  - `docs/iterations/v0.3/compatibility-audit.md`
  - `docs/iterations/v0.3/compatibility-audit.zh.md`
  - `docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/**`
- 修改：
  - `docs/iterations/v0.3/README.md`
  - `docs/iterations/v0.3/README.zh.md`
  - `docs/iterations/v0.3/v0.3-plan.md`
  - `docs/iterations/v0.3/v0.3-plan.zh.md`
- 不触及：
  - `backend/`
  - `frontend/`
  - schema 实现文件
  - 样例
  - 迁移
  - 测试实现文件
  - 旧路径 `backend/worldengine/`

## 步骤

1. 阅读仓库治理、v0.3 milestone 文档、模板和既有 v0.3 包 review。
2. 从已完成 package review 证据起草证据索引。
3. 起草兼容性审计，明确分类、假设、风险和 P1/P2/P3 发现。
4. 创建完整 0.3.6 包文档和中文镜像。
5. 将 0.3.6 milestone 状态更新为 `ready for review`。
6. 运行文档验证命令，并把结果记录到 `review.md`。

## 验证

使用 `test-plan.md` 中的命令。本包不运行实现测试，除非意外修改了实现文件；
这将属于范围违规。
