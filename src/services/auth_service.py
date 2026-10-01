"""Servicio de autenticación JWT.

SUPERFICIE DE PRÁCTICA - Stub para que el estudiante implemente.
"""

from typing import Optional
from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.config.settings import Settings, get_settings
from src.schemas.user import TokenData
from src.models.user import User
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class AuthService:
    """Servicio para autenticación y autorización mediante JWT.
    
    Este es un STUB que el estudiante debe completar.
    """
    
    def __init__(self, settings: Settings):
        self.settings = settings
    
    def authenticate_user(self, username: str, password: str, db: Session) -> Optional[User]:
        """Autentica un usuario con username y contraseña.
        
        TODO: Implementar validación de credenciales.
        """
        pass
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Crea un token JWT de acceso.
        
        TODO: Implementar generación de token JWT.
        """
        pass
    
    def verify_token(self, token: str) -> Optional[TokenData]:
        """Verifica y decodifica un token JWT.
        
        TODO: Implementar verificación de token.
        """
        pass
    
    def get_current_user(self, token: str, db: Session) -> User:
        """Obtiene el usuario actual desde el token JWT.
        
        TODO: Implementar extracción de usuario del token.
        """
        pass
    
    def get_current_active_user(self, current_user: User = Depends(lambda: None)) -> User:
        """Obtiene el usuario actual verificado.
        
        TODO: Implementar verificación de usuario activo.
        """
        pass