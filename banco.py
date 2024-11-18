import oracledb

def get_connection():
    return oracledb.connect(user= 'rm556182', password='101003',
                            dsn = "oracle.fiap.com.br/orcl")