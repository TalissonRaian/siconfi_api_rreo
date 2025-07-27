from db import Banco 
from extrair_dados import Extrair


#Criar conexão com o banco
banco_municipios = Banco('municipios')
banco_rreo = Banco('siconfi_api')

#conecatar o banco
connection_municipios = banco_municipios.connection()
connection_rreo = banco_rreo.connection()

#Cria o cursor
cursor_municipio = banco_municipios.criar_cursor()
cursor_rreo = banco_rreo.criar_cursor()

#executa a consulta no entes
entes = banco_municipios.result()


#Extrai dados com requests da api do siconfi
dados = Extrair([2024],[1,2,3,4,5,6],entes)
dados = dados.extrair_siconfi()
print(dados)

def insert_sql(tabela, dados):
    print("iniciando inserção...")
    nome_tabela = tabela#'dbo.rreo'
    insert = f'''insert into dbo.rreo 
        (
        [exercicio]
        ,[demonstrativo]
        ,[periodo]
        ,[periodicidade]
        ,[instituicao]
        ,[cod_ibge]
        ,[uf]
        ,[populacao]
        ,[anexo]
        ,[esfera]
        ,[rotulo]
        ,[coluna]
        ,[cod_conta]
        ,[conta]
        ,[valor])
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''



    for index, row in enumerate(dados):
            valores_inserir = (
                row['exercicio'],
                row['demonstrativo'],
                row['periodo'],
                row['periodicidade'],
                row['instituicao'],
                row['cod_ibge'],
                row['uf'],
                row['populacao'],
                row['anexo'],
                row['esfera'],
                row['coluna'],
                row['rotulo'],
                row['cod_conta'],
                row['conta'],
                row['valor']
            )
            try:
                cursor_rreo.execute(insert, valores_inserir)
                cursor_rreo.connection.commit()
                print(f'dados insesiros com sucesso')
            except KeyError as e:
                print(e)
 

insert_sql('dbo.rreo', dados.to_dict(orient='records'))