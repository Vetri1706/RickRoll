from __future__ import annotations

import random


class ContextAnalyzerAgent:
    def run(self, trend) -> dict:
        sentiment_label = random.choice(['positive', 'neutral', 'mixed'])
        category = random.choice(['tech', 'gaming', 'culture', 'work', 'news'])
        meme_worthy = trend.meme_potential > 0.5 and trend.sentiment_strength > 0.4
        return {
            'trend_id': trend.id,
            'topic': trend.topic,
            'sentiment': sentiment_label,
            'category': category,
            'meme_worthy': meme_worthy,
        }
