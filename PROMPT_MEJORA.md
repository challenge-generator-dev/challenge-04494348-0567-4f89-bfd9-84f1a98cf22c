# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `src/routes/auth.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `src/services/auth_service.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `src/utils/security.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `src/tests/test_auth.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `src/services/__init__.py`

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `src/models/__init__.py` — `User.extend`: Se invoca `extend` sobre `User`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/routes/users.py` — `UserUpdate.model_dump`: Se invoca `model_dump` sobre `UserUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/services/user_service.py` — `UserUpdate.dict`: Se invoca `dict` sobre `UserUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Crear una API REST con FastAPI, SQLAlchemy y autenticación JWT

### Reto
- Tema: api-rest
- Seniority: junior-l1
- Tipo: practical
- Título: Desarrollo de una API REST para gestión de usuarios
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición y modelado de la API — objetivo: Definir y modelar la estructura de la API REST, incluyendo los endpoints y los modelos de datos. — entregable (NO resolver): Diagrama de la API REST y modelos de datos definidos.
- Fase 2: Implementación de la autenticación JWT — objetivo: Implementar la autenticación mediante JWT en la API REST. — entregable (NO resolver): Implementación de la autenticación JWT en la API REST.
- Fase 3: Implementación de los endpoints de gestión de usuarios — objetivo: Implementar los endpoints para la creación, lectura, actualización y eliminación de usuarios. — entregable (NO resolver): Implementación de los endpoints de gestión de usuarios en la API REST.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: __init__.py ===
# Este archivo marca el directorio como un paquete Python
# Permite importaciones relativas entre módulos del proyecto

from fastapi import FastAPI
from src.config.settings import settings
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router

app = FastAPI(title="User Management API", version="1.0.0")

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to User Management API"}

// === ARCHIVO: src/main.py ===
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import Settings
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router

