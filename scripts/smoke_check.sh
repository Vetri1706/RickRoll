#!/usr/bin/env bash
set -euo pipefail

echo "[smoke] TrendMemeAI environment check"

if command -v docker >/dev/null 2>&1; then
  echo "[ok] docker found: $(docker --version)"
else
  echo "[warn] docker not found; docker-compose stack cannot be started in this environment"
fi

python - <<'PY'
import importlib.util
mods = [
    'fastapi',
    'uvicorn',
    'sqlalchemy',
    'pydantic_settings',
    'celery',
    'redis',
    'PIL',
]
missing = [m for m in mods if importlib.util.find_spec(m) is None]
if missing:
    print('[warn] missing python modules:', ', '.join(missing))
else:
    print('[ok] required python modules are importable')
PY

echo "[smoke] done"
