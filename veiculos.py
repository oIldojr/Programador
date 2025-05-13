class Veiculo:
    def __init__(self,modelo,combustivel):
        self.modelo = modelo 
        self.__combustivel = combustivel
    
    def abastecer(self,litros):
        if litros > 0:
            self.__combustivel += litros 
        else:
            print("Quantidade invalida")

    def get_combustive(self):
        return self.combustivel

    def exibir_info(self):
        print(f"Modelo: {self.modelo} - Combustivel: {self.combustivel}")

class Carro(Veiculo):
    def abastecer(self,litros):
        super().abastecer(litros)
        print(f"Carro{self.modelo} abastecido")

class Moto(Veiculo):
    def abastecer(self,litros):
        super().abastecer(litros)
        return print(f"Moto{self.modelo}abastecida")

moto1 = Moto("Yamaha R8,",0)
carrro1 = Carro("Mercedes", 0)

moto1.exibir_info()
carro1.exibir_info()

moto1.abastecer(50)
carro1.abastecer(40)

moto1.exibir_info()
carro1.exibir_info()

