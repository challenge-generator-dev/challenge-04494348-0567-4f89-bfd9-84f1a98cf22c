"""Módulo de utilidades de la aplicación.

Este módulo contiene funciones helper para seguridad, manejo de fechas,
y otras operaciones comunes usadas en toda la aplicación.
"""

from datetime import datetime, timedelta
from typing import Optional, Any
import re

from .security import (
    create_access_token,
    verify_token,
    get_password_hash,
    verify_password
)

# Constantes de tiempo para tokens JWT
TOKEN_EXPIRE_MINUTES = 30
TOKEN_EXPIRE_HOURS = 24
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Constantes de validación
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 50
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def get_token_expiration(expires_delta: Optional[timedelta] = None) -> datetime:
    """Calcula la fecha de expiración de un token.
    
    Args:
        expires_delta: Delta de tiempo personalizado. Si es None, usa 30 minutos.
        
    Returns:
        datetime con la fecha de expiración.
    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return datetime.utcnow() + expires_delta


def is_valid_email(email: str) -> bool:
    """Valida que un email tenga el formato correcto.
    
    Args:
        email: Cadena con el email a validar.
        
    Returns:
        True si el email es válido, False en caso contrario.
    """
    return bool(re.match(EMAIL_PATTERN, email))


def is_valid_username(username: str) -> bool:
    """Valida que un nombre de usuario cumpla las reglas de longitud.
    
    Args:
        username: Cadena con el nombre de usuario.
        
    Returns:
        True si el nombre de usuario es válido.
    """
    if not username:
        return False
    length = len(username)
    return MIN_USERNAME_LENGTH <= length <= MAX_USERNAME_LENGTH


def is_valid_password(password: str) -> bool:
    """Valida que una contraseña cumpla los requisitos mínimos de seguridad.
    
    Args:
        password: Cadena con la contraseña a validar.
        
    Returns:
        True si la contraseña es válida.
    """
    if not password:
        return False
    length = len(password)
    if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
        return False
    return True


def sanitize_string(value: str, max_length: Optional[int] = None) -> str:
    """Limpia una cadena de caracteres potencialmente peligrosos.
    
    Args:
        value: Cadena a sanitizar.
        max_length: Longitud máxima opcional.
        
    Returns:
        Cadena sanitizada.
    """
    if not value:
        return ""
    sanitized = value.strip()
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    return sanitized


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formatea un datetime como cadena legible.
    
    Args:
        dt: Objeto datetime a formatear.
        format_str: Cadena de formato strftime.
        
    Returns:
        Cadena formateada.
    """
    return dt.strftime(format_str)


__all__ = [
    "create_access_token",
    "verify_token",
    "get_password_hash",
    "verify_password",
    "TOKEN_EXPIRE_MINUTES",
    "TOKEN_EXPIRE_HOURS",
    "REFRESH_TOKEN_EXPIRE_DAYS",
    "MIN_PASSWORD_LENGTH",
    "MAX_PASSWORD_LENGTH",
    "MIN_USERNAME_LENGTH",
    "MAX_USERNAME_LENGTH",
    "get_token_expiration",
    "is_valid_email",
    "is_valid_username",
    "is_valid_password",
    "sanitize_string",
    "format_datetime",
]