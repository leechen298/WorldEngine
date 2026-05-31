# Intent

Status: review complete

## Why This Exists

Relationship state, self-summary, reflection records, and personality drift
signals are pseudo-self continuity concepts. They are also easy to overbuild:
they can imply agent identity changes, hidden action modifiers, summarization
pipelines, or world-specific personality rules.

`0.5.4` turns those concepts into stricter contracts and keeps implementation
closed for this child package.

## Outcomes

- clarify each concept's evidence, provenance, and inspectability rules.
- preserve v0.4/v0.5 loop compatibility.
- state that no schema-only implementation is authorized in `0.5.4`.
- define what a later package must prove before adding schemas or behavior.

## Non-Goals

- no backend code, schemas, tests, APIs, migrations, persistence, or frontend
  changes.
- no action modifiers, automatic reflection, self-summary generation, or
  relationship behavior.
- no concrete world content, validation oracle details, or application-specific
  backend logic.
- no `backend/worldengine/` changes.

## Handoff

The next package, `0.5.5-v0.5-evidence-and-compatibility-audit`, receives a
complete v0.5 evidence surface: implemented working/episodic memory substrate,
read-only loop memory context, and deferred continuity contracts for the
higher-risk concepts.
