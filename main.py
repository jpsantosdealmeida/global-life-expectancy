from pathlib import Path
from src.extract import extrair_dados
from src.transform import transformar_dados
from src.validate import validar_quantidade_registros,validar_dataframe_vazio

caminho_csv = Path(__file__).resolve().parent / 'data' / 'raw' / 'expectativa_de_vida.csv'

df_raw = extrair_dados(caminho_csv)

df_tratado = transformar_dados(df_raw)

# print('===== DF ORIGINAL ====')
# print(df_raw.columns)
# print('\n===== DF TRANSFORMADO ====')
# print(df_tratado.columns)

# validar_quantidade_registros(df_raw,df_tratado)