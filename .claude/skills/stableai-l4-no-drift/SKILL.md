---
name: stableai-l4-no-drift
description: Use when StableAI L4, No-Drift, deterministic/canonical output, exact reproduction, drift testing, or constrained repeatable AI behavior is explicitly requested.
---

# StableAI L4 No-Drift

StableAI L4 is a deterministic control layer for LLM output, retrieval, and agent behavior.

Core program:

`p = (S, C, R, A, V)`

- **S — State / Schema:** admissible task, evidence, output, and execution states
- **C — Constraints:** forbidden variation, unsupported facts, and forbidden actions
- **R — Repair:** deterministic projection of deviations back into the permitted state
- **A — Attractor:** canonical surviving output, evidence state, or action
- **V — Verification:** exact, structural, provenance, evidence-manifest, and hash checks

Core law:

`same task + same evidence state + same declared conditions -> same canonical result`

## 1. Task-preservation invariant

The user's objective is invariant. StableAI may constrain execution, retrieval, evidence, ordering, serialization, repair, and verification. It must not replace the requested task with an L4 diagnosis, attractor-building exercise, benchmark, hash report, or tutorial.

Default user experience: return the requested answer and keep StableAI machinery silent.

## 2. Activation

Apply when StableAI / L4 / No-Drift / deterministic or canonical behavior is explicitly requested, when the user supplies a target for exact reproduction, or when this skill has already been enabled for the task. Do not activate merely because an ordinary task could be structured.

## 3. Four operating modes

### A — Exact attractor
Use only when an exact target already exists. Never invent a TARGET.

### B — Closed canonical derivation
Use when output must be derived but permitted values can be closed by schema, vocabularies, ordered rules, null/conflict states, and deterministic tie-breaks.

### C — Retrieval / open-result control
Use for research, web retrieval, evidence synthesis, open-world fact finding, and summarization. This mode MUST use the Retrieval Lock below.

### D — Agent / tool control
Use for multi-step tool workflows:

`state -> allowed actions -> filter -> rank -> tie-break -> act -> verify -> repair/stop`

## 4. Retrieval Lock — mandatory for open-world research

Live retrieval is an external state, not a free continuation of the model.

Define:

`E = canonical evidence manifest`

The answer attractor is conditional on `E`:

`A = A(task, E, constraints)`

Therefore a No-Drift repeat run MUST NOT silently perform a new discovery crawl and compare that new evidence set with the previous answer.

### DISCOVERY
Used only when no evidence manifest exists or the user explicitly requests fresh/updated information. Discovery creates one bounded canonical evidence manifest.

### LOCKED
Once the manifest exists, all repeat runs for the same task MUST reuse that manifest.

Do not issue additional search queries, add newly discovered sources, widen the source set, change query wording, search for convergence, or create v2/v3/v4 attractors from fresh evidence unless the user explicitly requests refresh/update/latest/new search or the declared freshness policy requires a new evidence version.

A fresh crawl is a new evidence version, not drift of the previous version.

## 5. Canonical evidence manifest

Maintain a manifest conceptually equivalent to:

```json
{
  "manifest_version":"1",
  "task_key":"",
  "entity_key":"",
  "scope":"",
  "freshness_cutoff":"",
  "query_plan":[],
  "sources":[{"canonical_url":"","source_tier":"","retrieved_at":"","content_hash":"","supported_claim_ids":[]}]
}
```

Canonicalize the manifest and compute:

`evidence_hash = SHA256(canonical_manifest)`

The canonical answer is associated with both `evidence_hash` and `answer_hash`.

No-Drift for research is measured under a fixed evidence hash.

## 6. Bounded discovery contract

Discovery must be bounded before searching.

Use caller rules first. Otherwise:

1. preserve the literal user query as the task key;
2. determine entity identity before merging facts;
3. use a fixed non-adaptive query plan;
4. use a fixed maximum source count;
5. select sources by deterministic authority rules;
6. stop when the bounded plan is exhausted or the source limit is reached;
7. freeze the manifest.

Do not perform open-ended "search until no more facts appear."

Default entity query plan:

1. literal user query;
2. exact quoted user query;
3. literal query plus one identity disambiguator only if established by an authoritative source already selected under the first two queries.

Do not recursively invent new search phrases from newly found facts.

## 7. Source selection

Use caller priorities first. Otherwise rank:

1. system of record / authoritative primary source
2. official organization / issuer
3. first-party publication or direct statement
4. recognized institutional / technical source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

Within the same tier use: directness to claim, relevant date/version, completeness, then canonical URL lexical order.

Normalize URLs before comparison and remove tracking parameters/fragments when they do not identify distinct content.

## 8. Source propagation / duplicate evidence

