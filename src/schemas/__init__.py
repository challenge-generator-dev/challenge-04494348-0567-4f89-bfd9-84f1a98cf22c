from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime
from src.models import UserRole, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH
import re

class BaseSchema(BaseModel):
    """Clase base para esquemas con configuración común."""
    class Config:
        from_attributes = True
        str_strip_whitespace = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UserBase(BaseSchema):
    """Esquema base para datos de usuario."""
    username: str = Field(..., min_length=3, max_length=50, example="johndoe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="John Doe")

    @validator('username')
    def username_validator(cls, v):
        if not re.match(r"^[a-zA-Z0-9_]{3,50}$", v):
            raise ValueError("Username must be 3-50 characters and contain only letters, numbers, and underscores")
        return v

class UserCreate(UserBase):
    """Esquema para creación de usuario."""
    password: str = Field(..., min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWORD_LENGTH, example="SecurePassword123!")
    role: UserRole = Field(default=UserRole.USER, example=UserRole.USER.value)

    @validator('password')
    def password_validator(cls, v):
        errors = []
        if len(v) < MIN_PASSWORD_LENGTH:
            errors.append(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
        if len(v) > MAX_PASSWORD_LENGTH:
            errors.append(f"Password must be at most {MAX_PASSWORD_LENGTH} characters long")
        if not re.search(r"[a-z]", v):
            errors.append("Password must contain at least one lowercase letter")
        if not re.search(r"[A-Z]", v):
            errors.append("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", v):
            errors.append("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?":{}|<>]", v):
            errors.append("Password must contain at least one special character")
        if errors:
            raise ValueError(", ".join(errors))
        return v

class UserUpdate(BaseSchema):
    """Esquema para actualización de usuario."""
    username: Optional[str] = Field(None, min_length=3, max_length=50, example="johndoe")
    email: Optional[EmailStr] = Field(None, example="johndoe@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="John Doe")
    password: Optional[str] = Field(None, min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWORD_LENGTH, example="NewSecurePassword123!")
    role: Optional[UserRole] = Field(None, example=UserRole.USER.value)

    @validator('username', always=True)
    def username_validator(cls, v):
        if v is not None and not re.match(r"^[a-zA-Z0-9_]{3,50}$", v):
            raise ValueError("Username must be 3-50 characters and contain only letters, numbers, and underscores")
        return v

    @validator('password', always=True)
    def password_validator(cls, v):
        if v is not None:
            errors = []
            if len(v) < MIN_PASSWORD_LENGTH:
                errors.append(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
            if len(v) > MAX_PASSWORD_LENGTH:
                errors.append(f"Password must be at most {MAX_PASSWORD_LENGTH} characters long")
            if not re.search(r"[a-z]", v):
                errors.append("Password must contain at least one lowercase letter")
            if not re.search(r"[A-Z]", v):
                errors.append("Password must contain at least one uppercase letter")
            if not re.search(r"[0-9]", v):
                errors.append("Password must contain at least one digit")
            if not re.search(r"[!@#$%^&*(),.?":{}|<>]", v):
                errors.append("Password must contain at least one special character")
            if errors:
                raise ValueError(", ".join(errors))
        return v

class UserResponse(UserBase):
    """Esquema para respuesta de usuario."""
    id: int = Field(..., example=1)
    role: UserRole = Field(..., example=UserRole.USER.value)
    created_at: datetime = Field(..., example="2023-01-01T00:00:00")
    updated_at: datetime = Field(..., example="2023-01-01T00:00:00")

class Token(BaseSchema):
    """Esquema para respuesta de token."""
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = Field("bearer", example="bearer")

class TokenData(BaseSchema):
    """Esquema para datos del token."""
    username: Optional[str] = Field(None, example="johndoe")
    role: Optional[UserRole] = Field(None, example=UserRole.USER.value)

class UserLogin(BaseSchema):
    """Esquema para login de usuario."""
    username: str = Field(..., example="johndoe")
    password: str = Field(..., example="SecurePassword123!")

# Tipos para manejo de errores
class ErrorResponse(BaseSchema):
    """Esquema para respuestas de error."""
    detail: str = Field(..., example="Resource not found")

class ValidationErrorResponse(BaseSchema):
    """Esquema para errores de validación."""
    detail: List[dict] = Field(..., example=[{"loc": ["body", "username"], "msg": "field required", "type": "value_error.missing"}])

__all__ = [
    "BaseSchema", 
    "UserBase", 
    "UserCreate", 
    "UserUpdate", 
    "UserResponse", 
    "Token", 
    "TokenData", 
    "UserLogin", 
    "ErrorResponse", 
    "ValidationErrorResponse"
]