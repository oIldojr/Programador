consumo = float(input("Consumo em litros?: "))
moradores = int(input("Quantos moradores?: "))

if moradores <= 0:
    print("O numero de moradores deve ser maior que zero!")

def media():
    calculo = (consumo / 30 / moradores)
    if calculo < 110:
        print("Consumo conciente,Parabens!")

    elif calculo >= 110 and calculo <= 200:
         print("Consumo moderado,Atenção")

    elif calculo > 200:
        print("Alto consumo,Atenção necessária")

media()