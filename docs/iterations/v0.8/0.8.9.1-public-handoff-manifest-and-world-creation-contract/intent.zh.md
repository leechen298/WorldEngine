# Intent

英文源文件：`intent.md`。

## 为什么存在

0.8.9 父包识别了一个具体 handoff blocker：外部 Validation Client 可以访问 WorldEngine `/health` 和 `/openapi.json`，但无法发现 public world creation contract，也无法读取 public handoff manifest。

父包刻意保持 documentation-only。本子包把父包 handoff plan 转成可 review 的 bounded implementation package。

## 问题

如果没有本实现包：

- 简短的 `/goal implement 0.8.9` 请求会和父包 `implementation_authorized: no` 门禁冲突。
- agent 可能在没有 reviewed implementation contract 的情况下添加 runtime/API/schema 变更。
- Validation Client compatibility 可能被错误地通过修改外部 client 修复，而不是暴露 WorldEngine 自己拥有的 public contract。
- public output 可能意外包含 provider、prompt、evaluator 或 Agent private state 细节。

## 期望结果

review 并显式授权实现后，本包只添加 Validation Client handoff 所需的 WorldEngine public contract surface。Closeout 最多只能结论为 `WORLDENGINE_CONTRACT_READY`，不能声明 external validation PASS 或 human validation PASS。
