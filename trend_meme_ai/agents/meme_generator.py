from __future__ import annotations

from trend_meme_ai.services.meme_service import MemeService


class MemeGeneratorAgent:
    def __init__(self):
        self.meme_service = MemeService()

    def run(self, strategy: dict) -> dict:
        prompt, image_path = self.meme_service.generate_image(
            topic=strategy['topic'],
            format_name=strategy['template_name'],
            humor_style=strategy['humor_style'],
            audience_type=strategy['audience_type'],
        )
        return {**strategy, 'image_path': image_path, 'generation_prompt': prompt}
