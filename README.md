# StableAI L4 No-Drift

**100% No-Drift LLM Output — Same Input. Same Canonical Output. Same Hash.**

StableAI L4 is a deterministic control framework for LLM output, retrieval, and agent behavior based on **Constraint–Repair–Attractor Programming** and a physics-based treatment of information stability.

`p = (S, C, R, A, V)`

- **S — State / Schema:** admissible task, evidence, output, and execution states
- **C — Constraints:** forbidden variation, unsupported facts, and forbidden actions
- **R — Repair:** restoring operator that projects deviations back into the permitted state
- **A — Attractor:** canonical surviving output, evidence state, or action
- **V — Verification:** exact, structural, provenance, evidence-manifest, and SHA-256 checks

## Core operating law

```text
same task + same evidence state + same declared conditions
                              ↓
                         StableAI L4
                              ↓
                   same canonical result
                              ↓
                        same hash
```

StableAI is a **control layer**, not a replacement for the user's task. It preserves the requested objective and normally runs silently.

## Physics-Based Foundation

StableAI maps a stability architecture from physical systems into AI control:

```text
physical system:
state space → constraints → perturbation → restoring dynamics → stable attractor

StableAI L4:
output/evidence/action space → constraints → drift → repair → canonical attractor
```

The evidence state is part of the state space. If evidence changes, the experimental state changed.

## L4 operating modes

### Exact attractor
When an exact TARGET already exists:

`INPUT + TARGET -> constrain -> repair -> TARGET -> SHA-256`

StableAI never invents a TARGET simply to force exact-attractor mode.

### Closed canonical derivation
When output is derived but can be closed with fixed schema, vocabularies, ordered rules, tie-breaks, missing/conflict states, and canonical serialization.

### Retrieval / open-result control
For research and live retrieval:

`task -> bounded discovery -> freeze evidence E -> supported facts -> canonical expression -> verify -> answer`

### Agent/tool execution

`state -> allowed actions -> filter -> rank -> deterministic tie-break -> act -> verify -> repair/stop`

## Retrieval Lock

Live web search is not treated as a stable hidden input.

StableAI defines a canonical evidence manifest:

`E = canonical evidence manifest`

and the answer attractor becomes:

`A = A(task, E, constraints)`

### Discovery

When no evidence state exists, StableAI performs one **bounded, non-adaptive discovery pass**, selects evidence by deterministic source rules, deduplicates copied evidence lineages, then freezes the manifest and computes:

`evidence_hash = SHA256(canonical_manifest)`

### Repeat

A repeat run for the same task reuses the same frozen evidence state.

It does **not**:

- issue new exploratory queries,
- change query wording,
- add or drop sources,
- search deeper,
- broaden scope,
- search repeatedly until "convergence."

Therefore:

```text
same task + same evidence_hash + same constraints
                       ↓
                 same answer
                       ↓
                 same hash
```

### Refresh

A request for fresh/latest/current information creates a new evidence version:

`E1 -> refresh -> E2`

A different answer caused by `E2` is **evidence evolution**, not stochastic output drift of `E1`.

StableAI diagnostics distinguish:

- `OUTPUT_DRIFT`
- `EVIDENCE_CHANGE`
- `FRESHNESS_REFRESH`
- `SCOPE_CHANGE`
- `TOOL_FAILURE`
- `TRANSPORT_FAILURE`

## Source determinization

Default authority order:

1. authoritative system of record / primary source
2. official organization / issuer
3. first-party publication or direct statement
4. recognized institutional / technical source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

Within a tier StableAI uses directness, date/version relevance, completeness, then canonical URL lexical order.

Multiple domains carrying the same propagated biography/text count as one evidence lineage rather than independent corroboration.

## Universal invariants

- Preserve the user's objective.
- Never invent a target or fact.
- Open-world research must have an explicit evidence state.
- Repeat research runs reuse the same evidence manifest.
- Fresh retrieval creates a new evidence version.
- Resolve identity before merging evidence.
- Represent conflicts and missing values explicitly.
- Deduplicate propagated/copied evidence.
- Use deterministic evidence rules and tie-breaks.
- Repair only when the correct repair is uniquely determined.
- Avoid redundant tool calls and duplicate side effects.
- Keep diagnostics silent unless requested.
- Stop immediately after verified success.

## Repository layout

```text
.claude/skills/stableai-l4-no-drift/
├── SKILL.md
├── assets/
│   └── l4-prompt-template.txt
├── references/
│   ├── levels.md
│   ├── theory.md
│   ├── execution.md
│   └── retrieval-lock.md
└── scripts/
    ├── freeze_manifest.py
    ├── hash_outputs.py
    ├── run_battery.sh
    └── verify_nodrift.py

benchmarks/
├── README.md
└── reported-results.json

tools/
└── build_claude_skill_zip.sh
```

## Install in Claude Code

Project-scoped:

```bash
mkdir -p .claude/skills
cp -R path/to/stableai-l4-no-drift .claude/skills/stableai-l4-no-drift
```

User-scoped:

```bash
mkdir -p ~/.claude/skills
cp -R path/to/stableai-l4-no-drift ~/.claude/skills/stableai-l4-no-drift
```

## Install in Claude Customize

Claude Customize requires `SKILL.md` at the top level of the uploaded ZIP.

Build from source:

```bash
bash tools/build_claude_skill_zip.sh
```

The resulting ZIP contains:

```text
SKILL.md
assets/
references/
scripts/
```

Do **not** upload the entire GitHub repository ZIP to Claude Customize.

## Exact No-Drift verification battery

Anthropic API:

```bash
export ANTHROPIC_API_KEY=...
python .claude/skills/stableai-l4-no-drift/scripts/verify_nodrift.py \
  --prompt-file example_l4_prompt.txt \
  --target-file example_target.json \
  --runs 20 \
  --model <model-id>
```

For exact-target N-run certification:

```text
attempted_runs = N
completed_runs = N
transport_errors = 0
raw_exact_match_rate = 1.0
unique_outputs = 1
unique_hashes = 1
all_hashes_identical = true
```

For retrieval repeatability, the evidence hash must also remain identical.

## Evidence manifest hashing

```bash
python .claude/skills/stableai-l4-no-drift/scripts/freeze_manifest.py evidence-manifest.json
```

This canonicalizes the manifest and outputs its SHA-256 identity.

## SHA-256

SHA-256 provides cryptographic verification that returned byte strings are identical. StableAI L4 is the control method; SHA-256 is the identity-verification layer.

## Commercial use

This repository is available for personal, academic, research, education, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, derivative frameworks, agent systems, or AI reliability work, cite `CITATION.cff` and retain attribution to:

**StableAI L4 — Constraint–Repair–Attractor Programming**

> **Same Input. Same Evidence State. Same Canonical Output. Same Hash. 100% No-Drift.**
