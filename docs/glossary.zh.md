# Glossary

Status: working glossary

英文版本：`glossary.md`。

## World

一个随时间运行的 stateful system。World 包含 state、events、rules、entities、agents、resources、
history 和 projection surfaces。

## Recursive World

可以包含 child worlds、subjective worlds 或 specialized world cells 的 world。Recursive worlds
让 WorldEngine 表达 locations、inner models、dreams、memory spaces 和 nested runtime contexts。

## WorldCell

WorldCell 是 planned minimal recursive world unit。v0.2 会定义它的 schema/spec foundation，但不会让
RuntimeEngine 直接执行 WorldCell。

## WorldSpec

WorldSpec 是 generated 或 loadable world 的 structured representation。它必须可 validation、saving、
runtime loading 和 replay。

## Event

Event 是 runtime record。World、Agent、memory 和 external projections 都应该通过 Event contracts
收敛。

## Agent

Agent 是生活在 world 中的 actor。长期目标是让 Agent 拥有 identity、memory、goals、needs、
relationships、actions、feedback 和 self-narrative。

## Pseudo-self

Pseudo-self 是 Agent 长期 continuity 的 engineered behavior model。它不是 real consciousness claim。

## Surface

Surface 是面向用户或外部系统的 projection，例如 dashboard、game client、API 或 integration。

## Reference World

Reference world 是用于 validation、testing 和 product demonstration 的标准 world。第一款
village-like game surface 会建立在 reference village world 上。

## Tiny Village

Tiny Village 是 future reference fixture / reference world。它不能把 WorldEngine 变成 village-specific
backend。

## Legacy Path

`backend/worldengine/` 是 legacy path。Active backend path 是 `backend/app/`。
