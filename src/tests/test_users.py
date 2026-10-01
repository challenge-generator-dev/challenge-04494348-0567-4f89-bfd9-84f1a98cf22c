"""Pruebas unitarias para los endpoints de gestión de usuarios."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.models.user import User, UserRole
from src.schemas.user import UserCreate, UserResponse
from src.utils.security import get_password_hash


class TestUserEndpoints:
    """Suite de pruebas para los endpoints de usuarios."""

    def test_create_user_success(self, client: TestClient, test_user_data: dict):
        """Verifica que se puede crear un usuario correctamente."""
        response = client.post("/api/v1/users/", json=test_user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == test_user_data["username"]
        assert data["email"] == test_user_data["email"]
        assert data["full_name"] == test_user_data["full_name"]
        assert "password" not in data
        assert "hashed_password" not in data

    def test_create_user_duplicate_username(self, client: TestClient, created_user: User, test_user_data: dict):
        """Verifica que no se puede crear un usuario con username duplicado."""
        response = client.post("/api/v1/users/", json=test_user_data)
        assert response.status_code == 400
        assert "username" in response.json()["detail"].lower()

    def test_create_user_duplicate_email(self, client: TestClient, created_user: User, db_session: Session):
        """Verifica que no se puede crear un usuario con email duplicado."""
        user_data = {
            "username": "different_user",
            "email": created_user.email,
            "password": "SecurePass123!",
            "full_name": "Another User"
        }
        response = client.post("/api/v1/users/", json=user_data)
        assert response.status_code == 400
        assert "email" in response.json()["detail"].lower()

    def test_create_user_weak_password(self, client: TestClient):
        """Verifica que no se puede crear un usuario con contraseña débil."""
        user_data = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "weak",
            "full_name": "New User"
        }
        response = client.post("/api/v1/users/", json=user_data)
        assert response.status_code == 422

    def test_create_user_invalid_email(self, client: TestClient):
        """Verifica que no se puede crear un usuario con email inválido."""
        user_data = {
            "username": "newuser",
            "email": "invalid-email",
            "password": "SecurePass123!",
            "full_name": "New User"
        }
        response = client.post("/api/v1/users/", json=user_data)
        assert response.status_code == 422

    def test_get_user_by_id(self, client: TestClient, created_user: User):
        """Verifica que se puede obtener un usuario por su ID."""
        response = client.get(f"/api/v1/users/{created_user.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_user.id
        assert data["username"] == created_user.username

    def test_get_user_by_id_not_found(self, client: TestClient):
        """Verifica que se obtiene 404 al buscar un usuario inexistente."""
        response = client.get("/api/v1/users/99999")
        assert response.status_code == 404

    def test_get_all_users(self, client: TestClient, created_user: User):
        """Verifica que se pueden listar todos los usuarios."""
        response = client.get("/api/v1/users/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1

    def test_update_user(self, client: TestClient, created_user: User, auth_headers: dict):
        """Verifica que se puede actualizar un usuario."""
        update_data = {
            "full_name": "Updated Name",
            "email": "updated@example.com"
        }
        response = client.put(
            f"/api/v1/users/{created_user.id}",
            json=update_data,
            headers=auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["full_name"] == "Updated Name"
        assert data["email"] == "updated@example.com"

    def test_update_user_not_found(self, client: TestClient, auth_headers: dict):
        """Verifica que se obtiene 404 al actualizar un usuario inexistente."""
        response = client.put(
            "/api/v1/users/99999",
            json={"full_name": "Test"},
            headers=auth_headers
        )
        assert response.status_code == 404

    def test_update_user_duplicate_email(self, client: TestClient, db_session: Session, auth_headers: dict):
        """Verifica que no se puede actualizar a un email que ya existe."""
        user1 = User(
            username="user1",
            email="user1@example.com",
            hashed_password=get_password_hash("Pass123!"),
            role=UserRole.USER
        )
        user2 = User(
            username="user2",
            email="user2@example.com",
            hashed_password=get_password_hash("Pass123!"),
            role=UserRole.USER
        )
        db_session.add(user1)
        db_session.add(user2)
        db_session.commit()

        response = client.put(
            f"/api/v1/users/{user1.id}",
            json={"email": user2.email},
            headers=auth_headers
        )
        assert response.status_code == 400

    def test_delete_user(self, client: TestClient, created_user: User, auth_headers: dict):
        """Verifica que se puede eliminar un usuario."""
        response = client.delete(
            f"/api/v1/users/{created_user.id}",
            headers=auth_headers
        )
        assert response.status_code == 204

        get_response = client.get(f"/api/v1/users/{created_user.id}")
        assert get_response.status_code == 404

    def test_delete_user_not_found(self, client: TestClient, auth_headers: dict):
        """Verifica que se obtiene 404 al eliminar un usuario inexistente."""
        response = client.delete("/api/v1/users/99999", headers=auth_headers)
        assert response.status_code == 404

    def test_get_current_user(self, client: TestClient, auth_headers: dict, created_user: User):
        """Verifica que el usuario actual puede obtener su propio perfil."""
        response = client.get("/api/v1/users/me", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == created_user.username

    def test_unauthorized_access(self, client: TestClient):
        """Verifica que los endpoints protegidos requieren autenticación."""
        response = client.get("/api/v1/users/me")
        assert response.status_code == 401

    def test_update_password(self, client: TestClient, created_user: User, auth_headers: dict):
        """Verifica que un usuario puede cambiar su contraseña."""
        password_data = {
            "current_password": "SecurePass123!",
            "new_password": "NewSecurePass456!"
        }
        response = client.post(
            f"/api/v1/users/{created_user.id}/change-password",
            json=password_data,
            headers=auth_headers
        )
        assert response.status_code == 200

        login_response = client.post(
            "/api/v1/auth/login",
            json={
                "username": created_user.username,
                "password": "NewSecurePass456!"
            }
        )
        assert login_response.status_code == 200

    def test_update_password_wrong_current(self, client: TestClient, created_user: User, auth_headers: dict):
        """Verifica que no se puede cambiar contraseña con contraseña actual incorrecta."""
        password_data = {
            "current_password": "WrongPassword!",
            "new_password": "NewSecurePass456!"
        }
        response = client.post(
            f"/api/v1/users/{created_user.id}/change-password",
            json=password_data,
            headers=auth_headers
        )
        assert response.status_code == 400