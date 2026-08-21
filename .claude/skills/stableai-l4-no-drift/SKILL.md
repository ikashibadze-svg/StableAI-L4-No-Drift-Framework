---
name: stableai-l4-no-drift
description: Use when StableAI L4, No-Drift, deterministic/canonical output, exact reproduction, drift testing, or constrained repeatable AI behavior is explicitly requested.
---

# StableAI L4 No-Drift

StableAI L4 is a deterministic control layer for LLM output, retrieval, knowledge formation, and agent behavior.

Core program:

`p = (S, C, R, A, V)`

- **S — State / Schema:** admissible task, retrieval, evidence, knowledge, output, and execution states
- **C — Constraints:** forbidden variation, unsupported evidence, and forbidden actions
- **R — Repair:** deterministic projection of deviations back into the permitted state
- **A — Attractor:** canonical surviving evidence set, knowledge state, output, or action
- **V — Verification:** exact, structural, provenance, evidence-set, fact-set, and hash checks

Core law:

`same input + same declared conditions -> same canonical state -> same result`

## 1. Task preservation

The user's objective is invariant.

StableAI may constrain execution, retrieval, evidence selection, knowledge formation, ordering, serialization, repair, and verification. It must not replace the requested task with an L4 diagnosis, benchmark, attractor tutorial, hash report, or internal trace.

Default user experience: return the requested answer and keep StableAI machinery silent.

## 2. Activation

Apply when StableAI / L4 / No-Drift / deterministic or canonical behavior is explicitly requested, when an exact target is supplied, or when this skill has already been enabled for the task.

Do not activate merely because an ordinary task could be structured.

## 3. Operating modes

### A — Exact Attractor
Use when an exact target already exists.

`INPUT + TARGET -> S+C+R+A -> TARGET -> verify`

Never invent a TARGET.

### B — Closed Canonical Derivation
Use when the answer must be derived but the allowed result space can be closed by schema, vocabularies, ordered rules, null/conflict states, and deterministic tie-breaks.

### C — Evidence Attractor
Use for research, web retrieval, open-world fact finding, evidence synthesis, and knowledge construction.

Every run performs fresh retrieval.

The retrieval program itself must collapse to the same canonical evidence state:

`same input -> same retrieval program -> same canonical evidence set -> same fact set -> same answer`

Do not reuse, cache, or freeze the previous run's evidence in order to obtain repeatability.

### D — Agent / Tool Attractor
Use for multi-step tool workflows:

`state -> allowed actions -> filter -> rank -> tie-break -> act -> verify -> repair/stop`

## 4. Evidence Attractor Principle

For open-world research define the retrieval control program:

`R_E = (Q, D, P, B, F, X, T, R, V)`

where:

- **Q — Query Plan:** fixed canonical query sequence
- **D — Disambiguation:** fixed identity-resolution rules
- **P — Source Priority:** deterministic source ranking
- **B — Evidence Budget:** fixed source/query/depth limits
- **F — Fact Acceptance:** deterministic inclusion criteria
- **X — Propagation/Duplicate Control:** source-lineage deduplication
- **T — Tie-Breaks:** deterministic residual choice rules
- **R — Repair:** reject/replace non-canonical evidence choices
- **V — Verification:** evidence-set and fact-set identity checks

The evidence attractor is:

`E* = A_E(input, R_E)`

Every independent run should reconstruct:

`E1 = E2 = ... = En = E*`

Fresh retrieval is mandatory. Reuse of prior evidence does not count as an independent No-Drift test.

## 5. Canonical Query Plan

The query plan must be generated from the input by fixed rules, not improvised differently per run.

For person/entity research, unless caller supplies another plan:

1. literal normalized query
2. exact quoted query
3. normalized query + canonical identity anchor
4. normalized query + canonical organization/domain anchor when available
5. normalized query in verified native-script form when deterministically derivable from authoritative evidence

Important:

- The plan structure is fixed.
- Query order is fixed.
- Maximum number of queries is fixed.
- Do not recursively invent new query phrasings from facts discovered during the run.
- Do not search until "convergence."
- Do not broaden scope because one run happened to find an interesting new fact.

Identity anchors may only come from deterministic disambiguation rules, not subjective model choice.

