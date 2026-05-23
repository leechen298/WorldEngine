# Glossary

Status: shared vocabulary

## Agent

A world participant with identity, state, needs, goals, memory, relationships,
action intent, and feedback-shaped behavior.

## Agent-in-World Loop

The loop where an agent perceives world events, forms intent, acts, receives
world feedback, records memory, and changes future behavior.

## Event

A structured record of something that happened in a world. Events are the
spine for runtime history, memory, replay, evidence, and projection.

## Generation Metadata

Metadata that records how a world spec was created, including template,
prompt-derived direction, generator version, seed references, and validation
status.

## Projection

A consumer-facing view of the running world. Dashboards, games, APIs, and
external clients are projections, not owners of engine logic.

## Pseudo-self

An engineered model of sustained identity and behavior continuity. It can
include self-narrative, memory retrieval, relationship history, long-term
preferences, and personality drift. It is not a claim of real consciousness.

## Reference World

A standard world instance used to validate and demonstrate engine capability.
The first reference world may be a tiny village.

## Recursive World

A world structure where one world can contain child worlds or specialized
sub-worlds. Later milestones may model memory spaces or subjective agent
spaces as specialized recursive world cells.

## Surface

A user-facing or system-facing entry point that consumes WorldEngine state,
events, and projections. A game is a surface.

## WorldCell

The planned minimal recursive world unit. In v0.2 it is a schema/spec concept,
not a full runtime replacement.

## WorldSpec

The planned structured representation of a generated or loadable world. It
should be validatable, persistable, inspectable, and eventually runnable.
