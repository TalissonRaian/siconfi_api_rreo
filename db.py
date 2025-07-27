import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()
user = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
server = os.getenv("DB_SERVER")
class Banco:
    def __init__(self, db):
        self.db = db

    def connection(self):
        connection = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            fr'SERVER={server};'      # ATENÇÃO: Substitua pelo nome do seu servidor
            fr'DATABASE={self.db};'   # ATENÇÃO: Substitua pelo nome do seu banco de dados
            fr'UID={user};'                   # ATENÇÃO: Substitua pelo seu usuário municipios
            fr'PWD={senha};'             # ATENÇÃO: Substitua pela sua senha
        )
        
        return connection

    def criar_cursor(self):
        conn = pyodbc.connect(self.connection())
        print('Conexão ok!')
        cursor = conn.cursor()
        return cursor 
    
    def result(self):
        consulta_municipios_ro = "select * from  municipios_brasil where [ente_code] like '11%';"
        entes = {}
        for row in self.criar_cursor().execute(consulta_municipios_ro):
            entes[row[2]] = row[3]
        return entes
