from sqlmodel import Field, Relationship, SQLModel

from .materias_models import Materia


class TareaBase(SQLModel):
    titulo: str = Field(index=True)
    fecha: str
    prioridad: str
    materia_id: int | None = Field(default=None, foreign_key="materia.id")


class Tarea(TareaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    materia: Materia | None = Relationship(back_populates="tareas")


class TareaCreate(TareaBase):
    pass


class TareaPublic(TareaBase):
    id: int


class TareaPublicNested(TareaPublic):
    materia: Materia | None = None
