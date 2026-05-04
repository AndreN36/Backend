# FastAPI + Celery + Redis

Este projeto demonstra como usar **FastAPI** com **Celery** e **Redis** para executar tarefas longas em background sem bloquear a API.

## Estrutura do projeto

.
├── celery_app.py
├── main.py
├── pyproject.toml
├── poetry.lock
└── README.md

### Requisitos
Python 3.12
Poetry
Celery
Docker
Redis

### Instalação

Instale as dependências com Poetry:

poetry add fastapi uvicorn celery redis

Caso as dependências já estejam no pyproject.toml, execute:

poetry install

#### Executando o Redis com Docker

Suba um container Redis local:

docker run -d --name redis-local -p 6379:6379 redis

Se o container já existir, apenas inicie:

docker start redis-local

Para verificar se está rodando:

docker ps

### Arquivo celery_app.py

Responsável por:

configurar o broker Redis
configurar o backend Redis
definir as tarefas calcular_soma e calcular_fatorial
manter a chave/lista Redis usada para armazenar os task_id

Configuração usada:

broker="redis://localhost:6379/0"
backend="redis://localhost:6379/1"

### Inicialização do ambiente
## Execute com Poetry:

poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa:

http://127.0.0.1:8000/docs
Executando o worker do Celery

Em outro terminal, execute o seguinte comando para que possa analisar os logs do celery em tempo real:

poetry run celery -A celery_app worker -l info

# Endpoints
## Disparar soma

### POST /soma

Body:

{
  "a": 10,
  "b": 5
}

Resposta esperada:

{
  "mensagem": "Tarefa de soma enviada com sucesso.",
  "task_id": "seu-task-id",
  "status": "PENDING"
}

## Disparar fatorial
### POST /fatorial

Body:

{
  "n": 5
}

Resposta esperada:

{
  "mensagem": "Tarefa de fatorial enviada com sucesso.",
  "task_id": "seu-task-id",
  "status": "PENDING"
}

## Consultar resultado
### GET /resultado/{task_id}

Exemplo:

curl "http://127.0.0.1:8000/resultado/SEU_TASK_ID"

Enquanto estiver processando:

{
  "task_id": "SEU_TASK_ID",
  "status": "PENDING",
  "resultado": null
}

Após finalizar:

{
  "task_id": "SEU_TASK_ID",
  "status": "SUCCESS",
  "resultado": 15
}

## Listar tarefas
### GET /tarefas

Exemplo:

curl "http://127.0.0.1:8000/tarefas"

Resposta esperada:

{
  "total": 2,
  "tarefas": [
    {
      "task_id": "abc123",
      "status": "SUCCESS",
      "resultado": 15
    },
    {
      "task_id": "def456",
      "status": "PENDING",
      "resultado": null
    }
  ]
}

Exemplo de log esperado do worker
[tasks]
  . calcular_fatorial
  . calcular_soma

[INFO/MainProcess] Connected to redis://localhost:6379/0
[INFO/MainProcess] mingle: searching for neighbors
[INFO/MainProcess] mingle: all alone
[INFO/MainProcess] celery@host ready.
[INFO/MainProcess] Task calcular_soma[abc123] received
[INFO/ForkPoolWorker-1] Task calcular_soma[abc123] succeeded in 5.01s: 15

## Observações importantes
A API retorna imediatamente com o task_id.
O processamento ocorre em background pelo worker Celery.
O Redis roda localmente em container Docker.
O Redis DB 0 é usado como broker.
O Redis DB 1 é usado como backend de resultados.
O Redis DB 2 é usado para armazenar a lista de tarefas.
