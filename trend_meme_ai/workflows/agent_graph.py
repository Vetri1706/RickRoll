from __future__ import annotations

from sqlalchemy.orm import Session

from trend_meme_ai.agents.caption_agent import CaptionAgent
from trend_meme_ai.agents.context_analyzer import ContextAnalyzerAgent
from trend_meme_ai.agents.engagement_analyzer import EngagementAnalyzerAgent
from trend_meme_ai.agents.learning_agent import LearningAgent
from trend_meme_ai.agents.meme_generator import MemeGeneratorAgent
from trend_meme_ai.agents.meme_strategy import MemeStrategyAgent
from trend_meme_ai.agents.moderator import ContentModeratorAgent
from trend_meme_ai.agents.posting_agent import PostingAgent
from trend_meme_ai.agents.trend_hunter import TrendHunterAgent
from trend_meme_ai.database.models import MemePost


class TrendMemeGraph:
    def __init__(self):
        self.trend_hunter = TrendHunterAgent()
        self.context_analyzer = ContextAnalyzerAgent()
        self.strategy = MemeStrategyAgent()
        self.generator = MemeGeneratorAgent()
        self.captioner = CaptionAgent()
        self.moderator = ContentModeratorAgent()
        self.poster = PostingAgent()
        self.engagement = EngagementAnalyzerAgent()
        self.learning = LearningAgent()

    def run_cycle(self, db: Session) -> list[dict]:
        trends = self.trend_hunter.run(db)
        outputs = []

        for trend in trends:
            context = self.context_analyzer.run(trend)
            if not context['meme_worthy']:
                continue
            strategy = self.strategy.run(context)
            meme = self.generator.run(strategy)
            captioned = self.captioner.run(meme)
            moderated = self.moderator.run(captioned)
            posted = self.poster.run(moderated)
            analyzed = self.engagement.run(posted)
            learned = self.learning.run(analyzed)

            meme_row = MemePost(
                trend_id=trend.id,
                template_name=learned['template_name'],
                humor_style=learned['humor_style'],
                audience_type=learned['audience_type'],
                image_path=learned['image_path'],
                caption=learned['caption'],
                hashtags=learned['hashtags'],
                is_approved=learned['is_approved'],
                posted_to=learned.get('posted_to', {}),
            )
            db.add(meme_row)
            db.commit()
            db.refresh(meme_row)

            outputs.append({'trend_id': trend.id, 'meme_id': meme_row.id, **learned})
        return outputs
