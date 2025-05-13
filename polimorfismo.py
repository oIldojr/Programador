from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def __init__(self,valor):
        self.valor = valor 

    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self,valor,numero_cartao,cvv):
        super().__init__(valor)
        self.cvv = cvv
        self.numero_cartao = numero_cartao
    
    def processar_pagamento(self):
        if len(self.numero_cartao) == 16 and len(self.cvv) == 3:
            print("Pagamento via cartao efetuado")
    
        else:
            print("Dados inválidos")

class BoletoBancario(Pagamento):
    def __init__ (self,valor,cpf_cliente):
        super().__init__(valor)
        self.cpf_cliente = cpf_cliente

    def processar_pagamento(self):
        print(f"O boleto foi gerado pelo CPF {self.cpf_cliente},obrigado!")

class Pix(Pagamento):
    def __init__(self,valor, chave_pix):
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Pagamento efetuado intanteneamente pela chave{self.chave_pix}, obrigado!")


pagamentos = [CartaoCredito(500,"1234567891012130","123"),BoletoBancario(600,"12345678910"),Pix(1000,"ildo@gmail.com")]

for pagamento in pagamentos:
    pagamento.processar_pagamento()




