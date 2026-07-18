# Intent

Chinese mirror: `intent.zh.md`.

Status: documentation drafted / review pending

## Problem / Purpose

v0.11 needs user guidance, but direct natural-language commands cannot become
world facts. A command like "kill this Agent now" must be rejected. A softer
statement like "this Agent may face lightning-strike risk" may be accepted only
as public external pressure that future rule-bound event generation must still
evaluate through rules, state, probability, location, time, and legality.

## Why Now

`0.11.1` labeled provider/worldview readiness and `0.11.2` attached public
rules to sessions. Before `0.11.4` can generate legal events and diffs, the
engine needs a session-scoped place to store user direction as bounded public
guidance.

## Relationship To Roadmap

This package advances the v0.11 "MVP Rule-Bound World Evolution" milestone. It
does not implement Agent pseudo-self, long-term memory, autonomous validation,
or full MVP closeout. It prepares the direction input that later rule-bound
event generation can consume.

## Non-Goals

- no direct fact mutation from user guidance.
- no event generation, event application, or state diff application.
- no Agent private memory, goal, personality, relationship, injury, death, or
  inventory mutation.
- no Validation Client code or external validation execution.
- no provider calls.
- no persistence or migrations.
- no `backend/worldengine/` work.

## Expected Handoff

`0.11.4-rule-compliant-event-generation-and-diffs` receives a public
session-scoped direction queue with accepted/rejected evidence. Later event
generation may reference queued direction ids, but it must still prove legality
through public rules and current state.
