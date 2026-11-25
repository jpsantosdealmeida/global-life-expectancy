import pandas as pd
from pathlib import Path

# 1. Leitura dos dados
caminho_csv = Path().cwd() / 'data' / 'raw' / 'expectativa_de_vida.csv'

expect_vida_csv = pd.read_csv(caminho_csv)

print("=== PRIMEIRAS LINHAS ===")
print(expect_vida_csv.head())
# 2. Padronização das colunas
expect_vida_csv.columns = expect_vida_csv.columns.str.strip()
expect_vida_csv = expect_vida_csv.rename(
    columns={
        "Entity": "Entidade",
        "Code": "Codigo",
        "Year": "Ano",
        "Life expectancy": "Expectativa_Vida"
    }
)

# 3. Diagnóstico dos valores ausentes
print("\n=== VALORES AUSENTES ===")
print(expect_vida_csv.isna().sum())

# 4. Investigação das entidades sem código
entidades_sem_codigo = expect_vida_csv.loc[
    expect_vida_csv["Codigo"].isna(), "Entidade"
]

print("\n=== ENTIDADES SEM CÓDIGO ===")
print(entidades_sem_codigo.unique())

print("\n=== REGISTROS POR ENTIDADE SEM CÓDIGO ===")
print(entidades_sem_codigo.value_counts())

print("\n=== QUANTIDADE DE ENTIDADES SEM CÓDIGO ===")
print(entidades_sem_codigo.nunique())

# 5. Investigação do Brasil
brasil = expect_vida_csv.loc[
    expect_vida_csv["Entidade"] == "Brazil"
]

print("\n=== REGISTROS DO BRASIL ===")
print(brasil["Ano"].count())

print("\n=== ANOS DISTINTOS DO BRASIL ===")
print(brasil["Ano"].nunique())

print("\n=== PRIMEIROS REGISTROS DO BRASIL ===")
print(brasil.head())

print("\n=== ÚLTIMOS REGISTROS DO BRASIL ===")
print(brasil.tail())

# 6. Validação da granularidade
print("\n=== DUPLICIDADES POR ENTIDADE E ANO ===")
print( expect_vida_csv.duplicated(subset=["Entidade", "Ano"]).sum())

# 7. Investigação dos códigos
print("\n=== CÓDIGOS DE WORLD, EUROPE E BRAZIL ===")
print(
    expect_vida_csv.loc[expect_vida_csv["Entidade"].isin(["World", "Europe", "Brazil"]),["Entidade", "Codigo"]].drop_duplicates())
