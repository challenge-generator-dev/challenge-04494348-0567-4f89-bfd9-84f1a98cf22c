from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from sqlalchemy.orm import validates
from passlib.context import CryptContext
from datetime import datetime
from typing import Optional
from enum import Enum as PyEnum
from src.models import Base, UserRole, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH
import re

# Contexto para hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    """Modelo de usuario para persistencia en base de datos."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, username: str, email: str, hashed_password: str, full_name: Optional[str] = None, role: UserRole = UserRole.USER):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.full_name = full_name
        self.role = role

    @validates('email')
    def validate_email(self, key: str, email: str) -> str:
        """Validar formato de email."""
        if not re.match(r"^[^@]+@[^@]+.[^@]+$", email):
            raise ValueError("Invalid email format")
        return email

    @validates('username')
    def validate_username(self, key: str, username: str) -> str:
        """Validar formato de username."""
        if not re.match(r"^[a-zA-Z0-9_]{3,50}$", username):
            raise ValueError("Username must be 3-50 characters and contain only letters, numbers, and underscores")
        return username

    @validates('role')
    def validate_role(self, key: str, role: UserRole) -> UserRole:
        """Validar que el rol sea válido."""
        if role not in UserRole.list_roles():
            raise ValueError(f"Role must be one of {UserRole.list_roles()}")
        return role

    def validate(self):
        """Validar invariantes del modelo."""
        self.validate_email("email", self.email)
        self.validate_username("username", self.username)
        self.validate_role("role", self.role)
        if not self.hashed_password:
            raise ValueError("Password cannot be empty")

    def verify_password(self, plain_password: str) -> bool:
        """Verificar contraseña contra el hash almacenado."""
        return pwd_context.verify(plain_password, self.hashed_password)

    def get_password_hash(self, plain_password: str) -> str:
        """Generar hash de contraseña."""
        return pwd_context.hash(plain_password)

    @classmethod
    def create_user(cls, username: str, email: str, plain_password: str, full_name: Optional[str] = None, role: UserRole = UserRole.USER) -> "User":
        """Crear un nuevo usuario con contraseña hasheada."""
        hashed_password = cls.get_password_hash.__func__(plain_password)
        return cls(
            username=username,
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
            role=role
        )

    def update_password(self, plain_password: str) -> None:
        """Actualizar la contraseña del usuario."""
        self.hashed_password = self.get_password_hash(plain_password)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"

    def to_dict(self) -> dict:
        """Convertir el modelo a diccionario."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "role": self.role.value,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }