from fastapi import HTTPException, Path, APIRouter, Depends
from typing import Annotated
from database import get_db
from sqlmodel import Session, select
from models.tareas_models import (
    Tarea,
    TareaPublic,
    TareaCreate,
    TareaPublicNested,
)

tareas_router = APIRouter()


# TAREAS
@tareas_router.get("/", tags=["Tareas"], response_model=list[TareaPublic])
def ver_tareas(db: Session = Depends(get_db)):
    return db.exec(select(Tarea)).all()


# TAREA
@tareas_router.get(
    "/{id}",
    tags=["Tareas"],
    response_model=TareaPublicNested,
    responses={
        404: {
            "description": "Tarea no encontrada",
            "content": {
                "application/json": {"example": {"detail": "Tarea no encontrada"}}
            },
        }
    },
)
def ver_tarea(id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    tarea_obtenida = db.get(Tarea, id)

    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return tarea_obtenida


# AGREGAR TAREA
@tareas_router.post("/", tags=["Tareas"], response_model=TareaPublicNested)
def agregar_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = Tarea.model_validate(tarea)

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea


# REESCRIBIR TAREA
@tareas_router.put(
    "/{id}",
    tags=["Tareas"],
    response_model=TareaPublic,
    responses={
        404: {
            "description": "Tarea no encontrada",
            "content": {
                "application/json": {"example": {"detail": "Tarea no encontrada"}}
            },
        }
    },
)
def reescribir_tarea(
    id: Annotated[int, Path(gt=0)], tarea: TareaCreate, db: Session = Depends(get_db)
):
    tarea_obtenida = db.get(Tarea, id)

    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea_obtenida.titulo = tarea.titulo
    tarea_obtenida.fecha = tarea.fecha
    tarea_obtenida.prioridad = tarea.prioridad
    tarea_obtenida.materia_id = tarea.materia_id

    db.commit()
    db.refresh(tarea_obtenida)

    return tarea_obtenida


# BORRAR TAREA
@tareas_router.delete(
    "/{id}",
    tags=["Tareas"],
    response_model=list[Tarea],
    responses={
        404: {
            "description": "Tarea no encontrada",
            "content": {
                "application/json": {"example": {"detail": "Tarea no encontrada"}}
            },
        }
    },
)
def borrar_tarea(id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    tarea_obtenida = db.get(Tarea, id)
    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(tarea_obtenida)
    db.commit()

    return db.exec(select(Tarea)).all()
