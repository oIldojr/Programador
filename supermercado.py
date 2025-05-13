produto = float(input("Valor do produto: "))

quantidade = 0
total = 0.0

while produto != 0:
    total += produto
    quantidade += 1 

    produto = float(input("Valor do produto: "))


print("\n=== Resumo da Compra ===")
print(f"Total de produtos: {quantidade}")
print(f"Valor total a pagar: R$ {total: }")
print("Obrigado por comprar conosco!")

#f antes das aspas para entender que o valor que será exibido é variavel 
