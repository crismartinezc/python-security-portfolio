from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Pro Backend Automation API", version="1.0")

# Esquema de datos de entrada validado estrictamente con Pydantic
class TaskItem(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    priority: int = Field(default=1, ge=1, le=5)
    tags: List[str] = []

# Base de datos simulada en memoria para pruebas rápidas de arquitectura
fake_db = []

@app.post("/tasks/", status_code=201)
def create_task(task: TaskItem):
    """
    Crea una tarea validando automáticamente tipos y restricciones con Pydantic.
    """
    task_dict = task.dict()
    fake_db.append(task_dict)
    return {"message": "Task created successfully", "task": task_dict}

@app.get("/tasks/")
def get_tasks():
    """
    Retorna el listado de todas las tareas registradas en el sistema.
    """
    return {"total": len(fake_db), "tasks": fake_db}