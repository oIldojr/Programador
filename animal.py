class Animal:
    def __init__(self,nome,especie,peso):
        self.nome = nome
        self.especie = especie
        self.peso = peso

    def alimentar(self,quantidade):
        self.peso += quantidade * 0.2

    
    def exibir_info(self):
        print(self.nome)
        print(self.especie)
        print(self.peso)

    def verificar_dieta(self):
        if self.peso > 40:
                print(f"{self.nome} está acima do peso!")
        else: 
                print(f"{self.nome} está dentro do peso ideal!")
                

print("====Informações do Animal====")
nome = str(input("Nome do animal?: "))
especie = str(input("Qual a especie do animal?: "))
peso = float(input("Qual o peso do animal?: "))
quantidade = float(input("Quanto KG ele comeu?: "))

a = Animal(nome,especie,peso)

a.alimentar(quantidade)
a.exibir_info()
a.peso()
