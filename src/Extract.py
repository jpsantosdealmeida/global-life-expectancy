import pandas as pd
from pathlib import Path

# 1. Leitura dos dados
def extrair_dados(caminho):
    try:
        if caminho.is_file():
            csv = pd.read_csv(caminho)
            return csv
        else:
            raise FileNotFoundError('Arquivo não encontrado')
            
     # Lembrar de colocar o logging depois
        
    except pd.errors.EmptyDataError:
        print('Arquivo vazio.')
        raise
    except pd.errors.ParserError:
        print('Arquivo não pode ser interpretado.')
        raise
    
        
    

# csv_expec_vida = extrair_dados(caminho_csv)

# print("=== PRIMEIRAS LINHAS ===")
# print(csv_expec_vida.head())
# # 2. Padronização das colunas
# csv_expec_vida.columns = csv_expec_vida.columns.str.strip()
# csv_expec_vida = csv_expec_vida.rename(
#     columns={
#         "Entity": "Entidade",
#         "Code": "Codigo",
#         "Year": "Ano",
#         "Life expectancy": "Expectativa_Vida"
#     }
# )

# # 3. Diagnóstico dos valores ausentes
# print("\n=== VALORES AUSENTES ===")
# print(csv_expec_vida.isna().sum())

# # 4. Investigação das entidades sem código
# entidades_sem_codigo = csv_expec_vida.loc[
#     csv_expec_vida["Codigo"].isna(), "Entidade"
# ]

# print("\n=== ENTIDADES SEM CÓDIGO ===")
# print(entidades_sem_codigo.unique())

# print("\n=== REGISTROS POR ENTIDADE SEM CÓDIGO ===")
# print(entidades_sem_codigo.value_counts())

# print("\n=== QUANTIDADE DE ENTIDADES SEM CÓDIGO ===")
# print(entidades_sem_codigo.nunique())

# # 5. Investigação do Brasil
# brasil = csv_expec_vida.loc[
#     csv_expec_vida["Entidade"] == "Brazil"
# ]

# print("\n=== REGISTROS DO BRASIL ===")
# print(brasil["Ano"].count())

# print("\n=== ANOS DISTINTOS DO BRASIL ===")
# print(brasil["Ano"].nunique())

# print("\n=== PRIMEIROS REGISTROS DO BRASIL ===")
# print(brasil.head())

# print("\n=== ÚLTIMOS REGISTROS DO BRASIL ===")
# print(brasil.tail())

# # 6. Validação da granularidade
# print("\n=== DUPLICIDADES POR ENTIDADE E ANO ===")
# print( csv_expec_vida.duplicated(subset=["Entidade", "Ano"]).sum())

# # 7. Investigação dos códigos
# print("\n=== CÓDIGOS DE WORLD, EUROPE E BRAZIL ===")
# print(
#     csv_expec_vida.loc[csv_expec_vida["Entidade"].isin(["World", "Europe", "Brazil"]),["Entidade", "Codigo"]].drop_duplicates())

