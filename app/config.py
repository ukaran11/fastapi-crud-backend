# app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"  # Database connection string (SQLite here)
    SECRET_KEY: str = "your_secret_key_here"    # Secret key for JWT encoding
    ALGORITHM: str = "HS256"                    # Algorithm used for JWT tokens
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30       # Token expiry time in minutes

    class Config:
        env_file = ".env"  # Optionally load environment variables from a .env file

settings = Settings()  # Instantiate settings to be imported elsewhere
