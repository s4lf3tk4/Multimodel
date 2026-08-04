from pydantic_settings import BaseSettings
from pydantic import Field, field_validator
from typing import Optional

class Settings(BaseSettings):
    chatanywhere_api_key: str = Field(
            ...,
            alias="CHATANYWHERE_API_KEY",
            description="API-ключ для ChatAnywhere"
    )
    base_url: str = Field(
        "https://api.chatanywhere.tech/v1",
        alias="BASE_URL",
        description="Базовый URL для ChatAnywhere"
        )
    debug: bool = Field(
        False,
        alias="DEBUG",
        description="Режим отладки"
        )
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True

settings = Settings()
