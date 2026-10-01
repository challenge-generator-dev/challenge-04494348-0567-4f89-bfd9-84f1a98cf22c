"""
API REST de Gestión de Usuarios - Aplicación Fintech

Este paquete contiene la implementación de una API REST para la gestión
de usuarios con autenticación JWT, desarrollada con FastAPI.
"""

import os
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Versión de la aplicación
__version__ = "1.0.0"
__author__ = "Equipo de Desarrollo"
__app_name__ = "User Management API"

# Configuración de la aplicación
APP_ENV: str = os.getenv("APP_ENV", "development")
DEBUG_MODE: bool = APP_ENV == "development"

# Configuración de CORS
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8000"
).split(",")

def create_app() -> FastAPI:
    """
    Crea y configura la instancia principal de la aplicación FastAPI.
    
    Returns:
        FastAPI: Instancia configurada de la aplicación.
    """
    from src.main import app as main_app
    return main_app

def get_app_info() -> dict:
    """
    Retorna información general de la aplicación.
    
    Returns:
        dict: Diccionario con información de la aplicación.
    """
    return {
        "name": __app_name__,
        "version": __version__,
        "author": __author__,
        "environment": APP_ENV,
        "debug": DEBUG_MODE,
    }

def configure_cors(app: FastAPI) -> None:
    """
    Configura el middleware de CORS para la aplicación.
    
    Args:
        app: Instancia de FastAPI a configurar.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def validate_environment() -> bool:
    """
    Valida que las variables de entorno requeridas estén configuradas.
    
    Returns:
        bool: True si el entorno está correctamente configurado.
    
    Raises:
        ValueError: Si falta alguna variable de entorno crítica.
    """
    required_vars = ["DATABASE_URL", "JWT_SECRET_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars and APP_ENV == "production":
        raise ValueError(
            f"Variables de entorno requeridas faltantes: {', '.join(missing_vars)}"
        )
    
    return True

def initialize_application() -> FastAPI:
    """
    Inicializa la aplicación con todas las configuraciones necesarias.
    
    Returns:
        FastAPI: Aplicación completamente configurada y lista para usar.
    """
    # Validar configuración del entorno
    validate_environment()
    
    # Crear la aplicación
    app = create_app()
    
    # Configurar CORS
    configure_cors(app)
    
    return app

# Exports públicos del paquete
__all__ = [
    "__version__",
    "__author__",
    "__app_name__",
    "APP_ENV",
    "DEBUG_MODE",
    "create_app",
    "get_app_info",
    "configure_cors",
    "validate_environment",
    "initialize_application",
]

# Inicialización automática cuando se importa el paquete
# Esto permite usar "from app import app" directamente
def __getattr__(name: str):
    """
    Implementa la carga perezosa de módulos para optimizar el inicio.
    """
    if name == "app":
        from src.main import app
        return app
    elif name == "settings":
        from src.config.settings import get_settings
        return get_settings()
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")