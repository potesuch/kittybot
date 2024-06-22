from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """
    Класс для хранения настроек бота.

    Attributes:
        bot_token (SecretStr): Токен бота (секретная строка).
        cat_api (str): URL API для получения изображений котов.
        ai_cats (str): URL для получения сгенерированных изображений котов.
        ai_persons (str): URL для получения сгенерированных изображений людей.
        redis_host (str): Хост Redis для хранения состояний бота.
        redis_port (str): Порт Redis.
        redis_db (str): Номер базы данных Redis.
        web_server_host (str): Хост веб-сервера.
        web_server_port (str): Порт веб-сервера.
        ngrok_host (str): Хост ngrok для получения публичного URL.
        ngrok_port (str): Порт ngrok.
        webhook_path (str): Путь вебхука.
        webhook_base_url (str | None, optional): Базовый URL для вебхука.
        model_config (SettingsConfigDict): Конфигурация модели для загрузки настроек из файла .env.
    """
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
    webhook_base_url: str | None = None
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )


config = Settings()
