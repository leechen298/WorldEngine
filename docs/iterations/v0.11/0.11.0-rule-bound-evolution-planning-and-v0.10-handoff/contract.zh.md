# Contract

英文版本：`contract.md`。

## Public Concepts

- `v0.10 handoff`：已评审的 runnable-session MVP slice 以 PASS 关闭。
- `v0.11 input`：v0.11 在子包授权后可使用的 manifest、session、runtime、snapshot 和
  dashboard public evidence。
- `handoff caveat`：已知 unsupported 或 unproven area，必须保持可见，不得转换成 PASS claim。

## Allowed Changes

- 创建并评审本 package document set。
- 评审后更新 v0.11 parent docs，把 `0.11.1` 选为 next route。
- 记录当前 session 的 documentation checks 和 no-code-test rationale。

## Forbidden Changes

- 不修改 runtime、API、schema、frontend、checker、fixture、provider、generated result、
  Validation Client、migration、persistence 或 `backend/worldengine/` implementation。
- 不执行 live provider。
- 不执行 external Validation Client。
- 不声明 v0.10 已证明 Agent autonomy、durable persistence 或 product readiness。
- 相关 child package review 记录 authorization 前，不做 v0.11 implementation。

## Compatibility Requirements

- v0.10 closeout 的 PASS 只限 reviewed runnable-session MVP slice。
- provider credentials 未配置时，继续把 `manifest_status blocked` 保留为
  provider-readiness caveat。
- Validation Client 保持 external，只消费 evidence。
- 用户/玩家保持在世界外部。

## Out-of-Scope Follow-Ups

- Provider/worldview preflight implementation 属于 `0.11.1`。
- Structured rules and parameters 属于 `0.11.2`。
- Direction queue/boundary 属于 `0.11.3`。
- Rule-compliant events/diffs 属于 `0.11.4`。
- Fidelity validation 属于 `0.11.5`。
- Agent continuity 和 external automation 属于 v0.12。