Multiple domains are not automatically independent evidence. If sources reproduce materially identical text from one origin, treat them as one evidence lineage for corroboration. Do not inflate confidence because copied text appears on several domains.

## 9. Entity identity

Resolve identity before merging evidence. Use stable identity-bearing attributes appropriate to the task. If identity is unresolved, use the canonical unresolved state. Never merge similar names by assumption.

## 10. Facts, conflicts, and missing information

Never invent facts. Each accepted fact must be supported by the frozen evidence manifest.

If credible evidence conflicts, preserve the conflict or use the canonical `CONFLICT` / `UNRESOLVED` state. For missing information use one declared state such as `null`, `UNKNOWN`, `NOT_FOUND`, or `UNRESOLVED`.

## 11. Freshness and versioning

A refresh changes the evidence state:

`E1 -> refresh -> E2`

and therefore:

`A(task,E1) = answer_v1`
`A(task,E2) = answer_v2`

A difference caused by changed evidence is **evidence evolution**, not output drift. Never call a refreshed answer a repeat run of the old evidence state.

If the user asks a timeless question and does not request freshness, reuse the locked evidence state when available. If the user asks for latest/current/today, create a new evidence version according to that freshness boundary.

## 12. Canonical fact ordering and expression

First determine accepted facts from the frozen manifest, then serialize.

For prose use deterministic fact order:

1. identity
2. current primary role/status
3. major prior roles/history
4. major verified projects/publications
5. other relevant facts
6. material uncertainty/conflicts

Use stable terminology and avoid unnecessary synonyms when repeatability matters.

## 13. Repeat-run rule

When the same task is repeated and the same evidence manifest is available:

- reuse the same `E`;
- do not browse for additional facts;
- do not improve the source set;
- do not alter scope;
- do not widen the answer;
- regenerate only from the frozen facts and canonical expression policy.

A repeatability test is valid only when task key, evidence hash, constraints, and serialization policy are identical.

## 14. Repair

Repair only toward a uniquely determined permitted state. Repair may remove unsupported facts, restore ordering/schema/canonical values, restore target bytes, or replace an invalid choice with a declared unresolved state. Repair must never create new evidence.

## 15. Agent and tool lock

Before any tool call verify:

`allowed AND available AND necessary AND arguments_complete AND not_redundant`

For retrieval, an additional search is not necessary in LOCKED state.

For side effects verify user intent, target, and payload; execute once; verify observable result; never duplicate a non-idempotent action through blind retry.

## 16. Verification

### Exact attractor
Verify exact bytes, SHA-256, unique outputs, and exact-match rate.

### Closed derived output
Verify schema, vocabulary, ordering, evidence support, and repeated-run identity.

### Retrieval
Verify task key, evidence manifest identity, evidence hash, source lineage/deduplication, claim support, entity identity, conflict policy, fact order, and final answer hash when benchmarking.

Do not claim a research repeatability result if the evidence hash changed.

### Agents/tools
Verify allowed action, arguments, result, side-effect uniqueness, bounded retries, and terminal state.

## 17. Diagnostics

Keep diagnostics silent unless explicitly requested. When requested, distinguish `output_drift`, `evidence_change`, `transport_failure`, `tool_failure`, `scope_change`, and `freshness_refresh`.

## 18. Universal invariants

```text
I1  user objective preserved
I2  no invented target
I3  no invented fact
I4  evidence state explicit for open-world tasks
I5  repeat runs reuse the same evidence manifest
I6  fresh retrieval creates a new evidence version
I7  source propagation does not count as independent corroboration
I8  identity resolved before fact merge
I9  conflicts deterministic
I10 missing information explicit
I11 canonical ordering deterministic
I12 repair never invents evidence
I13 tool calls necessary and non-redundant
I14 diagnostics silent unless requested
I15 verified success terminates execution
```

## 19. Final execution laws

Exact / closed tasks:

`preserve intent -> constrain -> derive -> canonicalize -> repair -> verify -> answer`

Open-world research:

`preserve intent -> discover once -> freeze E -> derive facts -> canonicalize -> verify -> answer`

Repeat research run:

`same task -> reuse E -> derive same facts -> canonicalize -> verify -> same answer`

Explicit refresh:

`same task -> new discovery -> E2 -> new versioned answer`

## Resources

- `references/retrieval-lock.md` — frozen evidence and retrieval versioning.
- `references/execution.md` — agent/tool control.
- `references/levels.md` — L0–L4 ladder.
- `references/theory.md` — physics-based formulation.
- `assets/l4-prompt-template.txt` — exact-attractor template.
- `scripts/freeze_manifest.py` — canonical evidence-manifest hash helper.
- `scripts/hash_outputs.py` — offline answer/hash scorer.
- `scripts/verify_nodrift.py` — Anthropic API battery.
- `scripts/run_battery.sh` — Claude Code CLI battery.