## 6. Deterministic Disambiguation

Before merging evidence, construct a canonical entity identity key from stable attributes available from authoritative evidence.

Example conceptual key:

`entity_key = normalized_name | canonical_org | canonical_role/domain`

If multiple candidate entities exist, rank them by:

1. exact normalized name
2. authoritative organization/domain match
3. role match
4. geography match when relevant
5. canonical identifier
6. lexical tie-break

Do not merge unresolved candidates.

## 7. Fixed Evidence Budget

A run must use the same retrieval budget.

Declare or use defaults for:

- max queries
- max results per query
- max selected sources
- max source opens/fetches
- max depth of link-following
- freshness window when relevant

The budget is part of the experimental state.

Do not let one run search 6 sources and another search 15.

## 8. Deterministic Source Priority

Use caller priorities first. Otherwise rank sources:

1. authoritative system of record / official primary source
2. official organization / issuer
3. first-party publication or direct statement
4. recognized institutional / technical source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

Within one tier, rank by:

1. directness to the claim
2. identity confidence
3. relevant date/version
4. completeness
5. canonical URL lexical order

Select the first `B_sources` canonical survivors.

## 9. Source Canonicalization

Before comparing or selecting sources:

- normalize scheme/host casing
- remove fragments
- remove tracking parameters
- normalize trailing slash where equivalent
- resolve obvious duplicate URLs to one canonical URL
- prefer original source over mirrors when deterministically identifiable

Source identity should be stable across runs.

## 10. Propagation and Duplicate Control

Several domains may reproduce the same original biography or press text.

Do not count copied text as independent corroboration.

When two sources have materially identical content or one explicitly republishes another:

- assign them one lineage
- retain the canonical origin when identifiable
- otherwise choose the highest-priority source, then lexical canonical URL

Evidence ranking operates on canonical lineages, not raw domain count.

## 11. Deterministic Fact Acceptance

Facts are accepted only if they satisfy fixed rules.

Default order:

1. explicit statement in selected evidence
2. entity identity resolved
3. claim scope matches the task
4. no higher-priority contradiction
5. provenance retained
6. claim passes canonical confidence threshold if one is declared

Never add a fact solely because it is interesting.

Never infer unsupported personal residence, title, affiliation, dates, or other fields.

## 12. Conflict Rule

When selected credible evidence conflicts:

1. apply source priority
2. if one claim has strictly higher canonical priority, select it
3. if canonical priority is equal and claims materially conflict, emit `CONFLICT` / `UNRESOLVED`
4. do not choose based on wording preference

Conflict handling must produce the same result every run.

## 13. Missing Information

Use one fixed missing-value state per task, such as:

`null`
`UNKNOWN`
`NOT_FOUND`
`UNRESOLVED`

Do not fill gaps with plausible values.

## 14. Canonical Evidence Set

After retrieval and source ranking, create a canonical evidence set conceptually equivalent to:

```json
{
  "task_key":"",
  "entity_key":"",
  "query_plan":[],
  "budget":{},
  "sources":[
    {
      "canonical_url":"",
      "lineage_id":"",
      "source_tier":"",
      "content_hash":"",
      "accepted_claim_ids":[]
    }
  ]
}
```

Sort sources by canonical ranking order, not discovery order.

Canonicalize and hash:

`evidence_hash = SHA256(canonical_evidence_set)`

For No-Drift retrieval:

`unique_evidence_hashes = 1`

across independent fresh runs.

## 15. Canonical Fact Set

From the canonical evidence set produce a canonical fact set.

Each fact should conceptually contain:

```json
{
  "claim_id":"",
  "subject":"",
  "relation":"",
  "value":"",
  "provenance":[],
  "status":"VERIFIED"
}
```

Sort facts by fixed schema priority, then canonical claim identifier.

Hash:

`fact_hash = SHA256(canonical_fact_set)`

For No-Drift knowledge formation:

`unique_fact_hashes = 1`

## 16. Canonical Expression

Only after the fact set is stable should the final answer be generated.

For prose use deterministic fact order:

1. identity
2. current primary role/status
3. major prior roles
4. major projects/publications
5. other task-relevant verified facts
6. material conflicts/uncertainty

Use stable terminology and avoid unnecessary synonym variation when repeatability matters.

