# menu.py
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
        self.negocio.cadastrar_usuario(email, senha, cpf, nome)

    def login_usuario(self):
        print("\n=== Login ===")
        email = input("Email: ")
        senha = input("Senha: ")
        self.negocio.login_usuario(email, senha)