# Technical Design

## 文档结构

本包创建一个 documentation-only child package：

```text
docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline/
  README.md
  README.zh.md
  intent.md
  intent.zh.md
  contract.md
  contract.zh.md
  technical-design.md
  technical-design.zh.md
  test-plan.md
  test-plan.zh.md
  plan.md
  plan.zh.md
  review.md
  review.zh.md
```

该子包记录 v0.9 的第一次 route transition。父级 v0.9 surfaces 可以同步，使下一条
route 指向
`0.9.1-provider-live-smoke-and-redaction-boundary-documentation-package-needed`。

## 受影响文件

允许文件：

- `docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline/**`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.9/README.zh.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/v0.9-plan.zh.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/CURRENT_STATE.zh.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.9/review.md`
- `docs/iterations/v0.9/review.zh.md`

禁止文件包括所有 runtime、schema、API、frontend、backend test、checker、
fixture、migration、generated result、external repository、Validation Client、
provider configuration 和 `backend/worldengine/` implementation 文件。

## Route State Flow

本包之前：

```text
Active child package: none
Current route: 0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed
Implementation authorization: no
Evidence execution authorization: no
Provider live-call authorization: no
```

本包之后：

```text
Active child package: 0.9.1-provider-live-smoke-and-redaction-boundary selected / documentation package needed
Current route: 0.9.1-provider-live-smoke-and-redaction-boundary-documentation-package-needed
Implementation authorization: no
Evidence execution authorization: no
Provider live-call authorization: no
```

该 route transition 不创建 `0.9.1` package documents，也不授权 provider work。它只选择
下一个 documentation package target。

## 兼容性策略

- 保持所有变更 documentation-only。
- 保持 v0.8 basic lifecycle PASS 为 handoff context，而不是 v0.9 PASS。
- 保持 LLM-backed lifecycle validation 为 `BLOCKED`，直到未来包记录当前会话的
  checker 或 scorecard evidence。
- 保持 provider live-call authorization 关闭，直到 `0.9.1` package review 明确打开。
- 保持英文和中文 status semantics 一致。

## Anti-Drift Rules

- `v0.9-plan.md` 中的 planned package specs 仍只是 route-map inputs。
- 下一个 child package 必须在 implementation 前创建自己的完整 document set。
- 不把 LLM-backed testing documentation 转成 PASS evidence。
- 不把 external diagnostic dialogue 重新解释为 in-world dialogue 或 Agent memory。
- 不把 narrative projection 重新解释为 canonical world mutation。
- 不为方便而削弱 provider redaction rules。
- 不向 core repository 添加 concrete world content。
