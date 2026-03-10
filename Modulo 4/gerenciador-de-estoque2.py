# Dicionário principal do estoque
estoque = {}


# -------- FUNÇÕES --------

def adicionar_produto(estoque, nome, quantidade, preco):
    nome = nome.strip()

    if nome in estoque:
        return "Erro: Produto já cadastrado."

    if not str(quantidade).isdigit():
        return "Quantidade inválida."

    # valida preço (aceita "10" ou "10.5")
    preco_txt = str(preco).strip()
    if not preco_txt.replace(".", "", 1).isdigit():
        return "Preço inválido."

    estoque[nome] = {"quantidade": int(quantidade), "preço": float(preco)}
    return f"Produto '{nome}' adicionado com sucesso!"


def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."

    linhas = ["Lista de produtos:"]
    for nome, dados in sorted(estoque.items(), key=lambda x: x[0]):
        qtd = dados["quantidade"]
        preco = dados["preço"]
        linhas.append(f"{nome}: Quantidade disponível - {qtd} | Preço - R${preco:.2f}")
    return "\n".join(linhas)


def remover_produto(estoque, nome):
    nome = nome.strip()

    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    return "Erro: Produto não encontrado."


def atualizar_quantidade(estoque, nome, nova_qtd):
    nome = nome.strip()

    if nome not in estoque:
        return "Erro: Produto não encontrado."

    if not str(nova_qtd).isdigit():
        return "Quantidade inválida."

    estoque[nome]["quantidade"] = int(nova_qtd)
    return f"Quantidade do produto '{nome}' atualizada para {int(nova_qtd)}."



def exibir_menu():
    return (
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair"
    )

# -------- MAIN --------

def main():
    while True:
        print(exibir_menu())
        opcao = input().strip()

        if opcao == "1":
            nome = input("Nome: ")
            quantidade = input("Quantidade: ")
            preco = input("Preço: ")
            print(adicionar_produto(estoque, nome, quantidade, preco))

        elif opcao == "2":
            print(listar_produtos(estoque))

        elif opcao == "3":
            nome = input("Nome do produto: ")
            print(remover_produto(estoque, nome))

        elif opcao == "4":
            nome = input("Nome do produto: ")
            nova_qtd = input("Nova quantidade: ")
            print(atualizar_quantidade(estoque, nome, nova_qtd))

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
