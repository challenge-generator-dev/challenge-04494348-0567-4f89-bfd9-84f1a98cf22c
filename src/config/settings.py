from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr, PositiveInt, validator
from typing import Optional


class Settings(BaseSettings):
    # Configuración del servidor
    server_host: str = Field(default="0.0.0.0", env="SERVER_HOST")
    server_port: PositiveInt = Field(default=8000, env="SERVER_PORT")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    # Configuración de la base de datos
    database_url: str = Field(..., env="DATABASE_URL")
    database_pool_size: PositiveInt = Field(default=5, env="DATABASE_POOL_SIZE")
    database_max_overflow: PositiveInt = Field(default=10, env="DATABASE_MAX_OVERFLOW")
    database_pool_timeout: PositiveInt = Field(default=30, env="DATABASE_POOL_TIMEOUT")

    # Configuración de JWT
    jwt_secret_key: SecretStr = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    jwt_access_token_expire_minutes: PositiveInt = Field(default=30, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    jwt_refresh_token_expire_days: PositiveInt = Field(default=7, env="JWT_REFRESH_TOKEN_EXPIRE_DAYS")

    # Configuración de seguridad
    password_hash_rounds: PositiveInt = Field(default=12, env="PASSWORD_HASH_ROUNDS")
    password_min_length: PositiveInt = Field(default=8, env="PASSWORD_MIN_LENGTH")

    # Configuración de CORS
    cors_allow_origins: list[str] = Field(default=["*"], env="CORS_ALLOW_ORIGINS")
    cors_allow_methods: list[str] = Field(default=["*"], env="CORS_ALLOW_METHODS")
    cors_allow_headers: list[str] = Field(default=["*"], env="CORS_ALLOW_HEADERS")

    @validator("database_url")
    def validate_database_url(cls, v: str) -> str:
        if not v.startswith("postgresql://") and not v.startswith("sqlite:///"):
            raise ValueError("DATABASE_URL must start with 'postgresql://' or 'sqlite:///'")
        return v

    @validator("jwt_secret_key")
    def validate_jwt_secret(cls, v: SecretStr) -> SecretStr:
        if len(v.get_secret_value()) < 32:
            raise ValueError("JWT_SECRET_KEY must be at least 32 characters long")
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Instancia global de configuración
settings = Settings()