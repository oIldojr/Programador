print("==== Vamos calcular suas horas trabalhas! ====")

valor_hora = float(input("Valor da hora trabalhada?: "))
segunda = int(input("Quantas horas trabalhou segunda?: "))
terca = int(input("Quantas horas trabalhou terça?: "))
quarta = int(input("Quantas horas trabalhou quarta?: "))
quinta = int(input("Quantas horas trabalhou quinta?: "))
sexta = int(input("Quantas horas trabalhou sexta?: "))


def calcular_total_h(segunda,terca,quarta,quinta,sexta):
    return sum(segunda,terca,quarta,quinta,sexta)

def calcular_pagamento(valor_hora,calcular_total_h):    
    return valor_hora * calcular_total_h

calcular_total_h(segunda,terca,quarta,quinta,sexta)
calcular_pagamento(valor_hora,calcular_total_h)

print("/n==== Total de horas e valor a receber! ====")
print(calcular_total_h)
print(calcular_pagamento)

