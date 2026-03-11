from sqlalchemy.orm import Session

from trend_meme_ai.services.trend_service import TrendService


class TrendHunterAgent:
    def __init__(self):
        self.trend_service = TrendService()

    def run(self, db: Session):
        trends = self.trend_service.collect_all()
        return self.trend_service.persist_trends(db, trends)
