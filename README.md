# StableAI L4 No-Drift

**100% No-Drift LLM Output — Same Input. Same Canonical Output. Same Hash.**

StableAI L4 is a deterministic control framework for eliminating output drift in Large Language Models through **Constraint–Repair–Attractor Programming**.

StableAI L4 derives its control architecture from a **physics-based treatment of information stability**. Instead of treating LLM output only as text generation, StableAI models the task as a constrained state space in which valid outputs are restricted by structure, boundaries, repair dynamics, and attractors.

The framework translates stability concepts from physical systems into AI control:

```text
physical system:
state space → constraints → perturbation → restoring dynamics → stable attractor

StableAI L4:
output space → constraints → drift → repair → canonical attractor
```

The core principle is that stability is achieved by reducing the number of admissible states and forcing deviations back toward a stable configuration.

StableAI L4 encodes this as:

`p = (S, C, R, A, V)`

where:

- **S — Schema / State Space:** defines the permitted structure and admissible output states
- **C — Constraints:** eliminate forbidden structural, lexical, formatting, and semantic variation
- **R — Repair / Restoring Operator:** detects deviations and projects the output back toward the permitted state
- **A — Attractor:** defines the single canonical survivor or closed canonical output space
- **V — Verification / Measurement:** externally verifies exact identity using exact-match and SHA-256 checks

The operational objective is simple:

```text
same input
    ↓
same constrained generation process
    ↓
same canonical output
    ↓
same SHA-256 hash
```

---

## Physics-Based Foundation

StableAI L4 originates from a physics-based approach to information and system stability.

In a physical system, stability does not come from unlimited freedom. It comes from constraints that restrict possible states and from restoring dynamics that push perturbations back toward a stable configuration.

StableAI applies the same architecture to probabilistic AI output.

```text
Physical system

possible states
    ↓
constraints
    ↓
perturbation
    ↓
restoring dynamics
    ↓
stable attractor
```

```text
StableAI L4

possible outputs
    ↓
constraints
    ↓
output drift
    ↓
repair
    ↓
canonical attractor
```

This produces the StableAI control mapping:

```text
S = allowed state structure
C = boundary constraints
R = restoring / repair operator
A = stable attractor
V = measurement and verification
```

The objective is therefore not to ask a probabilistic model to "try to be consistent."

The objective is to construct a constrained system in which alternative output states are progressively eliminated until one canonical state survives.

---

## Core Principle

A normal LLM prompt leaves many valid output paths open.

Even when two answers are semantically equivalent, they may differ in:

- wording
- key order
- capitalization
- punctuation
- length
- formatting
- synonyms
- explanation style
- serialization

These differences create output drift.

StableAI L4 progressively collapses that output space.

```text
L0 = free generation
L1 = schema control
L2 = constraint control
L3 = canonical style control
L4 = exact no-drift control
```

At L4:

```text
Schema
+ Constraints
+ Repair
+ Attractor
+ Verification
= 100% No-Drift
```

The target is not merely semantically similar answers.

The target is:

```text
unique_outputs = 1
unique_hashes = 1
raw_exact_match_rate = 1.0
canonical_exact_match_rate = 1.0
valid_output_rate = 1.0
```

---

## Constraint–Repair–Attractor Architecture

StableAI L4 can be understood as a state-collapse process.

Start with a large set of possible outputs:

\[
Y = \{y_1,y_2,\ldots,y_n\}
\]

The schema removes structurally invalid states:

\[
Y \xrightarrow{S} Y_S
\]

Constraints eliminate prohibited variations:

\[
Y_S \xrightarrow{C} Y_C
\]

Repair removes surviving deviations:

\[
Y_C \xrightarrow{R} Y_R
\]

The attractor defines the canonical state:

\[
Y_R \xrightarrow{A} y^*
\]

Verification confirms that the returned state is identical to the required canonical state:

\[
V(y)=
\begin{cases}
1,& y=y^* \\
0,& y\neq y^*
\end{cases}
\]

