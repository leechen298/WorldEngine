# Intent

Chinese mirror: `intent.zh.md`.

## Problem

v0.9 has public generated rule/parameter schemas, bounded runtime controls, and
bounded natural-language world direction. It still lacks the bridge that proves
an event or parameter change is legal under public rules and current state.

Without that bridge, an LLM-backed lifecycle could still look like arbitrary
story fact insertion. A validator needs public evidence that an event was
selected because it matched rules, constraints, probability, causality,
location, time, and redacted direction pressure.

## Product Intent

This package establishes the first deterministic public rule-linked evolution
boundary. It lets WorldEngine inspect an event candidate, evaluate it against a
public generated rule/parameter set and a public state snapshot, and either:

- accept it as a legal world-evolution event with public state-diff evidence;
  or
- reject it with public diagnostics and no canonical state mutation.

The package is not a story engine, checker, provider-backed adjudicator, or
Agent autonomy system. It is a generic engine boundary for rule-linked event
legality.

## User Value

- Users can guide the world without forcing final facts.
- Validators can see why an event was legal or illegal.
- Later Agent continuity work can rely on an event stream whose world events
  are not arbitrary hidden mutations.
- Future LLM-backed checker support can consume public legality evidence
  without needing private prompts or provider traces.

## North Star Alignment

WorldEngine's north star requires worlds to run over time with events, rules,
timelines, resources, history, snapshots, and recovery. This package advances
that spine by making event legality inspectable before later Agent continuity
and checker packages depend on it.

## Non-Goals

- No live provider interpretation.
- No generated world or generated rule creation.
- No checker execution or fixture changes.
- No external validation.
- No frontend or Validation Client changes.
- No Agent private memory, goal, personality, skill, relationship, inventory,
  life/death, or location mutation beyond public state diffs explicitly
  covered by public world rules.
- No narrative projection or diagnostic dialogue.
- No durable scheduler or background evolution loop.
- No `backend/worldengine/` work.
