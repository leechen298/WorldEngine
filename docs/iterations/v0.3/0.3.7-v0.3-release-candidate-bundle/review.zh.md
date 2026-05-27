# 评审

状态：待评审

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`, `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md` | 新增 v0.3 发布候选证据包和同步中文镜像。 |
| `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/**` | 新增完整 0.3.7 文档包、最终评审包和中文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中标记 0.3.7 待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 将 0.3.5 和 0.3.6 同步为里程碑索引中的 `review complete` 状态，并保留 0.3.7 的文档阶段待评审状态。 |

## 已运行命令

```bash
git status --short --branch
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' docs/iterations/README.md
sed -n '1,220p' docs/project-north-star.md
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,320p' docs/iterations/v0.3/v0.3-plan.md
sed -n '1,240p' docs/iterations/v0.3/final-review-bundle-template.md
sed -n '1,280p' docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.md
sed -n '786,872p' docs/iterations/v0.3/v0.3-plan.md
sed -n '746,827p' docs/iterations/v0.3/v0.3-plan.zh.md
sed -n '1,280p' docs/iterations/v0.3/evidence-index.md
sed -n '1,300p' docs/iterations/v0.3/compatibility-audit.md
sed -n '1,220p' docs/iterations/v0.3/findings.md
```

验证命令将在执行后记录如下。

```bash
git diff --check
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.md
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.md" && test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.zh.md" || exit 1; done
rg -n '0\.3\.7-v0\.3-release-candidate-bundle|Status: ready for review|状态：待评审|状态：`待评审`' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.zh.md
rg -n 'not final|not released|release candidate|release-candidate|0\.3\.8|final closeout|final release|未发布|最终收口|发布候选' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
rg -n '0\.3\.[0-7]|evidence-index|compatibility-audit|findings|review\.md|implemented|documented|tested|planned|not implemented|partial|historical|finding|已实现|已文档化|已测试|未实现|问题' docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
! rg -n '<[c]oncrete demo-anchor sentinel patterns omitted from review evidence>' docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/findings.md
! rg -n '[ \t]$' docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle docs/iterations/v0.3/v0.3-release-candidate-bundle.md docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
git status --short --branch
git diff --stat
```

评审后 P1 状态一致性修订命令：

```bash
git diff --check
rg -n '0\.3\.5 External Fixture|0\.3\.6 Runtime Bridge|Status: review complete|状态：评审完成' docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
git status --short --branch
git diff --stat
```

## 测试结果

- `git diff --check` 退出码为 `0`；未报告空白字符错误。
- 发布候选包和最终评审包必需文件存在性检查退出码为 `0`。
- `README`、`intent`、`contract`、`technical-design`、`test-plan`、`plan` 和
  `review` 的包镜像存在性循环退出码为 `0`。
- 状态一致性 grep 退出码为 `0`；0.3.7 在包 README、里程碑索引和 v0.3 计划中
  标记为 `ready for review` / `待评审`。
- 发布状态表述 grep 退出码为 `0`；候选文档和发布占位文档保持发布候选 /
  非最终 / 未发布措辞，并把最终收口推迟到 0.3.8。
- 证据可追溯 grep 退出码为 `0`；发布候选文档包含包 ID、证据文档、评审引用和
  状态类别。
- 第一次抽象锚点扫描命令匹配到了 `review.md` 和 `review.zh.md` 中记录的命令
  文本自身，因此未作为验收证据。重新运行的具体演示锚点 sentinel 扫描退出码为
  `0`，无匹配。
- 对新增 0.3.7 包和发布候选包文件运行的尾随空白 grep 退出码为 `0`，无匹配。
- 变更文件范围护栏退出码为 `1` 且无输出；这是预期结果，表示所有变更文件都在
  批准的 `docs/iterations/v0.3/` 路径下。
- `git status --short --branch` 退出码为 `0`，只显示 v0.3 迭代文档变更。
- `git diff --stat` 退出码为 `0`；已跟踪状态更新仅限 v0.3 索引和计划文档，
  新增未跟踪 0.3.7 文档在 `git status` 中可见。
- 评审后 `git diff --check` 退出码为 `0`。
- 评审后 0.3.5/0.3.6 状态 grep 退出码为 `0`；`v0.3-plan.md`、
  `v0.3-plan.zh.md`、`README.md` 和 `README.zh.md` 现在一致记录
  0.3.5 和 0.3.6 为 `review complete` / `评审完成`。
- 评审后变更文件范围护栏退出码为 `1` 且无输出；这是预期结果，表示所有变更文件仍
  在批准的 `docs/iterations/v0.3/` 文档路径下。
- 未运行后端、前端、API 冒烟、E2E、Agent 冒烟、运行时行为、构建、迁移、
  fixture 或 schema 测试，因为本包仅文档且未修改实现文件。

## 文档修订记录

- P1 `status-consistency`：已解决。`v0.3-plan.md` 和
  `v0.3-plan.zh.md` 已更新，使 0.3.5 和 0.3.6 与里程碑索引中的
  `review complete` / `评审完成` 状态一致。
- 本次修订未扩大或关闭 P2/P3 问题。

## 兼容性评审

本包仅修改文档，因此运行时行为、schema 行为、API 响应形状、事件行为、
归档行为、参数行为、前端行为、fixture 行为、迁移行为、后端测试行为和旧路径
`backend/worldengine/` 行为保持不变。

## 范围评审

本包保持在 0.3.7 文档范围内。它打包证据并准备发布候选评审；不实现修复，也不
添加新的运行时能力。

## 假设

- 先前包评审准确记录历史证据。
- 0.3.6 证据和兼容性审计足以作为发布候选准备输入。
- 0.3.8 在发布候选评审批准前仍受阻塞。

## 未解决问题

- P1：无开放项。0.3.5 和 0.3.6 的评审后状态一致性问题已在本次文档修订中解决。
- P2：未发现。
- P3：`v0.3-P3-001` 保持开放。它记录 0.3.6 清单措辞不一致，不阻塞 0.3.7
  发布候选评审。
- P3：根据 0.3.2 证据，仓库根目录直接运行 `pytest` 不可靠；后续运行时验证应在
  `backend/` 使用后端 venv `python -m pytest`。
- P3：除非后续运行更广的 UI 或 E2E 冒烟，否则前端可见兼容性证据仍是间接的。
- P3：外部 fixture 报告可能在后续验证准备版本中需要更严格的机器可读细节。

## 最终判断

待评审
