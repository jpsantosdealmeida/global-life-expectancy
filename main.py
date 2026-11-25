import pandas as pd
from pathlib import Path
from src.Extract import extrair_dados

caminho_csv = Path(__file__).resolve().parent / 'data' / 'raw' /  'expectativa_de_vida.csv'
