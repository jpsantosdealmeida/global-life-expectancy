import pandas as pd

def validar_quantidade_registros(df_original, df_tratado):
    
    quantidade_registros_df_original = len(df_original)
    quantidade_registros_df_tratado = len(df_tratado)

    if quantidade_registros_df_original != quantidade_registros_df_tratado:
        raise ValueError(
            f'Divergência na quantidade de registros. '
            f'Original: {quantidade_registros_df_original} | '
            f'Tratado: {quantidade_registros_df_tratado}.'
        )
        
    
def validar_dataframe_vazio(df):

    if df.empty:
       raise ValueError(
            'O DataFrame está vazio.'
        )
   
def validar_duplicidades(df):

    if df.duplicated(subset=['Entidade','Ano']).any():
        raise ValueError(
            'Foram encontrados registros duplicados '
            'na combinação das colunas Entidade e Ano.'
        )

def validar_valores_nulos(df):

    if df[['Entidade','Ano','Expectativa_Vida','Tipo_Codigo']].isna().any().any():
        raise ValueError(
            'Foram encontrados valores nulos em colunas obrigatórias.'
        )

def validar_expectativa_vida(df):

    if (df['Expectativa_Vida'] <= 0).any():
        raise ValueError(
            'Foram encontrados valores menores ou iguais a zero '
            'na coluna Expectativa_Vida.'
        )


def validar_dados(df_original, df_tratado):
    validar_quantidade_registros(df_original,df_tratado)
    validar_dataframe_vazio(df_tratado)
    validar_duplicidades(df_tratado)
    validar_valores_nulos(df_tratado)
    validar_expectativa_vida(df_tratado)