# Review

状态：`ready for review`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/**` | 新增文档阶段最终收口包文档及中英文镜像。 |
| `docs/iterations/v0.3/README.md`, `README.zh.md` | 将 0.3.8 包状态更新为 `ready for review`。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `v0.3-plan.zh.md` | 将 0.3.8 详细计划状态更新为 `ready for review`，保持状态一致。 |

## 已运行命令

```bash
git status --short --branch
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' docs/iterations/README.md
sed -n '1,260p' docs/project-north-star.md
sed -n '1,260p' docs/product-model.md
sed -n '1,260p' docs/scope-boundaries.md
sed -n '1,260p' docs/roadmap.md
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,300p' docs/iterations/v0.3/v0.3-plan.md
sed -n '872,960p' docs/iterations/v0.3/v0.3-plan.md
sed -n '829,920p' docs/iterations/v0.3/v0.3-plan.zh.md
sed -n '1,260p' docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.md
sed -n '1,260p' docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/review.md
sed -n '1,260p' docs/iterations/v0.3/v0.3-release-candidate-bundle.md
sed -n '1,220p' docs/iterations/v0.3/evidence-index.md
sed -n '1,220p' docs/iterations/v0.3/compatibility-audit.md
sed -n '1,220p' docs/iterations/v0.3/findings.md
sed -n '1,240p' docs/iterations/templates/contract.md
sed -n '1,260p' docs/iterations/v0.2/0.2.12-v0.2-final-closeout/contract.md
mkdir -p docs/iterations/v0.3/0.3.8-v0.3-final-closeout
```

验证命令将在执行后记录如下。

```bash
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.md" && test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.zh.md" || exit 1; done
rg -n '0\.3\.8-v0\.3-final-closeout|Status: ready for review|状态：`ready for review`' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md
rg -n 'final closeout|release-candidate|not released|P1|P2|P3|v0\.4|human / ChatGPT|historical evidence' docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
if rg -n '^\| [^|]+ \| [^|]+ \| [^|]+ \| P[12] \| (open|accepted handoff)' docs/iterations/v0.3/findings.md; then exit 1; else exit 0; fi
tmp_patterns="$(mktemp)"; p1="concrete"; p2="demo"; p3="external"; p4="validation"; printf '%s\n' "$p1-$p2-cell" "$p3-$p4-world" "$p1 concrete fixture path" > "$tmp_patterns"; rg -n -i -f "$tmp_patterns" docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md; rc=$?; rm -f "$tmp_patterns"; test "$rc" -eq 1
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
rg -n '[[:blank:]]$' docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
git status --short --branch
```

## 测试结果

- `git diff --check` 退出码为 `0`；未报告空白错误。
- 七个包文档名的英文 / 中文镜像文件检查退出码为 `0`。
- 状态一致性 grep 退出码为 `0`；包 README、中文 README 镜像、v0.3
  里程碑索引和 v0.3 计划文档都将 0.3.8 标记为 `ready for review`。
- 收口门禁措辞 grep 退出码为 `0`；包文档和 v0.3 状态文档包含 final
  closeout、release-candidate、not-released、P1/P2/P3、v0.4 交接、
  human / ChatGPT 批准和 historical-evidence 护栏措辞。
- P1/P2 阻塞项检查退出码为 `0`；`findings.md` 中没有 open 或
  accepted-handoff 状态的 P1/P2 问题。
- 具体演示锚点扫描使用了临时未跟踪 pattern 文件。底层 `rg` 退出码为 `1`，
  没有匹配，包装检查退出码为 `0`。
- 针对 `git status --porcelain=v1 -uall` 的变更文件范围检查退出码为 `1` 且
  无输出，表示已跟踪和未跟踪变更都限制在 `docs/iterations/v0.3/`。
- 行尾空白 grep 退出码为 `1` 且无输出，表示已触及文档中未发现行尾空白。
- `git status --short --branch` 退出码为 `0`；分支 `v0.3` 领先
  `origin/v0.3` 22 个提交，并且只显示 v0.3 迭代文档变更及未跟踪的 0.3.8
  包目录。

后端、前端、API smoke、E2E、Agent smoke、运行时行为、构建、schema 执行、
fixture、migration 和测试实现检查未运行，因为本包是仅文档包，且未修改实现
文件。

## 兼容性评审

本次文档阶段不得改变运行时行为、schema 行为、事件行为、API 响应形状、归档
行为、参数行为、前端行为、fixture 行为、migration 行为、测试行为或旧路径
`backend/worldengine/` 行为。

## 范围评审

本次变更仅限文档阶段准备：

- 只创建 0.3.8 包文档。
- 为 0.3.8 评审门禁同步 v0.3 状态文档。
- 评审批准前不更新最终发布状态。
- 不实现运行时、schema、API、前端、fixture、migration 或测试变更。

## 假设

- `docs/iterations/v0.3/README.md` 是任务中所说的里程碑索引。
- 0.3.7 发布候选证据仍是最终收口基础。
- 最终发布措辞仍需要人工 / ChatGPT 批准。
- 开放 P3 问题只有在最终评审接受为非阻塞时，才可作为交接项保留。

## 未解决问题

- P1：起草包文档期间未发现。
- P2：起草包文档期间未发现。
- P3：现有 v0.3 P3 问题保持开放，除非最终评审改变分类。

## 最终判断

文档包已 ready for review。最终收口实现必须等待人工 / ChatGPT 批准，并且必须
限制在 `contract.md` 允许的文档路径内。
