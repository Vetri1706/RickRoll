from __future__ import annotations


class LearningAgent:
    def run(self, analyzed_content: dict) -> dict:
        engagement = analyzed_content.get('engagement', {})
        best_platform = None
        best_score = -1.0
        for platform, stats in engagement.items():
            if stats['virality_score'] > best_score:
                best_score = stats['virality_score']
                best_platform = platform

        recommendation = {
            'best_platform': best_platform,
            'best_virality_score': best_score,
            'next_humor_bias': analyzed_content.get('humor_style', 'sarcastic'),
            'next_template_bias': analyzed_content.get('template_name', 'Reaction meme'),
        }
        return {**analyzed_content, 'learning': recommendation}
