from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Todo API"

    class Config:
        env_file = ".env"