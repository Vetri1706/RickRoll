from celery import Celery

from trend_meme_ai.config.settings import settings
from trend_meme_ai.database.db import SessionLocal
from trend_meme_ai.workflows.agent_graph import TrendMemeGraph


celery_app = Celery('trend_meme_ai', broker=settings.celery_broker_url, backend=settings.celery_result_backend)


@celery_app.task(name='trend_meme_ai.run_pipeline')
def run_pipeline():
    db = SessionLocal()
    try:
        graph = TrendMemeGraph()
        return graph.run_cycle(db)
    finally:
        db.close()
