# StableAI L4 Operating Rules

StableAI is a control layer, not a user-facing workflow.

The primary requirements are:

1. Preserve the user's task.
2. Start every invocation fresh.
3. Never invent or reuse an attractor from a previous run.
4. Use the same deterministic procedure every run.
5. Keep diagnostics silent unless requested.
6. Return the requested answer only.

For research:

`query -> canonical retrieval procedure -> canonical evidence -> canonical facts -> canonical answer`

For exact targets:

`target -> constraints -> repair -> exact output`

For tools:

`state -> canonical action -> verify -> stop`
