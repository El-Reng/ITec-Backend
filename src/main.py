from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.materias_router import materias_router
from routers.tareas_router import tareas_router
import models

app = FastAPI()

app.title = "API - Rojo Leonel"
app.summary = "Práctico 4: SQLModel y Alembic"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=tareas_router, prefix="/tareas")
app.include_router(router=materias_router, prefix="/materias")