For structured output use fixed key order, vocabularies, null states, and canonical serialization.

## 17. Retrieval Repair

Repair acts on deviations from the canonical retrieval program.

Examples:

- non-canonical query wording -> replace with canonical query
- extra exploratory query -> remove
- source outside evidence budget -> discard
- lower-priority source selected over higher-priority source -> replace
- duplicate propagation source -> collapse to canonical lineage
- unsupported fact -> remove
- unresolved identity merge -> split / mark unresolved
- wrong source order -> restore canonical rank

Repair never uses previous-run evidence as the answer key.

## 18. Independent Repeat-Run Rule

A valid No-Drift research battery must satisfy:

- same literal user input
- same model/runtime/system conditions declared for the test
- same retrieval control program
- same retrieval budget
- fresh external retrieval for every run
- no reuse of prior run's source list, evidence set, fact set, or answer

Each run independently computes:

`input -> Q -> retrieval -> E_i -> F_i -> Y_i`

Success requires collapse:

`E_1 = ... = E_n`
`F_1 = ... = F_n`
`Y_1 = ... = Y_n`

## 19. Retrieval Verification Metrics

For N independent research runs report:

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

Strict full No-Drift target:

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

## 20. External World Changes

If the public web genuinely changes between calls, record the retrieval timestamp and freshness boundary.

For a controlled benchmark, keep the run window narrow enough that the external information state is intended to be equivalent.

Do not solve a changing-world benchmark by reusing old evidence.

The StableAI objective remains:

`same external state -> same evidence attractor`

If the external world changes materially, that is a changed experimental input condition.

## 21. Agent and Tool Attractor

Before every tool call verify:

`allowed AND available AND necessary AND arguments_complete AND canonical AND not_redundant`

Select tools and arguments using fixed priorities and tie-breaks.

For side effects verify user intent, exact target and payload; execute once; verify observable result; never duplicate a non-idempotent action through blind retry.

## 22. Repair

Repair only toward a uniquely determined permitted state.

Repair can restore schema, canonical evidence choice, source order, fact order, canonical vocabulary, tool arguments, target bytes, or an explicit unresolved state.

Repair never guesses.

## 23. Diagnostics

Keep diagnostics silent unless explicitly requested.

When requested distinguish:

- `OUTPUT_DRIFT`
- `EVIDENCE_DRIFT`
- `FACT_DRIFT`
- `QUERY_PLAN_DRIFT`
- `TRANSPORT_FAILURE`
- `TOOL_FAILURE`
- `EXTERNAL_STATE_CHANGE`

## 24. Universal Invariants

```text
I1  user objective preserved
I2  no invented target
I3  no invented fact
I4  every retrieval run is fresh and independent
I5  query plan is canonical
I6  retrieval budget is fixed
I7  evidence selection is deterministic
I8  source propagation is deduplicated
I9  identity is resolved before merging facts
I10 conflicts are deterministic
I11 fact acceptance is deterministic
I12 evidence set is canonicalized and hashable
I13 fact set is canonicalized and hashable
I14 repair never relies on cached prior-run evidence
I15 tool calls are canonical and non-redundant
I16 diagnostics stay silent unless requested
I17 verified success terminates execution
```

## 25. Final Laws

Exact target:

`same input + same target -> same output -> same hash`

Derived closed task:

`same input -> same canonical derivation -> same result`

Open-world research:

`same input -> same canonical retrieval program -> same evidence attractor -> same fact attractor -> same answer attractor`

Agent:

`same state -> same canonical action`

StableAI does not remember stability.

**StableAI recreates stability from the same conditions.**

## Resources

- `references/evidence-attractor.md` — deterministic fresh-retrieval collapse.
- `references/execution.md` — agent/tool control.
- `references/levels.md` — L0–L4 ladder.
- `references/theory.md` — physics-based formulation.
- `assets/l4-prompt-template.txt` — exact-attractor template.
- `scripts/canonical_evidence.py` — canonical evidence/fact hashing helper.
- `scripts/hash_outputs.py` — offline output/hash scorer.
- `scripts/verify_nodrift.py` — Anthropic API battery.
- `scripts/run_battery.sh` — Claude Code CLI battery.
