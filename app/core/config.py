from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BMI Calculator"
    debug: bool = False
    allowed_hosts: List[str] = ["*"]
    cors_origins: List[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
