#!/usr/bin/env bash
# Backtest-only runner: strips broker/API secrets from the environment.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for v in $(env | cut -d= -f1); do
  case "$v" in
    ALPACA_*|KALSHI_*|FINNHUB_*|FMP_*|APCA_*|*_API_KEY|*_API_KEY_*|*_SECRET*|*_TOKEN|*_KEY) unset "$v" ;;
  esac
done
export NAUTILUS_BACKTEST_ONLY=1
exec "$HERE/.venv/bin/python" "$@"
