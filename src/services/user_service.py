"""Servicio de gestión de usuarios.

Maneja la lógica de negocio relacionada con usuarios: operaciones CRUD,
validaciones de negocio, y coordinación con el repositorio.
"""

from typing import Optional, List
from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.user import User, UserRole
from src.schemas.user import UserCreate, UserUpdate, UserResponse
from src.repositories.user_repository import UserRepository


class UserService:
    """Servicio para la gestión de usuarios.
    
    Coordina las operaciones de negocio relacionadas con usuarios,
    incluyendo validación de datos y reglas de negocio.
    """
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def create_user(self, user_data: UserCreate, db: Session) -> UserResponse:
        """Crea un nuevo usuario en el sistema.
        
        Valida que el email y username no estén duplicados antes de crear.
        """
        existing_user = self.user_repository.get_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        existing_username = self.user_repository.get_by_username(db, user_data.username)
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre de usuario ya está en uso"
            )
        
        user = User.create_user(
            username=user_data.username,
            email=user_data.email,
            plain_password=user_data.password,
            full_name=user_data.full_name,
            role=user_data.role if hasattr(user_data, 'role') and user_data.role else UserRole.USER
        )
        
        created_user = self.user_repository.create(db, user)
        return UserResponse.from_orm(created_user)
    
    def get_user(self, user_id: int, db: Session) -> UserResponse:
        """Obtiene un usuario por su ID."""
        user = self.user_repository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con ID {user_id} no encontrado"
            )
        return UserResponse.from_orm(user)
    
    def get_user_by_email(self, email: str, db: Session) -> Optional[User]:
        """Obtiene un usuario por su email."""
        return self.user_repository.get_by_email(db, email)
    
    def get_user_by_username(self, username: str, db: Session) -> Optional[User]:
        """Obtiene un usuario por su nombre de usuario."""
        return self.user_repository.get_by_username(db, username)
    
    def get_all_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        """Obtiene una lista de usuarios con paginación."""
        users = self.user_repository.get_all(db, skip=skip, limit=limit)
        return [UserResponse.from_orm(user) for user in users]
    
    def update_user(self, user_id: int, user_data: UserUpdate, db: Session) -> UserResponse:
        """Actualiza un usuario existente.
        
        Valida que los nuevos datos no entren en conflicto con usuarios existentes.
        """
        existing_user = self.user_repository.get_by_id(db, user_id)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con ID {user_id} no encontrado"
            )
        
        if user_data.email and user_data.email != existing_user.email:
            email_taken = self.user_repository.get_by_email(db, user_data.email)
            if email_taken:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El email ya está registrado"
                )
        
        if user_data.username and user_data.username != existing_user.username:
            username_taken = self.user_repository.get_by_username(db, user_data.username)
            if username_taken:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El nombre de usuario ya está en uso"
                )
        
        update_data = user_data.dict(exclude_unset=True)
        
        if 'password' in update_data:
            update_data['hashed_password'] = User.get_password_hash(update_data.pop('password'))
        
        updated_user = self.user_repository.update(db, user_id, update_data)
        return UserResponse.from_orm(updated_user)
    
    def delete_user(self, user_id: int, db: Session) -> None:
        """Elimina un usuario del sistema."""
        existing_user = self.user_repository.get_by_id(db, user_id)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con ID {user_id} no encontrado"
            )
        
        self.user_repository.delete(db, user_id)
    
    def change_password(self, user_id: int, current_password: str, new_password: str, db: Session) -> None:
        """Cambia la contraseña de un usuario.
        
        Verifica que la contraseña actual sea correcta antes de cambiarla.
        """
        user = self.user_repository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con ID {user_id} no encontrado"
            )
        
        if not user.verify_password(current_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La contraseña actual es incorrecta"
            )
        
        user.update_password(new_password)
        self.user_repository.update(db, user_id, {'hashed_password': user.hashed_password})
    
    def update_user_role(self, user_id: int, new_role: UserRole, db: Session) -> UserResponse:
        """Actualiza el rol de un usuario."""
        user = self.user_repository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con ID {user_id} no encontrado"
            )
        
        updated_user = self.user_repository.update(db, user_id, {'role': new_role.value})
        return UserResponse.from_orm(updated_user)
    
    def count_users(self, db: Session) -> int:
        """Cuenta el total de usuarios en el sistema."""
        return self.user_repository.count(db)