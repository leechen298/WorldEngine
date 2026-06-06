# Intent

Chinese mirror: `intent.zh.md`.

## Why This Package Exists

v0.9 needs users to steer a running world without turning user text into direct
state mutation. The existing public director guidance endpoint proves a basic
redacted handoff surface, but it accepts guidance as a simple public event. It
does not yet define a structured boundary between allowed world-level pressure
and forbidden direct final outcomes.

`0.9.6` creates that boundary before `0.9.7` rule-linked evolution and event
legality. Direction must become queued guidance that later rule/evolution
packages may adjudicate. It must not itself decide illegal events or force
Agent outcomes.

## User Value

Users can say what kind of pressure, risk, trend, constraint, or environmental
direction they want the world to consider while WorldEngine preserves rule-led
causality and Agent autonomy boundaries.

## Engineering Value

The package gives later packages a public, structured direction artifact:

- what was accepted as world-level guidance.
- what was rejected as direct mutation.
- when guidance becomes eligible for consideration.
- what public rule references or future adjudication hooks may consume it.
- what redaction status protects evidence from private internals.

## In Scope

- Define and implement public direction intake semantics.
- Distinguish allowed environmental or event-bias guidance from forbidden final
  outcomes.
- Queue accepted guidance for bounded future consideration.
- Preserve the existing public director guidance endpoint compatibility.
- Add focused tests and review evidence.

## Out Of Scope

- Live provider interpretation of natural language.
- Generated result directories.
- Checker execution or external validation.
- Rule-linked event legality or final event adjudication.
- Agent private memory, goal, personality, relationship, inventory, or life
  state mutation.
- Frontend UI and Validation Client changes.
- Durable scheduling or background processing.
- `backend/worldengine/` changes.

## Handoff

The handoff to `0.9.7` is a public queue and summary contract for external
world guidance. `0.9.7` may later consume this contract to evaluate whether
events and parameter changes are legal under world rules.
