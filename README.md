# StableAI L4 No-Drift

**Constraint–Repair–Attractor control and verification for reproducible LLM output.**

StableAI L4 encodes a constrained generation task as:

`p = (S, C, R, A, V)`

- **S — Schema:** allowed output structure
- **C — Constraints:** forbidden variation
- **R — Repair:** deterministic correction instructions
- **A — Attractor:** exact canonical target or closed canonical value space
- **V — Verification:** external exact-match and SHA-256 checks

The strongest L4 mode is **exact-attractor lock**: when the canonical target is already known, repeated calls are tested for byte-for-byte identity. For outputs that must be derived from input, use fixed schemas, closed vocabularies, ordered decision rules, and deterministic tie-breaks, then verify empirically.

## Repository layout

```text
.claude/skills/l4-no-drift/
├── SKILL.md
├── assets/l4-prompt-template.txt
├── references/
│   ├── levels.md
│   └── theory.md
└── scripts/
    ├── hash_outputs.py
    ├── run_battery.sh
    └── verify_nodrift.py
benchmarks/
├── README.md
└── reported-results.json
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
cp -R path/to/l4-no-drift .claude/skills/l4-no-drift
```

User-scoped:

```bash
mkdir -p ~/.claude/skills
cp -R path/to/l4-no-drift ~/.claude/skills/l4-no-drift
```

The skill itself is located at `.claude/skills/l4-no-drift/` in this repository.

## Install in Claude Customize

Use the separate release artifact `stableai-l4-no-drift-claude-skill.zip`. Its ZIP root is the `l4-no-drift/` skill folder rather than the entire GitHub repository.

## Run the verification battery

### Anthropic API

```bash
export ANTHROPIC_API_KEY=...
python .claude/skills/l4-no-drift/scripts/verify_nodrift.py \
  --prompt-file example_l4_prompt.txt \
  --target-file example_target.json \
  --runs 20 \
  --model <model-id>
```

### Claude Code CLI

```bash
.claude/skills/l4-no-drift/scripts/run_battery.sh \
  <model> example_l4_prompt.txt example_target.json 20
```

A requested 20-run battery passes only if **all 20 model runs complete successfully** and every completed output matches the target exactly with one SHA-256 hash. Transport failures are reported separately and never silently reduce the denominator.

## What SHA-256 proves

SHA-256 does **not** make an LLM deterministic. It provides cryptographic verification that returned byte strings are identical. StableAI L4 is the control method; repeated measurement establishes whether a given prompt/model/runtime combination achieved no observed drift in the test battery.

## Reported reference results

The original StableAI experiments reported exact-match convergence and substantial output-token/latency reduction. A machine-readable summary is included in `benchmarks/reported-results.json`. These entries are labeled **reported** because the original raw run artifacts and hashes are not bundled in this repository. New public benchmark claims should include raw outputs or reproducible reports plus environment metadata.

## Commercial use

This repository is publicly inspectable and free for personal, research, educational, evaluation, and other non-commercial use. **Commercial use requires a separate license.** See `LICENSE.md`.

## Citation

If you use StableAI L4 in research, benchmarks, articles, or derivative frameworks, please cite this repository using `CITATION.cff` and retain attribution to **StableAI L4 / Constraint–Repair–Attractor Programming**.
