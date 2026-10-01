"""
Módulo de repositorios para acceso a datos.

Este módulo contiene las clases de acceso a datos que abstraen
las operaciones de base de datos del resto de la aplicación.
"""

from typing import TypeVar, Type, Optional, List, Any, Dict
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.repositories.user_repository import UserRepository


__all__ = [
    "UserRepository",
]


def get_user_repository(db_session: Session) -> UserRepository:
    """
    Factory para obtener una instancia del repositorio de usuarios.
    
    Args:
        db_session: Sesión de base de datos de SQLAlchemy
    
    Returns:
        UserRepository: Instancia del repositorio de usuarios
    """
    return UserRepository(db_session)


class BaseRepository:
    """
    Clase base abstracta para repositorios.
    
    Proporciona métodos comunes para todas las implementaciones de repositorios,
    como gestión de errores y operaciones genéricas de base de datos.
    """
    
    def __init__(self, db_session: Session, model_class: Type):
        self.db_session = db_session
        self.model_class = model_class
    
    def _handle_error(self, operation: str, exc: Exception) -> None:
        """
        Maneja errores de base de datos de forma centralizada.
        
        Args:
            operation: Nombre de la operación que falló
            exc: Excepción capturada
        """
        if isinstance(exc, SQLAlchemyError):
            raise exc
        raise RuntimeError(f"Error en {operation}: {str(exc)}")
    
    def get_by_id(self, id: int) -> Optional[Any]:
        """
        Obtiene un registro por su ID.
        
        Args:
            id: Identificador único del registro
        
        Returns:
            Optional[Any]: El registro si existe, None en caso contrario
        """
        try:
            stmt = select(self.model_class).where(
                self.model_class.__table__.c.id == id
            )
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            self._handle_error("get_by_id", e)
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Any]:
        """
        Obtiene todos los registros con paginación.
        
        Args:
            skip: Número de registros a omitir
            limit: Número máximo de registros a devolver
        
        Returns:
            List[Any]: Lista de registros
        """
        try:
            stmt = select(self.model_class).offset(skip).limit(limit)
            result = self.db_session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            self._handle_error("get_all", e)
    
    def count(self) -> int:
        """
        Cuenta el número total de registros.
        
        Returns:
            int: Número de registros
        """
        try:
            stmt = select(func.count(self.model_class.__table__.c.id))
            result = self.db_session.execute(stmt)
            return result.scalar() or 0
        except SQLAlchemyError as e:
            self._handle_error("count", e)
    
    def create(self, **kwargs: Any) -> Any:
        ""
        Crea un nuevo registro.
        
        Args:
            **kwargs: Datos del registro a crear
        
        Returns:
            Any: El registro creado
        """
        try:
            instance = self.model_class(**kwargs)
            self.db_session.add(instance)
            self.db_session.commit()
            self.db_session.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_error("create", e)
    
    def update(self, id: int, **kwargs: Any) -> Optional[Any]:
        """
        Actualiza un registro existente.
        
        Args:
            id: ID del registro a actualizar
            **kwargs: Datos a actualizar
        
        Returns:
            Optional[Any]: El registro actualizado si existe, None si no existe
        """
        try:
            existing = self.get_by_id(id)
            if not existing:
                return None
            
            for key, value in kwargs.items():
                if hasattr(existing, key):
                    setattr(existing, key, value)
            
            self.db_session.commit()
            self.db_session.refresh(existing)
            return existing
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_error("update", e)
    
    def delete(self, id: int) -> bool:
        """
        Elimina un registro.
        
        Args:
            id: ID del registro a eliminar
        
        Returns:
            bool: True si se eliminó, False si no existía
        """
        try:
            instance = self.get_by_id(id)
            if not instance:
                return False
            
            self.db_session.delete(instance)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_error("delete", e)