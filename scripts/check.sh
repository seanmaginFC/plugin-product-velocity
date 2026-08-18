#!/usr/bin/env bash
#
# Runs the exact same checks .github/workflows/plugin-checks.yml runs in CI,
# so a plugin editor gets Layer 1 + Layer 2 feedback before ever committing,
# not after pushing. CI stays in place as the last-resort backstop for
# anyone who skips this or doesn't have the hook installed.
#
# Usage: scripts/check.sh
# One-time setup to run this automatically before every commit:
#   git config core.hooksPath .githooks

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

status=0

echo "== Layer 2 — convention linter =="
python3 scripts/lint_plugin.py
if [ $? -ne 0 ]; then
  status=1
fi

echo ""
echo "== Layer 1 — structural validation =="
if command -v claude >/dev/null 2>&1; then
  claude plugin validate . --strict
  if [ $? -ne 0 ]; then
    status=1
  fi
else
  echo "WARN: 'claude' CLI not found on PATH — skipping this layer locally."
  echo "      Install it with: npm install -g @anthropic-ai/claude-code"
  echo "      CI will still run this check when you push."
fi

echo ""
if [ $status -eq 0 ]; then
  echo "All local checks passed."
else
  echo "One or more checks failed — fix before committing."
fi

exit $status
