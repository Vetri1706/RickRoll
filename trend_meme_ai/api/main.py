from fastapi import FastAPI

from trend_meme_ai.api.routes import router
from trend_meme_ai.config.settings import settings
from trend_meme_ai.database.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.include_router(router)
