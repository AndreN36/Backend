from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Usuário fixo da aplicação
USUARIO_FIXO = {
    "email": "admin@email.com",
    "senha": "123456"
}


class LoginRequest(BaseModel):
    email: str
    senha: str


@app.post("/auth/login")
def login(dados: LoginRequest):
    if (
        dados.email == USUARIO_FIXO["email"]
        and dados.senha == USUARIO_FIXO["senha"]
    ):
        return {
            "mensagem": "Autenticação realizada com sucesso",
            "token": "token-fake-123"
        }

    raise HTTPException(
        status_code=401,
        detail="Credenciais inválidas"
    )