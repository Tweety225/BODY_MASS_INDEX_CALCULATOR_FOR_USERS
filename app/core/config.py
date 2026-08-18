from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "BMI Calculator"
    debug: bool = False
    allowed_hosts: List[str] = ["*"]
    cors_origins: List[str] = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
