# Review

状态：待评审

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/evidence-index.md`, `docs/iterations/v0.3/evidence-index.zh.md` | 新增 v0.3 证据矩阵、兼容性表面索引、假设、风险和交接准备度。 |
| `docs/iterations/v0.3/compatibility-audit.md`, `docs/iterations/v0.3/compatibility-audit.zh.md` | 新增 v0.3 兼容性审计、发现、假设和发布候选验证要求。 |
| `docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/**` | 新增完整 0.3.6 包文档和中英文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在 milestone index 中将 0.3.6 标记为 ready for review。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 同步 0.3.6 文档阶段待评审状态。 |

## 已运行命令

```bash
git status --short --branch
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' docs/iterations/README.md
sed -n '1,260p' docs/project-north-star.md
sed -n '1,260p' docs/product-model.md
sed -n '1,260p' docs/scope-boundaries.md
sed -n '1,300p' docs/roadmap.md
find docs/iterations/v0.3 -maxdepth 2 -type f | sort
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,1040p' docs/iterations/v0.3/v0.3-plan.md
sed -n '1,320p' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md
sed -n '1,260p' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md
sed -n '1,320p' docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.md
```

验证命令会在执行后记录如下。

```bash
git diff --check
for f in docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/evidence-index.zh.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/compatibility-audit.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.zh.md; do test -f "$f" || exit 1; done
rg -n '0\.3\.6-runtime-bridge-evidence-and-compatibility-audit|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
rg -n 'runtime|API|event|archive|params|frontend|schema|fixture|legacy|WorldSpec loader|runtime context bridge|P1|P2|P3|handoff' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/evidence-index.zh.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/compatibility-audit.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
git status --short --branch
git diff --stat
```

## 测试结果

- `git diff --check` 退出 `0`；未报告空白错误。
- 必需的英文和中文审计文件、包文件存在性检查退出 `0`。
- 状态同步 grep 退出 `0`；0.3.6 已在包 README、milestone index 和 v0.3 plan 中标记为
  `ready for review` / `待评审`。
- 兼容性表面和发现术语 grep 退出 `0`；审计文档包含 runtime、API、event、archive、
  params、frontend、schema、fixture、legacy、loader、bridge、发现严重级别和 handoff 术语。
- 具体锚点哨兵 no-match 检查退出 `0`；未发现具体样例或外部验证世界哨兵内容。
- 实现范围状态检查退出 `0`；本仅文档包未修改 backend、frontend、schema、fixture、
  migration、test implementation 或 legacy runtime 路径。
- `git status --short --branch` 退出 `0`；变更路径仅限 v0.3 文档和新的 0.3.6
  审计/包文档。
- 后端、前端、API、E2E、Agent smoke、运行时行为、构建、迁移、样例和 schema 测试不在计划内，
  因为本包只修改文档。

## 兼容性评审

本仅文档包不改变运行时行为、schema 行为、API 返回形状、事件行为、归档行为、
参数行为、前端行为、样例行为、迁移行为、后端测试行为或旧路径 `backend/worldengine/` 行为。

## 范围评审

本包保持在 0.3.6 文档范围内。它审计既有证据和兼容性，不实现修复，也不添加新运行时能力。

## 假设

- 既有 package review 文件准确记录了本审计可用证据。
- 因为加载器和桥接包没有修改前端文件或暴露新 API route，所以前端可见兼容性可分类为未触及。
- v0.4 交接准备度表示在 v0.3 发布候选和收口门禁后可用于后续规划，不是实现许可。

## 未解决发现

- P1：未识别。
- P2：未识别。
- P3：根据 0.3.2 证据，仓库根目录直接 `pytest` 命令在当前环境不可靠；后续包的测试计划应从 `backend/` 使用后端 venv `python -m pytest`。
- P3：前端可见兼容性证据是间接的，除非后续发布候选包运行更广的 UI 或 E2E smoke 覆盖。
- P3：外部样例报告后续可能需要更严格的机器可读 schema 和更多公开 CLI/API 文档。

## 最终判断

待评审
