class Animal:  # Definição da classe base Animal
    def __init__(self, nome, idade): 
        self.nome = nome  
        self.idade = idade  

    def emitir_som(self):  
        return "O animal emitiu um som genérico."  


class Cachorro(Animal):  # Definição da classe Cachorro, que herda da classe Animal
    def emitir_som(self):  
        return "O cachorro latiu!"  


class Gato(Animal):  # Definição da classe Gato, que herda da classe Animal
    def emitir_som(self):  
        return "O gato miou!" 