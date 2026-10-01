"""Módulo de configuración de la aplicación.

Contiene la configuración centralizada basada en variables de entorno
y constantes de la aplicación.
"""

from typing import Optional, List
import os

from .settings import settings, Settings

# Constantes de la aplicación
APP_NAME = "User Management API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "API REST para gestión de usuarios con autenticación JWT"
APP_AUTHOR = "Pragma Team"

# URLs y endpoints
API_PREFIX = "/api/v1"
DOCS_URL = "/docs"
REDOC_URL = "/redoc"
OPENAPI_URL = "/openapi.json"

# Configuración de CORS
ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
ALLOWED_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE", "PATCH"]
ALLOWED_HEADERS: List[str] = ["*"]

# Configuración de paginación
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# Configuración de rate limiting
RATE_LIMIT_PER_MINUTE = 60
RATE_LIMIT_PER_HOUR = 1000

# Configuración de seguridad
PASSWORD_MIN_LENGTH = 8
PASSWORD_REQUIRE_UPPERCASE = True
PASSWORD_REQUIRE_LOWERCASE = True
PASSWORD_REQUIRE_DIGITS = True
PASSWORD_REQUIRE_SPECIAL = False

# Tiempos de sesión
SESSION_TIMEOUT_MINUTES = 30
REFRESH_TOKEN_DAYS = 7

# Configuración de base de datos
DB_POOL_SIZE = 5
DB_MAX_OVERFLOW = 10
DB_POOL_TIMEOUT = 30
DB_POOL_RECYCLE = 3600


def get_database_url() -> str:
    """Obtiene la URL de la base de datos desde la configuración.
    
    Returns:
        URL de conexión a la base de datos.
    """
    return settings.DATABASE_URL


def get_jwt_secret() -> str:
    """Obtiene la clave secreta para JWT desde la configuración.
    
    Returns:
        Clave secreta JWT.
    """
    return settings.JWT_SECRET.get_secret_value()


def get_jwt_algorithm() -> str:
    """Obtiene el algoritmo JWT configurado.
    
    Returns:
        Algoritmo JWT (HS256 por defecto).
    """
    return "HS256"


def is_development() -> bool:
    """Verifica si la aplicación está en modo desarrollo.
    
    Returns:
        True si está en desarrollo.
    """
    return os.getenv("ENVIRONMENT", "development").lower() == "development"


def is_production() -> bool:
    """Verifica si la aplicación está en modo producción.
    
    Returns:
        True si está en producción.
    """
    return os.getenv("ENVIRONMENT", "development").lower() == "production"


def is_debug_enabled() -> bool:
    """Verifica si el modo debug está habilitado.
    
    Returns:
        True si debug está habilitado.
    """
    return settings.DEBUG


def get_cors_origins() -> List[str]:
    """Obtiene los orígenes permitidos para CORS.
    
    Returns:
        Lista de orígenes permitidos.
    """
    return ALLOWED_ORIGINS


def get_allowed_methods() -> List[str]:
    """Obtiene los métodos HTTP permitidos.
    
    Returns:
        Lista de métodos permitidos.
    """
    return ALLOWED_METHODS


def get_allowed_headers() -> List[str]:
    """Obtiene las cabeceras permitidas.
    
    Returns:
        Lista de cabeceras permitidas.
    """
    return ALLOWED_HEADERS


__all__ = [
    "settings",
    "Settings",
    "APP_NAME",
    "APP_VERSION",
    "APP_DESCRIPTION",
    "APP_AUTHOR",
    "API_PREFIX",
    "DOCS_URL",
    "REDOC_URL",
    "OPENAPI_URL",
    "ALLOWED_ORIGINS",
    "ALLOWED_METHODS",
    "ALLOWED_HEADERS",
    "DEFAULT_PAGE_SIZE",
    "MAX_PAGE_SIZE",
    "RATE_LIMIT_PER_MINUTE",
    "RATE_LIMIT_PER_HOUR",
    "PASSWORD_MIN_LENGTH",
    "PASSWORD_REQUIRE_UPPERCASE",
    "PASSWORD_REQUIRE_LOWERCASE",
    "PASSWORD_REQUIRE_DIGITS",
    "PASSWORD_REQUIRE_SPECIAL",
    "SESSION_TIMEOUT_MINUTES",
    "REFRESH_TOKEN_DAYS",
    "DB_POOL_SIZE",
    "DB_MAX_OVERFLOW",
    "DB_POOL_TIMEOUT",
    "DB_POOL_RECYCLE",
    "get_database_url",
    "get_jwt_secret",
    "get_jwt_algorithm",
    "is_development",
    "is_production",
    "is_debug_enabled",
    "get_cors_origins",
    "get_allowed_methods",
    "get_allowed_headers",
]