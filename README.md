# TrendMemeAI

## Quick local checks

Run:

```bash
./scripts/smoke_check.sh
```

This validates whether Docker and required Python modules are available before starting:

- API: `uvicorn trend_meme_ai.api.main:app --host 0.0.0.0 --port 8000`
- Worker: `celery -A trend_meme_ai.scheduler.celery_worker.celery_app worker --loglevel=info`
- Full stack: `docker compose up --build`
