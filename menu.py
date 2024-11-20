from negocio import Negocio

class Menu:
    def __init__(self):
        self.negocio = Negocio()

    def exibir_menu(self):
        while True:
            print("\nBem-vindo ao SmartConsumo!")
            print("1. Cadastrar Usuário")
            print("2. Login")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.cadastrar_usuario()
            elif escolha == '2':
                self.login_usuario()
            elif escolha == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrar_usuario(self):
        print("\n=== Cadastro de Usuário ===")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        email.lower()
        self.negocio.cadastrar_usuario(email, senha, cpf, nome)

    def login_usuario(self):
        print("\n=== Login ===")
        email = input("Email: ")
        senha = input("Senha: ")
        email.lower()
        sucesso, nome_usuario = self.negocio.login_usuario(email, senha)
        if sucesso:
            self.menu_logado(nome_usuario)

    def menu_logado(self, nome_usuario):
        while True:
            print(f"\nBem-vindo, {nome_usuario}!")
            print("1. Cadastrar dispositivo de Monitoramento")
            print("2. Editar dispositivo")
            print("3. Listar Dispositivos de monitoramento")
            print("4. Excluir dispositivo de monitoramento")
            print("0. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.cadastrar_dispositivo()
            elif escolha == '2':
                self.editar_dispositivo()
            elif escolha == '3':
                self.listar_dispositivo()
            elif escolha == '4':
                self.excluir_dispositivo()
            elif escolha == '0':
                print("Fazendo logout...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrar_dispositivo(self):
        print("\n=== Cadastrar Dispositivo ===")
        
        print("Funcionalidade ainda não implementada.")

    def editar_dispositivo(self):
        print("\n=== Editar Dispositivo ===")
        
        print("Funcionalidade ainda não implementada.")
        
    def listar_dispositivo(self):
        print("\n=== Lista dos seus Dispositivos ===")
        
        print("ainda nao")
        
    def excluir_dispositivo(self):
        print("\n=== Deletar Dispositivo ===")
        
        print("ainda nao")

