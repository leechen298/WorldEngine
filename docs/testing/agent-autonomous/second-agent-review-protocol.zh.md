# 第二 Agent Evidence Review Protocol

状态：planned review protocol

## 目的

第二 Agent review 是只读 evidence review，用于防止第一 operating Agent 在产出 artifacts 后
自我声明 PASS。

## Inputs

- result directory path。
- scenario contract。
- scorecard contract。
- artifact contract。
- checker output。
- operation logs。
- API summaries。
- evidence bundle。

## 禁止行为

第二 Agent 不得：

- 修改 result artifacts。
- 重新运行 product flows 并覆盖 evidence。
- 修代码。
- 只凭 UI screenshots 推断 PASS。
- 检查 private provider keys 或 private WorldEngine internals。
- 使用 hidden reset APIs、database internals、private oracles 或 external world seed data。

## Review Checklist

第二 Agent 必须检查：

- required artifacts 存在。
- scenario name 与 result 匹配。
- checker 或 scorecard output 存在。
- 每个 critical score item 都有 supported PASS source。
- operation-log 中没有 direct API call 伪装成 Agent UI/CLI operation。
- API evidence 位于 API summary/log artifacts。
- redaction scan clean。
- 没有 raw prompt、raw response、API key、private Agent memory、raw thought、hidden
  context 或 oracle data。
- 没有 unsupported PASS claims。
- failures 已按 scenario taxonomy 分类。

## Output

写入或报告：

```text
second-agent-review.md
```

最低 sections：

- Scope。
- Inputs reviewed。
- Artifact completeness。
- Checker/scorecard review。
- Operation boundary review。
- Redaction review。
- PASS overclaim review。
- Findings table。
- Final review verdict。

任何 P1 或 P2 finding 都会阻断 full lifecycle PASS。
