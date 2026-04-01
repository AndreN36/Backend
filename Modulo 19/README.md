# 🧾 Pokédex CLI - Gerenciador de Pokémon

Projeto desenvolvido em Python para gerenciamento de uma Pokédex via linha de comando (CLI), permitindo controlar Pokémon, níveis e histórico de capturas.

---

## 🚀 Objetivo

Este projeto tem como objetivo consolidar conceitos fundamentais de programação em Python, como:

- Estruturas de dados (`dict`, `list`)
- Controle de fluxo
- Funções
- Validação de entrada
- Organização de código

---

## ⚙️ Funcionalidades

O sistema permite:

### 📌 Gerenciamento de Pokémon
- Adicionar Pokémon (nome, tipo e nível)
- Listar Pokémon em ordem alfabética
- Remover Pokémon
- Atualizar nível

### 🎯 Capturas
- Registrar capturas de Pokémon
- Armazenar quantidade de capturas por Pokémon
- Exibir histórico de capturas

### 🧭 Sistema interativo
- Menu em CLI
- Validação de entradas
- Feedback de erros e sucesso

---

## 🧱 Estrutura de Dados

### Pokédex

```python
{
  "Pikachu": {"tipo": "Elétrico", "nivel": 25, "capturas": 3}
}