app = FastAPI(title="User Management API", version="1.0.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "User Management API"}

if __name__ == "__main__":
    import uvicorn
    settings = Settings()
    uvicorn.run(
        app,
        host=settings.server_host,
        port=settings.server_port,
        log_level=settings.log_level.lower()
    )

// === ARCHIVO: src/config/settings.py ===
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr, PositiveInt, validator
from typing import Optional


class Settings(BaseSettings):
    # Configuración del servidor
    server_host: str = Field(default="0.0.0.0", env="SERVER_HOST")
    server_port: PositiveInt = Field(default=8000, env="SERVER_PORT")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    # Configuración de la base de datos
    database_url: str = Field(..., env="DATABASE_URL")
    database_pool_size: PositiveInt = Field(default=5, env="DATABASE_POOL_SIZE")
    database_max_overflow: PositiveInt = Field(default=10, env="DATABASE_MAX_OVERFLOW")
    database_pool_timeout: PositiveInt = Field(default=30, env="DATABASE_POOL_TIMEOUT")

    # Configuración de JWT
    jwt_secret_key: SecretStr = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    jwt_access_token_expire_minutes: PositiveInt = Field(default=30, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    jwt_refresh_token_expire_days: PositiveInt = Field(default=7, env="JWT_REFRESH_TOKEN_EXPIRE_DAYS")

    # Configuración de seguridad
    password_hash_rounds: PositiveInt = Field(default=12, env="PASSWORD_HASH_ROUNDS")
    password_min_length: PositiveInt = Field(default=8, env="PASSWORD_MIN_LENGTH")

    # Configuración de CORS
    cors_allow_origins: list[str] = Field(default=["*"], env="CORS_ALLOW_ORIGINS")
    cors_allow_methods: list[str] = Field(default=["*"], env="CORS_ALLOW_METHODS")
    cors_allow_headers: list[str] = Field(default=["*"], env="CORS_ALLOW_HEADERS")

    @validator("database_url")
    def validate_database_url(cls, v: str) -> str:
        if not v.startswith("postgresql://") and not v.startswith("sqlite:///"):
            raise ValueError("DATABASE_URL must start with 'postgresql://' or 'sqlite:///'")
        return v

    @validator("jwt_secret_key")
    def validate_jwt_secret(cls, v: SecretStr) -> SecretStr:
        if len(v.get_secret_value()) < 32:
            raise ValueError("JWT_SECRET_KEY must be at least 32 characters long")
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Instancia global de configuración
settings = Settings()

// === ARCHIVO: requirements.txt ===
fastapi==0.115.0
uvicorn==0.30.6
sqlalchemy==2.0.32
pydantic==2.9.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.1
pydantic-settings==2.4.0

# Dependencias de test
httpx==0.27.2
pytest==8.3.2

// === ARCHIVO: src/models/__init__.py ===
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

// === ARCHIVO: src/models/user.py ===
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

// === ARCHIVO: src/schemas/__init__.py ===
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime
from src.models import UserRole, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH
import re

class BaseSchema(BaseModel):
    """Clase base para esquemas con configuración común."""
    class Config:
        from_attributes = True
        str_strip_whitespace = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UserBase(BaseSchema):
    """Esquema base para datos de usuario."""
    username: str = Field(..., min_length=3, max_length=50, example="johndoe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="John Doe")

    @validator('username')
    def username_validator(cls, v):
        if not re.match(r"^[a-zA-Z0-9_]{3,50}$", v):
            raise ValueError("Username must be 3-50 characters and contain only letters, numbers, and underscores")
        return v

class UserCreate(UserBase):
    """Esquema para creación de usuario."""
    password: str = Field(..., min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWORD_LENGTH, example="SecurePassword123!")
    role: UserRole = Field(default=UserRole.USER, example=UserRole.USER.value)

    @validator('password')
    def password_validator(cls, v):
        errors = []
        if len(v) < MIN_PASSWORD_LENGTH:
            errors.append(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
        if len(v) > MAX_PASSWORD_LENGTH:
            errors.append(f"Password must be at most {MAX_PASSWORD_LENGTH} characters long")
        if not re.search(r"[a-z]", v):
            errors.append("Password must contain at least one lowercase letter")
        if not re.search(r"[A-Z]", v):
            errors.append("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", v):
            errors.append("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?":{}|<>]", v):
            errors.append("Password must contain at least one special character")
        if errors:
            raise ValueError(", ".join(errors))
        return v

class UserUpdate(BaseSchema):
    """Esquema para actualización de usuario."""
    username: Optional[str] = Field(None, min_length=3, max_length=50, example="johndoe")
    email: Optional[EmailStr] = Field(None, example="johndoe@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="John Doe")
    password: Optional[str] = Field(None, min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWORD_LENGTH, example="NewSecurePassword123!")
    role: Optional[UserRole] = Field(None, example=UserRole.USER.value)

    @validator('username', always=True)
    def username_validator(cls, v):
        if v is not None and not re.match(r"^[a-zA-Z0-9_]{3,50}$", v):
            raise ValueError("Username must be 3-50 characters and contain only letters, numbers, and underscores")
        return v

    @validator('password', always=True)
    def password_validator(cls, v):
        if v is not None:
            errors = []
            if len(v) < MIN_PASSWORD_LENGTH:
                errors.append(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
            if len(v) > MAX_PASSWORD_LENGTH:
                errors.append(f"Password must be at most {MAX_PASSWORD_LENGTH} characters long")
            if not re.search(r"[a-z]", v):
                errors.append("Password must contain at least one lowercase letter")
            if not re.search(r"[A-Z]", v):
                errors.append("Password must contain at least one uppercase letter")
            if not re.search(r"[0-9]", v):
                errors.append("Password must contain at least one digit")
            if not re.search(r"[!@#$%^&*(),.?":{}|<>]", v):
                errors.append("Password must contain at least one special character")
            if errors:
                raise ValueError(", ".join(errors))
        return v

class UserResponse(UserBase):
    """Esquema para respuesta de usuario."""
    id: int = Field(..., example=1)
    role: UserRole = Field(..., example=UserRole.USER.value)
    created_at: datetime = Field(..., example="2023-01-01T00:00:00")
    updated_at: datetime = Field(..., example="2023-01-01T00:00:00")

class Token(BaseSchema):
    """Esquema para respuesta de token."""
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = Field("bearer", example="bearer")

class TokenData(BaseSchema):
    """Esquema para datos del token."""
    username: Optional[str] = Field(None, example="johndoe")
    role: Optional[UserRole] = Field(None, example=UserRole.USER.value)

class UserLogin(BaseSchema):
    """Esquema para login de usuario."""
    username: str = Field(..., example="johndoe")
    password: str = Field(..., example="SecurePassword123!")

# Tipos para manejo de errores
class ErrorResponse(BaseSchema):
    """Esquema para respuestas de error."""
    detail: str = Field(..., example="Resource not found")

class ValidationErrorResponse(BaseSchema):
    """Esquema para errores de validación."""
    detail: List[dict] = Field(..., example=[{"loc": ["body", "username"], "msg": "field required", "type": "value_error.missing"}])

__all__ = [
    "BaseSchema", 
    "UserBase", 
    "UserCreate", 
    "UserUpdate", 
    "UserResponse", 
    "Token", 
    "TokenData", 
    "UserLogin", 
    "ErrorResponse", 
    "ValidationErrorResponse"
]

// === ARCHIVO: src/schemas/user.py ===
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator, SecretStr
from src.schemas import BaseSchema


class UserBase(BaseSchema):
    """Schema base para usuarios con campos comunes de validación."""
    
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern=r'^[a-zA-Z0-9_-]+$',
        description="Nombre de usuario único"
    )
    email: EmailStr = Field(description="Correo electrónico válido")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Nombre completo del usuario")
    
    @field_validator('username')
    @classmethod
    def username_validator(cls, v: str) -> str:
        if not v:
            raise ValueError("El nombre de usuario no puede estar vacío")
        if len(v) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(v) > 50:
            raise ValueError("El nombre de usuario no puede exceder 50 caracteres")
        return v.strip().lower()


class UserCreate(UserBase):
    """Schema para creación de usuarios con validación de contraseña."""
    
    password: SecretStr = Field(
        min_length=8,
        max_length=100,
        description="Contraseña del usuario"
    )
    role: Optional[str] = Field(default="user", description="Rol del usuario")
    
    @field_validator('password')
    @classmethod
    def password_validator(cls, v: SecretStr) -> str:
        password_value = v.get_secret_value()
        if not password_value:
            raise ValueError("La contraseña no puede estar vacía")
        if len(password_value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not any(c.isupper() for c in password_value):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula")
        if not any(c.islower() for c in password_value):
            raise ValueError("La contraseña debe tener al menos una letra minúscula")
        if not any(c.isdigit() for c in password_value):
            raise ValueError("La contraseña debe tener al menos un número")
        return password_value


class UserUpdate(BaseSchema):
    """Schema para actualización de usuarios con campos opcionales."""
    
    username: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=50,
        pattern=r'^[a-zA-Z0-9_-]+$',
        description="Nuevo nombre de usuario"
    )
    email: Optional[EmailStr] = Field(default=None, description="Nuevo correo electrónico")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Nuevo nombre completo")
    password: Optional[SecretStr] = Field(default=None, min_length=8, max_length=100, description="Nueva contraseña")
    is_active: Optional[bool] = Field(default=None, description="Estado de activación del usuario")
    
    @field_validator('username')
    @classmethod
    def username_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if not v:
                raise ValueError("El nombre de usuario no puede estar vacío")
            if len(v) < 3:
                raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
            if len(v) > 50:
                raise ValueError("El nombre de usuario no puede exceder 50 caracteres")
            return v.strip().lower()
        return v
    
    @field_validator('password')
    @classmethod
    def password_validator(cls, v: Optional[SecretStr]) -> Optional[str]:
        if v is not None:
            password_value = v.get_secret_value()
            if not password_value:
                raise ValueError("La contraseña no puede estar vacía")
            if len(password_value) < 8:
                raise ValueError("La contraseña debe tener al menos 8 caracteres")
            if not any(c.isupper() for c in password_value):
                raise ValueError("La contraseña debe tener al menos una letra mayúscula")
            if not any(c.islower() for c in password_value):
                raise ValueError("La contraseña debe tener al menos una letra minúscula")
            if not any(c.isdigit() for c in password_value):
                raise ValueError("La contraseña debe tener al menos un número")
            return password_value
        return v


class UserResponse(UserBase):
    """Schema para respuesta de usuario sin datos sensibles."""
    
    id: int = Field(description="ID único del usuario")
    role: str = Field(description="Rol del usuario")
    is_active: bool = Field(default=True, description="Estado de activación")
    created_at: datetime = Field(description="Fecha de creación")
    updated_at: Optional[datetime] = Field(default=None, description="Fecha de última actualización")
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "johndoe@example.com",
                "full_name": "John Doe",
                "role": "user",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": None
            }
        }


class Token(BaseSchema):
    """Schema para respuesta de token de acceso."""
    
    access_token: str = Field(description="Token de acceso JWT")
    token_type: str = Field(default="bearer", description="Tipo de token")
    expires_in: Optional[int] = Field(default=1800, description="Tiempo de expiración en segundos")
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 1800
            }
        }


class TokenData(BaseSchema):
    """Schema para datos contenidos en el token JWT."""
    
    username: Optional[str] = Field(default=None, description="Nombre de usuario del token")
    user_id: Optional[int] = Field(default=None, description="ID de usuario del token")
    role: Optional[str] = Field(default=None, description="Rol del usuario del token")
    exp: Optional[datetime] = Field(default=None, description="Fecha de expiración del token")


class UserLogin(BaseSchema):
    """Schema para solicitud de inicio de sesión."""
    
    username: str = Field(min_length=3, max_length=50, description="Nombre de usuario")
    password: SecretStr = Field(min_length=8, max_length=100, description="Contraseña del usuario")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "SecurePass123"
            }
        }


