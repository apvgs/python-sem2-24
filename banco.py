import oracledb

class Banco:
    def __init__(self):
        self.usuario_id = None
        self.usuario_nome = None

    @staticmethod
    def get_connection():
        return oracledb.connect(user='rm554489', password='280606', dsn="oracle.fiap.com.br/orcl")

    def insere_login_banco(self, email, senha):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT email FROM t_gs_login WHERE email = :email", email=email)
            if cursor.fetchone():
                print("E-mail já registrado. Tente fazer login ou use outro e-mail.")
                return None
            
            cursor.execute("SELECT sq_id_login.nextval FROM dual")
            login_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO t_gs_login (id_login, email, senha)
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
                INSERT INTO t_gs_usuario (id_usuario, cpf, nome, login_id)
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
                SELECT l.id_login, u.nome, u.id_usuario AS usuario_id
                FROM t_gs_login l
                JOIN t_gs_usuario u ON l.id_login = u.login_id
                WHERE l.email = :email AND l.senha = :senha
            """, email=email, senha=senha)
            
            usuario = cursor.fetchone()
            if usuario:
                self.usuario_id = usuario[2]
                self.usuario_nome = usuario[1]
                print(f"Bem-vindo, {usuario[1]}!")
                return True, usuario[1]
            else:
                print("Email ou senha incorretos.")
                return False, None
        except oracledb.Error as error:
            print(f"Erro ao fazer login: {error}")
            return False, None
        finally:
            cursor.close()
            connection.close()

    def insere_dispositivo(self, codigo, localizacao):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO t_gs_dispositivo_medicao (id_dispositivo, codigo, status, localizacao, usuario_id)
                VALUES (sq_id_dispositivo.nextval, :codigo, :status, :localizacao, :usuario_id)
            """, codigo=codigo, status="A", localizacao=localizacao, usuario_id=self.usuario_id)
            connection.commit()
        except oracledb.Error as error:
            print(f"Erro ao inserir Dispositivo: {error}")
            connection.rollback()
        finally:
            print("Dispositivo Casdastrado com sucesso!")
            cursor.close()
            connection.close()

    def lista_dispositivos(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        dispositivos = []  
        try:
            cursor.execute("""
                SELECT id_dispositivo, codigo, status, localizacao
                FROM t_gs_dispositivo_medicao
                WHERE usuario_id = :usuario_id
            """, usuario_id=self.usuario_id)
            dispositivos = cursor.fetchall()
            
            if dispositivos:
                print("\n=== Lista de Dispositivos ===")
                for dispositivo in dispositivos:
                    id_dispositivo, codigo, status, localizacao = dispositivo
                    print(f"ID Dispositivo: {id_dispositivo}")
                    print(f"Código: {codigo}")
                    print(f"Status: {status}")
                    print(f"Localização: {localizacao}")
                    print("------------------------------")
            else:
                print("Nenhum dispositivo encontrado para este usuário.")
        except oracledb.Error as error:
            print(f"Erro ao listar dispositivos: {error}")
        finally:
            cursor.close()
            connection.close()

        return dispositivos

    def edita_dispositivo(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        dispositivos = self.lista_dispositivos()
        try:
            if dispositivos:
                id_dispositivo = int(input("\nDigite o ID do dispositivo que deseja editar: "))

                dispositivo = next((d for d in dispositivos if d[0] == id_dispositivo), None)
                if not dispositivo:
                    print("ID do dispositivo não encontrado.")
                    return

                print("\nO que você deseja editar?")
                print("1. Código")
                print("2. Status")
                print("3. Localização")
                escolha = input("Escolha uma opção: ")

                if escolha == '1':
                    novo_codigo = input("Digite o novo código: ")
                    cursor.execute("""
                        UPDATE t_gs_dispositivo_medicao
                        SET codigo = :novo_codigo
                        WHERE id_dispositivo = :id_dispositivo
                    """, novo_codigo=novo_codigo, id_dispositivo=id_dispositivo)
                elif escolha == '2':
                    novo_status = input("Digite o novo status: ")
                    cursor.execute("""
                        UPDATE t_gs_dispositivo_medicao
                        SET status = :novo_status
                        WHERE id_dispositivo = :id_dispositivo
                    """, novo_status=novo_status, id_dispositivo=id_dispositivo)
                elif escolha == '3':
                    nova_localizacao = input("Digite a nova localização: ")
                    cursor.execute("""
                        UPDATE t_gs_dispositivo_medicao
                        SET localizacao = :nova_localizacao
                        WHERE id_dispositivo = :id_dispositivo
                    """, nova_localizacao=nova_localizacao, id_dispositivo=id_dispositivo)
                else:
                    print("Opção inválida.")
                    return

                connection.commit()
                print("Dispositivo atualizado com sucesso!")
            else:
                print("Nenhum dispositivo encontrado para este usuário.")
        except oracledb.Error as error:
            print(f"Erro ao editar dispositivo: {error}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

        
        
    def exclui_dispositivo(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        dispositivos = self.lista_dispositivos()
        try:
            if dispositivos:
                id_dispositivo = int(input("\nDigite o ID do dispositivo que deseja excluir: "))

                dispositivo = next((d for d in dispositivos if d[0] == id_dispositivo), None)
                if not dispositivo:
                    print("ID do dispositivo não encontrado.")
                    return

                confirmacao = input(f"Tem certeza que deseja excluir o dispositivo {id_dispositivo}? (s/n): ")
                if confirmacao.lower() == 's':
                    cursor.execute("""
                        DELETE FROM t_gs_dispositivo_medicao
                        WHERE id_dispositivo = :id_dispositivo
                    """, id_dispositivo=id_dispositivo)

                    connection.commit()
                    print("Dispositivo excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Nenhum dispositivo encontrado para este usuário.")
        except oracledb.Error as error:
            print(f"Erro ao excluir dispositivo: {error}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

