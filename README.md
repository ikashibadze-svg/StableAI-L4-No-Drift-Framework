# StableAI L4 No-Drift

**100% No-Drift LLM Output — Same Input. Same Canonical Output. Same Hash.**

StableAI L4 is a deterministic control framework for LLM output and agent behavior based on **Constraint–Repair–Attractor Programming** and a physics-based treatment of information stability.

`p = (S, C, R, A, V)`

- **S — State / Schema:** admissible output or execution states
- **C — Constraints:** forbidden variation and actions
- **R — Repair:** restoring operator that projects deviations back into the allowed state
- **A — Attractor:** exact canonical target or canonical surviving state/action
- **V — Verification:** exact, structural, provenance, and SHA-256 checks

## Core operating law

```text
same input + same evidence + same declared conditions
                         ↓
                  StableAI L4
                         ↓
              same canonical result
                         ↓
                   same hash
```

StableAI is a **control layer**, not a replacement for the user's task. When active, it preserves the requested objective and normally runs silently. L4 diagnostics, hashes, batteries, and S/C/R/A/V traces are shown only when explicitly requested.

## Physics-Based Foundation

StableAI translates a stability architecture from physical systems into AI control:

```text
physical system:
state space → constraints → perturbation → restoring dynamics → stable attractor

StableAI L4:
output/action space → constraints → drift → repair → canonical attractor
```

The principle is to reduce admissible states and deterministically repair deviations until only the canonical state survives.

## L4 operating modes

### Exact-attractor
When an exact TARGET already exists:

`INPUT + TARGET -> S+C+R+A -> TARGET -> SHA-256`

### Closed canonical derivation
When output is derived but can be closed with fixed schema, vocabularies, ordered rules, tie-breaks, missing/conflict states, and canonical serialization.

### Canonical open-result control
For research, retrieval, summarization, or other tasks where the answer is not known beforehand:

`task -> evidence -> supported facts -> canonical order/expression -> repair -> verification -> answer`

StableAI never invents a TARGET merely to force exact-attractor mode.

### Agent/tool execution

`state -> allowed actions -> filter -> rank -> deterministic tie-break -> act -> verify -> repair/stop`

The same observable state, evidence, tools, and constraints select the same canonical next action.

## Universal invariants

- Preserve the user's objective.
- Never invent a target or fact.
- Resolve identity before merging evidence.
- Represent conflicts and missing values explicitly.
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
│   └── execution.md
└── scripts/
    ├── hash_outputs.py
    ├── run_battery.sh
    └── verify_nodrift.py

benchmarks/
├── README.md
└── reported-results.json

tools/
└── build_claude_skill_zip.sh

example_l4_prompt.txt
example_target.json
LICENSE.md
CITATION.cff
CONTRIBUTING.md
SECURITY.md
CHANGELOG.md
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

Build the upload package directly from the checked-in skill source:

```bash
bash tools/build_claude_skill_zip.sh
```

This creates:

`stableai-l4-no-drift-claude-ready.zip`

with the correct structure:

```text
SKILL.md
assets/
references/
scripts/
```

Do **not** upload the entire GitHub repository ZIP to Claude Customize.

## Run the No-Drift verification battery

Anthropic API:

```bash
export ANTHROPIC_API_KEY=...
python .claude/skills/stableai-l4-no-drift/scripts/verify_nodrift.py \
  --prompt-file example_l4_prompt.txt \
  --target-file example_target.json \
  --runs 20 \
  --model <model-id>
```

Claude Code CLI:

```bash
.claude/skills/stableai-l4-no-drift/scripts/run_battery.sh \
  <model> example_l4_prompt.txt example_target.json 20
```

For an exact-target N-run certification, strict success requires:

```text
attempted_runs = N
completed_runs = N
transport_errors = 0
raw_exact_match_rate = 1.0
unique_outputs = 1
unique_hashes = 1
all_hashes_identical = true
```

Add schema validity requirements when the target format requires them.

## SHA-256

SHA-256 provides cryptographic verification that returned byte strings are identical. StableAI L4 is the control method; SHA-256 is the identity-verification layer.

## Reference results

StableAI L4 experiments reported full no-drift convergence across repeated calls and substantial output-token/latency reduction. Machine-readable reference results are in `benchmarks/reported-results.json`.

## Commercial use

This repository is available for personal, academic, research, education, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, derivative frameworks, agent systems, or AI reliability work, cite `CITATION.cff` and retain attribution to:

**StableAI L4 — Constraint–Repair–Attractor Programming**

> **Same Input. Same Canonical Output. Same Hash. 100% No-Drift.**
