# Operações usando lambda
operacoes = {
    "Soma": lambda a, b: a + b,
    "Subtração": lambda a, b: a - b,
    "Multiplicação": lambda a, b: a * b,
    "Divisão": lambda a, b: a / b
}

while True:

    # Entrada dos números
    while True:
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            break
        except ValueError:
            print("Erro: Por favor insira apenas números válidos.\n")
    
    # Exibição do menu de operações
    print("\nEscolha uma operação:")
    for i, op in enumerate(operacoes.keys()):
        print(f"{i+1} - {op}")

    try:
        escolha = int(input("Digite o número da operação desejada: "))

        if escolha < 1 or escolha > len(operacoes):
            print("Operação inválida.\n")
            continue

        operacao_nome = list(operacoes.keys())[escolha - 1]
        print(f"Você escolheu: {operacao_nome}")

        # Verificação de divisão por zero
        if operacao_nome == "Divisão":
            while num2 == 0:
                try:
                    num2 = float(input("Divisão por zero não é permitida. Por favor, insira outro número: "))
                except ValueError:
                    print("Valor inválido.")

        # Executa operação
        resultado = operacoes[operacao_nome](num1, num2)

        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Entrada inválida.\n")
        continue

    # Pergunta se deseja continuar
    continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()

    if continuar != "S":
        print("Encerrando a calculadora. Até mais!")
        break