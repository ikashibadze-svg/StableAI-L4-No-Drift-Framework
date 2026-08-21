# StableAI L4 No-Drift

**100% No-Drift — Same Input. Same Canonical Evidence. Same Canonical Output. Same Hash.**

StableAI L4 is a deterministic control framework for LLM output, retrieval, knowledge formation, and agent behavior based on **Constraint–Repair–Attractor Programming** and a physics-based treatment of information stability.

`p = (S, C, R, A, V)`

- **S — State / Schema:** admissible retrieval, evidence, knowledge, output, and execution states
- **C — Constraints:** forbidden variation, unsupported evidence, and forbidden actions
- **R — Repair:** restoring operator that projects deviations back into the permitted state
- **A — Attractor:** canonical surviving evidence set, fact set, output, or action
- **V — Verification:** exact, structural, provenance, evidence-set, fact-set, and SHA-256 checks

## Core operating law

```text
same input + same declared conditions
                ↓
            StableAI L4
                ↓
same canonical evidence attractor
                ↓
same canonical fact attractor
                ↓
same canonical output attractor
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

StableAI does not remember stability. It recreates stability from the same conditions.

## L4 Operating Modes

### Exact Attractor
When an exact TARGET already exists:

`INPUT + TARGET -> constrain -> repair -> TARGET -> SHA-256`

StableAI never invents a TARGET simply to force exact-attractor mode.

### Closed Canonical Derivation
When output is derived but can be closed with fixed schema, vocabularies, ordered rules, tie-breaks, missing/conflict states, and canonical serialization.

### Evidence Attractor
For research and live retrieval:

`same input -> same canonical retrieval program -> same canonical evidence -> same canonical facts -> same answer`

Every run performs **fresh independent retrieval**. Prior-run evidence is not reused, frozen, or cached to manufacture repeatability.

### Agent / Tool Attractor

`state -> allowed actions -> filter -> rank -> deterministic tie-break -> act -> verify -> repair/stop`

## Evidence Attractor

For open-world research StableAI defines:

`R_E = (Q, D, P, B, F, X, T, R, V)`

- **Q — Query Plan:** fixed canonical query sequence
- **D — Disambiguation:** deterministic identity rules
- **P — Source Priority:** deterministic ranking
- **B — Evidence Budget:** fixed query/source/depth budget
- **F — Fact Acceptance:** deterministic inclusion criteria
- **X — Duplicate/Propagation Control:** evidence-lineage deduplication
- **T — Tie-Breaks:** deterministic residual choices
- **R — Repair:** correction of non-canonical retrieval choices
- **V — Verification:** evidence-set and fact-set identity checks

The evidence attractor is:

`E* = A_E(input, R_E)`

Every independent run should reconstruct:

`E1 = E2 = ... = En = E*`

## Independent Fresh-Retrieval Requirement

A valid StableAI research repeatability test requires:

- same literal user input
- same retrieval control program
- same retrieval budget
- same model/runtime/system conditions declared for the benchmark
- fresh external retrieval on every run
- no reuse of prior-run URLs, evidence records, fact records, or answer text

Each run independently computes:

`input -> canonical query plan -> retrieval -> evidence_i -> facts_i -> answer_i`

The target is:

```text
unique_query_plans = 1
unique_evidence_hashes = 1
unique_fact_hashes = 1
unique_output_hashes = 1
```

This is the core difference between StableAI No-Drift and caching.

## Canonical Query Plan

The retrieval plan is generated from fixed rules rather than improvised differently per run.

For entity research, the default structure is:

1. literal normalized query
2. exact quoted query
3. normalized query + canonical identity anchor
4. normalized query + canonical organization/domain anchor when available
5. verified native-script form when deterministically derivable

Query order and maximum query count are fixed. StableAI does not recursively invent new search phrases from newly discovered facts and does not search until subjective "convergence."

## Fixed Evidence Budget

Every run uses the same declared limits for:

- query count
- results per query
- selected source count
- source opens/fetches
- link-follow depth
- freshness window when relevant

One run must not search six sources while another searches fifteen.

## Source Determinization

Default authority order:

1. authoritative system of record / official primary source
2. official organization / issuer
3. first-party publication or direct statement
4. recognized institutional / technical source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

Within a tier, StableAI uses directness, identity confidence, date/version relevance, completeness, then canonical URL lexical order.

Several domains reproducing the same biography/text count as one evidence lineage rather than independent corroboration.

## Canonical Evidence and Fact Sets

After fresh retrieval, StableAI produces a canonical evidence set and hashes it:

`evidence_hash = SHA256(canonical_evidence_set)`

Then it derives a canonical fact set and hashes that:

`fact_hash = SHA256(canonical_fact_set)`

Only after the fact set is determined does StableAI serialize the final answer.

This produces three independently testable attractors:

```text
Evidence Attractor
      ↓
