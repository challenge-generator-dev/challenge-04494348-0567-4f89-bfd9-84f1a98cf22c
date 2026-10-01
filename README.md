# Desarrollo de una API REST para gestión de usuarios

En el contexto de una plataforma fintech, necesitas desarrollar una API REST que gestione usuarios. La API debe permitir la creación, lectura, actualización y eliminación de usuarios, así como la autenticación mediante JWT. Los usuarios tendrán atributos como nombre, email, contraseña y rol. La API debe manejar errores comunes como usuarios duplicados, contraseñas débiles y tokens expirados. Deberás asegurar la idempotencia en las operaciones de creación y actualización de usuarios, y manejar la consistencia de los datos en caso de fallos temporales del sistema.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | api-rest |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición y modelado de la API

**Objetivo:** Definir y modelar la estructura de la API REST, incluyendo los endpoints y los modelos de datos.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica los endpoints necesarios para la gestión de usuarios.
- Define los modelos de datos para los usuarios, incluyendo los atributos y las restricciones.
- Establece las reglas de validación para los atributos de los usuarios.

**Entregable:** Diagrama de la API REST y modelos de datos definidos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los diferentes roles de los usuarios y cómo afectarán a las operaciones que pueden realizar.
- Piensa en los posibles edge cases y cómo manejarlos.

</details>

### Fase 2: Implementación de la autenticación JWT

**Objetivo:** Implementar la autenticación mediante JWT en la API REST.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Diseña el flujo de autenticación utilizando JWT.
- Implementa la generación y verificación de tokens JWT.
- Maneja los casos de tokens expirados o inválidos.

**Entregable:** Implementación de la autenticación JWT en la API REST.

<details>
<summary>Pistas de conocimiento</summary>

- Investiga sobre la seguridad de los tokens JWT y las mejores prácticas para su implementación.
- Considera cómo manejar los tokens expirados o inválidos y cómo comunicar estos errores al usuario.

</details>

### Fase 3: Implementación de los endpoints de gestión de usuarios

**Objetivo:** Implementar los endpoints para la creación, lectura, actualización y eliminación de usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementa los endpoints para la creación, lectura, actualización y eliminación de usuarios.
- Asegura la idempotencia en las operaciones de creación y actualización de usuarios.
- Maneja los errores comunes como usuarios duplicados y contraseñas débiles.

**Entregable:** Implementación de los endpoints de gestión de usuarios en la API REST.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo asegurar la idempotencia en las operaciones de creación y actualización de usuarios.
- Piensa en los posibles errores comunes y cómo manejarlos de manera efectiva.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuál es su propósito en el contexto de una plataforma fintech?
- **paraQueSirve**: ¿Para qué sirve la autenticación JWT en una API REST y cómo se implementa?
- **comoSeUsa**: ¿Cómo se usan los endpoints de gestión de usuarios en una API REST y qué operaciones permiten?
- **erroresComunes**: ¿Cuáles son los errores comunes en la gestión de usuarios y cómo se manejan en una API REST?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de una API REST con autenticación JWT y gestión de usuarios?

## Criterios de Evaluacion

- Definición y modelado correcto de la API REST y los modelos de datos.
- Implementación efectiva de la autenticación JWT.
- Implementación de los endpoints de gestión de usuarios con idempotencia y manejo de errores comunes.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
