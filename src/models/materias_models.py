from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .tareas_models import Tarea


class MateriaBase(SQLModel):
    nombre: str
    anio: str


class Materia(MateriaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tareas: list["Tarea"] = Relationship(back_populates="materia")


class MateriaCreate(MateriaBase):
    pass


class MateriaPublic(MateriaBase):
    id: int
