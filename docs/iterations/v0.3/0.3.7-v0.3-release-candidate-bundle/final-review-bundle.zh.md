# 最终评审包

## 包名

`0.3.7-v0.3-release-candidate-bundle`

## 分支

`v0.3`

## 基础提交

`<最终评审前用 git rev-parse 确认>`

## 头部提交

`<最终评审前用 git rev-parse 确认>`

## 状态

`待评审 / 发布候选 / 非最终发布`

## 摘要

本仅文档包组装了 v0.3 发布候选证据包和最终评审交接。它不修改运行时、schema、
API、前端、fixture、迁移、测试或旧实现文件，也不声明 v0.3 最终发布。

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/v0.3-release-candidate-bundle.md` | 新增英文发布候选证据包。 |
| `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md` | 新增同步中文发布候选证据包。 |
| `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md` | 新增英文最终评审交接。 |
| `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md` | 新增同步中文最终评审交接。 |
| `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/**` | 新增包文档和评审证据。 |
| `docs/iterations/v0.3/README.md`, `README.zh.md` | 标记 0.3.7 待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `v0.3-plan.zh.md` | 同步 0.3.7 状态。 |

## 契约映射

| 契约要求 | 证据 |
|---|---|
| 创建发布候选包文档和中文镜像。 | `v0.3-release-candidate-bundle.md` 和 `.zh.md` 存在。 |
| 创建最终评审包文档和中文镜像。 | `final-review-bundle.md` 和 `.zh.md` 遵循最终评审模板章节。 |
| 将声明映射到证据或限制状态。 | 候选包包含包、兼容性和声明到证据矩阵。 |
| 保持 P1/P2/P3 问题可见。 | 候选包列出没有开放 P1/P2，并记录开放 P3。 |
| 避免最终发布状态。 | 状态措辞保持发布候选 / 非最终 / 未发布。 |
| 保持变更文件限于文档。 | 评审证据记录变更文件范围护栏。 |

## 禁止变更确认

本包不计划变更运行时服务、schema 实现文件、API 路由、前端文件、fixture、迁移、
测试实现文件、旧路径 `backend/worldengine/`、外部仓库、私有验证内部细节或具体
外部世界数据。不声明最终发布状态。

## 已运行命令

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.md
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.md" && test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.zh.md" || exit 1; done
rg -n '0\.3\.7-v0\.3-release-candidate-bundle|Status: ready for review|状态：待评审|状态：`待评审`' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.zh.md
rg -n 'not final|not released|release candidate|release-candidate|0\.3\.8|final closeout|final release|未发布|最终收口|发布候选' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
rg -n '0\.3\.[0-7]|evidence-index|compatibility-audit|findings|review\.md|implemented|documented|tested|planned|not implemented|partial|historical|finding' docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
git status --short --branch
```

## 测试结果

`review.md` 记录了精确验证结果。文档健康、文件存在性、镜像存在性、状态一致、
发布措辞、证据可追溯、具体演示锚点 sentinel 扫描和变更文件范围检查均通过。
未运行后端、前端、API 冒烟、E2E、Agent 冒烟、运行时、schema、fixture、迁移或
构建测试，因为本包仅文档。

## 兼容性评审

运行时行为、API 响应形状、事件行为、归档行为、参数行为、前端可见行为、schema
行为、测试、fixture、迁移和旧路径行为因仅文档范围而保持不变。

## 范围评审

预期 diff 保持在 0.3.7 包契约内：仅 v0.3 迭代文档、发布候选包文档、最终评审包
文档和状态同步。

## 未解决 P1/P2/P3

- P1：未发现。
- P2：未发现。
- P3：0.3.6 清单措辞问题保持开放，且不阻塞。
- P3：根目录 pytest 命令不可靠仍是未来验证计划注意事项。
- P3：除非要求新的 UI 或 E2E 冒烟，否则前端可见兼容性证据仍是间接的。
- P3：更严格的外部 fixture 报告自动化属于后续验证准备版本。

## 建议下一步

人工 / ChatGPT 应评审本发布候选包。如果接受，
`0.3.8-v0.3-final-closeout` 可以执行最终收口。

## ChatGPT 整体评审请求

请评审范围、证据可追溯性、兼容性声明、未解决问题、发布状态措辞，以及进入
0.3.8 最终收口的准备度。
