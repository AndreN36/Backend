# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    if nome in tarefas:
        return "Essa tarefa já existe."
    tarefas[nome] = False
    return f"Tarefa '{nome}' adicionada com sucesso!!"


def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    
    linhas = []
    for nome, status_bool in sorted(tarefas.items()):
        status = "Concluída" if status_bool else "Não concluída"
        linhas.append(f"{nome} - {status}")
    return "\n".join(linhas)


def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    return "Erro: Tarefa não encontrada."


def marcar_concluida(nome):
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    return "Erro: Tarefa não encontrada."


def exibir_menu():
    return (
        "Menu:\n"
        "1 - Adicionar tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Remover tarefa\n"
        "4 - Marcar tarefa como concluída\n"
        "5 - Sair"
    )


def main():
    while True:
        print(exibir_menu())
        opcao = input().strip()

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ").strip()
            print(adicionar_tarefa(nome))

        elif opcao == "2":
            print(listar_tarefas(tarefas))

        elif opcao == "3":
            print(listar_tarefas(tarefas)) 
            nome = input("Qual tarefa remover? ").strip()
            print(remover_tarefa(nome))

        elif opcao == "4":
            print(listar_tarefas(tarefas)) 
            nome = input("Qual tarefa concluir? ").strip()
            print(marcar_concluida(nome))

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
