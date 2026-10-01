"""Módulo de pruebas para la API REST de gestión de usuarios."""

import pytest
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from src.main import app
from src.config.settings import get_settings
from src.models import Base
from src.models.user import User, UserRole
from src.schemas.user import UserCreate, UserResponse
from src.utils.security import get_password_hash


# Configuración de la base de datos de prueba
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    """Crea una sesión de base de datos limpia para cada test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, None, None]:
    """Crea un cliente de pruebas con acceso a la base de datos de prueba."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_settings] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data() -> dict:
    """Datos de prueba para crear un usuario válido."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "SecurePass123!",
        "full_name": "Test User",
        "role": UserRole.USER.value
    }


@pytest.fixture
def test_admin_data() -> dict:
    """Datos de prueba para crear un usuario administrador."""
    return {
        "username": "adminuser",
        "email": "admin@example.com",
        "password": "AdminPass123!",
        "full_name": "Admin User",
        "role": UserRole.ADMIN.value
    }


@pytest.fixture
def created_user(db_session: Session, test_user_data: dict) -> User:
    """Crea un usuario de prueba en la base de datos."""
    hashed_password = get_password_hash(test_user_data["password"])
    user = User(
        username=test_user_data["username"],
        email=test_user_data["email"],
        hashed_password=hashed_password,
        full_name=test_user_data.get("full_name"),
        role=UserRole(test_user_data["role"])
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def auth_headers(client: TestClient, test_user_data: dict) -> dict:
    """Obtiene headers de autenticación para un usuario de prueba."""
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": test_user_data["username"],
            "password": test_user_data["password"]
        }
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def admin_auth_headers(client: TestClient, test_admin_data: dict) -> dict:
    """Obtiene headers de autenticación para un usuario administrador."""
    client.post("/api/v1/users/", json=test_admin_data)
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": test_admin_data["username"],
            "password": test_admin_data["password"]
        }
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}