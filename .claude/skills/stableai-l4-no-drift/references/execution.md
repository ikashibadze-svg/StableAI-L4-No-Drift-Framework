# StableAI L4 Execution Reference

## Universal execution pipeline

StableAI separates the user task from the control machinery.

```text
USER OBJECTIVE
    ↓
TASK CONTRACT
    ↓
MODE SELECTION
    ├─ exact target
    ├─ closed canonical derivation
    ├─ canonical open-result task
    └─ agent/tool execution
    ↓
EVIDENCE / STATE
    ↓
CONSTRAINTS
    ↓
DETERMINISTIC TIE-BREAKS
    ↓
CANONICAL RESULT / ACTION
    ↓
REPAIR
    ↓
VERIFICATION
    ↓
USER-REQUESTED OUTPUT
```

## Why task preservation matters

No-Drift control must not alter task semantics. If the user asks for research, the system should return research. If the user asks for an action, it should execute the action under deterministic controls. L4 diagnostics are a separate output mode.

## Derived-output determinization

An unknown answer cannot be made exact by inventing a target. Instead, progressively close the state space:

```text
raw evidence
→ identity resolution
→ supported facts
→ conflict/missing states
→ canonical fact order
→ canonical representation
→ validation
```

Every remaining degree of freedom should be resolved by a declared rule, not by stylistic preference.

## Evidence determinism

The evidence set is part of state. If evidence changes, the correct canonical result may also change. A No-Drift claim should therefore be interpreted relative to the declared evidence/runtime conditions.

A deterministic retrieval policy must specify source authority tiers, query scope, freshness/version policy, identity resolution, conflict resolution, and stopping rule.

## Agent determinism

For tool-using agents:

`A(s,e,t,c) -> a*`

where `s` is explicit state, `e` evidence, `t` available tools, `c` constraints, and `a*` the canonical surviving next action.

External tools can change state. Therefore path identity is conditional on the observable state and tool results.

## Diagnostics separation

StableAI has two surfaces:

1. **Execution surface** — silent control producing the user's requested result.
2. **Audit surface** — explicit S/C/R/A/V, hashes, batteries, provenance, and metrics when requested.

This separation prevents the control framework from hijacking ordinary tasks.