Operationally:

```text
large output space
      ↓
schema
      ↓
smaller output space
      ↓
constraints
      ↓
smaller output space
      ↓
repair
      ↓
canonical attractor
      ↓
verification
      ↓
one surviving output
```

---

## Two L4 Operating Modes

### 1. Exact-Attractor Lock

When the canonical output is known in advance, StableAI L4 constrains the model to one exact permitted output.

```text
INPUT + TARGET
      ↓
S + C + R + A
      ↓
TARGET
      ↓
SHA-256
```

The returned output is tested byte-for-byte against the canonical target.

The allowed output space is:

\[
Y_{\text{allowed}}=\{y^*\}
\]

Only one output is permitted.

Any deviation in:

- whitespace
- punctuation
- capitalization
- values
- key order
- quotes
- formatting

fails verification.

---

### 2. Canonical Derived Output

In many practical tasks, the answer is not known before the model processes the input.

Examples include:

- classification
- extraction
- structured analysis
- record generation
- agent decisions
- normalization
- deterministic transformation

In these tasks, StableAI first reduces semantic freedom before applying final output verification.

It uses:

- fixed schemas
- closed vocabularies
- ordered decision rules
- explicit normalization rules
- deterministic tie-breaks
- canonical serialization
- repair gates
- external verification

The execution model becomes:

```text
INPUT
  ↓
DERIVE
  ↓
CONSTRAIN
  ↓
CANONICALIZE
  ↓
REPAIR
  ↓
VERIFY
  ↓
CANONICAL OUTPUT
```

The goal remains the same:

```text
same input
→ same canonical state
→ same serialized output
→ same hash
```

---

## Why Normal Prompting Drifts

A conventional prompt may define the task but leave a large number of acceptable realizations open.

For example:

```text
Analyze this startup.
```

Possible responses may all be correct while differing substantially.

Even a structured prompt such as:

```text
Product:
Customer:
Problem:
Value:
```

still leaves lexical freedom.

The model may return:

```text
parents
```

or:

```text
parents of schoolchildren
```

or:

```text
families
```

All may be semantically reasonable.

StableAI eliminates this freedom by progressively restricting the admissible output state.

---

## StableAI Control Levels

### L0 — Free Generation

```text
Analyze this startup.
```

Characteristics:

```text
high output entropy
high wording variation
high token use
high drift
```

---

### L1 — Structure Lock

```text
Product:
Customer:
Problem:
Value:
```

Structure becomes more stable, but wording remains open.

---

### L2 — Constraint Lock

```text
No extra text.
Use fixed labels.
Use short wording.
No markdown.
```

Formatting drift decreases, but lexical alternatives remain.

---

### L3 — Canonical Style Lock

```text
Return exactly 8 lines.
Use one concise phrase per field.
Use stable business language.
```

This strongly compresses output freedom.

Previous StableAI experiments demonstrated substantial token reduction and speed improvement at this level, but multiple exact outputs could still survive.

---

### L4 — Exact Attractor Lock

L4 adds the final mechanism:

```text
exact canonical state
+ repair
+ external verification
```

At this level, the model is no longer asked to freely compose an answer.

It is asked to collapse into the canonical survivor.

---

## StableAI L4 Prompt Structure

A compact L4 program follows:

```text
L4 NO-DRIFT MODE.

You are not writing freely.
You are performing exact attractor lock.

S = schema:
Return one valid JSON object only.

C = constraints:
No markdown.
No explanation.
No code fences.
No extra text.
No paraphrase.
No synonyms.
No added keys.
No removed keys.
No key reorder.
No punctuation changes.
No case changes.
No value changes.

R = repair:
Before final output, compare output against TARGET.
If any key, value, order, case, comma, quote, or punctuation differs, repair it.
If any text exists before or after JSON, remove it.

A = attractor:
TARGET is the only allowed survivor.

V = verification:
Internally verify exact match before final output.

FINAL:
Return TARGET exactly and nothing else.
```

A compressed version is:

