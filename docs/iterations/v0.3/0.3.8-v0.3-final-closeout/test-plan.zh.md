# Test Plan

## 单元测试

文档阶段或最终收口实现阶段均不计划单元测试，因为本包不得修改运行时、schema、
API、前端、fixture、migration 或测试实现文件。

## 回归测试

文档阶段不要求后端、前端、API smoke、E2E、Agent smoke、运行时、schema 执行、
fixture、migration 或构建回归测试。如果最终评审要求在收口前提供新的行为
证据，必须在 0.3.8 实现会话运行相应命令，并记录到 `review.md`。

## 命令

文档阶段验证：

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

评审批准后的预期实现阶段验证：

```bash
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.md" && test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.zh.md" || exit 1; done
rg -n 'final / closeout complete|final closeout complete|final review|no unresolved P1/P2|0\.3\.8|review complete|accepted handoff' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md docs/iterations/v0.3/findings.md
if rg -n '^\| [^|]+ \| [^|]+ \| [^|]+ \| P[12] \| (open|accepted handoff)' docs/iterations/v0.3/findings.md; then exit 1; else exit 0; fi
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/(releases/v0\.3|iterations/v0\.3/)'
rg -n '[[:blank:]]$' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/findings.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout
git status --short --branch
```

## 验收标准

- README、intent、contract、technical design、test plan、plan 和 review 的包文档
  及中文镜像都存在。
- 文档阶段状态在本包 README 和 v0.3 里程碑索引中为 `ready for review`。
- 最终发布状态保持受人工 / ChatGPT 评审批准约束。
- 未解决 P1/P2 问题不得通过最终收口。
- 当前会话验证必须区分文档检查与历史包测试证据。
- 变更文件保持在允许的文档路径内。
- 不引入具体演示世界、具体外部验证世界、fixture 种子数据、产品 UI 或应用
  专用后端细节。

## 未运行

后端、前端、API smoke、E2E、Agent smoke、运行时行为、构建、schema 执行、
fixture、migration 和测试实现检查不计划用于文档阶段，因为本阶段只创建包文档
和状态文档。