Fact / Knowledge Attractor
      ↓
Output Attractor
```

## Research No-Drift Metrics

For N independent fresh-retrieval runs report:

```text
attempted_runs
completed_runs
transport_errors

unique_query_plans
unique_evidence_sets
unique_evidence_hashes
unique_fact_sets
unique_fact_hashes
unique_outputs
unique_output_hashes

evidence_exact_match_rate
fact_exact_match_rate
output_exact_match_rate
```

Strict target:

```text
completed_runs = attempted_runs
unique_query_plans = 1
unique_evidence_hashes = 1
unique_fact_hashes = 1
unique_output_hashes = 1
evidence_exact_match_rate = 1.0
fact_exact_match_rate = 1.0
output_exact_match_rate = 1.0
```

## External World Boundary

A live search index is an external system. Controlled benchmarks should use a declared time window/freshness policy so the external state is intended to be equivalent across runs.

If the public world materially changes, the experimental input condition changed. StableAI does **not** hide this by reusing old evidence.

## Universal Invariants

- Preserve the user's objective.
- Never invent a target or fact.
- Every research run performs fresh independent retrieval.
- Query plans are canonical.
- Retrieval budgets are fixed.
- Evidence selection is deterministic.
- Resolve identity before merging evidence.
- Represent conflicts and missing values explicitly.
- Deduplicate propagated/copied evidence.
- Canonicalize and hash evidence and fact sets.
- Repair only when the correct repair is uniquely determined.
- Never use cached previous-run evidence as the repair target.
- Keep diagnostics silent unless requested.
- Stop immediately after verified success.

## Repository Layout

```text
.claude/skills/stableai-l4-no-drift/
├── SKILL.md
├── assets/
│   └── l4-prompt-template.txt
├── references/
│   ├── levels.md
│   ├── theory.md
│   ├── execution.md
│   └── evidence-attractor.md
└── scripts/
    ├── canonical_evidence.py
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

The ZIP contains:

```text
SKILL.md
assets/
references/
scripts/
```

Do **not** upload the entire GitHub repository ZIP to Claude Customize.

## Exact No-Drift Verification

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

## Evidence / Fact Hashing

```bash
python .claude/skills/stableai-l4-no-drift/scripts/canonical_evidence.py evidence.json --kind evidence
python .claude/skills/stableai-l4-no-drift/scripts/canonical_evidence.py facts.json --kind facts
```

## SHA-256

SHA-256 provides cryptographic verification that canonical byte strings are identical. StableAI L4 is the control method; SHA-256 is the identity-verification layer.

## Commercial Use

This repository is available for personal, academic, research, education, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, derivative frameworks, agent systems, or AI reliability work, cite `CITATION.cff` and retain attribution to:

**StableAI L4 — Constraint–Repair–Attractor Programming**

> **Same Input. Same Canonical Evidence. Same Canonical Output. Same Hash. 100% No-Drift.**
