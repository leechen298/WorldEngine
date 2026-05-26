# Test Plan

英文版本：`test-plan.md`

## Verification Scope

本包是 documentation-only。Verification 检查 documentation presence、status
consistency、release wording、mirror synchronization、boundary language 和 changed-file
scope。

Runtime、schema、API、frontend、fixture、migration 和 test implementation behavior 不在
scope，除非 reviewer 明确要求 read-only regression commands，且这些 commands 在当前
0.2.12 session 中运行。

## Required Documentation Checks

Documentation-stage preparation 期间运行：

```bash
git diff --check
```

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.2/0.2.12-v0.2-final-closeout/$f.md" &&
  test -f "docs/iterations/v0.2/0.2.12-v0.2-final-closeout/$f.zh.md" ||
  exit 1
done
```

```bash
rg -n '0\.2\.12-v0\.2-final-closeout|Status: ready for review|状态：`ready for review`' \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.md \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.zh.md
```

```bash
rg -n 'final closeout|release-candidate|not final|P1|P2|P3|v0\.2-P3-003|v0\.3 handoff|human / ChatGPT' \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md
```

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.2/'
```

```bash
rg -n '[[:blank:]]$' \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md
```

## Required Implementation-Stage Checks

Review approval 后如 implementation final closeout，运行：

- `git diff --check`
- required file presence check for package mirrors。
- status consistency grep across package README、milestone index、plan docs 和 release
  docs。
- release-status wording check，证明只有在 approval recorded 时才出现 final status。
- blocker wording check，证明 final status 前没有 unresolved P1/P2 findings，或它们已明确
  resolved。
- 对 touched closeout docs 做 concrete demo anchor sweep。
- changed-file scope guard，证明只修改 approved documentation paths。

## Not Planned

- backend tests。
- frontend tests。
- API smoke。
- E2E tests。
- Agent smoke or autonomous tests。
- runtime behavior tests。
- schema execution tests。
- fixture or migration tests。

这些检查不计划运行，因为 0.2.12 是 documentation-only。如果任何 implementation file
发生变化，本 test plan 失效，package 必须停止并重新 review。

## Pass Criteria

- Documentation checks 成功退出，或 expected no-match checks 在 `review.md` 中解释。
- Status wording 在 English 和 Chinese mirrors 中同步。
- Final closeout 继续由 approval gate。
- 没有修改 runtime、schema、API、frontend、fixture、migration 或 test implementation files。
