from __future__ import annotations

from datetime import datetime


class PostingService:
    def post_to_twitter(self, image_path: str, caption: str) -> dict:
        return {'platform': 'twitter', 'post_id': f'tw_{int(datetime.utcnow().timestamp())}', 'image_path': image_path, 'caption': caption}

    def post_to_instagram(self, image_path: str, caption: str) -> dict:
        return {'platform': 'instagram', 'post_id': f'ig_{int(datetime.utcnow().timestamp())}', 'image_path': image_path, 'caption': caption}

    def post_to_tiktok(self, image_path: str, caption: str) -> dict:
        return {'platform': 'tiktok', 'post_id': f'tt_{int(datetime.utcnow().timestamp())}', 'image_path': image_path, 'caption': caption}

    def post_all(self, image_path: str, caption: str) -> dict:
        return {
            'twitter': self.post_to_twitter(image_path, caption),
            'instagram': self.post_to_instagram(image_path, caption),
            'tiktok': self.post_to_tiktok(image_path, caption),
        }
