from pathlib import Path
from src.extract import extrair_dados
from src.transform import transformar_dados
from src.validate import validar_dados
from src.load import exportar_csv

def main():
    dir_base = Path(__file__).resolve().parent 
    caminho_csv = dir_base / 'data' / 'raw' / 'expectativa_de_vida.csv'
    caminho_csv_tratado = dir_base / 'data' / 'processed' / 'expectativa_de_vida_tratada.csv'

    # Extraindo dados df cru
    df_raw = extrair_dados(caminho_csv)

    # Transformando os dados
    df_tratado = transformar_dados(df_raw)

    # Validando a transformação
    validar_dados(df_raw,df_tratado)

    # Exportando csv
    exportar_csv(df_tratado,caminho_csv_tratado)

if __name__ == '__main__':
    main()