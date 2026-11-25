import pandas as pd

# Funções Transformações
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
    
def transformar_dados(dataframe_original):

    dataframe_copia = dataframe_original.copy(deep=True)
    # Limpando espaços nos nomes das colunas
    dataframe_copia.columns = dataframe_copia.columns.str.strip()

    # Alterando nomes das colunas
    dataframe_copia = dataframe_copia.rename(
    columns={
        "Entity": "Entidade",
        "Code": "Codigo",
        "Year": "Ano",
        "Life expectancy": "Expectativa_Vida"
            }
        )

    dataframe_copia['Tipo_Codigo'] = dataframe_copia['Codigo'].apply(classificacao_codigo)

    return dataframe_copia









