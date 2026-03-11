from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


MEME_FORMATS = [
    'Drake meme',
    'Distracted boyfriend',
    'NPC meme',
    'Reaction meme',
    'Gaming meme',
    'Tech meme',
]


def calculate_trend_score(
    trend_velocity: float,
    sentiment_strength: float,
    meme_potential: float,
    audience_relevance: float,
) -> float:
    return round(trend_velocity * sentiment_strength * meme_potential * audience_relevance, 4)


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def overlay_text(image_path: str, top_text: str = '', bottom_text: str = '', out_path: str = '') -> str:
    image = Image.open(image_path).convert('RGB')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    if top_text:
        draw.text((20, 20), top_text, font=font, fill='white')
    if bottom_text:
        draw.text((20, image.height - 40), bottom_text, font=font, fill='white')

    output = out_path or image_path.replace('.png', '_captioned.png')
    image.save(output)
    return output


def meme_generation_prompt(topic: str, format_name: str, humor_style: str, audience_type: str) -> str:
    return (
        f'Create a high-quality meme image in {format_name} format about "{topic}". '
        f'Humor style: {humor_style}. Audience: {audience_type}. '
        'Readable composition, expressive faces, internet-native humor, vibrant contrast.'
    )


def hashtagify(topic: str) -> list[str]:
    base = ''.join(ch for ch in topic.title() if ch.isalnum())
    return [f'#{base}', '#Meme', '#Trending', '#Viral', '#TrendMemeAI']


def safe_json(data: Any) -> dict:
    return data if isinstance(data, dict) else {'value': str(data)}
