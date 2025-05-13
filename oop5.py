''' POLOMORFISMO
class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

animais = [Animal(), Cachorro(), Gato()]

for animal in animais:
    animal.falar()
    '''

# ABSTRAÇÃO
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    def calcular_area(self):
        return self.altura * self.largura

class Ciruculo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return self.raio * 2 * 3.14

formas = [Retangulo(4,3), Ciruculo(4)]

for forma in formas:
    print( forma.calcular_area())