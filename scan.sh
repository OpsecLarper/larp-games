#!/usr/bin/env bash
# scan.sh — LARP Games index generator (bash version)
# Run:  bash scan.sh

GAMES_DIR="$(dirname "$0")/games"
OUT="$GAMES_DIR/index.json"

mkdir -p "$GAMES_DIR"

files=( "$GAMES_DIR"/*.html "$GAMES_DIR"/*.htm )
json="["
first=true

for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  base="$(basename "$f")"
  # strip extension, replace -_ with space, title-case
  name="$(echo "$base" | sed -E 's/\.(html?|htm)$//I; s/[-_]+/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); print}')"
  $first || json+=","
  json+="{\"name\":\"$name\",\"file\":\"$base\"}"
  first=false
  echo "  • $name  ($base)"
done

json+="]"
echo "$json" > "$OUT"
echo ""
echo "Wrote $OUT"
