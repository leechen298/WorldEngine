# Intent

Chinese mirror: `intent.zh.md`.

`0.12.1` made the Agent visible inside a session. `0.12.2` gives that Agent a
minimal public memory trail.

The intent is not to simulate a private mind. The MVP needs durable-looking,
redaction-safe public summaries that let validators see:

- what the Agent publicly observed.
- what short-term public memory was recorded.
- when rest consolidated observations into an episodic public summary.
- which event/runtime refs support that summary.

This package deliberately avoids personality and skill mutation, raw private
memory, diagnostic conversation memory, and final validation automation.
