from fastapi import FastAPI, HTTPException, Response, Path, Query, Header, Depends
from models import Curso, cursos
from typing import List, Optional, Any, Dict

from time import sleep

def fake_db():

    try:

        print('Abrindo conexão com banco de dados')
        sleep(1)
    finally:

        print('Fechando conexão com banco de dados')
        sleep(1)

app = FastAPI(
    title='API de Cursos da Geek University',
    version="0.01",
    description="Uma api para estudo do FastAPI"
)



@app.get("/cursos", 
    description="retorna todos os cursos ou uma lista vazia", 
    summary="retorna todos os cursos",
    response_model=List[Curso],
    response_description="Cursos encontrados com sucesso")
async def get_cursos(db: Any = Depends(fake_db)):

    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None, title="id do curso", description='Deve ser entre 1 e 2', gt=0,lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=404, detail="curso não encontrado")

@app.post("/cursos", status_code=201, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):

    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):

    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso

    else:

        raise HTTPException(status_code=404, detail=f"Não existe curso id {curso_id}")

@app.delete("/cursos/{curso_id}",)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    try:
        del cursos[curso_id]
        return Response(status_code=204 )
    except KeyError:
        raise HTTPException(status_code=404, detail="curso não encontrado")

@app.get("/calculadora")
async def calcular( x_geek: str = Header(default=None), a: int = Query(default=None, gt=5) , b:int = Query(default=None, gt=10), c:Optional[int] = Query(default=None)  ):

    soma = a + b + c

    print(f'X-GEEK {x_geek}')

    return {'Resultado: ', soma}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)