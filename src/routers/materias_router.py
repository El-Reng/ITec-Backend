from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlmodel import Session, select

from database import get_db
from models.materias_models import Materia, MateriaCreate, MateriaPublic

materias_router = APIRouter()


@materias_router.get("/", tags=["Materias"], response_model=list[MateriaPublic])
def ver_materias(db: Session = Depends(get_db)):
    return db.exec(select(Materia)).all()


@materias_router.get("/{id}", tags=["Materias"], response_model=MateriaPublic)
def ver_materia(id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    materia = db.get(Materia, id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia


@materias_router.post("/", tags=["Materias"], response_model=MateriaPublic)
def agregar_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    nueva_materia = Materia.model_validate(materia)
    db.add(nueva_materia)
    db.commit()
    db.refresh(nueva_materia)
    return nueva_materia
