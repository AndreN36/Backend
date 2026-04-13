# 🚀 FastAPI com Docker, Docker Compose e Poetry

Este projeto demonstra como executar uma aplicação Python utilizando **FastAPI**, **Docker**, **Docker Compose** e **Poetry**, garantindo um ambiente consistente e reproduzível.

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

* Docker
* Docker Compose (ou Docker com suporte ao comando `docker compose`)

---

## 📥 Como clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd fastapi-docker-poetry
```

---

## 🐳 Como construir e executar a aplicação

Para construir a imagem e iniciar os containers em segundo plano:

```bash
docker-compose up --build -d
```

ou (versão mais recente do Docker):

```bash
docker compose up --build -d
```

---

## 🌐 Como acessar a aplicação

Após iniciar os containers, acesse:

* Aplicação: http://localhost:8000
* Documentação Swagger: http://localhost:8000/docs
---

## 🔄 Atualização em tempo real (Hot Reload)

O projeto utiliza volume Docker para sincronizar o código local com o container:

```yaml
volumes:
  - ./app:/app/app
```

Isso permite que alterações no código sejam refletidas automaticamente.

---

## 🛑 Como parar os containers

Para parar e remover os containers:

```bash
docker-compose down
```

ou:

```bash
docker compose down
```

---

## 📊 Logs da aplicação

Para visualizar os logs em tempo real:

```bash
docker compose logs -f
```

---

## ♻️ Reinício automático

O container está configurado com política de reinício automático:

```yaml
restart: unless-stopped
```

Isso garante que ele será reiniciado automaticamente em caso de falha.

---

## 📁 Estrutura do projeto

```text
fastapi-docker-poetry/
├── app/
│   └── pokedex.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
└── README.md
```


