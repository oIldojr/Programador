def saudacao(nome):
    return f"ola {nome}"


def dobro(valor):
    return valor * 2 

usuario = "Ana"
mensagem = saudacao(usuario)
print(mensagem)

valor = 10 
resultado = dobro(valor)
print(f"o dobro de {valor} é {resultado}")