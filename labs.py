temperatura = int(input("Temperatura em graus Celsius?: ")) #Ideal entre 36 e 38
pH = float(input("ph?: ")) #Ideal entre 6,5 e 7,5 
tempo = int(input("Tempo em horas?: ")) #Ideal entre 18 e 24 horas 

if (temperatura >= 36 and temperatura <= 38) and (pH >= 6.5 and pH <= 7.5) and (tempo >= 18 and tempo <= 24):
    print("Condições ideais")

elif (temperatura >= 36 and temperatura <= 38) or (pH >= 6.5 and pH <= 7.5) or (tempo >= 18 and tempo <= 24):
    print("Condições parciais")

else:
    print("Condições ruins")