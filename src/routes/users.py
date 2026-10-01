from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from src.schemas import UserCreate, UserUpdate, UserResponse, ErrorResponse
from src.services.user_service import UserService
from src.models import User, UserRole, get_model_by_id, handle_sqlalchemy_exception
from src.config.settings import Settings
from src.config import get_db, get_current_user

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, responses={
    400: {"model": ErrorResponse, "description": "Usuario ya existe o datos inválidos"},
    401: {"model": ErrorResponse, "description": "No autorizado"},
    403: {"model": ErrorResponse, "description": "Sin permisos de administrador"}
})
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los administradores pueden crear usuarios"
        )
    
    try:
        user_service = UserService(db)
        existing_user = user_service.get_user_by_username(user_data.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El username '{user_data.username}' ya está registrado"
            )
        
        existing_email = user_service.get_user_by_email(user_data.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El email '{user_data.email}' ya está registrado"
            )
        
        new_user = user_service.create_user(
            username=user_data.username,
            email=user_data.email,
            plain_password=user_data.password,
            full_name=user_data.full_name,
            role=user_data.role
        )
        return UserResponse.model_validate(new_user)
    except HTTPException:
        raise
    except Exception as exc:
        raise handle_sqlalchemy_exception(exc)


@router.get("/", response_model=List[UserResponse], responses={
    401: {"model": ErrorResponse, "description": "No autorizado"},
    403: {"model": ErrorResponse, "description": "Sin permisos de administrador"}
})
def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requieren permisos de administrador para listar usuarios"
        )
    
    if limit > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El límite máximo es 100 usuarios"
        )
    
    try:
        user_service = UserService(db)
        users = user_service.get_users(skip=skip, limit=limit)
        return [UserResponse.model_validate(user) for user in users]
    except Exception as exc:
        raise handle_sqlalchemy_exception(exc)


@router.get("/me", response_model=UserResponse, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"}
})
def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    return UserResponse.model_validate(current_user)


@router.get("/{user_id}", response_model=UserResponse, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"},
    403: {"model": ErrorResponse, "description": "Sin permisos"},
    404: {"model": ErrorResponse, "description": "Usuario no encontrado"}
})
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para ver este usuario"
        )
    
    try:
        user_service = UserService(db)
        user = user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con id {user_id} no encontrado"
            )
        return UserResponse.model_validate(user)
    except HTTPException:
        raise
    except Exception as exc:
        raise handle_sqlalchemy_exception(exc)


@router.put("/{user_id}", response_model=UserResponse, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"},
    403: {"model": ErrorResponse, "description": "Sin permisos"},
    404: {"model": ErrorResponse, "description": "Usuario no encontrado"}
})
def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para actualizar este usuario"
        )
    
    update_data = user_update.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No hay datos para actualizar"
        )
    
    try:
        user_service = UserService(db)
        
        if "username" in update_data:
            existing = user_service.get_user_by_username(update_data["username"])
            if existing and existing.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"El username '{update_data['username']}' ya está en uso"
                )
        
        if "email" in update_data:
            existing = user_service.get_user_by_email(update_data["email"])
            if existing and existing.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"El email '{update_data['email']}' ya está en uso"
                )
        
        if "password" in update_data:
            update_data["hashed_password"] = user_service.hash_password(update_data.pop("password"))
        
        updated_user = user_service.update_user(user_id, update_data)
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con id {user_id} no encontrado"
            )
        return UserResponse.model_validate(updated_user)
    except HTTPException:
        raise
    except Exception as exc:
        raise handle_sqlalchemy_exception(exc)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"},
    403: {"model": ErrorResponse, "description": "Sin permisos de administrador"},
    404: {"model": ErrorResponse, "description": "Usuario no encontrado"}
})
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los administradores pueden eliminar usuarios"
        )
    
    if current_user.id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No puedes eliminar tu propio usuario"
        )
    
    try:
        user_service = UserService(db)
        deleted = user_service.delete_user(user_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con id {user_id} no encontrado"
            )
    except HTTPException:
        raise
    except Exception as exc:
        raise handle_sqlalchemy_exception(exc)