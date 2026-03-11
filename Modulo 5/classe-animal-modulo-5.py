class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")


class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")


class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")


# Programa principal
cachorro = Cachorro("Max", 8)
gato = Gato("Milker", 5)

print("Nome do cachorro:", cachorro.nome)
print("Idade do cachorro:", cachorro.idade)
cachorro.emitir_som()

print()

print("Nome do gato:", gato.nome)
print("Idade do gato:", gato.idade)
gato.emitir_som()