# 📘 Assignment: Database-backed APIs with SQLite and SQLAlchemy

## 🎯 Objetivo

Construir una API REST en Python que persista datos en una base de datos SQLite usando SQLAlchemy. Los estudiantes aprenderán a definir modelos, ejecutar operaciones CRUD y exponer datos a través de endpoints HTTP.

## ⏱️ Duración estimada

3-5 horas

## ✅ Prerrequisitos

- Conocimientos básicos de Python y estructuras de datos
- Familiaridad con funciones y clases
- Experiencia previa con APIs o FastAPI es útil, pero no obligatoria

## 📦 Archivos incluidos

- `starter-code.py` — Aplicación FastAPI con SQLAlchemy y SQLite
- `requirements.txt` — Dependencias necesarias

## 📝 Tareas

### 🛠️ 1) Crear y configurar la base de datos

#### Descripción
Define un modelo SQLAlchemy para una entidad `Task` y crea la base de datos SQLite junto con la tabla necesaria.

#### Requisitos
La aplicación debe:

- Usar SQLAlchemy ORM para definir un modelo `Task`
- Crear una base de datos local SQLite llamada `tasks.db`
- Inicializar las tablas automáticamente al arrancar la aplicación

### 🛠️ 2) Implementar operaciones CRUD

#### Descripción
Añade los endpoints para crear, leer, actualizar y eliminar tareas desde la base de datos.

#### Requisitos
El servicio debe incluir:

- `GET /tasks` — Lista todas las tareas
- `GET /tasks/{task_id}` — Obtiene una tarea por id
- `POST /tasks` — Crea una tarea nueva
- `PUT /tasks/{task_id}` — Actualiza una tarea existente
- `DELETE /tasks/{task_id}` — Elimina una tarea
- Usar Pydantic para validar entradas y respuestas
- Devolver códigos HTTP correctos (200, 201, 404, 204)

### 🛠️ 3) Mejorar el filtrado y la consistencia de datos

#### Descripción
Soporta filtrado opcional por estado y asegura que las respuestas sean claras.

#### Requisitos
- `GET /tasks?completed=true` debe devolver solo tareas completadas
- Los errores deben devolver JSON con `detail`
- El endpoint `POST /tasks` no debe aceptar una tarea sin título

## 📥 Entregables

- Implementación completa en `starter-code.py`
- Base de datos SQLite creada automáticamente cuando se ejecuta la aplicación

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

3. Abrir `http://127.0.0.1:8000/docs` para probar la API

## 🔗 Recursos útiles

- FastAPI — https://fastapi.tiangolo.com/
- SQLAlchemy — https://docs.sqlalchemy.org/
- SQLite — https://www.sqlite.org/docs.html
