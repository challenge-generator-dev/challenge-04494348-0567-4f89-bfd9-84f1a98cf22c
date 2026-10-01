from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator, SecretStr
from src.schemas import BaseSchema


class UserBase(BaseSchema):
    """Schema base para usuarios con campos comunes de validación."""
    
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern=r'^[a-zA-Z0-9_-]+$',
        description="Nombre de usuario único"
    )
    email: EmailStr = Field(description="Correo electrónico válido")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Nombre completo del usuario")
    
    @field_validator('username')
    @classmethod
    def username_validator(cls, v: str) -> str:
        if not v:
            raise ValueError("El nombre de usuario no puede estar vacío")
        if len(v) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(v) > 50:
            raise ValueError("El nombre de usuario no puede exceder 50 caracteres")
        return v.strip().lower()


class UserCreate(UserBase):
    """Schema para creación de usuarios con validación de contraseña."""
    
    password: SecretStr = Field(
        min_length=8,
        max_length=100,
        description="Contraseña del usuario"
    )
    role: Optional[str] = Field(default="user", description="Rol del usuario")
    
    @field_validator('password')
    @classmethod
    def password_validator(cls, v: SecretStr) -> str:
        password_value = v.get_secret_value()
        if not password_value:
            raise ValueError("La contraseña no puede estar vacía")
        if len(password_value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not any(c.isupper() for c in password_value):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula")
        if not any(c.islower() for c in password_value):
            raise ValueError("La contraseña debe tener al menos una letra minúscula")
        if not any(c.isdigit() for c in password_value):
            raise ValueError("La contraseña debe tener al menos un número")
        return password_value


class UserUpdate(BaseSchema):
    """Schema para actualización de usuarios con campos opcionales."""
    
    username: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=50,
        pattern=r'^[a-zA-Z0-9_-]+$',
        description="Nuevo nombre de usuario"
    )
    email: Optional[EmailStr] = Field(default=None, description="Nuevo correo electrónico")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Nuevo nombre completo")
    password: Optional[SecretStr] = Field(default=None, min_length=8, max_length=100, description="Nueva contraseña")
    is_active: Optional[bool] = Field(default=None, description="Estado de activación del usuario")
    
    @field_validator('username')
    @classmethod
    def username_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if not v:
                raise ValueError("El nombre de usuario no puede estar vacío")
            if len(v) < 3:
                raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
            if len(v) > 50:
                raise ValueError("El nombre de usuario no puede exceder 50 caracteres")
            return v.strip().lower()
        return v
    
    @field_validator('password')
    @classmethod
    def password_validator(cls, v: Optional[SecretStr]) -> Optional[str]:
        if v is not None:
            password_value = v.get_secret_value()
            if not password_value:
                raise ValueError("La contraseña no puede estar vacía")
            if len(password_value) < 8:
                raise ValueError("La contraseña debe tener al menos 8 caracteres")
            if not any(c.isupper() for c in password_value):
                raise ValueError("La contraseña debe tener al menos una letra mayúscula")
            if not any(c.islower() for c in password_value):
                raise ValueError("La contraseña debe tener al menos una letra minúscula")
            if not any(c.isdigit() for c in password_value):
                raise ValueError("La contraseña debe tener al menos un número")
            return password_value
        return v


class UserResponse(UserBase):
    """Schema para respuesta de usuario sin datos sensibles."""
    
    id: int = Field(description="ID único del usuario")
    role: str = Field(description="Rol del usuario")
    is_active: bool = Field(default=True, description="Estado de activación")
    created_at: datetime = Field(description="Fecha de creación")
    updated_at: Optional[datetime] = Field(default=None, description="Fecha de última actualización")
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "johndoe@example.com",
                "full_name": "John Doe",
                "role": "user",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": None
            }
        }


class Token(BaseSchema):
    """Schema para respuesta de token de acceso."""
    
    access_token: str = Field(description="Token de acceso JWT")
    token_type: str = Field(default="bearer", description="Tipo de token")
    expires_in: Optional[int] = Field(default=1800, description="Tiempo de expiración en segundos")
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 1800
            }
        }


class TokenData(BaseSchema):
    """Schema para datos contenidos en el token JWT."""
    
    username: Optional[str] = Field(default=None, description="Nombre de usuario del token")
    user_id: Optional[int] = Field(default=None, description="ID de usuario del token")
    role: Optional[str] = Field(default=None, description="Rol del usuario del token")
    exp: Optional[datetime] = Field(default=None, description="Fecha de expiración del token")


class UserLogin(BaseSchema):
    """Schema para solicitud de inicio de sesión."""
    
    username: str = Field(min_length=3, max_length=50, description="Nombre de usuario")
    password: SecretStr = Field(min_length=8, max_length=100, description="Contraseña del usuario")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "SecurePass123"
            }
        }


class ErrorResponse(BaseSchema):
    """Schema para respuestas de error genéricas."""
    
    detail: str = Field(description="Mensaje de error detallado")
    error_code: Optional[str] = Field(default=None, description="Código de error específico")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Marca de tiempo del error")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Usuario no encontrado",
                "error_code": "USER_NOT_FOUND",
                "timestamp": "2024-01-01T00:00:00"
            }
        }


class ValidationErrorResponse(BaseSchema):
    """Schema para respuestas de error de validación."""
    
    detail: list = Field(description="Lista de errores de validación")
    error_code: str = Field(default="VALIDATION_ERROR", description="Código de error de validación")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Marca de tiempo del error")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": [
                    {"loc": ["body", "username"], "msg": "El nombre de usuario debe tener al menos 3 caracteres", "type": "value_error"},
                    {"loc": ["body", "email"], "msg": "Correo electrónico inválido", "type": "value_error"}
                ],
                "error_code": "VALIDATION_ERROR",
                "timestamp": "2024-01-01T00:00:00"
            }
        }