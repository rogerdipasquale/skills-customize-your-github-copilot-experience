# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprender a diseñar e implementar una API REST básica usando el framework FastAPI. Los estudiantes construirán un servicio con operaciones CRUD, validación de datos, documentación automática y pruebas básicas.

## ⏱️ Duración estimada

3-5 horas

## ✅ Prerrequisitos

- Conocimientos básicos de Python (funciones, listas, diccionarios)
- Python 3.8+ instalado
- Familiaridad básica con HTTP y JSON

## 📦 Archivos incluidos

- `starter-code.py` — Esqueleto inicial de la aplicación FastAPI
- `requirements.txt` — Dependencias necesarias

## 📝 Tareas

### 🛠️ 1) API CRUD de tareas (Tasks)

#### Descripción
Implementa una API para gestionar una lista de "tasks" con los endpoints básicos: crear, leer (uno y lista), actualizar y eliminar.

#### Requisitos
El servicio debe:

- Exponer los siguientes endpoints:
  - `GET /tasks` — Lista todas las tareas
  - `GET /tasks/{task_id}` — Devuelve una tarea por id
  - `POST /tasks` — Crea una nueva tarea
  - `PUT /tasks/{task_id}` — Actualiza una tarea existente
  - `DELETE /tasks/{task_id}` — Elimina una tarea
- Usar Pydantic para validación de entrada y modelos de respuesta
- Mantener los datos en memoria (por ejemplo, una lista o dict) — no es necesario persistir en BD
- Devolver códigos HTTP apropiados (200, 201, 404, 400, 204)
- Documentación automática disponible en `/docs`

### 🛠️ 2) Búsqueda y filtrado (opcional)

#### Descripción
Añade soporte para filtrar tareas por estado (por ejemplo: `completed=true`) y búsqueda por título.

#### Requisitos
- `GET /tasks?completed=true&search=keyword` debe filtrar la lista según los parámetros proporcionados.

### 🛠️ 3) Manejo de errores y respuestas claras

#### Descripción
Asegúrate de manejar errores comunes (recurso no encontrado, datos inválidos) y devolver mensajes JSON claros.

#### Requisitos
- Respuestas de error deben incluir `detail` con mensaje legible.

## 📥 Entregables

- Implementación completa en `starter-code.py` (o archivos adicionales si lo prefieres)
- Instrucciones para ejecutar la API localmente

## 🧪 Pruebas y evaluación

- La API será probada manualmente con `curl` o `httpie` y la interfaz Swagger en `/docs`.
- Puntos clave: rutas correctas, validación con Pydantic, códigos HTTP adecuados, documentación automática.

## 🔧 Cómo ejecutar (local)

1. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Ejecutar la aplicación

```bash
uvicorn starter-code:app --reload --port 8000
```

3. Abrir `http://localhost:8000/docs` para la documentación interactiva

## 🔗 Recursos útiles

- FastAPI — https://fastapi.tiangolo.com/
- Pydantic — https://pydantic-docs.helpmanual.io/
- Uvicorn — https://www.uvicorn.org/
