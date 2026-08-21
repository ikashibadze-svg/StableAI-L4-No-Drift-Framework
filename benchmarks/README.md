# Benchmarks

Public benchmark claims should include enough information to reproduce and audit the result.

Recommended per benchmark:

```text
benchmarks/<date>-<model>/
├── report.json
├── execution_summary.json
├── environment.json
├── target.json
├── prompt.txt
└── outputs/
    ├── run_01.txt
    └── ...
```

`environment.json` should record the exact model identifier, date, SDK/CLI version, temperature, max tokens, system prompt condition, tool configuration, and any other material runtime settings.

The repository currently includes `reported-results.json`, a summary transcribed from prior StableAI experiments. Because raw historical outputs/hashes are not included here, those entries are explicitly labeled `reported` rather than `reproduced`.
