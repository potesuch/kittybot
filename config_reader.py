from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    cat_api: str
    ai_cats: str
    ai_persons: str
    redis_host: str
    redis_port: str
    redis_db: str
    web_server_host: str
    web_server_port: str
    ngrok_host: str
    ngrok_port: str
    webhook_path: str
    webhook_base_url: str = None
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