class ErrorResponse(BaseSchema):
    """Schema para respuestas de error genéricas."""
    
    detail: str = Field(description="Mensaje de error detallado")
    error_code: Optional[str] = Field(default=None, description="Código de error específico")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Marca de tiempo del error")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Usuario no encontrado",
                "error_code": "USER_NOT_FOUND",
                "timestamp": "2024-01-01T00:00:00"
            }
        }


class ValidationErrorResponse(BaseSchema):
    """Schema para respuestas de error de validación."""
    
    detail: list = Field(description="Lista de errores de validación")
    error_code: str = Field(default="VALIDATION_ERROR", description="Código de error de validación")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Marca de tiempo del error")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": [
                    {"loc": ["body", "username"], "msg": "El nombre de usuario debe tener al menos 3 caracteres", "type": "value_error"},
                    {"loc": ["body", "email"], "msg": "Correo electrónico inválido", "type": "value_error"}
                ],
                "error_code": "VALIDATION_ERROR",
                "timestamp": "2024-01-01T00:00:00"
            }
        }

// === ARCHIVO: src/repositories/user_repository.py ===
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

// === ARCHIVO: src/repositories/__init__.py ===
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

// === ARCHIVO: __init__.py ===
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

// === ARCHIVO: README.md ===
# API REST de Gestión de Usuarios

