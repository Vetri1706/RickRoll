from __future__ import annotations

from trend_meme_ai.services.posting_service import PostingService


class PostingAgent:
    def __init__(self):
        self.posting_service = PostingService()

    def run(self, approved_content: dict) -> dict:
        if not approved_content.get('is_approved'):
            return {**approved_content, 'posted_to': {}}

        posted = self.posting_service.post_all(
            image_path=approved_content['image_path'],
            caption=approved_content['caption'],
        )
        return {**approved_content, 'posted_to': posted}
