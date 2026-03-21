from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dicionário de tarefas
tarefas = {}

# Validação de dados
class Tarefa(BaseModel):
    nome: str
    descricao: str

# Main route
@app.get("/")
def home():
    return {"mensagem": "API de tarefas com FastAPI"}


# Adicionar uma nova tarefa
@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    if tarefa.nome in tarefas:
        raise HTTPException(status_code=400, detail="Tarefa já cadastrada")

    tarefas[tarefa.nome] = {
        "descricao": tarefa.descricao,
        "concluida": False
    }

    return {
        "mensagem": "Tarefa adicionada com sucesso",
        "tarefa": {
            "nome": tarefa.nome,
            "descricao": tarefas[tarefa.nome]["descricao"],
            "concluida": tarefas[tarefa.nome]["concluida"]
        }
    }


# Listar todas as tarefas
@app.get("/tarefas")
def listar_tarefas():
    lista_tarefas = []

    for nome, dados in tarefas.items():
        lista_tarefas.append({
            "nome": nome,
            "descricao": dados["descricao"],
            "concluida": dados["concluida"]
        })

    return {"tarefas": lista_tarefas}


# Marcar uma tarefa como concluída
@app.put("/tarefas/{nome_tarefa}")
def concluir_tarefa(nome_tarefa: str):
    if nome_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefas[nome_tarefa]["concluida"] = True

    return {
        "mensagem": "Tarefa marcada como concluída",
        "tarefa": {
            "nome": nome_tarefa,
            "descricao": tarefas[nome_tarefa]["descricao"],
            "concluida": tarefas[nome_tarefa]["concluida"]
        }
    }


# Remover uma tarefa
@app.delete("/tarefas/{nome_tarefa}")
def remover_tarefa(nome_tarefa: str):
    if nome_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa_removida = {
        "nome": nome_tarefa,
        "descricao": tarefas[nome_tarefa]["descricao"],
        "concluida": tarefas[nome_tarefa]["concluida"]
    }

    del tarefas[nome_tarefa]

    return {
        "mensagem": "Tarefa removida com sucesso",
        "tarefa": tarefa_removida
    }