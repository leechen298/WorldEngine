# Test Plan

英文版本：`test-plan.md`

## 验证范围

本包是 documentation-only。验证重点是 document presence、status consistency、
release wording、mirror synchronization、scope guardrails 和 evidence traceability。

除非 implementation files 被修改，否则不需要 backend、frontend、API smoke、E2E、
Agent smoke、runtime、schema、fixture 或 migration tests。如果这些文件发生变化，
应停止并视为 contract violation。

## 必需检查

### Documentation Sanity

```bash
git diff --check
```

预期结果：exit `0`。

### Required File Presence

```bash
test -f docs/iterations/v0.2/v0.2-release-candidate-bundle.md
test -f docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md
test -f docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md
```

预期结果：implementation 后所有命令 exit `0`。

### Package Mirror Presence

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/$f.md" &&
  test -f "docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/$f.zh.md" ||
  exit 1
done
```

预期结果：exit `0`。

### Status Consistency

```bash
rg -n '0\.2\.11-v0\.2-release-candidate-bundle|Status: ready for review|状态：`ready for review`|Status: review complete|状态：`review complete`' \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/README.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/README.zh.md
```

预期结果：exit `0`；status 与实际 stage 一致。

### Release-Status Wording Check

```bash
rg -n 'final release|not released|release candidate|release-candidate|0\.2\.12|final closeout' \
  docs/releases/v0.2.md \
  docs/releases/v0.2.zh.md \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.md \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md
```

预期结果：exit `0`；wording 确认 candidate status，且不声明 final release。

### Evidence Traceability Check

```bash
rg -n '0\.2\.[1-9]|0\.2\.10|evidence-index|boundary-audit|compatibility-review|findings|review\.md|implemented|documented|tested|reviewed|planned|not implemented|historical artifact|finding' \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md
```

预期结果：exit `0`；release-candidate claims 引用 evidence 和 status classes。

### Concrete Demo Anchor Sweep

使用 temporary untracked pattern file，并且只在 `review.md` 中记录 abstract result
categories。不要提交 concrete pattern list。

预期结果：没有 active-direction matches。所有 residual matches 必须在 final closeout
前归类为 historical package evidence、review-only text 或 false positive。

### Changed-File Scope Guard

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/(releases/v0\.2|iterations/v0\.2/)'
```

预期结果：exit `1` 且无输出，表示 changed files 限于 approved documentation paths。

## 不计划运行的测试

- 不计划 backend tests，因为本包不得修改 backend implementation files。
- 不计划 frontend tests，因为本包不得修改 frontend implementation files。
- 不计划 API smoke、E2E、Agent smoke、runtime、schema、fixture 和 migration
  tests，因为本包是 documentation-only。

## 失败处理

- 如果 runtime、schema、API、frontend、fixture、migration 或 test file 发生变化，
  停止，并且只在用户批准后 revert 本包的 out-of-scope edits。
- 如果出现 P1/P2 evidence gap，记录到 `findings.md`，并保持 v0.2 final closeout
  blocked。
- 如果 release wording 暗示 final status，在 review 前修正 wording。
