from contextlib import asynccontextmanager
from typing import List, Optional

import json
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_CACHE_KEY = "livros"
REDIS_TTL_SECONDS = 60


class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str
    disponivel: bool = True


# "Banco" em memória temporario
livros_db: List[Livro] = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        decode_responses=True
    )
    try:
        yield
    finally:
        await app.state.redis.aclose()


app = FastAPI(
    title="API de Livros com Redis",
    version="1.0.0",
    lifespan=lifespan
)


def obter_redis():
    return app.state.redis


async def salvar_livros_redis(livros: List[Livro]) -> None:
    """
    Salva a lista de livros no Redis com TTL.
    """
    redis_client = obter_redis()
    livros_json = json.dumps([livro.model_dump() for livro in livros], ensure_ascii=False)
    await redis_client.set(REDIS_CACHE_KEY, livros_json, ex=REDIS_TTL_SECONDS)


async def deletar_livros_redis() -> None:
    """
    Remove a chave de cache dos livros no Redis.
    """
    redis_client = obter_redis()
    await redis_client.delete(REDIS_CACHE_KEY)


@app.get("/")
async def healthcheck():
    return {"mensagem": "API de livros com Redis está no ar"}


@app.get("/livros", response_model=List[Livro])
async def listar_livros():
    """
    Primeiro tenta retornar os livros do Redis.
    Se não encontrar no cache, busca da lista em memória,
    salva no Redis e retorna os dados.
    """
    redis_client = obter_redis()
    cache = await redis_client.get(REDIS_CACHE_KEY)

    if cache:
        livros_cache = json.loads(cache)
        return [Livro(**livro) for livro in livros_cache]

    await salvar_livros_redis(livros_db)
    return livros_db


@app.post("/livros", response_model=Livro, status_code=201)
async def criar_livro(livro: Livro):
    """
    Adiciona um novo livro e invalida o cache.
    """
    for item in livros_db:
        if item.id == livro.id:
            raise HTTPException(status_code=400, detail="Já existe um livro com esse ID")

    livros_db.append(livro)
    await deletar_livros_redis()
    return livro


@app.put("/livros/{livro_id}", response_model=Livro)
async def atualizar_livro(livro_id: int, livro_atualizado: Livro):
    """
    Atualiza um livro existente e invalida o cache.
    """
    for indice, livro in enumerate(livros_db):
        if livro.id == livro_id:
            if livro_atualizado.id != livro_id:
                raise HTTPException(
                    status_code=400,
                    detail="O ID do corpo deve ser igual ao ID da URL"
                )

            livros_db[indice] = livro_atualizado
            await deletar_livros_redis()
            return livro_atualizado

    raise HTTPException(status_code=404, detail="Livro não encontrado")


@app.delete("/livros/{livro_id}")
async def deletar_livro(livro_id: int):
    """
    Remove um livro e invalida o cache.
    """
    for indice, livro in enumerate(livros_db):
        if livro.id == livro_id:
            del livros_db[indice]
            await deletar_livros_redis()
            return {"mensagem": "Livro removido com sucesso"}

    raise HTTPException(status_code=404, detail="Livro não encontrado")


@app.get("/cache/livros")
async def verificar_cache():
    """
    Endpoint auxiliar para verificar o conteúdo salvo no Redis.
    """
    redis_client = obter_redis()
    cache = await redis_client.get(REDIS_CACHE_KEY)

    if not cache:
        return {"cache": None, "mensagem": "Nenhum dado em cache"}

    return {"cache": json.loads(cache)}