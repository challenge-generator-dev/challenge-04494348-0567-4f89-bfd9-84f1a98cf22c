from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Optional
from src.schemas import Token, UserLogin, UserCreate, UserResponse, ErrorResponse
from src.services.auth_service import AuthService
from src.services.user_service import UserService
from src.models import User, UserRole, handle_sqlalchemy_exception
from src.config import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, responses={
    400: {"model": ErrorResponse, "description": "Usuario ya existe o datos inválidos"}
})
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Registra un nuevo usuario en el sistema."""
    pass


@router.post("/login", response_model=Token, responses={
    401: {"model": ErrorResponse, "description": "Credenciales incorrectas"}
})
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Autentica un usuario y retorna un token JWT."""
    pass


@router.post("/logout", status_code=status.HTTP_200_OK, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"}
})
def logout(current_user: User = Depends(get_db)):
    """Cierra la sesión del usuario actual."""
    pass


@router.post("/refresh", response_model=Token, responses={
    401: {"model": ErrorResponse, "description": "Token inválido o expirado"}
})
def refresh_token(
    current_user: User = Depends(get_db)
):
    """Refresca el token JWT del usuario actual."""
    pass


@router.get("/me", response_model=UserResponse, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"}
})
def get_current_user(current_user: User = Depends(get_db)):
    """Retorna la información del usuario autenticado actualmente."""
    pass


from .user_service import UserService
from .auth_service import AuthService

__all__ = ["UserService", "AuthService"]