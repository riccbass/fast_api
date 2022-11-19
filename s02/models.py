from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="Programação leigos", aulas=42, horas=56),
    Curso(id=2, titulo="Algoritmos", aulas=100, horas=20)
]
