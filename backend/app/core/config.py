from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Booking Platform"

    DATABASE_URL: str
    REDIS_URL: str

    JWT_SECRET: str
    JWT_REFRESH_SECRET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()