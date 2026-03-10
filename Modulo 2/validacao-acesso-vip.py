# Lista de convidados VIP (pode ser modificada nos testes)
convidados_vip = ["Alice", "Bob", "Carol"]

# Função para verificar se a idade permite entrada
def verificar_idade(idade):
    if idade >= 18:
        return "Entrada permitida. Bem-vindo ao evento!"
    else:
        return "Entrada negada. Este evento é apenas para maiores de idade."

# Função para verificar se o nome está na lista VIP
def verificar_vip(nome):
    if nome in convidados_vip:
        return "Você é um convidado VIP! Aproveite o evento com acesso especial."
    return None

# Programa principal
def main():
    while True:
        idade_input = input("Qual a sua idade? ")

        if idade_input.lower() == "sair":
            break

        try:
            idade = int(idade_input)
        except ValueError:
            print("Por favor, digite uma idade válida.")
            continue

        mensagem = verificar_idade(idade)
        print(mensagem)

        if idade >= 18:
            nome = input("Qual o seu nome? ")
            if nome.lower() == "sair":
                break
            mensagem_vip = verificar_vip(nome)
            if mensagem_vip:
                print(mensagem_vip)

if __name__ == "__main__":
    main()
