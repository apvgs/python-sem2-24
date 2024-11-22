# negocio.py
from banco import Banco
import re
import json

class Negocio:
    def __init__(self):
        self.banco = Banco()
    
    def cadastrar_usuario(self, email, senha, cpf, nome):
        try:
            if not self.valida_cpf(cpf):
                print("CPF inválido. Por favor, insira um CPF válido.")
                return

            login_id = self.banco.insere_login_banco(email, senha)  
            if login_id:
                self.banco.insere_usuario_banco(cpf, nome, login_id) 
                print("Usuário cadastrado com sucesso!")
            else:
                print("Erro ao obter ID do login.")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")

    @staticmethod
    def valida_cpf(cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * len(cpf):
            return False

        sum_val = sum(int(cpf[i]) * (10 - i) for i in range(9))
        first_check_digit = 11 - (sum_val % 11)
        if first_check_digit >= 10:
            first_check_digit = 0

        sum_val = sum(int(cpf[i]) * (11 - i) for i in range(10))
        second_check_digit = 11 - (sum_val % 11)
        if second_check_digit >= 10:
            second_check_digit = 0

        return cpf[-2:] == f"{first_check_digit}{second_check_digit}"

    def login_usuario(self, email, senha):
        return self.banco.login_usuario(email, senha)

    def insere_dispositivo(self,codigo, localizacao):
        return self.banco.insere_dispositivo(codigo, localizacao)
    
    

    def exportar_dispositivos_json(self, nome_arquivo):
        dispositivos = self.banco.lista_dispositivos()
        if dispositivos:
            dispositivos_dict = [
                {
                    "ID Dispositivo": dispositivo[0],
                    "Código": dispositivo[1],
                    "Status": dispositivo[2],
                    "Localização": dispositivo[3]
                }
                for dispositivo in dispositivos
            ]
            
            with open(nome_arquivo, 'w', encoding='utf-8') as json_file:
                json.dump(dispositivos_dict, json_file, ensure_ascii=False, indent=4)
            
            print(f"Dispositivos exportados para {nome_arquivo} com sucesso!")
        else:
            print("Nenhum dispositivo encontrado para exportar.")


        