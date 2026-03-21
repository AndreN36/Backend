# Dicionário de livros
biblioteca = {}

# Lista para armazenar o histórico de empréstimos
historico_emprestimos = []

# Loop principal
while True:

    # Menu
    print("\n=== MENU BIBLIOTECA ===")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Remover livro")
    print("4 - Atualizar quantidade de livros")
    print("5 - Registrar empréstimo")
    print("6 - Exibir histórico de empréstimos")
    print("7 - Sair")

    # Entrada opção
    opcao = input("Escolha uma opção: ")

    
    # OPÇÃO 1 - ADICIONAR LIVRO
    
    if opcao == "1":
        titulo = input("Digite o título do livro: ").strip()
        autor = input("Digite o nome do autor: ").strip()

        try:
            # Converte para inteiro
            quantidade = int(input("Digite a quantidade de exemplares: "))

            # Validação para evitar números negativos
            if quantidade < 0:
                print("Erro: a quantidade não pode ser negativa.")
            else:
                # Adiciona ou atualiza o livro (Sobreescrevendo se já existir)
                biblioteca[titulo] = {
                    "autor": autor,
                    "quantidade": quantidade
                }
                print("Livro adicionado com sucesso.")

        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("Erro: digite um número inteiro válido para a quantidade.")

   
    # OPÇÃO 2 - LISTAR LIVROS
    elif opcao == "2":

        # Verifica se há livros cadastrados
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        else:
            print("\n=== LIVROS CADASTRADOS ===")

            for titulo in sorted(biblioteca.keys()):
                autor = biblioteca[titulo]["autor"]
                quantidade = biblioteca[titulo]["quantidade"]
                print(f"{titulo} - {autor} - {quantidade} disponível(is)")

    
    # OPÇÃO 3 - REMOVER LIVRO
    elif opcao == "3":
        titulo = input("Digite o título do livro a ser removido: ").strip()

        # Verifica se o livro existe no dicionário
        if titulo in biblioteca:
            del biblioteca[titulo]  # Remove o livro
            print("Livro removido com sucesso.")
        else:
            print("Erro: livro não encontrado.")

    # OPÇÃO 4 - ATUALIZAR QUANTIDADE DE LIVROS
    elif opcao == "4":
        titulo = input("Digite o título do livro: ").strip()

        # Verifica se o livro existe
        if titulo in biblioteca:
            try:
                nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))

                # Validação de número negativo
                if nova_quantidade < 0:
                    print("Erro: a quantidade não pode ser negativa.")
                else:
                    # Atualiza o valor
                    biblioteca[titulo]["quantidade"] = nova_quantidade
                    print("Quantidade atualizada com sucesso.")

            except ValueError:
                print("Erro: digite um número inteiro válido.")
        else:
            print("Erro: livro não encontrado.")

    # OPÇÃO 5 - REGISTRAR EMPRÉSTIMO
    elif opcao == "5":
        titulo = input("Digite o título do livro para empréstimo: ").strip()

        # Verifica se o livro existe
        if titulo in biblioteca:
            try:
                quantidade_emprestimo = int(input("Digite a quantidade de exemplares a ser emprestada: "))

                # Validação de número negativo ou zero
                if quantidade_emprestimo <= 0:
                    print("Erro: a quantidade deve ser maior que zero.")

                # Verifica se há exemplares suficientes
                elif biblioteca[titulo]["quantidade"] >= quantidade_emprestimo:
                    
                    # Atualiza a quantidade disponível
                    biblioteca[titulo]["quantidade"] -= quantidade_emprestimo

                    # Registra o empréstimo no histórico
                    historico_emprestimos.append((titulo, quantidade_emprestimo))

                    print("Empréstimo registrado com sucesso.")
                else:
                    print("Erro: não há exemplares suficientes disponíveis.")

            except ValueError:
                print("Erro: digite um número inteiro válido.")
        else:
            print("Erro: livro não encontrado.")

    # OPÇÃO 6 - HISTÓRICO
    elif opcao == "6":

        # Verifica se há registros
        if not historico_emprestimos:
            print("Nenhum empréstimo registrado.")
        else:
            print("\n=== HISTÓRICO DE EMPRÉSTIMOS ===")

            for titulo, quantidade in historico_emprestimos:
                print(f"{titulo} - {quantidade} exemplar(es) emprestado(s)")

    # OPÇÃO 7 - SAIR
    elif opcao == "7":
        print("Encerrando o programa...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")