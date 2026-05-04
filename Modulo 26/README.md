# API de Livros com FastAPI e Redis

Este projeto é uma API simples de livros desenvolvida com **FastAPI**, utilizando **Redis** como cache para armazenar temporariamente a lista de livros.

A aplicação permite:

- Listar livros
- Criar livros
- Atualizar livros
- Remover livros
- Verificar o conteúdo salvo no cache Redis

---

## Tecnologias utilizadas

- python = 3.12
- uvicorn = 0.42.0
- fastapi = 0.135.2
- redis = 5.0.0
- docker = 28.2.2
- poetry = 1.8.2

---

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.12
- pip
- Docker
- poetry

---

## Instalação das dependências

- Adicione as dependências do projeto:

poetry add fastapi uvicorn redis

- Faça a instalcação efetiva:

poetry install

- Ativando o ambiente virtual:

poetry shell

- Executando o Redis com Docker

Como a aplicação roda localmente e o Redis roda em Docker, é necessário expor a porta 6379 do container para a máquina local.

Execute o comando:

docker run --name redis-local -p 6379:6379 -d redis

Verifique se o container está rodando:

docker ps

Você deverá ver o container redis-local em execução, algo como o exemplo abaixo:

CONTAINER ID   IMAGE     COMMAND                  CREATED        STATUS        PORTS                                         NAMES
070105578ae0   redis     "docker-entrypoint.s…"   21 hours ago   Up 21 hours   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   redis-local

## Configuração do Redis na aplicação

No código da aplicação, a configuração do Redis está definida assim:

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_CACHE_KEY = "livros"
REDIS_TTL_SECONDS = 60

Como somente o Redis está em Docker e a API está rodando fora do container, o host deve ser:

REDIS_HOST = "localhost"

Caso a aplicação também fosse executada em Docker, o host poderia ser o nome do serviço/container, por exemplo:

REDIS_HOST = "redis-local"

Obs.: Caso a instalação do Redis renha sido feita local diretamente no host a opção com localhost também irá funcionar corretamente.

## Executando a API

Salve o código em um arquivo chamado main.py.

Você pode rodar a aplicação diretamente com:

poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

A aplicação ficará disponível em:

http://127.0.0.1:8000

O Swagger FastAPI estará disponível em:

http://127.0.0.1:8000/docs

## Testando a API

- Healthcheck
GET /

Resposta esperada:

{
  "mensagem": "API de livros com Redis está no ar"
}

- Criar um livro
POST /livros

Exemplo de body JSON:

{
    "id": 1,
    "titulo": "No body knows",
    "autor": "Steve",
    "ano": 2010,
    "genero": "Terror",
    "disponivel": true
}

- Listar livros
GET /livros

Na primeira chamada, os dados são buscados da lista em memória e salvos no Redis.

Nas próximas chamadas, enquanto o cache estiver válido, os dados serão retornados diretamente do Redis.

- Atualizar um livro
PUT /livros/1

Exemplo de body JSON alterando o valor de true para false:

{
    "id": 1,
    "titulo": "No body knows",
    "autor": "Steve",
    "ano": 2010,
    "genero": "Terror",
    "disponivel": false
}

Ao atualizar um livro, o cache é removido para evitar dados desatualizados.

- Deletar um livro
DELETE /livros/1

Ao remover um livro, o cache também é invalidado.

- Verificar o cache
GET /cache/livros

Se houver dados no Redis, será retornado o conteúdo salvo no cache, como por exemplo:
{
    "cache": [
        {
            "id": 1,
            "titulo": "No body knows",
            "autor": "Steve",
            "ano": 2010,
            "genero": "Terror",
            "disponivel": true
        }
    ]
}

Se não houver cache, a resposta será:

{
  "cache": null,
  "mensagem": "Nenhum dado em cache"
}

## Verificando dados diretamente no Redis

Acesse o terminal do container Redis:

docker exec -it redis-local redis-cli

Dentro do Redis CLI, execute:

SCAN 0

Para visualizar o conteúdo da chave livros:

get livros

Para verificar o tempo restante do cache:

ttl livros

Para sair do Redis CLI:

exit

## Observação sobre o cache

O cache dos livros possui tempo de expiração de 60 segundos, definido pela constante:

REDIS_TTL_SECONDS = 60

Após esse tempo, a chave livros expira automaticamente no Redis.

Sempre que um livro é criado, atualizado ou removido, o cache é deletado para garantir que os dados retornados estejam atualizados.

## Encerrando o Redis

Para parar o container:

docker stop redis-local

Para remover o container:

docker rm redis-local

## Resumo do fluxo
O usuário cria livros usando POST /livros.
Ao listar livros com GET /livros, a API verifica primeiro o Redis.
Se existir cache, os dados são retornados do Redis.
Se não existir cache, os dados vêm da lista em memória e são salvos no Redis.
Ao criar, atualizar ou deletar livros, o cache é invalidado.