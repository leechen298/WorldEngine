# Contract

状态：package complete / passed current campaign

## Public concepts

- Independent review：由 separate Codex validation run 产生的 output。
- Review verification：检查 independent review 是否读取 required files、运行 commands
  或记录 blockers、检查 release claims，并分类 findings。
- Unsupported claim：没有 cited file reads 或 command evidence 支撑的 statement。

## 允许修改

执行期间更新：

- `codex-autonomous-review.md`
- `codex-autonomous-review.zh.md`
- `review.md`
- `review.zh.md`

同时更新 `GOAL_RUNNER.md` 要求的 package status 和父级路由文档，把 campaign 从 `04`
交接到 `05`。

只有 final bundle step 才更新更宽的 validation summaries。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend tests、fixtures 或 migrations。
- 不接受只复述 summaries 的 review。
- 不接受没有为 unrun commands 记录 blockers 的 review。
- 不接受 unsupported success claims。

## Review quality checks

execution review 必须检查 independent review 是否：

- 读取 necessary files。
- 运行 commands 或记录 blockers。
- 检查 release claims。
- 检查 concrete demo-world regression。
- 分类 P1/P2/P3。
- 列出 unsupported claims。

如果 independent review 只是复述 documentation、没有运行 tests、也没有记录 blockers，
则把结果分类为 `blocked`。

## 兼容性要求

autonomous execution package 只验证 evidence，不改变 v0.2 release status 或
implementation。

## 范围外 follow-ups

- 修复 findings。
- 重新运行 E2E / API smoke，除非它明确属于 independent review。
- 创建 external validation repositories。
