import aiohttp
import asyncio
exercicio = [2024,2025]
periodo = [1,2,3,4,5,6]
demo = ['RREO']
esferas = ['M']
ente = {'teste1':'1100015', 'teste2':'1100114'}
async def main():
    async with aiohttp.ClientSession() as session:
        for ex in exercicio:
            for per in periodo:
                for dem in demo:
                    for  esfera in esferas:
                        for i, id_ente in ente.items():
                            async with session.get(f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt//rreo?an_exercicio={ex}&nr_periodo={per}&co_tipo_demonstrativo={dem}&no_anexo=&co_esfera={esfera}&id_ente={id_ente}') as response:
                                #https://apidatalake.tesouro.gov.br/ords/siconfi/tt//rreo?an_exercicio=2024&nr_periodo=1&co_tipo_demonstrativo=RREO&no_anexo=&co_esfera=M&id_ente=1100015
                                print(await response.json())

asyncio.run(main())
