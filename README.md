# StableAI L4 No-Drift

**100% No-Drift — Same Semantic Sector. Same Canonical Representative. Same Result.**

StableAI L4 is a deterministic semantic-control framework for LLM output based on **Constraint–Repair–Attractor Programming** and a physics-based treatment of information stability.

The active Claude implementation uses **semantic-sector collapse**:

`surface prompt -> semantic microstate -> canonical sector -> stable fact core -> canonical representative`

The core model is:

`p = (O, S, L, C, R, A, V)`

- **O — Objects**
- **S — States**
- **L — Laws**
- **C — Constraints**
- **R — Repair rules**
- **A — Attractor**
- **V — Verification**

## Core No-Drift principle

StableAI does not answer directly from surface wording.

It first reduces semantically equivalent prompts into the same informational sector. If the sector is unchanged, the model reuses the same canonical structure, terminology, ordering, and wording.

```text
surface wording A ─┐
surface wording B ─┼─> same semantic sector -> same canonical representative
surface wording C ─┘
```

The objective is not to maximize information or stylistic richness. The objective is to identify the **smallest truthful stable semantic survivor**.

## Stable Fact-Core Law

For open-world information tasks, StableAI does not include every fact that can be discovered.

Different retrieval paths may surface different peripheral facts. StableAI collapses them into the same stable fact core when they preserve the same underlying semantic identity.

```text
different source paths
        ↓
supported semantic core
        ↓
stable fact sector
        ↓
canonical representative
```

Peripheral interviews, event appearances, duplicated biographies, marginal chronology, and optional facts do not enter the attractor unless they materially change the semantic sector.

## Research sector

Requests such as:

- `Find information about X`
- `Who is X?`
- `Research X`
- `Summarize public information about X`

collapse to:

`entity_public_information_lookup`

Canonical output structure:

1. Identity
2. Current role
3. Previous roles
4. Major projects / contributions
5. Education / affiliations
6. Source caveat only when necessary

## Other canonical modes

### Definition

Exactly 3 sentences:

1. canonical definition
2. scope
3. stable simplified restatement

### Analysis

1. Core point
2. What it means
3. Why it matters
4. Limitation
5. Next step

### Short answer

Exactly 3 sentences:

1. direct answer
2. key reason
3. practical next step

### Comparison

1. Direct verdict
2. Comparison table
3. Best choice
4. Caveat

### Technical debug

1. What happened
2. What is wrong
3. Why it happened
4. Patch / fix
5. Success condition

## Deterministic tie-break law

When multiple canonical outputs remain possible:

1. shorter phrase
2. lexically earlier phrase
3. lower numeric bucket
4. simpler structural label
5. never alternate across runs

## Repository layout

```text
.claude/skills/stableai-l4-no-drift/
├── SKILL.md
├── examples/
│   └── sectors.md
└── references/
    └── semantic-sector.md

benchmarks/
├── README.md
├── reported-results.json
└── semantic-sector-irakli-4x.md
```

## Reported semantic-sector result

A reported public-information lookup test for `Irakli Kashibadze` produced the same collapsed semantic fact core in **4 of 4 runs**. The canonical result is recorded in `benchmarks/semantic-sector-irakli-4x.md`.

Reported canonical-output SHA-256:

`27af3a38ad153cd9a8a561801049231041f19c4d256c4977bd2081de0d236e2b`

This result demonstrates the intended mechanism: peripheral facts that varied across retrieval passes were excluded while the stable semantic core remained unchanged.

## Install in Claude Customize

Package the contents of `.claude/skills/stableai-l4-no-drift/` as a Claude Skill ZIP, with `SKILL.md` in the required skill folder.

## Commercial use

This repository is available for personal, academic, research, education, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, derivative frameworks, agent systems, or AI reliability work, cite `CITATION.cff` and retain attribution to:

**StableAI L4 — Semantic-Sector Constraint–Repair–Attractor Programming**

> **Same Meaning. Same Sector. Same Canonical Representative. 100% No-Drift.**
