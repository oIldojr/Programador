from abc import ABC, abstractmethod

class Tarefa():                                      #Criação das Classes 
    def __init__(self,descriçao,prioridade,titulo):
        self.descrião = descriçao
        self.status = status
        self.prioridade = prioridade                    #Iniciação dos parâmetros
        self.titulo = titulo                                        
                                 
class Usuario():
    def __init__(nome,mail,senha):
        self.nome = nome
        self.mail = mail 
        self.senha = senha


class Funcionalidades:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None

    def cadastrar_usuario(self):  #Cadastrando novo usuario
        nome = input("Digite um nome")
        mail = input("Digite o E-mail")
        senha = input("Crie uma senha")
    

        if "@" not in mail:
            print("E-mail inválido")    
            return
        if len(senha) < 4:
            print("Senha muito curta!")
 
        else:
            novo_usuario = Usuario(nome,mail,senha)
            self.lista_usuarios.append(novo_usuario)
            print("Usuario cadastrao com sucesso!")

    def login(self):                                     #Login de Usuario
        mail = input("Faça login com seu E-mail!: ")
        senha = input("Senha?: ")

        for Usuario in self.lista_usuarios:
            if (usuario.mail == mail) and (usuario.senha == senha):

                self.usuario_logado = usuario 
                print(f"Usuario Logado: {self.usuario_logado.nome}")
                return

            print("Usuario inexistente ou Senha inváliida")

    def menu_principal(self):                    #Metodo menu pricipal
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("Bem vindo! Escolha uma opção")
            print("1. Cadastrar novo usuario")
            print("2. Fazer login")
            print("0. Sair")
            opcao_escolhida == input("Escolha: ")

            if opcao_escolhida == "1":
                self.cadastrar_usuario()

            elif opcao_escolhida == "2":
                self.login()

            elif opcao_escolhida == "0":
                print("Saindo...")

            else:
                print("Opção inválida!")
            


class SistemasDeTarefas(Tarefa):                        #Herança de Tarefas para Sistemas de tarefas
    def criar_tarefa(self,descriçao,prioridade,titulo):
        pass

    
    def marcar_concluida(self):
        pass




    def listar_pendentes(self,status):
        print("/n====Suas tarefas pendentes====")
        
                                                                            #Metodos Da classe Sistema de tarefas

    def listar_concluidas(self,status):
        print("/n====Suas tarefas concluidas")



    def listar_tarefas(self): 
        print("/n====Suas tarefas====")
        

    
    
    def remover_tarefa(self):
        pass


teste = Funcionalidades()
teste.menu_principal()

        







