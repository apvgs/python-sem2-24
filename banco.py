# banco.py
import oracledb

class Banco:
    def __init__(self):
        self.usuario_id = None
    @staticmethod
    def get_connection():
        return oracledb.connect(user='rm556182', password='101003', dsn="oracle.fiap.com.br/orcl")

    def insere_login_banco(self, email, senha):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            # Verificar se o email já existe
            cursor.execute("SELECT email FROM t_gs_login WHERE email = :email", email=email)
            if cursor.fetchone():
                print("E-mail já registrado. Tente fazer login ou use outro e-mail.")
                return None
            
            # Obter o próximo valor da sequência
            cursor.execute("SELECT sq_id_login.nextval FROM dual")
            login_id = cursor.fetchone()[0]

            # Inserir no t_gs_login
            cursor.execute("""
                INSERT INTO t_gs_login (id, email, senha)
                VALUES (:id, :email, :senha)
            """, id=login_id, email=email, senha=senha)
            connection.commit()

            return login_id
        except oracledb.Error as error:
            print(f"Erro ao inserir login: {error}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            connection.close()


    
    def insere_usuario_banco(self, cpf, nome, login_id):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO t_gs_usuario (id, cpf, nome, login_id)
                VALUES (sq_id_usuario.nextval, :cpf, :nome, :login_id)
            """, cpf=cpf, nome=nome, login_id=login_id)
            connection.commit()
        except oracledb.Error as error:
            print(f"Erro ao inserir usuário: {error}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def login_usuario(self, email, senha):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT l.id, u.nome
                FROM t_gs_login l
                JOIN t_gs_usuario u ON l.id = u.login_id
                WHERE l.email = :email AND l.senha = :senha
            """, email=email, senha=senha)
            
            usuario = cursor.fetchone()
            if usuario:
                self.usuario_id = usuario[0]  # Salva o ID do usuário logado
                print(f"Bem-vindo, {usuario[1]}!")
            else:
                print("Email ou senha incorretos.")
        except oracledb.Error as error:
            print(f"Erro ao fazer login: {error}")
        finally:
            cursor.close()
            connection.close()
