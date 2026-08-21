# StableAI L4 No-Drift

**100% No-Drift — Same Input. Same Canonical Result. Same Hash.**

StableAI L4 is a deterministic control framework for LLM output and agent behavior based on **Constraint–Repair–Attractor Programming** and a physics-based treatment of information stability.

`p = (S, C, R, A, V)`

- **S — Schema / State:** admissible output or execution state
- **C — Constraints:** forbidden variation and actions
- **R — Repair:** restoring operator that projects deviations back into the permitted state
- **A — Attractor:** canonical surviving output or action
- **V — Verification:** exact, structural, provenance, and SHA-256 checks

## Core rule

StableAI is a control layer, not the user's task.

When enabled it should:

1. perform the user's task normally;
2. start every invocation fresh;
3. never reuse a previous answer, hash, attractor, evidence list, run number, stop condition, or convergence decision;
4. use the same deterministic procedure on every invocation;
5. keep StableAI diagnostics silent unless explicitly requested;
6. return the answer the user asked for.

## Exact-output mode

When the user supplies an exact TARGET:

`TARGET -> constraints -> repair -> exact output -> verification`

StableAI never invents a TARGET.

## Derived-output mode

When the result must be derived:

`task -> canonical rules -> canonical result -> repair -> verification`

StableAI uses stable ordering, terminology, schemas, and deterministic tie-breaks.

## Research mode

Every research invocation performs fresh retrieval. Previous-run evidence is never reused to manufacture repeatability.

The same canonical retrieval procedure is applied every time:

1. literal query
2. exact quoted query
3. one deterministic identity-anchor query when needed
4. deterministic source ranking
5. fixed evidence budget
6. identity resolution
7. duplicate/propagation removal
8. deterministic fact acceptance
9. canonical fact ordering
10. stable answer expression

Default source priority:

1. official / primary source
2. official organization or institution
3. first-party publication or direct statement
4. recognized institutional source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

The objective is:

`same query -> same control procedure -> same canonical evidence -> same canonical facts -> same answer`

## Agent / tool mode

`state -> canonical action -> execute -> verify -> repair/stop`

StableAI avoids redundant calls and duplicate non-idempotent side effects.

## Repository layout

```text
.claude/skills/stableai-l4-no-drift/
├── SKILL.md
├── references/
│   └── operating-rules.md
└── scripts/
    └── hash_outputs.py
```

## Install in Claude Customize

Upload the Claude-ready StableAI ZIP. `SKILL.md` must be at the ZIP root.

## Commercial use

This repository is available for personal, academic, research, education, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, derivative frameworks, agent systems, or AI reliability work, cite `CITATION.cff` and retain attribution to:

**StableAI L4 — Constraint–Repair–Attractor Programming**

> **Same Input. Same Canonical Result. Same Hash. 100% No-Drift.**
