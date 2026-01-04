import os
from typing import Literal
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Tell pydantic to read from .env by default
    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE", ".env.local"),
        env_file_encoding="utf-8"
    )

    # App/Environment
    app_env: Literal["dev", "staging", "prod"] = Field(default="dev", alias="APP_ENV")

    # Postgres
    postgres_host: str =  Field(default="db", alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, alias="POSTGRES_PORT")
    # Required without default values
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: SecretStr = Field(alias="POSTGRES_PASSWORD")  # Use SecretStr for hiding content when logged

    # Redis
    redis_host: str = Field(default="redis", alias="REDIS_HOST")
    redis_port: int = Field(6379, alias="REDIS_PORT")

    # APIs
    weather_api_key: SecretStr = Field(
        default=SecretStr("changeme"),
        alias=("WEATHER_API_KEY")
    )

    astro_api_key: SecretStr = Field(
        default=SecretStr("changeme"),
        alias="ASTRO_API_KEY"
    )

    app_name: str = "FishRadar"
    debug: bool = False

    @property
    def db_url(self) -> str:
        password = self.postgres_password.get_secret_value()
        return (
            f"postgresql+psycopg://{self.postgres_user}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/0"

    @property
    def full_app_name(self):
        return f"{self.app_name}_{self.app_env}"


config = Config()
