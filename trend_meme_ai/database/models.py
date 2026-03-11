from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from trend_meme_ai.database.db import Base


class Trend(Base):
    __tablename__ = 'trends'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source: Mapped[str] = mapped_column(String(50), index=True)
    topic: Mapped[str] = mapped_column(String(300), index=True)
    velocity: Mapped[float] = mapped_column(Float, default=0.0)
    sentiment_strength: Mapped[float] = mapped_column(Float, default=0.0)
    meme_potential: Mapped[float] = mapped_column(Float, default=0.0)
    audience_relevance: Mapped[float] = mapped_column(Float, default=0.0)
    trend_score: Mapped[float] = mapped_column(Float, default=0.0)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    memes = relationship('MemePost', back_populates='trend')


class MemePost(Base):
    __tablename__ = 'meme_posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    trend_id: Mapped[int] = mapped_column(ForeignKey('trends.id'))
    template_name: Mapped[str] = mapped_column(String(100))
    humor_style: Mapped[str] = mapped_column(String(100))
    audience_type: Mapped[str] = mapped_column(String(100))
    image_path: Mapped[str] = mapped_column(String(500))
    caption: Mapped[str] = mapped_column(Text)
    hashtags: Mapped[list] = mapped_column(JSON, default=list)
    is_approved: Mapped[bool] = mapped_column(Boolean, default=False)
    posted_to: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    trend = relationship('Trend', back_populates='memes')
    engagements = relationship('Engagement', back_populates='meme')


class Engagement(Base):
    __tablename__ = 'engagements'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    meme_id: Mapped[int] = mapped_column(ForeignKey('meme_posts.id'), index=True)
    platform: Mapped[str] = mapped_column(String(50), index=True)
    likes: Mapped[int] = mapped_column(Integer, default=0)
    comments: Mapped[int] = mapped_column(Integer, default=0)
    shares: Mapped[int] = mapped_column(Integer, default=0)
    views: Mapped[int] = mapped_column(Integer, default=0)
    virality_score: Mapped[float] = mapped_column(Float, default=0.0)
    captured_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    meme = relationship('MemePost', back_populates='engagements')
