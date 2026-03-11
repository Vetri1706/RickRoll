from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = 'TrendMemeAI'
    environment: str = 'development'

    postgres_dsn: str = 'postgresql+psycopg2://postgres:postgres@db:5432/trend_meme_ai'
    redis_url: str = 'redis://redis:6379/0'
    chroma_persist_dir: str = './chroma_data'

    twitter_bearer_token: str = ''
    twitter_api_key: str = ''
    twitter_api_secret: str = ''
    twitter_access_token: str = ''
    twitter_access_secret: str = ''

    reddit_client_id: str = ''
    reddit_client_secret: str = ''
    reddit_user_agent: str = 'TrendMemeAI/1.0'

    google_trends_geo: str = 'US'

    stability_api_key: str = ''
    sdxl_model: str = 'stable-diffusion-xl-1024-v1-0'

    instagram_access_token: str = ''
    instagram_business_account_id: str = ''

    tiktok_access_token: str = ''

    openai_api_key: str = ''

    celery_broker_url: str = 'redis://redis:6379/1'
    celery_result_backend: str = 'redis://redis:6379/2'


settings = Settings()
