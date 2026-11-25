import pandas as pd

def validar_quantidade_registros(df_original, df_tratado):
    
    quantidade_registros_df_original = len(df_original)
    quantidade_registros_df_tratado = len(df_tratado)

    if quantidade_registros_df_original != quantidade_registros_df_tratado:
        raise ValueError(f'Valor do df original diferente após o tratamento, Original {quantidade_registros_df_original} -> Após Tratadas {quantidade_registros_df_tratado} ')
        
    
def validar_dataframe_vazio(df):

    if df.empty:
        raise ValueError('Erro! O dataframe está vazio..')
    
def validar_duplicidades(df):
    pass


def validar_valores_nulos(df):
    pass


def validar_expectativa_vida(df):
    pass


def validar_dados(df_original, df_tratado):
    pass