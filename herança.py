class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def exibir_info(self):
        print("Dados funcionario")
        print(self.nome,self.salario)

class GerenteTI(Funcionario):
        def calcualar_bonus(self)
        return self.salario * 0.1


class Programador(Funcionario):
        def calcualar_bonus(self)
        return self.salario * 0.05

func1 = GeremteTI("Matheus", 6000)
func2 = Programador("Ildo", 10000)

func1.exibir_info()
func2.exibir_info()