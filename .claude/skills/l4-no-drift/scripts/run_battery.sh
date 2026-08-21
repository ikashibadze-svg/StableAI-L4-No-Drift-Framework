#!/usr/bin/env bash
# StableAI L4 battery via Claude Code CLI.
# Usage: run_battery.sh <model> <prompt-file> <target-file> [runs=20] [outdir=battery_out]
set -u

if [ "$#" -lt 3 ]; then
  echo "usage: $0 <model> <prompt-file> <target-file> [runs=20] [outdir=battery_out]" >&2
  exit 2
fi

m=$1; p=$2; target=$3; n=${4:-20}; d=${5:-battery_out}
here="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$d"; mkdir -p "$d"
sp=""; [ -n "${SYSTEM_PROMPT_FILE:-}" ] && sp="$(cat "$SYSTEM_PROMPT_FILE")"

one() {
  i=$1
  for t in 1 2 3; do
    if timeout 120 claude -p --model "$m" --output-format json --tools "" --system-prompt "$sp" < "$p" > "$d/raw_$i.json" 2>"$d/error_$i.log"; then
      if grep -q '"is_error":false' "$d/raw_$i.json" && ! grep -q '"result":"API Error' "$d/raw_$i.json"; then
        return 0
      fi
    fi
    sleep $((t*2))
  done
  return 1
}

for i in $(seq -w 1 "$n"); do
  one "$i" &
  if (( 10#$i % 3 == 0 )); then wait || true; fi
done
wait || true

python3 - "$d" "$n" <<'PY'
import glob, json, os, sys

d=sys.argv[1]; requested=int(sys.argv[2]); completed=0; failures=[]
for f in sorted(glob.glob(os.path.join(d, "raw_*.json"))):
    run=os.path.basename(f).split("_")[1].split(".")[0]
    try:
        j=json.load(open(f, encoding="utf-8"))
    except Exception:
        failures.append(run); continue
    result=str(j.get("result", ""))
    if j.get("is_error") or result.startswith("API Error") or not result:
        failures.append(run); continue
    open(os.path.join(d, f"run_{run}.txt"), "w", encoding="utf-8").write(result)
    usage=j.get("usage", {}) or {}
    meta={"output_tokens": usage.get("output_tokens"), "duration_api_ms": j.get("duration_api_ms")}
    open(os.path.join(d, f"meta_{run}.json"), "w", encoding="utf-8").write(json.dumps(meta))
    completed += 1
summary={
    "attempted_runs": requested,
    "completed_runs": completed,
    "transport_or_runtime_errors": requested-completed,
    "failed_run_ids": failures,
}
open(os.path.join(d, "execution_summary.json"), "w", encoding="utf-8").write(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
PY

mapfile -t runs < <(find "$d" -maxdepth 1 -name 'run_*.txt' -type f | sort)
if [ "${#runs[@]}" -eq 0 ]; then
  echo '{"l4_success":false,"error":"no completed outputs"}' | tee "$d/report.json"
  exit 1
fi

python3 "$here/hash_outputs.py" --target "$target" --required-runs "$n" "${runs[@]}" | tee "$d/report.json"
score_status=${PIPESTATUS[0]}

python3 - "$d" <<'PY'
import glob,json,statistics,sys
m=[]
for f in glob.glob(sys.argv[1]+"/meta_*.json"):
    try: m.append(json.load(open(f)))
    except Exception: pass
outs=[x.get("output_tokens") for x in m if isinstance(x.get("output_tokens"),(int,float))]
ms=[x.get("duration_api_ms") for x in m if isinstance(x.get("duration_api_ms"),(int,float))]
if outs: print("avg_output_tokens", round(statistics.mean(outs),1))
if ms: print("avg_latency_s", round(statistics.mean(ms)/1000,2))
PY

exit "$score_status"
