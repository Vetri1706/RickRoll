from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from trend_meme_ai.config.settings import settings


engine = create_engine(settings.postgres_dsn, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
