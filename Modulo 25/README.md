- API de Livros Assíncrona

API REST desenvolvida com FastAPI, utilizando async/await e gerenciada com Poetry.

- Funcionalidades
Listar livros
Buscar livro por ID
Criar novo livro
Atualizar livro
Deletar livro

- Observação:
Os dados são armazenados em memória, sendo perdidos ao reiniciar a aplicação.

- Tecnologias utilizadas
Python 3.12
FastAPI
Uvicorn
Poetry

- Pré-requisitos

Antes de começar, você precisa ter instalado:

Python 3.12+
Poetry

- Instalar Poetry (caso não tenha)
pip install poetry

ou via script oficial:

curl -sSL https://install.python-poetry.org | python3 -

- Instalação do projeto

Baixe o arquivo main.py.

No mesmo diretório dele instale as dependencias do Poetry:

poetry install

- Executando a aplicação
Opção 1 (recomendada)
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Opção 2 (usando shell do Poetry)
poetry shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

- Acessando a API

Após iniciar o servidor:

API:

http://127.0.0.1:8000

Swagger (documentação interativa):

http://127.0.0.1:8000/docs


- Endpoints
🔹 GET http://127.0.0.1:8000/livros

Lista todos os livros

🔹 POST http://127.0.0.1:8000/livros

Cria um novo livro

Exemplo de body(Pode ser validado pelo Swagger):
{
  "id": 1,
  "titulo": "História da Alimentação",
  "autor": "Giles Fumey",
  "ano": 2015
}
🔹 PUT http://127.0.0.1:8000/livros/{id}

Atualiza um livro existente

🔹 DELETE http://127.0.0.1:8000/livros/{id}

Remove um livro