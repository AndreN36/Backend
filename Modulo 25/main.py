from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI(
    title="API de Livros Assíncrona",
    description="API REST com FastAPI utilizando async/await",
    version="1.0.0"
)

# Modelo de dados
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int

# Lista em memória (inicialmente vazia)
livros: List[Livro] = []

# Endpoint raiz
@app.get("/")
async def home():
    await asyncio.sleep(0.1)
    return {"mensagem": "API de livros funcionando"}

# GET - listar todos os livros
@app.get("/livros", response_model=List[Livro])
async def listar_livros():
    await asyncio.sleep(0.1)
    return livros

# GET - buscar livro por ID
@app.get("/livros/{id}", response_model=Livro)
async def buscar_livro(id: int):
    await asyncio.sleep(0.1)

    for livro in livros:
        if livro.id == id:
            return livro

    raise HTTPException(status_code=404, detail="Livro não encontrado")

# POST - criar novo livro
@app.post("/livros", response_model=Livro, status_code=201)
async def criar_livro(novo_livro: Livro):
    await asyncio.sleep(0.1)

    # Verifica se já existe ID
    for livro in livros:
        if livro.id == novo_livro.id:
            raise HTTPException(status_code=400, detail="ID já existe")

    livros.append(novo_livro)
    return novo_livro

# PUT - atualizar livro
@app.put("/livros/{id}", response_model=Livro)
async def atualizar_livro(id: int, livro_atualizado: Livro):
    await asyncio.sleep(0.1)

    for i, livro in enumerate(livros):
        if livro.id == id:
            livro_atualizado.id = id
            livros[i] = livro_atualizado
            return livro_atualizado

    raise HTTPException(status_code=404, detail="Livro não encontrado")

# DELETE - remover livro
@app.delete("/livros/{id}")
async def deletar_livro(id: int):
    await asyncio.sleep(0.1)

    for i, livro in enumerate(livros):
        if livro.id == id:
            livro_removido = livros.pop(i)
            return {
                "mensagem": "Livro removido com sucesso",
                "livro": livro_removido
            }

    raise HTTPException(status_code=404, detail="Livro não encontrado")