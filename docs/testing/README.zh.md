# Testing and Evidence

Status: testing evidence guide

英文版本：`README.md`。

本目录记录 WorldEngine iterations 的 testing standards 和 evidence。

## Evidence Rules

- 没有在当前 work session 运行命令时，不要声称 tests passed。
- Code packages 必须在 package `review.md` 中列出 exact commands 和 results。
- Runtime、UI、E2E 或 live smoke claims 必须包含可 review 的 evidence。
- Docs-only packages 可以跳过 code tests，但必须在 `review.md` 说明 no-test rationale。

## Result Files

使用 `docs/testing/results/` 存放 durable evidence summaries，适用于 package 运行 broader
verification 或 manual/runtime checks 的场景。

建议命名格式：

```text
YYYY-MM-DD-<version-package>-<slug>.md
```

每个 result file 应包含：

- command 或 workflow。
- environment assumptions。
- output summary。
- failures 或 skipped checks。
- 回链到 iteration package。
