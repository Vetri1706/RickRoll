from __future__ import annotations

from pathlib import Path

from PIL import Image

from trend_meme_ai.utils.helpers import ensure_dir, meme_generation_prompt, overlay_text


class MemeService:
    def __init__(self, output_dir: str = 'trend_meme_ai/generated_memes'):
        self.output_dir = ensure_dir(output_dir)

    def generate_image(self, topic: str, format_name: str, humor_style: str, audience_type: str) -> tuple[str, str]:
        prompt = meme_generation_prompt(topic, format_name, humor_style, audience_type)
        filename = f"{topic.replace(' ', '_').lower()}_{format_name.replace(' ', '_').lower()}.png"
        image_path = Path(self.output_dir) / filename

        # placeholder for Stability AI SDXL generation output
        Image.new('RGB', (1024, 1024), color=(22, 22, 22)).save(image_path)

        captioned_path = overlay_text(str(image_path), top_text=topic, bottom_text=humor_style)
        return prompt, captioned_path
