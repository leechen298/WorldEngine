# Intent

## Problem / Purpose

v0.10 需要一个稳定单位，让 external clients 和 dashboard 后续可以 create、inspect、run
和 export。现有 world 和 runtime surfaces 有用，但还没有绑定成一个 session。

## Why Now

`0.10.1` 已让 session surfaces 可发现但不可用。下一步是在 worldview creation 和 bounded
runtime 接入之前，先让 session identity 和 status store 真实存在。

## Relationship To Roadmap

本包只实现 v0.10 计划中的 “World Session Contract And State Store” slice。
`0.10.3` 负责 worldview-to-runtime session creation；`0.10.4` 负责 bounded session
runtime 和 snapshot evidence。

## Non-Goals

- 不从 worldview input 生成 world content。
- 不通过 session 执行 runtime。
- 不做 dashboard UI。
- 不做 durable database。
- 不做 provider live calls 或 quality claims。
- 不做 Validation Client implementation 或 external validation PASS。

## Expected Handoff

closeout 后，`0.10.3` 可以基于这个 public session unit 创建 worldview sessions，而不再发明
另一套 identity/status contract。
