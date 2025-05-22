from abc import ABC, abstractmethod


class Tarefa:                                      #Criação das Classes 

    incrementa_id = 1                                   #Criando ID para as tarefas
    def __init__(self,descricao,prioridade,titulo):

        self.descriao = descricao
        self.prioridade = prioridade                    #Iniciação dos parâmetros
        self.titulo = titulo    
        self.status = "Pendente" 
        self.id = Tarefa.incrementa_id
        Tarefa.incrementa_id += 1

    def  __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao} - {self.prioridade}"                                   
                                 

    def concluir_tarefa(sefl):                      #Concluir Tarefas
        self.status = "Concluida"
        print(f"Tarefa {self.titulo} Concluida")


    def editar_tarefa(self,novo_titulo,nova_descricao,nova_prioridade):        #Editar tarefas
        novo_titulo = novo_titulo
        nova_descricao = nova_descricao
        nova_prioridade = nova_prioridade

   

class Usuario():
    def __init__(self, nome,mail,senha):
        self.nome = nome
        self.mail = mail 
        self.senha = senha
        self.lista_tarefas = []


    def criar_tarefa(self,descricao,prioridade,titulo):       # Método para criar tarefas
        nova_tarefa = Tarefa(descricao, prioridade, titulo)
        self.lista_tarefas.append(nova_tarefa)


    def remover_tarefa(self,id_Tarefa):                   # Método para remover tarefas
        tarefa_buscada = self.proucura_tarefa(id_Tarefa)
        if tarefa_buscada:
            self.lista_tarefas.remove(tarefa_buscada)

        else:
             print("Tarefa não encontrada!")

    def limpar_concluidas(self):
        tarefas_ativas = []
        for tarefa in lista_tarefas:
            if tarefas.status != "Concluida":
                tarefas_ativas.append(tarefa)
            self.lista_tarefas = tarefas_ativas



class Funcionalidades:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None

    def cadastrar_usuario(self):                     #Cadastrando novo usuario
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
            print("Usuario cadastrado com sucesso!")

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

    def menu_principal(self):                    #Menu pricipal
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
            
    def menu_funcionalidades(self):                         #Menu de funcionalidades
        escolha = ""
        while escolha != "0":
            print("------ Tarefas-----")
            print("1 - Criar Tarefa")
            print("2 - Listar Tarefas")
            print("3 - Listar Tarefas pendentes")
            print("4 - Listar Tarefas concluidas")
            print("5 - Concluir Tarefa")
            print("6 - Editar Tarefa")
            print("7 - Remover Tarefa")
            print("8 - Limpar Concluidas")



            escolha = input("Selecione: ")

            if escolha == "1":
                descricao = str(input("Descrição da tarefa?: "))
                prioridade = str(input("Prioridade?(Alta,Média ou Baixa): "))
                titulo = str(input("titulo?: "))
                self.usuario_logado.criar_tarefa(descricao,prioridade,titulo)

            elif escolha == "2":
                self.usuario_logado.lista_tarefas

            elif escolha == "3":
                self.usuario_logado.lista_tarefas("Pendente")

            elif escolha == "4":
                self.usuario_logado.lista_tarefas("Concluida")

            elif escolha == "5":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.proucura_tarefa(int(id))

                if tarefa_buscada:
                    self.usuario_logado.concluir_tarefa()

                else:
                    print("Tarefa não encontrada!")


            elif escolha == "6":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.proucura_tarefa(int(id))
                    if tarefa_buscada:
                        novo_titulo = input("Novo Titulo?: ")
                        nova_descricao = input("Nova descrição?: ")
                        nova_prioridade = input("Nova prioridade?: ")
                        tarefa.editar_tarefa(novo_titulo,nova_descricao,nova_prioridade)
                        
                    else:
                        print("Tarefa não encontrada!")

            elif escolha == "7":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.remover_tarefa(int(id))

            elif escolha == "8":
                self.usuario_logado.limpar_concluidas()





    def listar_tarefas(self,status=None):                        #Exibir Tarefas
        print("/n====Suas tarefas====")
        for Tarefa in self.lista_tarefas:
            if status is None or Tarefa.status == status:
                print(Tarefa)


    def proucura_tarefa(self,id_tarefa):
        for Tarefa in self.lista_tarefas:
            if Tarefa.id == id_Tarefa:
                return Tarefa
        return None

''

teste = Funcionalidades()               #Exibindo Menu
teste.menu_principal()






