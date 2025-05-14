from abc import ABC, abstractmethod

print("====Menu Inicial====")

class Tarefa(): 
    def __init__(self,descriçao,prioridade,titulo)
        self.descrião = descriçao
        self.status = status
        self.prioridade = prioridade
        self.titulo = titulo
                                 
class Usuario():
    def __init__(nome,mail,suas_tarefas)
        self.nome = nome
        self.mail = mail 
        self.suas_tarefas = suas_tarefas

class SistemasDeTarefas(Tarefa):                        #Métodos Da classe Tarefas
    def criar_tarefa(self,descriçao,prioridade,titulo):



    def marcar_concluida(self):




    def listar_pendentes(self):
        print("/n====Suas tarefas pendentes====")
        print tarefas_pendentes


    def listar_concluidas(self):
        print("/n====Suas tarefas concluidas")
        print tarefas_concluidas


    def listar_tarefas(self): 
        print("/n====Suas tarefas====")
        print tarefas

    
    
    def remover_tarefa(self):
        





print("Cadastra-se")
mail = str(input("E-mail?: "))
    if "@" in mail:
        print("E-mail válido")
    else:
        print("E-mail inválido")

nome = str(input("Nome?: "))