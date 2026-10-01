# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Desarrollo de una API REST para gestión de usuarios**.

| | |
|---|---|
| Tema | api-rest |
| Nivel | junior-l1 |
| Chapter | Backend |
| Especialidad | Python |
| Stack | Python / FastAPI 0.115.0 |
| Patron arquitectonico | capas estándar (presentación, servicio, persistencia, dominio) |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la instancia de FastAPI`
- `app/domain con entidades y puertos (Protocol o ABC)`
- `app/application con casos de uso`
- `app/infrastructure con repositorios y routers`

Dependencias:

- fastapi 0.115.0
- uvicorn 0.30.6
- sqlalchemy 2.0.32
- pydantic 2.9.1
- python-jose[cryptography] 3.3.0
- passlib[bcrypt] 1.7.4
- python-dotenv 1.0.1
- pydantic-settings 2.4.0
- httpx 0.27.2
- pytest 8.3.2

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && python -c "import app.main"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && python -c "import app.main"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Definición y modelado de la API**: Diagrama de la API REST y modelos de datos definidos.
- **Fase 2 — Implementación de la autenticación JWT**: Implementación de la autenticación JWT en la API REST.
- **Fase 3 — Implementación de los endpoints de gestión de usuarios**: Implementación de los endpoints de gestión de usuarios en la API REST.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `src/routes/auth.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- [ ] `src/services/auth_service.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- [ ] `src/utils/security.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- [ ] `src/tests/test_auth.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.

## Lo que falta y tenes que completar

### 1. Boilerplate del stack (1)

Sin esto el proyecto no compila ni arranca. **Es tu trabajo crearlo**, y no toca nada de lo pedagogico: es andamiaje del stack.

- [ ] **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### 2. Archivos que la arquitectura declara (1 de 20)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `src/services/__init__.py`

### 3. Referencias colgando (3)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `src/models/__init__.py` — `User.extend`
      Se invoca `extend` sobre `User`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- [ ] `src/routes/users.py` — `UserUpdate.model_dump`
      Se invoca `model_dump` sobre `UserUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- [ ] `src/services/user_service.py` — `UserUpdate.dict`
      Se invoca `dict` sobre `UserUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (22)

- `__init__.py`
- `src/main.py`
- `src/config/settings.py`
- `requirements.txt`
- `src/models/__init__.py`
- `src/models/user.py`
- `src/schemas/__init__.py`
- `src/schemas/user.py`
- `src/repositories/user_repository.py`
- `src/repositories/__init__.py`
- `README.md`
- `src/routes/__init__.py`
- `src/routes/users.py`
- `src/routes/auth.py`
- `src/services/user_service.py`
- `src/services/auth_service.py`
- `src/utils/__init__.py`
- `src/utils/security.py`
- `src/config/__init__.py`
- `src/tests/__init__.py`
- `src/tests/test_users.py`
- `src/tests/test_auth.py`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `src`
- `src/routes`
- `src/services`
- `src/models`
- `src/schemas`
- `src/repositories`
- `src/utils`
- `src/config`
- `src/tests`

## Verificacion

```bash
pip install -r requirements.txt && python -c "import app.main"
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **capas estándar (presentación, servicio, persistencia, dominio)**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Brecha que el reto ataca: Crear una API REST con FastAPI, SQLAlchemy y autenticación JWT

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
