from __future__ import annotations


class ContentModeratorAgent:
    banned_terms = {'hate', 'violence', 'slur'}

    def run(self, content: dict) -> dict:
        text = (content.get('caption', '') + ' ' + content.get('topic', '')).lower()
        approved = not any(term in text for term in self.banned_terms)
        return {**content, 'is_approved': approved, 'moderation_reason': 'approved' if approved else 'blocked'}
