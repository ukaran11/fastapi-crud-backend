# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"  # Connection string for SQLite
    SECRET_KEY: str = "your_secret_key_here"    # Secret key for JWT encoding
    ALGORITHM: str = "HS256"                    # JWT encryption algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30       # Access token expiry in minutes

    class Config:
        env_file = ".env"  # Optionally load environment variables from a .env file

settings = Settings()  # Create a settings instance to be imported elsewhere
