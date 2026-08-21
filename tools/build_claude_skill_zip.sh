#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/.claude/skills/stableai-l4-no-drift"
OUT="${1:-$ROOT/stableai-l4-no-drift-claude-ready.zip}"

if [ ! -f "$SKILL/SKILL.md" ]; then
  echo "SKILL.md not found at $SKILL" >&2
  exit 1
fi

rm -f "$OUT"
(
  cd "$SKILL"
  zip -qr "$OUT" .
)

echo "Created $OUT"
unzip -l "$OUT"
