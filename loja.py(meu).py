
num_produtos = int(input("Quantos pordutos foram vendidos hoje?: "))

produtos = []
precos = []
qtd_vendida = []

for i in range(num_produtos):
    nome_do_produto = str(input("Produto?: "))
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço?: "))

    produtos.append(nome_do_produto)
    qtd_vendida.append(quantidade)
    precos.append(preco)


total_vendas = 0
mais_vendido_nome = ""
mais_vendido_qtd = 0
total_itens = 0

for i in range(num_produtos):
    sub_total = qtd_vendida[i] * precos[i]
    total_vendas += sub_total
    total_itens += qtd_vendida[i]

    if qtd_vendida[i] > mais_vendido_qtd:
        mais_vendido_nome = produtos[i]
        mais_vendido_qtde = qtd_vendida


print("=====Valor vendido=====")
print(f"total_vendido : {total_vendas} com {mais_vendido_qtd} unidades")

print("=====Produto mais vendido=====")
print(f"Produto mais vendido:{mais_vendido_nome} ")

print("=====Quantidade vendida=====")
print(f"Produto mais vendido:{total_itens} ")

