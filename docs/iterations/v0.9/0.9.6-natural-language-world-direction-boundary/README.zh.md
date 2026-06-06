# 0.9.6 Natural Language World Direction Boundary

英文原文：`README.md`。

Status：implementation complete / focused verification passed / evaluator PASS
Type：mixed implementation package

## 目标

把用户 natural-language direction 转成 bounded world-level guidance。它可以影响
environment trends、external pressure、event candidate bias 和 future rule evaluation，
但不能直接 mutate Agent private state、Agent goals、inventory、relationships、
life/death state 或 final world facts。

## 范围

本包可在 `backend/app/` active backend path 中扩展：

- public world-direction request and response schemas。
- deterministic classification，用于区分 allowed world-level guidance 和 forbidden direct
  outcomes。
- bounded in-memory direction queue 或 summary，挂接到 active world API surface。
- public rejection reasons，覆盖 direct final facts、private Agent mutation、inventory
  injection、rule bypass 或 private-marker leakage。
- 对既有 `/worlds/{world_id}/director-guidance` public endpoint 的兼容行为。
- focused backend and API tests，覆盖 allowed guidance、rejected direct outcomes、delayed
  application windows、public summaries 和 redaction。

本包不得实现 event legality、rule-linked event generation、Agent continuity、private memory
mutation、live provider calls、generated result creation、checker execution、external
validation、frontend UI、durable scheduling 或 Validation Client changes。

## 交付物

- Public direction intake contract。
- Public direction classification 和 rejection taxonomy。
- 带 bounded timing fields 的 in-memory queued-guidance semantics。
- 不暴露 raw private internals 的 public direction summary evidence。
- Focused tests，证明 allowed guidance 会被 queued，forbidden direct outcomes 会被
  blocked，且不会 mutate Agent private state 或 final facts。

## 当前授权

Documentation/contract/design/test-plan review 已通过。Implementation 已完成本包记录的
scoped active-backend natural-language world direction boundary work。

Provider live calls、generated-result creation、checker execution、external validation、
Validation Client changes、frontend UI、event legality、Agent continuity、durable scheduling
和 `backend/worldengine/` changes 仍未授权。

## 最终评估状态

已完成 reviewed `0.9.6` scope。Focused、related public-surface 和 backend regression
verification 已通过，implementation-scope evaluator re-review 已通过，且无 P0/P1/P2/P3
findings。
