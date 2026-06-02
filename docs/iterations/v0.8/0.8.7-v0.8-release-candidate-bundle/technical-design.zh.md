# Technical Design

状态：documentation-stage design

## Artifact Shape

本 package 创建 documentation-only release-candidate bundle，包含：

- package governance docs：`README.md`、`intent.md`、`contract.md`、
  `technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`。
- 每个 governance doc 的中文 mirror。
- release-candidate artifact：`release-candidate-summary.md` 和
  `release-candidate-summary.zh.md`。

## Bundle Model

Release-candidate summary 以 bounded tables 组织：

1. Package matrix：reviewed package、evidence source、disposition 和 boundary。
2. Evidence references：path、existence expectation、supported claim 和 claim limit。
3. Compatibility summary：v0.3 through v0.7 surfaces 及其 reviewed evidence relationship。
4. Exclusions：v0.8 release-candidate packaging 不声明的 surfaces。
5. Findings：P1/P2/P3 status 和 handoff disposition。
6. Handoff decision：final closeout review 是否可以开始。

## Status Transitions

本 package 允许的 transition：

```text
0.8.7-documentation-package-needed
  -> documentation-review-needed
  -> review complete
  -> 0.8.8-documentation-package-needed
```

Initial package creation 只包含第一步 transition。后续 transition 必须有 `review.md`
中的 review evidence。

## Evidence Boundaries

Summary 必须这样处理 evidence：

- `0.8.3` backend/app changes 和 focused tests 只是 bounded core-readiness surface 的
  current-session implementation evidence。
- `0.8.5` smoke evidence 只是 current-session bounded core/backend evidence。
- v0.7 code-review 和 `0.7.9` repair evidence 只是 handoff evidence。
- `0.8.6` audit 只是 release-candidate packaging authorization evidence。
- Historical v0.1 through v0.7 testing docs 是 context，除非 reviewed v0.8 package
  以 boundary 显式引用。

## Redaction Design

本 package 只存 public repository paths 和 redacted evidence classifications。不得引入
private external validator commands、private repository paths、hidden scenario data、
UI selectors、oracle internals、raw prompts、provider traces、secrets 或 concrete
validation-world details。

## Implementation Impact

不允许产生 runtime、schema、API、frontend、backend test、checker、fixture、migration、
external repository、generated result、deployment 或 `backend/worldengine/` implementation
impact。
