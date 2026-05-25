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

## Projection Consumer

Projection consumer 是面向用户或外部系统的 consumer，通过 public contracts 读取 WorldEngine
state、events 和 projections。它不拥有 core engine logic。

## External Validation World

External validation world 是外部 validation suite 或 product consumer 使用的 out-of-repository
world。它可以通过 public contracts 验证 engine capability，但它的 seed data 和内部 validation
details 不属于 core repository。

## Legacy Path

`backend/worldengine/` 是 legacy path。Active backend path 是 `backend/app/`。
