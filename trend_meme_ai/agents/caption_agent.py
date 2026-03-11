from __future__ import annotations

from trend_meme_ai.utils.helpers import hashtagify


class CaptionAgent:
    def run(self, meme_data: dict) -> dict:
        hook = f"POV: {meme_data['topic']} just got too real 😅"
        hashtags = hashtagify(meme_data['topic'])
        caption = f"{hook}\n\n{(' '.join(hashtags))}"
        return {**meme_data, 'caption': caption, 'hashtags': hashtags}
