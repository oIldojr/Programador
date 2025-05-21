from abc import ABC, abstractmethod

class Tarefa():                                      #Criação das Classes 
    def __init__(self,descricao,prioridade,titulo):
        self.descriao = descricao
        self.prioridade = prioridade                    #Iniciação dos parâmetros
        self.titulo = titulo     

    def  __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao} - {self.prioridade}"                                   
                                 
class Usuario():
    def __init__(self, nome,mail,senha):
        self.nome = nome
        self.mail = mail 
        self.senha = senha
        self.lista_tarefas = []


    def criar_tarefa(self,descricao,prioridade,titulo):       # Método para criar tarefas
        nova_tarefa = Tarefa(titulo,descricao,prioridade)
        self.lista_tarefas.append(nova_tarefa)


    def remover_tarefa(self):                   # Método para remover tarefas
        self.lista_tarefas.remove()



class Funcionalidades:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None

    def cadastrar_usuario(self):  #Cadastrando novo usuario
        nome = input("Digite um nome: ")
        mail = input("Digite o E-mail: ")
        senha = input("Crie uma senha: ")
    

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

        for usuario in self.lista_usuarios:
            if (usuario.mail == mail) and (usuario.senha == senha):

                self.usuario_logado = usuario 
                print(f"Usuario Logado: {self.usuario_logado.nome}")
                self.menu_funcionalidades()
                return

            print("Usuario inexistente ou Senha inváliida")

    def menu_principal(self):                    #Metodo menu pricipal
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("Bem vindo! Escolha uma opção")
            print("1. Cadastrar novo usuario")
            print("2. Fazer login")
            print("0. Sair")
            opcao_escolhida = input("Escolha: ")

            if opcao_escolhida == "1":
                self.cadastrar_usuario()

            elif opcao_escolhida == "2":
                self.login()

            elif opcao_escolhida == "0":
                print("Saindo...")

            else:
                print("Opção inválida!")
            
    def menu_funcionalidades(self):
        escolha = ""
        while escolha != "0":
            print("------ Tarefas-----")
            print("1 - Criar Tarefa")
            print("2 - Listar Tarefas")
            escolha = input("Selecione: ")

            if escolha == "1":
                descricao = str(input("Descrição da tarefa?: "))
                prioridade = str(input("Prioridade?: "))
                titulo = str(input("titulo?: "))
                self.usuario_logado.criar_tarefa(descricao,prioridade,titulo)

            elif escolha == "2":
                self.usuario_logado.lista_tarefas



    def listar_tarefas(self,status):                        #Exibir Tarefas
        print("/n====Suas tarefas====")
        for Tarefa in self.lista_tarefas:
            print(Tarefa)

        

            



teste = Funcionalidades()
teste.menu_principal()






