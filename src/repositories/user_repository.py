from typing import Optional, List
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from src.models.user import User
from src.models import UserRole, handle_sqlalchemy_exception


class UserRepository:
    """
    Repositorio para operaciones CRUD de usuarios.
    
    Esta clase encapsula toda la lógica de acceso a datos para usuarios,
    abstrayendo las operaciones de base de datos del servicio.
    """
    
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def _handle_db_error(self, operation: str, exc: Exception) -> None:
        """Maneja errores de base de datos y lanza excepciones apropiadas."""
        if isinstance(exc, IntegrityError):
            if "username" in str(exc.orig):
                raise ValueError("El nombre de usuario ya existe")
            if "email" in str(exc.orig):
                raise ValueError("El correo electrónico ya está registrado")
        handle_sqlalchemy_error(exc)
    
    def create(self, username: str, email: str, hashed_password: str, full_name: Optional[str] = None, role: UserRole = UserRole.USER) -> User:
        """
        Crea un nuevo usuario en la base de datos.
        
        Args:
            username: Nombre de usuario único
            email: Correo electrónico válido
            hashed_password: Contraseña hasheada
            full_name: Nombre completo opcional
            role: Rol del usuario (por defecto USER)
        
        Returns:
            User: El usuario creado
        
        Raises:
            ValueError: Si el username o email ya existen
            SQLAlchemyError: Si hay error de base de datos
        """
        try:
            user = User(
                username=username,
                email=email,
                hashed_password=hashed_password,
                full_name=full_name,
                role=role
            )
            self.db_session.add(user)
            self.db_session.commit()
            self.db_session.refresh(user)
            return user
        except IntegrityError as e:
            self.db_session.rollback()
            self._handle_db_error("create", e)
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_db_error("create", e)
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        Obtiene un usuario por su ID.
        
        Args:
            user_id: ID único del usuario
        
        Returns:
            Optional[User]: El usuario si existe, None en caso contrario
        """
        try:
            stmt = select(User).where(User.id == user_id)
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            self._handle_db_error("get_by_id", e)
    
    def get_by_username(self, username: str) -> Optional[User]:
        """
        Obtiene un usuario por su nombre de usuario.
        
        Args:
            username: Nombre de usuario a buscar
        
        Returns:
            Optional[User]: El usuario si existe, None en caso contrario
        """
        try:
            stmt = select(User).where(User.username == username.lower())
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            self._handle_db_error("get_by_username", e)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """
        Obtiene un usuario por su correo electrónico.
        
        Args:
            email: Correo electrónico a buscar
        
        Returns:
            Optional[User]: El usuario si existe, None en caso contrario
        """
        try:
            stmt = select(User).where(User.email == email.lower())
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            self._handle_db_error("get_by_email", e)
    
    def get_all(self, skip: int = 0, limit: int = 100, active_only: bool = True) -> List[User]:
        """
        Obtiene una lista de usuarios con paginación.
        
        Args:
            skip: Número de registros a omitir
            limit: Número máximo de registros a devolver
            active_only: Si True, solo devuelve usuarios activos
        
        Returns:
            List[User]: Lista de usuarios
        """
        try:
            stmt = select(User)
            if active_only:
                stmt = stmt.where(User.is_active == True)
            stmt = stmt.offset(skip).limit(limit).order_by(User.created_at.desc())
            result = self.db_session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            self._handle_db_error("get_all", e)
    
    def update(self, user_id: int, **kwargs) -> Optional[User]:
        """
        Actualiza los datos de un usuario existente.
        
        Args:
            user_id: ID del usuario a actualizar
            **kwargs: Campos a actualizar (username, email, full_name, is_active, etc.)
        
        Returns:
            Optional[User]: El usuario actualizado si existe, None si no existe
        
        Raises:
            ValueError: Si el username o email ya existen
        """
        try:
            user = self.get_by_id(user_id)
            if not user:
                return None
            
            update_data = {}
            if 'username' in kwargs and kwargs['username']:
                update_data['username'] = kwargs['username'].lower()
            if 'email' in kwargs and kwargs['email']:
                update_data['email'] = kwargs['email'].lower()
            if 'full_name' in kwargs and kwargs['full_name'] is not None:
                update_data['full_name'] = kwargs['full_name']
            if 'hashed_password' in kwargs and kwargs['hashed_password']:
                update_data['hashed_password'] = kwargs['hashed_password']
            if 'is_active' in kwargs and kwargs['is_active'] is not None:
                update_data['is_active'] = kwargs['is_active']
            if 'role' in kwargs and kwargs['role']:
                update_data['role'] = kwargs['role']
            
            update_data['updated_at'] = datetime.utcnow()
            
            stmt = update(User).where(User.id == user_id).values(**update_data)
            self.db_session.execute(stmt)
            self.db_session.commit()
            
            return self.get_by_id(user_id)
        except IntegrityError as e:
            self.db_session.rollback()
            self._handle_db_error("update", e)
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_db_error("update", e)
    
    def delete(self, user_id: int) -> bool:
        """
        Elimina (desactiva) un usuario de la base de datos.
        
        Args:
            user_id: ID del usuario a eliminar
        
        Returns:
            bool: True si el usuario fue desactivado, False si no existía
        """
        try:
            user = self.get_by_id(user_id)
            if not user:
                return False
            
            stmt = update(User).where(User.id == user_id).values(
                is_active=False,
                updated_at=datetime.utcnow()
            )
            self.db_session.execute(stmt)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_db_error("delete", e)
    
    def hard_delete(self, user_id: int) -> bool:
        """
        Elimina permanentemente un usuario de la base de datos.
        
        Args:
            user_id: ID del usuario a eliminar permanentemente
        
        Returns:
            bool: True si el usuario fue eliminado, False si no existía
        """
        try:
            user = self.get_by_id(user_id)
            if not user:
                return False
            
            stmt = delete(User).where(User.id == user_id)
            self.db_session.execute(stmt)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            self._handle_db_error("hard_delete", e)
    
    def count(self, active_only: bool = True) -> int:
        """
        Cuenta el número de usuarios en la base de datos.
        
        Args:
            active_only: Si True, solo cuenta usuarios activos
        
        Returns:
            int: Número de usuarios
        """
        try:
            from sqlalchemy import func
            stmt = select(func.count(User.id))
            if active_only:
                stmt = stmt.where(User.is_active == True)
            result = self.db_session.execute(stmt)
            return result.scalar() or 0
        except SQLAlchemyError as e:
            self._handle_db_error("count", e)
    
    def exists_by_username(self, username: str) -> bool:
        """
        Verifica si existe un usuario con el nombre de usuario dado.
        
        Args:
            username: Nombre de usuario a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        try:
            stmt = select(User.id).where(User.username == username.lower())
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none() is not None
        except SQLAlchemyError as e:
            self._handle_db_error("exists_by_username", e)
    
    def exists_by_email(self, email: str) -> bool:
        """
        Verifica si existe un usuario con el correo electrónico dado.
        
        Args:
            email: Correo electrónico a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        try:
            stmt = select(User.id).where(User.email == email.lower())
            result = self.db_session.execute(stmt)
            return result.scalar_one_or_none() is not None
        except SQLAlchemyError as e:
            self._handle_db_error("exists_by_email", e)