```text
Return ONLY valid JSON. Copy TARGET exactly.
No markdown, explanation, paraphrase, synonym, key, case, order, or punctuation change.
Verify exact match; if different, repair.
TARGET is the only allowed output.
```

---

## Repository Layout

```text
.claude/skills/l4-no-drift/
├── SKILL.md
├── assets/
│   └── l4-prompt-template.txt
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

The Claude Skill itself is located at:

```text
.claude/skills/l4-no-drift/
```

---

## Install in Claude Code

### Project-Scoped Installation

```bash
mkdir -p .claude/skills
cp -R path/to/l4-no-drift .claude/skills/l4-no-drift
```

### User-Scoped Installation

```bash
mkdir -p ~/.claude/skills
cp -R path/to/l4-no-drift ~/.claude/skills/l4-no-drift
```

Claude can then load StableAI L4 as a reusable execution capability.

---

## Install in Claude Customize

Use the release artifact:

```text
stableai-l4-no-drift-claude-skill.zip
```

The ZIP root contains the `l4-no-drift/` skill directory directly rather than the complete GitHub repository.

```text
l4-no-drift/
├── SKILL.md
├── assets/
├── references/
└── scripts/
```

---

## Run the No-Drift Verification Battery

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

A 20-run StableAI battery succeeds only when:

```text
attempted_runs = 20
completed_runs = 20
transport_errors = 0

valid_output_rate = 1.0
raw_exact_match_rate = 1.0
canonical_exact_match_rate = 1.0

unique_outputs = 1
unique_hashes = 1
```

Transport or API failures are reported separately and never silently removed from the requested run count.

---

## SHA-256 Verification

StableAI L4 controls the model output.

SHA-256 independently verifies that returned byte sequences are identical across runs.

```text
output_1 → SHA-256 → H
output_2 → SHA-256 → H
output_3 → SHA-256 → H
...
output_n → SHA-256 → H
```

If:

```text
H₁ = H₂ = H₃ = ... = Hₙ
```

and exact byte comparison succeeds, then:

```text
unique_hashes = 1
exact_match_rate = 1.0
```

This produces an externally auditable no-drift result.

The layers are distinct:

```text
StableAI L4 = deterministic control layer
SHA-256      = cryptographic output identity verification
```

---

## 100% No-Drift Criterion

StableAI defines a successful no-drift battery as:

\[
D = 0
\]

where output drift can be represented as the number of unique outputs beyond the canonical output.

For \(N\) completed calls:

\[
|\{y_1,\ldots,y_N\}| = 1
\]

and:

\[
H(y_1)=H(y_2)=\ldots=H(y_N)
\]

where \(H\) is SHA-256.

Operationally:

```text
100% completed runs
100% exact match
1 unique output
1 unique hash
0 observed output drift
```

---

## Reference Results

StableAI L4 experiments demonstrated full no-drift convergence across repeated model calls together with substantial reductions in generated output tokens and response latency.

Reported measurements include:

```text
unique_outputs = 1
all_hashes_identical = true
valid_json_rate = 1.0
raw_exact_match_rate = 1.0
canonical_exact_match_rate = 1.0
```

In the reported L4 benchmark:

```text
Baseline average output tokens: 1193.65
L4 average output tokens:         53.0

Output-token reduction:           95.56%

Baseline average latency:         28.53 s
L4 average latency:                1.51 s

Speedup:                          18.94×
```

Machine-readable reference results are available in:

```text
benchmarks/reported-results.json
```

New benchmark releases should include sufficient execution metadata to make the result reproducible and independently auditable.

---

## StableAI No-Drift Law

StableAI L4 follows the principle:

```text
Output freedom ↓
Constraints ↑
Repair pressure ↑
Attractor strength ↑
        ↓
Admissible output states collapse
        ↓
