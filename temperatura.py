temperatura = int(input("Digite a temperatura: "))
estado = str(input("Digite o estado: "))

if temperatura < 0 and estado == "nublado":
    print("Clima extremo:frio e nublado")

elif temperatura >= 0 and temperatura < 15 and (estado == "chuvoso" or estado == "nublado"):
    print("Muito frio e úmido")

elif temperatura >= 15 and temperatura < 20 and estado == "nublado":
    print("Frio com nuvens")

elif temperatura >= 20 and temperatura < 25 and estado == "ensolarado":
    print ("Agradável e ensolarado")

elif temperatura >= 25 and temperatura < 30 and estado != "chuvoso":
    print("Quente e seco")

elif temperatura >= 30 and estado == "ensolarado":
    print("Muito quente e ensolarado cuidado com o calor")

else:
    print("Clima não definido")

