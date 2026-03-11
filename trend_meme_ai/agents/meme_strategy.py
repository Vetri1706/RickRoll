from __future__ import annotations

import random

from trend_meme_ai.utils.helpers import MEME_FORMATS


class MemeStrategyAgent:
    def run(self, context: dict) -> dict:
        humor_style = random.choice(['sarcastic', 'absurdist', 'wholesome', 'self-deprecating'])
        audience_type = random.choice(['gen-z', 'gamers', 'developers', 'general'])
        template = random.choice(MEME_FORMATS)
        return {
            **context,
            'humor_style': humor_style,
            'audience_type': audience_type,
            'template_name': template,
        }