One canonical survivor
```

Using the StableAI control program:

\[
p=(S,C,R,A,V)
\]

the operational target is:

\[
P(y\mid p)\rightarrow\delta(y^*)
\]

where \(y^*\) is the canonical surviving output.

Operationally:

```text
drift → 0
unique_outputs → 1
unique_hashes → 1
exact_match_rate → 1.0
```

---

## Low-Token Effect

StableAI L4 also reduces output cost by eliminating unnecessary generation freedom.

A normal prompt allows many continuations:

```text
free generation
      ↓
many admissible continuations
      ↓
longer and more variable output
```

StableAI restricts those continuations:

```text
StableAI L4
      ↓
collapsed output space
      ↓
short canonical output
      ↓
lower token use
      ↓
lower latency
```

The practical relationship is:

\[
H(\text{output space})\downarrow
\Rightarrow
T_{\text{output}}\downarrow
\Rightarrow
\text{latency}\downarrow
\]

without requiring fine-tuning or model retraining.

---

## Constraint-Induced Token Reduction

Let total token cost be:

\[
T=T_{\text{input}}+T_{\text{output}}
\]

A free prompt leaves many valid continuations available.

StableAI reduces the output search space by fixing:

```text
schema
constraints
canonical vocabulary
repair rules
attractor
serialization
```

Therefore:

\[
\text{admissible output states}\downarrow
\]

which operationally produces:

\[
T_{\text{output}}^{L4}\ll T_{\text{output}}^{free}
\]

for tasks where the canonical representation is substantially shorter than unrestricted generation.

---

## What StableAI L4 Is

StableAI L4 is not another language model.

It is a **deterministic control architecture around probabilistic language models**.

```text
LLM
 ↓
StableAI L4
 ↓
Schema
 ↓
Constraints
 ↓
Repair
 ↓
Canonical Attractor
 ↓
Verification
 ↓
No-Drift Output
```

It changes the model's operating conditions rather than requiring model retraining.

This means StableAI can potentially operate across different foundation models while preserving the same control principles.

---

## StableAI and Probabilistic AI

Modern LLMs are probabilistic generators.

StableAI does not require replacing that probabilistic generator.

Instead, it places a deterministic control structure around it.

```text
Probabilistic generator
          +
Deterministic control structure
          ↓
Constrained AI behavior
```

The distinction is:

```text
model intelligence ≠ output control
```

The model can remain probabilistic internally while its externally permitted output space is tightly constrained.

---

## Beyond Output Control

The same architecture can be extended beyond text generation.

```text
state
 ↓
allowed actions
 ↓
constraints
 ↓
repair
 ↓
canonical action
 ↓
verification
```

This creates a path from:

```text
No-Drift Output
```

toward:

```text
No-Drift Agents
No-Drift Tool Use
Deterministic Knowledge Processing
Deterministic AI Workflows
```

The broader StableAI objective is therefore deterministic AI behavior across:

```text
knowledge
reasoning
output
actions
verification
```

---

## Reproducibility

A public StableAI benchmark should record:

```text
model identifier
model/runtime version
date
system prompt
user prompt
temperature/settings
requested runs
completed runs
transport failures
input tokens
output tokens
latency
raw outputs
canonical outputs
SHA-256 hashes
exact-match rate
```

This allows others to independently reproduce and audit the result.

---

## Commercial Use

This repository is publicly inspectable and available for:

- personal use
- academic research
- education
- evaluation
- experimentation
- other non-commercial purposes

**Commercial use, commercial integration, commercial deployment, resale, sublicensing, or incorporation into commercial AI products requires a separate commercial license.**

See:

```text
LICENSE.md
```

---

## Citation and Attribution

If you use StableAI L4 in:

- academic research
- benchmarks
- articles
- presentations
- derivative frameworks
- Claude Skills
- agent architectures
- AI reliability systems
- commercial evaluations

please cite this repository using `CITATION.cff` and retain attribution to:

**StableAI L4 — Constraint–Repair–Attractor Programming**

---

## StableAI L4

> **Same Input. Same Canonical Output. Same Hash. 100% No-Drift.**

**Constraint the state space. Repair deviations. Collapse to the attractor. Verify the result.**
