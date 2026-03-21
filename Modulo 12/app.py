from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
import secrets

app = FastAPI()

security = HTTPBasic()

# Armazenamento em memória
minhas_tarefas = {}

# Usuário e senha fixos para exemplo
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "admin"


class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False


def validar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    usuario_valido = secrets.compare_digest(credentials.username, USUARIO_CORRETO)
    senha_valida = secrets.compare_digest(credentials.password, SENHA_CORRETA)

    if not (usuario_valido and senha_valida):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


@app.get("/")
def hello_world():
    return {"Hello": "World!"}


# Listar tarefas com autenticação, paginação e ordenação
@app.get("/tarefas", response_model=List[Tarefa])
def get_tarefas(
    usuario: str = Depends(validar_usuario),
    page: int = Query(1, ge=1, description="Número da página"),
    size: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
    ordenar: str = Query("nome", description="Campo para ordenação: nome ou descricao")
):
    lista_tarefas = list(minhas_tarefas.values())

    if ordenar not in ["nome", "descricao"]:
        raise HTTPException(
            status_code=400,
            detail="Parâmetro de ordenação inválido. Use 'nome' ou 'descricao'."
        )

    lista_tarefas.sort(key=lambda tarefa: getattr(tarefa, ordenar).lower())

    inicio = (page - 1) * size
    fim = inicio + size

    return lista_tarefas[inicio:fim]


# Adicionar tarefa
@app.post("/tarefas")
def post_tarefa(
    tarefa: Tarefa,
    usuario: str = Depends(validar_usuario)
):
    if tarefa.nome in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe!")

    minhas_tarefas[tarefa.nome] = tarefa
    return {"message": "A tarefa foi criada com sucesso!"}


# Marcar tarefa como concluída
@app.put("/tarefas/{nome_tarefa}")
def put_tarefa(
    nome_tarefa: str,
    usuario: str = Depends(validar_usuario)
):
    minha_tarefa = minhas_tarefas.get(nome_tarefa)

    if not minha_tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")

    minha_tarefa.concluida = True
    return {"message": "A tarefa foi marcada como concluída com sucesso!"}


# Deletar tarefa
@app.delete("/tarefas/{nome_tarefa}")
def delete_tarefa(
    nome_tarefa: str,
    usuario: str = Depends(validar_usuario)
):
    if nome_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")

    del minhas_tarefas[nome_tarefa]
    return {"message": "Sua tarefa foi deletada com sucesso!"}