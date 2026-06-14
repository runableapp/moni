#!/usr/bin/env bash
# Generate static Moni GitHub Pages landing pages (one HTML file per language).
# Manual pages under manual/ are hand-authored; this script only runs build-pages.py.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "build.sh: python3 is required." >&2
  exit 2
fi

python3 "$ROOT/build-pages.py"
python3 "$ROOT/manual_i18n/apply_locales.py"
python3 "$ROOT/manual_i18n/sync_app_terms.py"
python3 "$ROOT/build-manual.py"
