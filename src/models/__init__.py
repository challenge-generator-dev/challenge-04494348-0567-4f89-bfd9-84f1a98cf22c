from sqlalchemy.orm import declarative_base

# Base declarativa para modelos SQLAlchemy
Base = declarative_base()

# Importación de los modelos para que SQLAlchemy los registre
from src.models.user import User

__all__ = ["Base", "User"]

# Inicialización de metadata para la creación de tablas
from sqlalchemy import MetaData
metadata = MetaData()

# Configuración de eventos para validación de modelos
from sqlalchemy import event

def validate_model_before_flush(target, connection, *args, **kwargs):
    """Validar invariantes del modelo antes de guardar en la base de datos."""
    if hasattr(target, 'validate'):
        target.validate()

# Registrar eventos para todos los modelos
@event.listens_for(Base, 'before_insert')
@event.listens_for(Base, 'before_update')
def receive_before_flush(mapper, connection, target):
    validate_model_before_flush(target, connection)

# Tipos personalizados para manejo de roles
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

    @classmethod
    def list_roles(cls):
        return [role.value for role in cls]

# Constantes para validación de contraseñas
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
REQUIRED_PASSWORD_CHARS = {"lower": True, "upper": True, "digit": True, "special": True}

# Funciones utilitarias para modelos
from typing import TypeVar, Type
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

ModelType = TypeVar("ModelType", bound=Base)

def get_model_by_id(model_class: Type[ModelType], db_session, id: int) -> ModelType:
    """Obtener un modelo por su ID o lanzar excepción si no existe."""
    model = db_session.get(model_class, id)
    if not model:
        raise HTTPException(status_code=404, detail=f"{model_class.__name__} not found")
    return model

# Mapeo de excepciones SQLAlchemy a HTTPException
def handle_sqlalchemy_exception(exc: SQLAlchemyError) -> HTTPException:
    """Convertir excepciones de SQLAlchemy a excepciones HTTP."""
    if "UNIQUE constraint failed" in str(exc):
        return HTTPException(status_code=409, detail="Resource already exists")
    return HTTPException(status_code=500, detail="Database error")

__all__.extend(["UserRole", "MIN_PASSWORD_LENGTH", "MAX_PASSWORD_LENGTH", "get_model_by_id", "handle_sqlalchemy_exception"])