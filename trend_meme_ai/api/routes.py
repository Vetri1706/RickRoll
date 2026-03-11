from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from trend_meme_ai.database.db import get_db
from trend_meme_ai.database.models import Engagement, Trend
from trend_meme_ai.scheduler.celery_worker import run_pipeline


router = APIRouter()


@router.post('/start-agent')
def start_agent() -> dict:
    task = run_pipeline.delay()
    return {'status': 'started', 'task_id': task.id}


@router.post('/stop-agent')
def stop_agent(task_id: str) -> dict:
    run_pipeline.app.control.revoke(task_id, terminate=True)
    return {'status': 'stopped', 'task_id': task_id}


@router.get('/trends')
def list_trends(limit: int = 20, db: Session = Depends(get_db)) -> list[dict]:
    rows = db.query(Trend).order_by(desc(Trend.created_at)).limit(limit).all()
    return [
        {
            'id': row.id,
            'topic': row.topic,
            'source': row.source,
            'trend_score': row.trend_score,
            'created_at': row.created_at.isoformat(),
        }
        for row in rows
    ]


@router.get('/analytics')
def analytics(db: Session = Depends(get_db)) -> dict:
    total_trends = db.query(func.count(Trend.id)).scalar() or 0
    avg_score = db.query(func.avg(Trend.trend_score)).scalar() or 0.0
    top_engagement = db.query(Engagement).order_by(desc(Engagement.virality_score)).first()
    return {
        'total_trends': total_trends,
        'avg_trend_score': float(avg_score),
        'top_engagement': {
            'platform': top_engagement.platform,
            'virality_score': top_engagement.virality_score,
        }
        if top_engagement
        else None,
    }
