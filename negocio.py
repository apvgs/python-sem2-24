# negocio.py
from banco import Banco

class Negocio:
    def __init__(self):
        self.banco = Banco()
    
    def cadastrar_usuario(self, email, senha, cpf, nome):
        try:
            login_id = self.banco.insere_login_banco(email, senha)  
            if login_id:
                self.banco.insere_usuario_banco(cpf, nome, login_id) 
                print("Usuário cadastrado com sucesso!")
            else:
                print("Erro ao obter ID do login.")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def login_usuario(self, email, senha):
        return self.banco.login_usuario(email, senha)