## Descripción

API REST desarrollada con FastAPI para la gestión de usuarios en una plataforma fintech. Proporciona funcionalidades completas de CRUD (Crear, Leer, Actualizar, Eliminar) junto con autenticación segura mediante tokens JWT.

## Características

- **Gestión de Usuarios**: Creación, lectura, actualización y eliminación de usuarios
- **Autenticación JWT**: Seguridad basada en tokens web JSON
- **Roles de Usuario**: Sistema de roles (USER, ADMIN, OPERATOR)
- **Validación de Datos**: Validación automática de esquemas con Pydantic
- **Hash de Contraseñas**: Seguridad con bcrypt
- **Configuración Centralizada**: Gestión mediante variables de entorno

## Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:
```bash
git clone <repositorio-url>
cd user-management-api
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\\Scripts\\activate  # Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
```bash
cp .env.example .env
# Edita .env con tu configuración
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=sqlite:///./users.db
JWT_SECRET_KEY=tu_secret_key_aqui
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=30
APP_ENV=development
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

## Ejecución

### Servidor de Desarrollo

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`

### Documentación Interactiva

FastAPI proporciona documentación automática:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Endpoints Disponibles

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/login` | Iniciar sesión y obtener token JWT |
| POST | `/auth/register` | Registrar un nuevo usuario |
| POST | `/auth/refresh` | Renovar token JWT |
| POST | `/auth/logout` | Cerrar sesión |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/users` | Listar todos los usuarios (solo admin) |
| GET | `/users/{user_id}` | Obtener usuario por ID |
| POST | `/users` | Crear nuevo usuario |
| PUT | `/users/{user_id}` | Actualizar usuario |
| DELETE | `/users/{user_id}` | Eliminar usuario (solo admin) |

### Sistema

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Endpoint raíz de la API |
| GET | `/health` | Verificar estado de la API |

## Ejemplos de Uso

### Registro de Usuario

```bash
curl -X POST "http://localhost:8000/auth/register" \\
  -H "Content-Type: application/json" \\
  -d '{
    "username": "juanperez",
    "email": "juan@example.com",
    "password": "SecurePass123!",
    "full_name": "Juan Pérez"
  }'
