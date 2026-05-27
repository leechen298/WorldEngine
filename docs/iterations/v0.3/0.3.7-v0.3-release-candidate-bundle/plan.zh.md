# 计划

## 文件

创建：

- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md`
- 本包英文和中文包文档。

修改：

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
- 仅在发现新的或变化的问题时修改 `docs/iterations/v0.3/findings.md`。
- 本包 `review.md` 和 `review.zh.md`。

不要触碰：

- 运行时实现文件。
- schema 实现文件。
- API 路由文件。
- 前端实现文件。
- fixture 文件。
- 迁移文件。
- 测试实现文件。
- `backend/worldengine/`。
- 外部仓库路径或私有验证内部细节。

## 步骤

1. 阅读仓库指导、v0.3 里程碑文档、包模板、0.3.0 到 0.3.6 评审、
   `evidence-index.md` 和 `compatibility-audit.md`。
2. 从已有证据构建发布候选声明到证据的矩阵。
3. 创建包文档和中文镜像。
4. 创建发布候选包和中文镜像。
5. 使用已有模板结构创建最终评审包和中文镜像。
6. 将 v0.3 包状态字段更新为 `ready for review` / `待评审`。
7. 如果出现证据缺口，记录新的或变化的问题。
8. 运行 `test-plan.md` 中的文档验证检查。
9. 更新本包评审证据和最终判断。

## 验证

必需：

- `git diff --check`
- 必需文件存在性检查。
- 包镜像存在性检查。
- 状态一致性 grep。
- 发布状态表述检查。
- 证据可追溯检查。
- 具体演示锚点扫描。
- 变更文件范围护栏。

不计划：

- 后端测试。
- 前端测试。
- API 冒烟。
- E2E。
- Agent 冒烟。
- 运行时、schema、fixture、迁移或构建测试。

只有在变更文件保持仅文档时，不计划运行这些测试才有效。

## 退出条件

- 发布候选包可交给人工 / ChatGPT 评审。
- 最终评审包完整并符合模板。
- P1/P2 问题可见，并在解决或明确接受前阻塞最终收口。
- 不声明最终发布状态。
- 变更文件保持在批准的文档范围内。
