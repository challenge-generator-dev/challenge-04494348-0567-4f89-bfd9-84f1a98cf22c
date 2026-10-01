"""Utilidades de seguridad para autenticación y manejo de contraseñas.

Este módulo proporciona funciones para:
- Hashing y verificación de contraseñas.
- Generación y verificación de tokens JWT.

SUPERFICIE DE PRÁCTICA: Este archivo es el ejercicio a completar.
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any

# TODO: Implementar las funciones de este módulo
# El participante debe completar la lógica de seguridad


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Genera un token JWT de acceso.
    
    Args:
        data: Diccionario con los datos a incluir en el token.
        expires_delta: Tiempo de expiración opcional.
        
    Returns:
        Token JWT como cadena.
    """
    raise NotImplementedError("Implementar create_access_token")


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """Verifica y decodifica un token JWT.
    
    Args:
        token: Token JWT a verificar.
        
    Returns:
        Datos decodificados si el token es válido, None si no lo es.
    """
    raise NotImplementedError("Implementar verify_token")


def get_password_hash(password: str) -> str:
    """Genera el hash de una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano.
        
    Returns:
        Hash de la contraseña.
    """
    raise NotImplementedError("Implementar get_password_hash")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra su hash.
    
    Args:
        plain_password: Contraseña en texto plano.
        hashed_password: Hash de la contraseña almacenado.
        
    Returns:
        True si la contraseña es correcta, False en caso contrario.
    """
    raise NotImplementedError("Implementar verify_password")