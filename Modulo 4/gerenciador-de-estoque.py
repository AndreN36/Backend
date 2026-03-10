# Dicionário principal do estoque
estoque = {}


# -------- FUNÇÕES --------

def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip().lower()
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    estoque[nome] = {
        "quantidade": quantidade,
        "preço": preco
    }

    print("Produto adicionado com sucesso!")


def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio.")
        return

    for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
        print(f"{nome}: {dados['quantidade']} - {dados['preço']}")


def remover_produto(estoque):
    nome = input("Nome do produto a remover: ").strip().lower()

    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")
    else:
        print("Erro: produto não encontrado.")


def atualizar_quantidade(estoque):
    nome = input("Nome do produto: ").strip().lower()

    if nome in estoque:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[nome]["quantidade"] = nova_qtd
        print("Quantidade atualizada com sucesso!")
    else:
        print("Erro: produto não encontrado.")


def exibir_menu():
    print("\nMenu")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade de produto")
    print("5 - Sair")


# -------- MAIN --------

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(estoque)

        elif opcao == "2":
            listar_produtos(estoque)

        elif opcao == "3":
            remover_produto(estoque)

        elif opcao == "4":
            atualizar_quantidade(estoque)

        elif opcao == "5":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
