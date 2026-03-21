from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dicionário para armazenar as tarefas
minhas_tarefas = {}

# Modelo Pydantic
class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False


@app.get("/")
def hello_world():
    return {"Hello": "World!"}


# Listar tarefas
@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa!"}

    return list(minhas_tarefas.values())


# Adicionar tarefa
@app.post("/adiciona")
def post_tarefa(tarefa: Tarefa):
    if tarefa.nome in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe!")
    else:
        minhas_tarefas[tarefa.nome] = tarefa
        return {"message": "A tarefa foi criada com sucesso!"}


# Marcar tarefa como concluída
@app.put("/atualiza/{nome_tarefa}")
def put_tarefa(nome_tarefa: str):
    minha_tarefa = minhas_tarefas.get(nome_tarefa)

    if not minha_tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    else:
        minha_tarefa.concluida = True
        return {"message": "A tarefa foi marcada como concluída com sucesso!"}


# Deletar tarefa
@app.delete("/deletar/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str):
    if nome_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    else:
        del minhas_tarefas[nome_tarefa]
        return {"message": "Sua tarefa foi deletada com sucesso!"}