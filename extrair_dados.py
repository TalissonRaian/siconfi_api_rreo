import requests
import pandas as pd
class Extrair:

   
    def __init__(self, exercicio, periodo, entes):
         self.exercicio = exercicio
         self.periodo = periodo
         self.entes = entes

    def extrair_siconfi(self):
        dem = 'RREO'
        esfera = 'M'
        dados = []
        for ex in self.exercicio:
            for per in self.periodo:         
                    for nome, id_ente in self.entes.items():
                        url = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt//rreo?an_exercicio={ex}&nr_periodo={per}&co_tipo_demonstrativo={dem}&no_anexo=&co_esfera={esfera}&id_ente={id_ente}'
                        requisicao = requests.get(url)
                        if requisicao.status_code == 200:
                            # print(f'requisção ref: {nome}')
                            # print(requisicao.status_code)
                            result = requisicao.json()
                            df = pd.json_normalize(result['items'])
                            dados.append(df)
                            print(f'{nome} incluido,\nPeriodo: {per},\nExercicio {ex}')                     
                        else:
                            print(f'Erro {requisicao.status_code}')
                                               
        if dados:
            return pd.concat(dados, ignore_index=True)
        else:
            return pd.DataFrame() 

    
