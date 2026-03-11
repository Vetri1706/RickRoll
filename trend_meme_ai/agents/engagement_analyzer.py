from __future__ import annotations

import random


class EngagementAnalyzerAgent:
    def run(self, posted_content: dict) -> dict:
        metrics = {}
        for platform in posted_content.get('posted_to', {}).keys():
            likes = random.randint(10, 5000)
            comments = random.randint(1, 800)
            shares = random.randint(1, 1000)
            views = random.randint(100, 100000)
            virality_score = round((likes * 0.2 + comments * 0.3 + shares * 0.5) / max(views, 1), 4)
            metrics[platform] = {
                'likes': likes,
                'comments': comments,
                'shares': shares,
                'views': views,
                'virality_score': virality_score,
            }
        return {**posted_content, 'engagement': metrics}
