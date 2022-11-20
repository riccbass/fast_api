from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split()
        if len(palavras) < 3:
            raise ValueError('Deve ter mais três palavras')

        if value.islower():
            raise ValueError('O título deve ser em maiúscula')
        return value

    @validator('aulas')
    def validar_aulas(cls, value):

        if value < 12:
            raise ValueError('Aula deve ser mais que 12')

        return value

cursos = [
    Curso(id=1, titulo="Programação para leigos", aulas=42, horas=56),
    Curso(id=2, titulo="Algoritmos de python", aulas=100, horas=20)
]
