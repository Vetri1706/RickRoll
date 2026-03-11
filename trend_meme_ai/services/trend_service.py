from __future__ import annotations

import random
from datetime import datetime

from sqlalchemy.orm import Session

from trend_meme_ai.database.models import Trend
from trend_meme_ai.utils.helpers import calculate_trend_score


class TrendService:
    def fetch_twitter_trends(self) -> list[dict]:
        return [
            {'topic': 'AI glasses', 'source': 'twitter', 'mentions': random.randint(1000, 10000)},
            {'topic': 'New game patch', 'source': 'twitter', 'mentions': random.randint(1000, 10000)},
        ]

    def fetch_reddit_trends(self) -> list[dict]:
        return [
            {'topic': 'Remote work memes', 'source': 'reddit', 'mentions': random.randint(500, 7000)},
        ]

    def fetch_google_trends(self) -> list[dict]:
        return [
            {'topic': 'Robot assistant', 'source': 'google_trends', 'mentions': random.randint(500, 9000)},
        ]

    def collect_all(self) -> list[dict]:
        return self.fetch_twitter_trends() + self.fetch_reddit_trends() + self.fetch_google_trends()

    def persist_trends(self, db: Session, trends: list[dict]) -> list[Trend]:
        rows: list[Trend] = []
        now = datetime.utcnow()
        for t in trends:
            velocity = min(1.0, t['mentions'] / 10000)
            sentiment = random.uniform(0.5, 1.0)
            meme_potential = random.uniform(0.4, 1.0)
            relevance = random.uniform(0.4, 1.0)
            score = calculate_trend_score(velocity, sentiment, meme_potential, relevance)
            row = Trend(
                source=t['source'],
                topic=t['topic'],
                velocity=velocity,
                sentiment_strength=sentiment,
                meme_potential=meme_potential,
                audience_relevance=relevance,
                trend_score=score,
                metadata_json={'mentions': t['mentions'], 'captured_at': now.isoformat()},
            )
            db.add(row)
            rows.append(row)
        db.commit()
        for row in rows:
            db.refresh(row)
        return rows
