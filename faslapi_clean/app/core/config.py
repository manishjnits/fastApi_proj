from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FaslaAPI"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"


settings = Settings()
