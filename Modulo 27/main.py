from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from celery.result import AsyncResult
import redis

from celery_app import calcular_soma, calcular_fatorial, celery, redis_client, REDIS_TASK_LIST_KEY


app = FastAPI(title="API com FastAPI + Celery + Redis")

# Modelos de dados para requisições

class SomaRequest(BaseModel):
    a: float
    b: float


class FatorialRequest(BaseModel):
    n: int = Field(..., ge=0)

# Rota home para validação rápida da API
@app.get("/")
async def root():
    return {"mensagem": "API no ar com FastAPI, Celery e Redis"}


# Rota para disparar tarefa de soma
@app.post("/soma")
async def disparar_soma(dados: SomaRequest):
    tarefa = calcular_soma.delay(dados.a, dados.b)

    redis_client.lpush(REDIS_TASK_LIST_KEY, tarefa.id)

    return {
        "mensagem": "Tarefa de soma enviada com sucesso.",
        "task_id": tarefa.id,
        "status": "PENDING",
    }

# Rota para disparar tarefa de fatorial
@app.post("/fatorial")
async def disparar_fatorial(dados: FatorialRequest):
    tarefa = calcular_fatorial.delay(dados.n)

    redis_client.lpush(REDIS_TASK_LIST_KEY, tarefa.id)

    return {
        "mensagem": "Tarefa de fatorial enviada com sucesso.",
        "task_id": tarefa.id,
        "status": "PENDING",
    }

# Rota para consultar resultado de uma tarefa com ID específico
@app.get("/resultado/{task_id}")
async def consultar_resultado(task_id: str):
    resultado = AsyncResult(task_id, app=celery)

    if resultado.state == "PENDING":
        return {
            "task_id": task_id,
            "status": resultado.state,
            "resultado": None,
        }

    if resultado.state == "FAILURE":
        raise HTTPException(
            status_code=500,
            detail={
                "task_id": task_id,
                "status": resultado.state,
                "erro": str(resultado.result),
            },
        )

    return {
        "task_id": task_id,
        "status": resultado.state,
        "resultado": resultado.result,
    }


# Rota para listar todas as tarefas e seus status (consulta geral)

@app.get("/tarefas")
async def listar_tarefas():
    task_ids = redis_client.lrange(REDIS_TASK_LIST_KEY, 0, -1)

    tarefas = []

    for task_id in task_ids:
        resultado = AsyncResult(task_id, app=celery)

        tarefas.append({
            "task_id": task_id,
            "status": resultado.state,
            "resultado": resultado.result if resultado.state == "SUCCESS" else None,
        })

    return {
        "total": len(tarefas),
        "tarefas": tarefas,
    }
