# 📦 FastAPI Docker Architecture

Este projeto demonstra a arquitetura de uma aplicação FastAPI containerizada utilizando Docker e Docker Compose.

---

## 🔧 Componentes

### 1. main.py

Arquivo principal da aplicação FastAPI.

Responsável por:

* Definir endpoints HTTP
* Implementar a lógica da aplicação
* Responder às requisições dos clientes

---

### 2. Dockerfile

Arquivo responsável por definir a construção da imagem Docker.

Ele executa:

* Definição da imagem base
* Instalação das dependências
* Cópia do código da aplicação

---

### 3. Docker Image

A imagem Docker é um artefato criado a partir do Dockerfile.

Ela contém:

* Ambiente de execução
* Dependências
* Código da aplicação

---

### 4. Container em Execução

O container é uma instância da imagem Docker.

Responsável por:

* Executar a aplicação FastAPI
* Processar requisições
* Utilizar recursos do sistema host

---

### 5. docker-compose.yml

Arquivo responsável por orquestrar o ambiente.

Define:

* Build da imagem
* Criação do container e orquestração
* Mapeamento de portas
* Volumes
* Variáveis de ambiente

---

## 🔄 Fluxo da Aplicação

1. O cliente externo envia uma requisição HTTP
2. A requisição chega ao host (localhost:8000)
3. O Docker redireciona para o container (porta 8000)
4. O container executa o servidor FastAPI
5. O FastAPI processa a requisição (main.py)
6. A resposta retorna ao cliente

---

## 📊 Diagrama da Arquitetura

O diagrama ilustra:

* A máquina host contendo os arquivos locais
* O ambiente Docker com a imagem e container
* O fluxo de execução da aplicação
* O mapeamento de portas
* A comunicação com clientes externos

