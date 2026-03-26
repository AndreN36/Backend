from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
import secrets

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

security = HTTPBasic()

# Usuário e senha fixos para exemplo
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "admin"

# Configuração do banco SQLite com SQLAlchemy
DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TarefaModel(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)


class TarefaResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    concluida: bool = False

class TarefaCreate(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False    


# Cria as tabelas
Base.metadata.create_all(bind=engine)


# Sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.get("/tarefas", response_model=List[TarefaResponse])
def get_tarefas(
    usuario: str = Depends(validar_usuario),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Número da página"),
    size: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
):
    offset = (page - 1) * size

    tarefas = (
        db.query(TarefaModel)
        .offset(offset)
        .limit(size)
        .all()
    )

    return tarefas


# Adicionar tarefa
@app.post("/tarefas")
def post_tarefa(
    tarefa: TarefaCreate,
    usuario: str = Depends(validar_usuario),
    db: Session = Depends(get_db)
):
    tarefa_existente = db.query(TarefaModel).filter(TarefaModel.nome == tarefa.nome).first()

    if tarefa_existente:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe!")

    nova_tarefa = TarefaModel(
        nome=tarefa.nome,
        descricao=tarefa.descricao,
        concluida=tarefa.concluida
    )

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return {"message": "A tarefa foi criada com sucesso!"}


# Marcar tarefa como concluída
@app.put("/tarefas/{tarefa_id}")
def put_tarefa(
    tarefa_id: int,
    usuario: str = Depends(validar_usuario),
    db: Session = Depends(get_db)
):
    minha_tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()

    if not minha_tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")

    minha_tarefa.concluida = True
    db.commit()
    db.refresh(minha_tarefa)

    return {"message": "A tarefa foi marcada como concluída com sucesso!"}


# Deletar tarefa
@app.delete("/tarefas/{tarefa_id}")
def delete_tarefa(
    tarefa_id: int,
    usuario: str = Depends(validar_usuario),
    db: Session = Depends(get_db)
):
    minha_tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()

    if not minha_tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")

    db.delete(minha_tarefa)
    db.commit()

    return {"message": "Sua tarefa foi deletada com sucesso!"}