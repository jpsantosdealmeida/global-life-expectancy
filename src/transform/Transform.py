import pandas as pd
from pathlib import Path


# Funções

def classificacao_codigo(codigo):
    if pd.isna(codigo):
        return 'SEM_CODIGO'

    codigo = codigo.strip()

    if codigo.startswith('OWID_'):
        return 'OWID'
    elif codigo.isalpha() and len(codigo) == 3:
        return 'POSSIVEL_ISO'
    else:
        return 'OUTRO'
    
# 1. Leitura dos dados
caminho_csv = Path().cwd() / 'data' / 'raw' / 'expectativa_de_vida.csv'

expect_vida_csv = pd.read_csv(caminho_csv)

print("=== PRIMEIRAS LINHAS ===")
print(expect_vida_csv.head())

expect_vida_csv.columns = expect_vida_csv.columns.str.strip()

# 2. Padronização das colunas
expect_vida_csv = expect_vida_csv.rename(
    columns={
        "Entity": "Entidade",
        "Code": "Codigo",
        "Year": "Ano",
        "Life expectancy": "Expectativa_Vida"
    }
)

# Verificando tipagem 
print("=== TIPAGEM DADOS ===")
print(expect_vida_csv.dtypes)

# 3. Verificando menor valor de expectativa de vida e mairo
print("=== MENOR E MAIOR VALOR  ===")
menor_valor = expect_vida_csv['Expectativa_Vida'].min()
maior_valor = expect_vida_csv['Expectativa_Vida'].max()
print(f'MENOR -> {menor_valor}')
print(f'MAIOR -> {maior_valor}')

print("\n=== VERIFICACAO MENOR OU IGUAL A ZERO ===")
quantidade_valores_nao_positivos = (expect_vida_csv['Expectativa_Vida'] <= 0).sum()
print(quantidade_valores_nao_positivos)

print("\n=== DADOS DOS VALORES EXTREMOS ===")
print(expect_vida_csv.loc[(expect_vida_csv['Expectativa_Vida'] == menor_valor) | (expect_vida_csv['Expectativa_Vida'] == maior_valor)])


print("\n=== VERIFICAÇÃO ANTES DA TRANSFORMAÇÃO ===")
print(f'Qtd Registros: {len(expect_vida_csv)}')
print(f'Valores Nulos: {expect_vida_csv.isna().sum()}')

print("\n=== PÓS TRANSFORMAÇÃO ===")

# df criação nova coluna aplicando a classificação
expect_vida_csv['Tipo_Codigo'] = expect_vida_csv['Codigo'].apply(classificacao_codigo)

print(f'\n{expect_vida_csv['Tipo_Codigo'].value_counts()}')
print(f'\nValores Nulos: {expect_vida_csv.isna().sum()}')
print(f'\nQtd Registros: {len(expect_vida_csv)}')



print(expect_vida_csv.head(10))




