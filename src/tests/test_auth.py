"""Pruebas unitarias para autenticación y tokens JWT.

ESTE ARCHIVO ES SUPERFICIE DE PRÁCTICA - STUB.
El estudiante debe implementar los casos de prueba marcados con skip.
"""

import pytest
from fastapi.testclient import TestClient


class TestAuthentication:
    """Suite de pruebas para autenticación JWT."""

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_login_success(self, client: TestClient, test_user_data: dict):
        """Verifica que el login es exitoso con credenciales válidas."""
        # Arrange
        # TODO: Crear usuario en la base de datos
        pass

        # Act
        # TODO: Realizar solicitud POST a /auth/login con credenciales
        pass

        # Assert
        # TODO: Verificar respuesta 200 y token presente
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_login_invalid_username(self, client: TestClient):
        """Verifica que el login falla con usuario inexistente."""
        # Arrange
        # TODO: Credenciales con usuario que no existe
        pass

        # Act
        # TODO: Realizar login
        pass

        # Assert
        # TODO: Verificar respuesta 401
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_login_invalid_password(self, client: TestClient, test_user_data: dict):
        """Verifica que el login falla con contraseña incorrecta."""
        # Arrange
        # TODO: Crear usuario
        # TODO: Credenciales con contraseña incorrecta
        pass

        # Act
        # TODO: Realizar login
        pass

        # Assert
        # TODO: Verificar respuesta 401
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_token_contains_expected_claims(self, client: TestClient, test_user_data: dict):
        """Verifica que el token JWT contiene los claims esperados."""
        # Arrange
        # TODO: Crear usuario y realizar login
        pass

        # Act
        # TODO: Decodificar el token
        pass

        # Assert
        # TODO: Verificar sub, username y exp en el payload
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_expired_token_rejected(self, client: TestClient):
        """Verifica que un token expirado es rechazado."""
        # Arrange
        # TODO: Generar token con fecha de expiración en el pasado
        pass

        # Act
        # TODO: Realizar solicitud protegida con token expirado
        pass

        # Assert
        # TODO: Verificar respuesta 401
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_missing_token_rejected(self, client: TestClient):
        """Verifica que solicitudes sin token son rechazadas."""
        # Act
        # TODO: Realizar solicitud a endpoint protegido sin token
        pass

        # Assert
        # TODO: Verificar respuesta 401
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_invalid_token_format(self, client: TestClient):
        """Verifica que tokens con formato inválido son rechazados."""
        # Arrange
        # TODO: Token con formato inválido (no JWT)
        pass

        # Act
        # TODO: Realizar solicitud con token inválido
        pass

        # Assert
        # TODO: Verificar respuesta 401
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_register_new_user(self, client: TestClient, test_user_data: dict):
        """Verifica que un nuevo usuario puede registrarse."""
        # Arrange
        # TODO: Datos de usuario nuevo
        pass

        # Act
        # TODO: Realizar POST a /auth/register
        pass

        # Assert
        # TODO: Verificar 201 y usuario creado
        pass

    @pytest.mark.skip(reason="Superficie de práctica - implementar por el estudiante")
    def test_register_duplicate_user(self, client: TestClient, created_user: User):
        """Verifica que no se puede registrar un usuario duplicado."""
        # Arrange
        # TODO: Datos del usuario ya creado
        pass

        # Act
        # TODO: Intentar registrar mismo usuario
        pass

        # Assert
        # TODO: Verificar 400
        pass