"""
Version: 1.0.0
Projeto: Gerenciador de Pokédex

Instruções de execução:
* 1. Dentro da pasta do projeto onde esta o pokedex.py, execute o poetry install para instalar 
as dependências.
2. Ative o ambiente virtual criado pelo Poetry com poetry shell.
3. Execute o programa com python pokedex.py.
4. Siga as instruções no menu para gerenciar sua Pokédex.
5. Para sair do programa, escolha a opção "7 - Sair" no menu.
6. Para desativar o ambiente virtual, use o comando exit ou Ctrl+D.

Dependências:
* Esse projeto utiliza um pyproject padrão, visando eveluair o mesmo, 
no entanto para essa versão não há dependências externas, apenas a biblioteca padrão do Python como:

- dict => para armazenar os dados dos Pokémon
- list => armazenar histórico de capturas
- input() => entrada de dados do usuário
- print() => saída de informações
- try/except => tratamento de erros

"""

# Dicionário principal da Pokédex
# Estrutura exemplo:
# {
#     "Pikachu": {"tipo": "Elétrico", "nivel": 25, "capturas": 3},
#     "Charmander": {"tipo": "Fogo", "nivel": 12, "capturas": 1}
# }
pokedex = {}

# Lista para armazenar o histórico de capturas
# Cada item será uma tupla: (nome_pokemon, quantidade_capturada)
historico_capturas = []


def exibir_menu():
    """Exibe o menu principal do programa."""
    print("\n=== POKÉDEX ===")
    print("1 - Adicionar Pokémon")
    print("2 - Listar Pokémon")
    print("3 - Remover Pokémon")
    print("4 - Atualizar nível do Pokémon")
    print("5 - Registrar captura de Pokémon")
    print("6 - Exibir histórico de capturas")
    print("7 - Sair")


def obter_nivel():
    """
    Solicita ao usuário um nível válido entre 1 e 100.
    Continua pedindo até que o valor informado seja válido.
    """
    while True:
        try:
            nivel = int(input("Digite o nível do Pokémon (1 a 100): "))
            if 1 <= nivel <= 100:
                return nivel
            print("Erro: o nível deve estar entre 1 e 100.")
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def obter_quantidade_captura():
    """
    Solicita a quantidade de capturas.
    Deve ser um número inteiro maior que zero.
    """
    while True:
        try:
            quantidade = int(input("Digite a quantidade de vezes capturada: "))
            if quantidade > 0:
                return quantidade
            print("Erro: a quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def adicionar_pokemon():
    """Adiciona um novo Pokémon à Pokédex."""
    nome = input("Digite o nome do Pokémon: ").strip()
    tipo = input("Digite o tipo do Pokémon: ").strip()
    nivel = obter_nivel()

    if nome in pokedex:
        print(f"Erro: o Pokémon '{nome}' já está cadastrado.")
    else:
        pokedex[nome] = {
            "tipo": tipo,
            "nivel": nivel,
            "capturas": 0
        }
        print(f"Pokémon '{nome}' adicionado com sucesso.")


def listar_pokemons():
    """Lista todos os Pokémon cadastrados em ordem alfabética."""
    if not pokedex:
        print("Nenhum Pokémon cadastrado.")
        return

    print("\n=== POKÉMON CADASTRADOS ===")
    for nome in sorted(pokedex.keys()):
        tipo = pokedex[nome]["tipo"]
        nivel = pokedex[nome]["nivel"]
        print(f"{nome} - {tipo} - Nível {nivel}")


def remover_pokemon():
    """Remove um Pokémon da Pokédex pelo nome."""
    nome = input("Digite o nome do Pokémon a ser removido: ").strip()

    if nome in pokedex:
        del pokedex[nome]
        print(f"Pokémon '{nome}' removido com sucesso.")
    else:
        print(f"Erro: o Pokémon '{nome}' não foi encontrado.")


def atualizar_nivel():
    """Atualiza o nível de um Pokémon existente."""
    nome = input("Digite o nome do Pokémon: ").strip()

    if nome in pokedex:
        novo_nivel = obter_nivel()
        pokedex[nome]["nivel"] = novo_nivel
        print(f"Nível do Pokémon '{nome}' atualizado para {novo_nivel}.")
    else:
        print(f"Erro: o Pokémon '{nome}' não foi encontrado.")


def registrar_captura():
    """
    Registra uma captura de Pokémon.
    Soma a quantidade capturada ao campo 'capturas'
    e também salva no histórico.
    """
    nome = input("Digite o nome do Pokémon: ").strip()

    if nome in pokedex:
        quantidade = obter_quantidade_captura()
        pokedex[nome]["capturas"] += quantidade
        historico_capturas.append((nome, quantidade))
        print(f"Captura registrada: '{nome}' foi capturado {quantidade} vez(es).")
    else:
        print(f"Erro: o Pokémon '{nome}' não foi encontrado.")


def exibir_historico():
    """Exibe o histórico de capturas registradas."""
    if not historico_capturas:
        print("Nenhuma captura registrada.")
        return

    print("\n=== HISTÓRICO DE CAPTURAS ===")
    for nome, quantidade in historico_capturas:
        print(f"{nome} - {quantidade} captura(s)")


def main():
    """Função principal de fluxo."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_pokemon()
        elif opcao == "2":
            listar_pokemons()
        elif opcao == "3":
            remover_pokemon()
        elif opcao == "4":
            atualizar_nivel()
        elif opcao == "5":
            registrar_captura()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Entrada do programa
if __name__ == "__main__":
    main()