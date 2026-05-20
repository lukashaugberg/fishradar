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

    # MySQL
    mysql_host: str =  Field(default="db", alias="MYSQL_HOST")
    mysql_port: int = Field(default=3306, alias="MYSQL_PORT")
    # Required without default values
    mysql_database: str = Field(alias="MYSQL_DATABASE")
    mysql_user: str = Field(alias="MYSQL_USER")
    mysql_password: SecretStr = Field(alias="MYSQL_PASSWORD")
    mysql_root_password: SecretStr = Field(alias="MYSQL_ROOT_PASSWORD")

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

    jwt_secret_key: SecretStr = Field(alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    jwt_access_token_exp_minutes: int = Field(default=60, alias="JWT_ACCESS_TOKEN_EXP_MINUTES")

    app_name: str = "FishRadar"
    debug: bool = False

    @property
    def db_url(self) -> str:
        password = self.mysql_password.get_secret_value()
        return (
            f"mysql+pymysql://{self.mysql_user}:{password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/0"

    @property
    def full_app_name(self):
        return f"{self.app_name}_{self.app_env}"


config = Config()
