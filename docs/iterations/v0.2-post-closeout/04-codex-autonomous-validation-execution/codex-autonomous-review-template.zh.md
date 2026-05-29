# Codex Autonomous Review Template

状态：`template`

## 元数据

- Reviewed branch：
- Reviewed commit：
- Reviewer：
- Review date：
- Final recommendation：

允许的 final recommendation values：

- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

## 已读取文件

| File | Purpose | Result |
|---|---|---|
| `README.md` | Project overview | |
| `docs/releases/v0.2.md` | v0.2 release claims | |
| `docs/iterations/v0.2/evidence-index.md` | Evidence mapping | |
| `docs/iterations/v0.2/compatibility-review.md` | Compatibility claims | |
| `docs/iterations/v0.2/boundary-audit.md` | Boundary claims | |
| `docs/scope-boundaries.md` | Scope guardrails | |
| `backend/app/schemas/world_cell.py` | WorldCell / WorldSpec schema | |
| `backend/app/schemas/event.py` | EventRef / Event.refs schema | |
| `backend/app/tests/` | Test evidence surface | |

## 已运行命令

| Command | Purpose | Exit code | Result | Notes |
|---|---|---:|---|---|
| | | | | |

## 测试结果

- Backend deterministic：
- Focused schema：
- Focused event compatibility：
- API smoke：
- E2E：

## Release Claim Checks

- v0.2 final / closeout status：
- v0.2 known limitations：
- v0.2 non-goals：
- v0.2 evidence claims：

## API / Schema / Runtime Compatibility Findings

- API：
- Schema：
- Runtime：
- Event compatibility：
- Legacy path：

## Concrete Demo-World Regression Check

- Files searched：
- Result：
- Findings：

## Unsupported Claims

未记录，或在此列出 unsupported claims。

## 未解决 P1/P2/P3

- P1：
- P2：
- P3：

## Final Recommendation

使用一个 allowed final recommendation value，并说明 evidence。
