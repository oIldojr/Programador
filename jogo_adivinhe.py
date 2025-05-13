import random

numero_sorteado = random.randint(1,10)

numero = int(input("Adivinhe o número entre 1 e 10: "))

while numero != numero_sorteado:
    numero = int(input("Adivinhe o número entre 1 e 10: "))
    print("Incorreto,tente novamente")
    
print("Parabéns,você acertou")