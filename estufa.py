class Planta:
    def __init__(self,nome_comum,nome_cientifico,umidade,luz):
        self.nome_cientifico = nome_cientifico
        self.nome_comum = nome_comum
        self._umidade = umidade
        self._luz = luz 
    def get_umidade(self,umidade):
        return self._umidade


    def set_umidade(self,umidade):
        if umidade >= 0 and umidade <= 100:
            self._umidade = umidade
        else:
            print("Valores inválidos")
               
    def get_luz(self):
        return self._luz


    def set_luz(self):
        if luz >= 0 and luz <= 100:
            self._luz = luz 
        else:
            print("Valores inválidos")


    def verificar_cuidados(self):
        pass
    def exibir_info(self):
        return print(f"Conhecida comumunmente como {self.nome_comum} cientificamente como {self.nome_cientifico}")

class Cacto(Planta):
    def __init__(self,nome_cientifico,nome_comum,umidade,luz):
        super().__init__(nome_cientifico,nome_comum,umidade,luz)

    def verificar_cuidados(self):
      if self._umidade < 30 and self._luz > 70:
       print(f"Os cuidados estão adequados, não esqueça da pouca água!")

      else:
        print("As condiçoes não estão adequadas!")

class Flor(Planta):
    def __init__(self,nome_cientifico,nome_comum,umidade,luz):
        self.verificar_cuidados = verificar_cuidados 
        super().__init__(nome_cientifico,nome_comum,umidade,luz)

    def verificar_cuidados(self):
        if (self._umidade >= 40 and self._umidade <= 70 ) and (self._luz > 70):
            print("Os cuidados estão adequados!")

        else:
            print("Os cuidados não estão adequados!")

class PlantaAquatica(Planta):
    def __init__(self,nome_cientifico,nome_comum,umidade,luz):
        self.verificar_cuidados = verificar_cuidados 
        super().__init__(nome_cientifico,nome_comum,umidade,luz)

    def verificar_cuidados(self):
        if self._umidade >= 90 and self._luz < 50:
            print("Os cuidados estão adequados!")

        else:
            print("Os cuidados não estão adequados!")

nome_comum = str(input("Nome comum?: "))
nome_cientifico = str(input("Nome cientifico?: "))
luz = int(input("Luz?: "))
umidade = int(input("umidade?: " ))
tipo = str(input("Tipo da planta?: "))



if tipo == "Cacto":
    planta1 = Cacto(nome_comum,nome_cientifico,luz,umidade)
    planta1.exibir_info()
    planta1.verificar_cuidados()


elif tipo == "Flor":
    planta1 = Flor(nome_comum,nome_cientifico,luz,umidade)

elif tipo == "PlantaAquatica":
    planta1 = PlantaAquatica(nome_comum,nome_cientifico,luz,umidade)