```

### Inicio de Sesión

```bash
curl -X POST "http://localhost:8000/auth/login" \\
  -H "Content-Type: application/json" \\
  -d '{
    "username": "juanperez",
    "password": "SecurePass123!"
  }'
```

### Obtener Usuario Autenticado

```bash
curl -X GET "http://localhost:8000/users/me" \\
  -H "Authorization: Bearer <tu_token_jwt>"
```

### Listar Usuarios (requiere rol admin)

```bash
curl -X GET "http://localhost:8000/users" \\
  -H "Authorization: Bearer <tu_token_jwt_admin>"
```

### Actualizar Usuario

```bash
curl -X PUT "http://localhost:8000/users/1" \\
  -H "Authorization: Bearer <tu_token_jwt>" \\
  -H "Content-Type: application/json" \\
  -d '{
    "full_name": "Juan Pérez Actualizado",
    "email": "juan.nuevo@example.com"
  }'
```

### Eliminar Usuario

```bash
curl -X DELETE "http://localhost:8000/users/1" \\
  -H "Authorization: Bearer <tu_token_jwt_admin>"
```

## Estructura del Proyecto

```
user-management-api/
├── src/
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py      # Configuración centralizada
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # Modelo de usuario (SQLAlchemy)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py          # Esquemas Pydantic
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── auth_service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── auth.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── security.py
│   └── tests/
│       ├── __init__.py
│       ├── test_users.py
│       └── test_auth.py
├── .env
├── requirements.txt
└── README.md
```

## Ejecución de Tests

```bash
# Todos los tests
pytest

# Tests específicos
pytest src/tests/test_auth.py
pytest src/tests/test_users.py

