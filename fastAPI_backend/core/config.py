from pathlib import Path
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    ENVIRONMENT: str = "dev"

    # General
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Food Delivery"
    ALLOW_ORIGINS: list[str] = ["*"]

    ROOT_DIR: Path = Path(__file__).parent.parent.parent

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Setting()
