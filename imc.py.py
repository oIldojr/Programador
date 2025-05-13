altura = float(input('digite seu peso'))
peso = float(input("digite sua altura"))

imc = peso/ (altura * 2)
 print(imc) 
if imc < 18.5:
    print("abaixo do peso")

if imc > 18.5 and imc < 25:
    print("peso normal")

if imc > 25 and imc < 30:
    print("sobrepeso")

if imc > 30:
    print("obesidade")