# Coverage
pytest --cov=src --cov-report=html
```

## Roles de Usuario

| Rol | Permisos |
|-----|----------|
| USER | Leer su propio perfil, actualizar su información |
| OPERATOR | Todas las operaciones de USER + crear usuarios |
| ADMIN | Acceso completo a todos los endpoints |

## Manejo de Errores

La API responde con códigos de estado HTTP estándar:

- `200` - Éxito
- `201` - Creado
- `400` - Solicitud incorrecta
- `401` - No autorizado
- `403` - Prohibido
- `404` - No encontrado
- `422` - Error de validación
- `500` - Error interno del servidor

## Seguridad

- Las contraseñas se almacenan hasheadas con bcrypt
- Tokens JWT con expiración configurable
- Validación de datos en todos los endpoints
- Protección contra ataques comunes (CORS configurado)
- Middleware de manejo de errores centralizado

## Licencia

MIT License - Ver archivo LICENSE para más detalles.

// === ARCHIVO: src/routes/__init__.py ===
from fastapi import APIRouter
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router

api_router = APIRouter()

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["users"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

__all__ = ["api_router", "users_router", "auth_router"]

// === ARCHIVO: src/routes/users.py ===
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

// === ARCHIVO: src/routes/auth.py ===
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Optional
from src.schemas import Token, UserLogin, UserCreate, UserResponse, ErrorResponse
from src.services.auth_service import AuthService
from src.services.user_service import UserService
from src.models import User, UserRole, handle_sqlalchemy_exception
from src.config import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, responses={
    400: {"model": ErrorResponse, "description": "Usuario ya existe o datos inválidos"}
})
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Registra un nuevo usuario en el sistema."""
    pass


@router.post("/login", response_model=Token, responses={
    401: {"model": ErrorResponse, "description": "Credenciales incorrectas"}
})
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Autentica un usuario y retorna un token JWT."""
    pass


@router.post("/logout", status_code=status.HTTP_200_OK, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"}
})
def logout(current_user: User = Depends(get_db)):
    """Cierra la sesión del usuario actual."""
    pass


@router.post("/refresh", response_model=Token, responses={
    401: {"model": ErrorResponse, "description": "Token inválido o expirado"}
})
def refresh_token(
    current_user: User = Depends(get_db)
):
    """Refresca el token JWT del usuario actual."""
    pass


@router.get("/me", response_model=UserResponse, responses={
    401: {"model": ErrorResponse, "description": "No autorizado"}
})
def get_current_user(current_user: User = Depends(get_db)):
    """Retorna la información del usuario autenticado actualmente."""
    pass


from .user_service import UserService
from .auth_service import AuthService

__all__ = ["UserService", "AuthService"]

// === ARCHIVO: src/services/user_service.py ===
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

// === ARCHIVO: src/services/auth_service.py ===
"""Servicio de autenticación JWT.

SUPERFICIE DE PRÁCTICA - Stub para que el estudiante implemente.
"""

from typing import Optional
from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.config.settings import Settings, get_settings
from src.schemas.user import TokenData
from src.models.user import User
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class AuthService:
    """Servicio para autenticación y autorización mediante JWT.
    
    Este es un STUB que el estudiante debe completar.
    """
    
    def __init__(self, settings: Settings):
        self.settings = settings
    
    def authenticate_user(self, username: str, password: str, db: Session) -> Optional[User]:
        """Autentica un usuario con username y contraseña.
        
        TODO: Implementar validación de credenciales.
        """
        pass
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Crea un token JWT de acceso.
        
        TODO: Implementar generación de token JWT.
        """
        pass
    
    def verify_token(self, token: str) -> Optional[TokenData]:
        """Verifica y decodifica un token JWT.
        
        TODO: Implementar verificación de token.
        """
        pass
    
    def get_current_user(self, token: str, db: Session) -> User:
        """Obtiene el usuario actual desde el token JWT.
        
        TODO: Implementar extracción de usuario del token.
        """
        pass
    
    def get_current_active_user(self, current_user: User = Depends(lambda: None)) -> User:
        """Obtiene el usuario actual verificado.
        
        TODO: Implementar verificación de usuario activo.
        """
        pass

// === ARCHIVO: src/utils/__init__.py ===
"""Módulo de utilidades de la aplicación.

Este módulo contiene funciones helper para seguridad, manejo de fechas,
y otras operaciones comunes usadas en toda la aplicación.
"""

from datetime import datetime, timedelta
from typing import Optional, Any
import re

from .security import (
    create_access_token,
    verify_token,
    get_password_hash,
    verify_password
)

# Constantes de tiempo para tokens JWT
TOKEN_EXPIRE_MINUTES = 30
TOKEN_EXPIRE_HOURS = 24
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Constantes de validación
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 50
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def get_token_expiration(expires_delta: Optional[timedelta] = None) -> datetime:
    """Calcula la fecha de expiración de un token.
    
    Args:
        expires_delta: Delta de tiempo personalizado. Si es None, usa 30 minutos.
        
    Returns:
        datetime con la fecha de expiración.
    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return datetime.utcnow() + expires_delta


def is_valid_email(email: str) -> bool:
    """Valida que un email tenga el formato correcto.
    
    Args:
        email: Cadena con el email a validar.
        
    Returns:
        True si el email es válido, False en caso contrario.
    """
    return bool(re.match(EMAIL_PATTERN, email))


def is_valid_username(username: str) -> bool:
    """Valida que un nombre de usuario cumpla las reglas de longitud.
    
    Args:
        username: Cadena con el nombre de usuario.
        
    Returns:
        True si el nombre de usuario es válido.
    """
    if not username:
        return False
    length = len(username)
    return MIN_USERNAME_LENGTH <= length <= MAX_USERNAME_LENGTH


def is_valid_password(password: str) -> bool:
    """Valida que una contraseña cumpla los requisitos mínimos de seguridad.
    
    Args:
        password: Cadena con la contraseña a validar.
        
    Returns:
        True si la contraseña es válida.
    """
    if not password:
        return False
    length = len(password)
    if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
        return False
    return True


def sanitize_string(value: str, max_length: Optional[int] = None) -> str:
    """Limpia una cadena de caracteres potencialmente peligrosos.
    
    Args:
        value: Cadena a sanitizar.
        max_length: Longitud máxima opcional.
        
    Returns:
        Cadena sanitizada.
    """
    if not value:
        return ""
    sanitized = value.strip()
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    return sanitized


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formatea un datetime como cadena legible.
    
    Args:
        dt: Objeto datetime a formatear.
        format_str: Cadena de formato strftime.
        
    Returns:
        Cadena formateada.
    """
    return dt.strftime(format_str)


__all__ = [
    "create_access_token",
    "verify_token",
    "get_password_hash",
    "verify_password",
    "TOKEN_EXPIRE_MINUTES",
    "TOKEN_EXPIRE_HOURS",
    "REFRESH_TOKEN_EXPIRE_DAYS",
    "MIN_PASSWORD_LENGTH",
    "MAX_PASSWORD_LENGTH",
    "MIN_USERNAME_LENGTH",
    "MAX_USERNAME_LENGTH",
    "get_token_expiration",
    "is_valid_email",
    "is_valid_username",
    "is_valid_password",
    "sanitize_string",
    "format_datetime",
]

// === ARCHIVO: src/utils/security.py ===
"""Utilidades de seguridad para autenticación y manejo de contraseñas.

Este módulo proporciona funciones para:
- Hashing y verificación de contraseñas.
- Generación y verificación de tokens JWT.

SUPERFICIE DE PRÁCTICA: Este archivo es el ejercicio a completar.
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any

# TODO: Implementar las funciones de este módulo
# El participante debe completar la lógica de seguridad


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Genera un token JWT de acceso.
    
    Args:
        data: Diccionario con los datos a incluir en el token.
        expires_delta: Tiempo de expiración opcional.
        
    Returns:
        Token JWT como cadena.
    """
    raise NotImplementedError("Implementar create_access_token")


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """Verifica y decodifica un token JWT.
    
    Args:
        token: Token JWT a verificar.
        
    Returns:
        Datos decodificados si el token es válido, None si no lo es.
    """
    raise NotImplementedError("Implementar verify_token")


def get_password_hash(password: str) -> str:
    """Genera el hash de una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano.
        
    Returns:
        Hash de la contraseña.
    """
    raise NotImplementedError("Implementar get_password_hash")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra su hash.
    
    Args:
        plain_password: Contraseña en texto plano.
        hashed_password: Hash de la contraseña almacenado.
        
    Returns:
        True si la contraseña es correcta, False en caso contrario.
    """
    raise NotImplementedError("Implementar verify_password")

// === ARCHIVO: src/config/__init__.py ===
"""Módulo de configuración de la aplicación.

Contiene la configuración centralizada basada en variables de entorno
y constantes de la aplicación.
"""

from typing import Optional, List
import os

from .settings import settings, Settings

# Constantes de la aplicación
APP_NAME = "User Management API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "API REST para gestión de usuarios con autenticación JWT"
APP_AUTHOR = "Pragma Team"

# URLs y endpoints
API_PREFIX = "/api/v1"
DOCS_URL = "/docs"
REDOC_URL = "/redoc"
OPENAPI_URL = "/openapi.json"

# Configuración de CORS
ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
ALLOWED_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE", "PATCH"]
ALLOWED_HEADERS: List[str] = ["*"]

# Configuración de paginación
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# Configuración de rate limiting
RATE_LIMIT_PER_MINUTE = 60
RATE_LIMIT_PER_HOUR = 1000

# Configuración de seguridad
PASSWORD_MIN_LENGTH = 8
PASSWORD_REQUIRE_UPPERCASE = True
PASSWORD_REQUIRE_LOWERCASE = True
PASSWORD_REQUIRE_DIGITS = True
PASSWORD_REQUIRE_SPECIAL = False

# Tiempos de sesión
SESSION_TIMEOUT_MINUTES = 30
REFRESH_TOKEN_DAYS = 7

# Configuración de base de datos
DB_POOL_SIZE = 5
DB_MAX_OVERFLOW = 10
DB_POOL_TIMEOUT = 30
DB_POOL_RECYCLE = 3600


def get_database_url() -> str:
    """Obtiene la URL de la base de datos desde la configuración.
    
    Returns:
        URL de conexión a la base de datos.
    """
    return settings.DATABASE_URL


def get_jwt_secret() -> str:
    """Obtiene la clave secreta para JWT desde la configuración.
    
    Returns:
        Clave secreta JWT.
    """
    return settings.JWT_SECRET.get_secret_value()


def get_jwt_algorithm() -> str:
    """Obtiene el algoritmo JWT configurado.
    
    Returns:
        Algoritmo JWT (HS256 por defecto).
    """
    return "HS256"


def is_development() -> bool:
    """Verifica si la aplicación está en modo desarrollo.
    
    Returns:
        True si está en desarrollo.
    """
    return os.getenv("ENVIRONMENT", "development").lower() == "development"


def is_production() -> bool:
    """Verifica si la aplicación está en modo producción.
    
    Returns:
        True si está en producción.
    """
    return os.getenv("ENVIRONMENT", "development").lower() == "production"


def is_debug_enabled() -> bool:
    """Verifica si el modo debug está habilitado.
    
    Returns:
        True si debug está habilitado.
    """
    return settings.DEBUG


def get_cors_origins() -> List[str]:
    """Obtiene los orígenes permitidos para CORS.
    
    Returns:
        Lista de orígenes permitidos.
    """
    return ALLOWED_ORIGINS


def get_allowed_methods() -> List[str]:
    """Obtiene los métodos HTTP permitidos.
    
    Returns:
        Lista de métodos permitidos.
    """
    return ALLOWED_METHODS


def get_allowed_headers() -> List[str]:
    """Obtiene las cabeceras permitidas.
    
    Returns:
        Lista de cabeceras permitidas.
    """
    return ALLOWED_HEADERS


__all__ = [
    "settings",
    "Settings",
    "APP_NAME",
    "APP_VERSION",
    "APP_DESCRIPTION",
    "APP_AUTHOR",
    "API_PREFIX",
    "DOCS_URL",
    "REDOC_URL",
    "OPENAPI_URL",
    "ALLOWED_ORIGINS",
    "ALLOWED_METHODS",
    "ALLOWED_HEADERS",
    "DEFAULT_PAGE_SIZE",
    "MAX_PAGE_SIZE",
    "RATE_LIMIT_PER_MINUTE",
    "RATE_LIMIT_PER_HOUR",
    "PASSWORD_MIN_LENGTH",
    "PASSWORD_REQUIRE_UPPERCASE",
    "PASSWORD_REQUIRE_LOWERCASE",
    "PASSWORD_REQUIRE_DIGITS",
    "PASSWORD_REQUIRE_SPECIAL",
    "SESSION_TIMEOUT_MINUTES",
    "REFRESH_TOKEN_DAYS",
    "DB_POOL_SIZE",
    "DB_MAX_OVERFLOW",
    "DB_POOL_TIMEOUT",
    "DB_POOL_RECYCLE",
    "get_database_url",
    "get_jwt_secret",
    "get_jwt_algorithm",
    "is_development",
    "is_production",
    "is_debug_enabled",
    "get_cors_origins",
    "get_allowed_methods",
    "get_allowed_headers",
]

// === ARCHIVO: src/tests/__init__.py ===
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

// === ARCHIVO: src/tests/test_users.py ===
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

// === ARCHIVO: src/tests/test_auth.py ===
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
```
