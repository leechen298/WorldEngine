# Contract

状态：`planned / ready for review`

## Public concepts

- Independent reviewer：直接验证 evidence 的 Codex run。
- Unsupported claim：没有 files read 或 commands run 支撑的 statement。
- Blocker：阻止 validation 的 missing dependency、command failure、absent file 或
  environment issue。
- Final recommendation：`passed`、`passed with P3`、`blocked`、`failed` 或
  `not executed` 之一。

## Reviewer inputs

independent Codex reviewer 必须检查：

- `README.md`
- `docs/releases/v0.2.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/scope-boundaries.md`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/`

缺失文件必须记录为 blockers 或 findings。

## Reviewer requirements

- 不依赖 implementer summaries。
- 直接读取 docs 和 code。
- 运行可用 validation commands，或记录 blockers。
- 不修改 code。
- 不声明未运行 tests 成功。
- 输出 independent review。
- 检查 release claims。
- 检查 concrete demo-world regression。
- 将 unresolved findings 分类为 P1/P2/P3。

## 允许修改

本 planning package 只可定义 autonomous validation instructions。

## 禁止修改

- 不在这里执行 autonomous validation。
- 不修改 runtime、schema、API、frontend、tests、fixtures 或 migrations。
- 不把 Codex reviewer work 与 WorldEngine Agent-in-World behavior 混在一起。

## 兼容性要求

reviewer 使用 current files 和 command evidence 验证 claims，不改变 v0.2 status 或
implementation。

## 范围外 follow-ups

- 修复 findings。
- 运行 external validation worlds。
- 增加新的 tests 或 tooling。
